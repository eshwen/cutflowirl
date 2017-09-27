#!/usr/bin/env python
# Tai Sakuma <sakuma@fnal.gov>
import os, sys
import argparse
import logging
import pprint

##__________________________________________________________________||
alphatwirl_path = os.path.join(os.path.dirname(__file__), 'AlphaTwirl')
sys.path.insert(1, alphatwirl_path)
import AlphaTwirl

##__________________________________________________________________||
import FrameworkHeppy

##__________________________________________________________________||
default_heppydir = '/vols/cms/RA1/80X/MC/LongLived/20170904/AtLogic_MC_LL'

##__________________________________________________________________||
parser = argparse.ArgumentParser()
parser.add_argument("--mc", action = "store_const", dest = 'datamc', const = 'mc', default = 'mc', help = "for processing MC")
parser.add_argument("--data", action = "store_const", dest = 'datamc', const = 'data', help = "for processing data")
parser.add_argument('--parallel-mode', default = 'multiprocessing', choices = ['multiprocessing', 'subprocess', 'htcondor'], help = "mode for concurrency")
parser.add_argument('--profile', action = "store_true", help = "run profile")
parser.add_argument('--profile-out-path', default = None, help = "path to write the result of profile")

parser.add_argument('-o', '--outDir', default = os.path.join('tbl', 'out'))
parser.add_argument('-n', '--nevents', default = -1, type = int, help = 'maximum number of events to process for each component')
parser.add_argument('--max-events-per-process', default = -1, type = int, help = 'maximum number of events per process')
parser.add_argument('--force', action = 'store_true', default = False, dest='force', help = 'recreate all 0output files')

parser.add_argument('--logging-level', default = 'WARN', choices = ['DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL'], help = "level for logging")

parser.add_argument('-i', '--heppydir', default = default_heppydir, help = 'Heppy results dir')
parser.add_argument('-p', '--processes', default = None, type = int, help = 'number of processes to run in parallel')
parser.add_argument('-q', '--quiet', default = False, action = 'store_true', help = 'quiet mode')
parser.add_argument('-c', '--components', default = None, nargs = '*', help = 'the list of components')

args = parser.parse_args()

