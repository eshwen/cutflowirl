# Tai Sakuma <sakuma@cern.ch>
import os
import sys
import logging

import ROOT

import AlphaTwirl
import AlphaTwirl.HeppyResult as HeppyResult
HeppyResult.componentHasTheseFiles[:] = ['roctree']

ROOT.gROOT.SetBatch(1)

##__________________________________________________________________||
import logging
logger = logging.getLogger(__name__)
log_handler = logging.StreamHandler(stream=sys.stdout)
log_formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
log_handler.setFormatter(log_formatter)
logger.addHandler(log_handler)

##__________________________________________________________________||
class FrameworkHeppy(object):
    """A simple framework for using AlphaTwirl

    Args:
        outdir (str): the output directory
        datamc (str): 'data' or 'mc'
        force (bool): overwrite the output if True
        quiet (bool): don't show progress bars if True
        parallel_mode (str): 'multiprocessing', 'subprocess', 'htcondor'
        process (int): the number of processes for the 'multiprocessing' mode
        user_modules (list of str): names of python modules to be copied for the 'subprocess' mode
        max_events_per_dataset (int):
        max_events_per_process (int):
        profile (bool): run cProfile if True
        profile_out_path (bool): path to store the result of the profile. stdout if None

    """
    def __init__(self, outdir, heppydir,
                 datamc = 'mc',
                 force = False, quiet = False,
                 parallel_mode = 'multiprocessing',
                 process = 8,
                 user_modules = (),
                 max_events_per_dataset = -1, max_events_per_process = -1,
                 profile = False, profile_out_path = None
    ):
        self.parallel = build_parallel(
            parallel_mode = parallel_mode,
            quiet = quiet,
            processes = process,
            user_modules = user_modules
        )
        self.outdir = outdir
        self.heppydir = heppydir
        self.datamc = datamc
        self.force =  force
        self.max_events_per_dataset = max_events_per_dataset
        self.max_events_per_process = max_events_per_process
        self.profile = profile
        self.profile_out_path = profile_out_path

    def run(self, components,
            reader_collector_pairs,
            analyzerName = 'roctree',
            fileName = 'tree.root',
            treeName = 'tree'
    ):

        self._begin()
        loop = self._configure(components, reader_collector_pairs, analyzerName, fileName, treeName)
        self._run(loop)
        self._end()

    def _begin(self):
        self.parallel.begin()

    def _configure(self, components, reader_collector_pairs, analyzerName, fileName, treeName):

        component_readers = AlphaTwirl.HeppyResult.ComponentReaderComposite()

        # tbl_heppyresult.txt
        tbl_heppyresult_path = os.path.join(self.outdir, 'tbl_heppyresult.txt')
        if self.force or not os.path.exists(tbl_heppyresult_path):
            # e.g., '74X/MC/20150810_MC/20150810_SingleMu'
            heppydir_rel = '/'.join(self.heppydir.rstrip('/').split('/')[-4:])
            AlphaTwirl.mkdir_p(os.path.dirname(tbl_heppyresult_path))
            f = open(tbl_heppyresult_path, 'w')
            f.write('heppyresult\n')
            f.write(heppydir_rel + '\n')
            f.close()

        # tbl_dataset.txt
        tbl_dataset_path = os.path.join(self.outdir, 'tbl_dataset.txt')
        if self.force or not os.path.exists(tbl_dataset_path):
            tblDataset = HeppyResult.TblComponentConfig(
                outPath = tbl_dataset_path,
                columnNames = ('dataset', ),
                keys = ('dataset', ),
            )
            component_readers.add(tblDataset)

        # tbl_xsec.txt for MC
        if self.datamc == 'mc':
            tbl_xsec_path = os.path.join(self.outdir, 'tbl_xsec.txt')
            if self.force or not os.path.exists(tbl_xsec_path):
                tblXsec = HeppyResult.TblComponentConfig(
                    outPath = tbl_xsec_path,
                    columnNames = ('xsec', ),
                    keys = ('xSection', ),
                )
                component_readers.add(tblXsec)

        # tbl_nevt.txt for MC
        if self.datamc == 'mc':
            tbl_nevt_path = os.path.join(self.outdir, 'tbl_nevt.txt')
            if self.force or not os.path.exists(tbl_nevt_path):
                tblNevt = HeppyResult.TblCounter(
                    outPath = tbl_nevt_path,
                    columnNames = ('nevt', 'nevt_sumw'),
                    analyzerName = 'skimAnalyzerCount',
                    fileName = 'SkimReport.txt',
                    levels = ('All Events', 'Sum Weights')
                )
                component_readers.add(tblNevt)

        # event loop
        reader = AlphaTwirl.Loop.ReaderComposite()
        collector = AlphaTwirl.Loop.CollectorComposite(self.parallel.progressMonitor.createReporter())
        for r, c in reader_collector_pairs:
            reader.add(r)
            collector.add(c)
        eventLoopRunner = AlphaTwirl.Loop.MPEventLoopRunner(self.parallel.communicationChannel)
        eventBuilderConfigMaker = AlphaTwirl.HeppyResult.EventBuilderConfigMaker(
            analyzerName = analyzerName,
            fileName = fileName,
            treeName = treeName,
        )
        datasetIntoEventBuildersSplitter = AlphaTwirl.Loop.DatasetIntoEventBuildersSplitter(
            EventBuilder = AlphaTwirl.HeppyResult.BEventBuilder,
            eventBuilderConfigMaker = eventBuilderConfigMaker,
            maxEvents = self.max_events_per_dataset,
            maxEventsPerRun = self.max_events_per_process
        )
        eventReader = AlphaTwirl.Loop.EventReader(
            eventLoopRunner = eventLoopRunner,
            reader = reader,
            collector = collector,
            split_into_build_events = datasetIntoEventBuildersSplitter
        )
        component_readers.add(eventReader)

        if components == ['all']: components = None
        heppyResult = HeppyResult.HeppyResult(path = self.heppydir, componentNames = components)
        componentLoop = AlphaTwirl.HeppyResult.ComponentLoop(heppyResult, component_readers)

        return componentLoop

    def _run(self, componentLoop):

        if not self.profile:
            componentLoop()
        else:
            import cProfile, pstats, StringIO
            pr = cProfile.Profile()
            pr.enable()

            componentLoop()

            pr.disable()
            s = StringIO.StringIO()
            sortby = 'cumulative'
            ps = pstats.Stats(pr, stream = s).strip_dirs().sort_stats(sortby)
            ps.print_stats()
            if self.profile_out_path is None:
                print s.getvalue()
            else:
                f = open(self.profile_out_path, 'w')
                f.write(s.getvalue())
                f.close()

    def _end(self):
        self.parallel.end()

##__________________________________________________________________||
class Parallel(object):
    def __init__(self, progressMonitor, communicationChannel):
        self.progressMonitor = progressMonitor
        self.communicationChannel = communicationChannel

    def begin(self):
        self.progressMonitor.begin()
        self.communicationChannel.begin()

    def end(self):
        self.progressMonitor.end()
        self.communicationChannel.end()

##__________________________________________________________________||
def build_parallel(parallel_mode, quiet, processes, user_modules):

    default_parallel_mode = 'multiprocessing'

    if parallel_mode in ('subprocess', 'htcondor'):
        return build_parallel_dropbox(
            parallel_mode = parallel_mode,
            quiet = quiet,
            user_modules = user_modules
        )

    if not parallel_mode == default_parallel_mode:
        logger = logging.getLogger(__name__)
        logger.warning('unknown parallel_mode "{}", use default "{}"'.format(
            parallel_mode, default_parallel_mode
        ))

    return build_parallel_multiprocessing(quiet = quiet, processes = processes)

##__________________________________________________________________||
def build_parallel_dropbox(parallel_mode, quiet, user_modules):
    tmpdir = '_ccsp_temp'
    user_modules = list(user_modules)
    user_modules.append('AlphaTwirl')
    AlphaTwirl.mkdir_p(tmpdir)
    progressMonitor = AlphaTwirl.ProgressBar.NullProgressMonitor()
    if parallel_mode == 'htcondor':
        dispatcher = AlphaTwirl.Concurrently.HTCondorJobSubmitter()
    else:
        dispatcher = AlphaTwirl.Concurrently.SubprocessRunner()
    workingArea = AlphaTwirl.Concurrently.WorkingArea(
        dir = tmpdir,
        python_modules = user_modules
    )
    dropbox = AlphaTwirl.Concurrently.TaskPackageDropbox(
        workingArea = workingArea,
        dispatcher = dispatcher
    )
    communicationChannel = AlphaTwirl.Concurrently.CommunicationChannel(
        dropbox = dropbox
    )
    return Parallel(progressMonitor, communicationChannel)

##__________________________________________________________________||
def build_parallel_multiprocessing(quiet, processes):
    progressMonitor, communicationChannel = AlphaTwirl.Configure.build_progressMonitor_communicationChannel(quiet = quiet, processes = processes)
    return Parallel(progressMonitor, communicationChannel)

##__________________________________________________________________||