##__________________________________________________________________||
def main():

    #
    # configure logger
    #
    log_level = logging.getLevelName(args.logging_level)
    log_handler = logging.StreamHandler()
    log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    log_handler.setFormatter(log_formatter)

    names_for_logger = ["FrameworkHeppy", "AlphaTwirl"]
    for n in names_for_logger:
        logger = logging.getLogger(n)
        logger.setLevel(log_level)
        logger.handlers[:] = [ ]
        logger.addHandler(log_handler)

    #
    #
    #
    reader_collector_pairs = [ ]

    #
    # configure scribblers
    #
    from atlogic.Scribblers.htbin import htbin
    from atlogic.Scribblers.MhtOverMet import MhtOverMet
    scribblers = [
        htbin(),
        MhtOverMet()
       ]

    from scribblers.SMSMass import SMSMass
    scribblers_SMS = [
        SMSMass(),
    ]

    scribblers.extend(scribblers_SMS)

    reader_collector_pairs.extend([(r, AlphaTwirl.Loop.NullCollector()) for r in scribblers])

    #
    # configure event selections
    #
    std_cutflow = dict(All = (
        dict(All = ("ev : ev.nElectronsVeto[0] == 0",
                    "ev : ev.nMuonsVeto[0] == 0",
                    )), # Lepton vetoes 
        "ev : ev.nIsoTracksVeto[0] <= 0",
        "ev : ev.nPhotonsVeto[0] == 0",
        "ev : ev.nJet40[0] >= 2",
        "ev : ev.jet_pt[0] > 100",
        "ev : ev.ht40[0] > 200",
        "ev : ev.mht40_pt[0] > 200",
        "ev : ev.nJet40Fwd[0] == 0",
        "ev : ev.MhtOverMet[0] < 1.25",
        dict(Any = (dict(All = ('htbin_200', ('alphaT', dict(v = 0.65)))),
                    dict(All = ('htbin_250', ('alphaT', dict(v = 0.60)))),
                    dict(All = ('htbin_300', ('alphaT', dict(v = 0.55)))),
                    dict(All = ('htbin_350', ('alphaT', dict(v = 0.53)))),
                    dict(All = ('htbin_400', ('alphaT', dict(v = 0.52)))),
                    dict(All = ('htbin_600', ('alphaT', dict(v = 0.52)))),
                    dict(All = ('htbin_900',))
                    )
             ), # HT-dependent AlphaT cuts
        "ev : ev.biasedDPhi[0] > 0.5",
        dict(All = ( dict(Any = ("ev : ev.nBJet40[0] == 0", "ev : ev.nBJet40[0] == 1")),
                     dict(Any = ("ev : ev.nJet100[0] == 2", "ev : ev.nJet100[0] == 3")), #eq01b_eq23j
             )), # Most sensitive simplified njet, nb category
        ))


    path_cfg = dict(Any = (
        # std_cutflow,
        dict(All = ('ev : ev.GenSusyMGluino[0] == 1000', 'ev : ev.GenSusyMNeutralino[0] == 900', std_cutflow)),
        # dict(All = ('ev : ev.GenSusyMStop[0] == 300', 'ev : ev.GenSusyMNeutralino[0] == 250', std_cutflow)),
        # dict(All = ('ev : ev.GenSusyMSbottom[0] == 1000', 'ev : ev.GenSusyMNeutralino[0] == 300', std_cutflow)),
        # dict(All = ('ev : ev.GenSusyMSquark[0] == 400', 'ev : ev.GenSusyMNeutralino[0] == 250', std_cutflow)),
        # Can add more samples here in the same vein as above. Current values are for T1tttt
    ))
    
    from atlogic.EventSelectionModules.EventSelectionAllCount import EventSelectionAllCount
    from atlogic.EventSelectionModules.EventSelectionAnyCount import EventSelectionAnyCount
    from atlogic.EventSelectionModules.EventSelectionNotCount import EventSelectionNotCount

    from atlogic.buildEventSelection import buildEventSelection
    eventSelection = buildEventSelection(
        path_cfg = path_cfg,
        AllClass = EventSelectionAllCount,
        AnyClass = EventSelectionAnyCount,
        NotClass = EventSelectionNotCount
    )

    from atlogic.event_selection_str import event_selection_str
    eventselection_path = os.path.join(args.outDir, 'eventselection.txt')
    if args.force or not os.path.exists(eventselection_path):
        AlphaTwirl.mkdir_p(os.path.dirname(eventselection_path))
        with open(eventselection_path, 'w') as f:
            pprint.pprint(path_cfg, stream = f)

    tbl_cutflow_path = os.path.join(args.outDir, 'tbl_cutflow.txt')

    resultsCombinationMethod = AlphaTwirl.Collector.CombineIntoList(
        summaryColumnNames = ('depth', 'class', 'name', 'pass', 'total'),
        sort = False,
        summarizer_to_tuple_list = summarizer_to_tuple_list
    )
    deliveryMethod = AlphaTwirl.Collector.WriteListToFile(tbl_cutflow_path)
    collector = AlphaTwirl.Loop.Collector(resultsCombinationMethod, deliveryMethod)
    reader_collector_pairs.append((eventSelection, collector))

    #
    # run
    #
    fw =  FrameworkHeppy.FrameworkHeppy(
        outdir = args.outDir,
        heppydir = args.heppydir,
        datamc = args.datamc,
        force = args.force,
        quiet = args.quiet,
        parallel_mode = args.parallel_mode,
        process = args.processes,
        user_modules = ('atlogic', 'scribblers'),
        max_events_per_dataset = args.nevents,
        max_events_per_process = args.max_events_per_process,
        profile = args.profile,
        profile_out_path = args.profile_out_path

    )
    fw.run(
        components = args.components,
        reader_collector_pairs = reader_collector_pairs
    )

##__________________________________________________________________||
def summarizer_to_tuple_list(summarizer, sort):
    return [tuple(e) for e in summarizer._results]

##__________________________________________________________________||
if __name__ == '__main__':
    main()
