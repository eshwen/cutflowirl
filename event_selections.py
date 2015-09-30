
##__________________________________________________________________||
class AllEvents(object):
    def __call__(self, event): return True

##__________________________________________________________________||
class EventSelectionAll(object):
    """select events that meet all conditions

    """

    def __init__(self, name = None):
        if name is not None: self.name = name
        self.selections = [ ]

    def add(self, selection):
        self.selections.append(selection)

    def begin(self, event):
        for s in self.selections:
            if hasattr(s, 'begin'): s.begin(event)

    def __call__(self, event):
        for s in self.selections:
            if not s(event): return False
        return True

    def end(self):
        for s in self.selections:
            if hasattr(s, 'end'): s.end()

##__________________________________________________________________||
class EventSelectionAny(object):
    """select events that meet any of the conditions

    """

    def __init__(self, name = None):
        if name is not None: self.name = name
        self.selections = [ ]

    def add(self, selection):
        self.selections.append(selection)

    def begin(self, event):
        for s in self.selections:
            if hasattr(s, 'begin'): s.begin(event)

    def __call__(self, event):
        for s in self.selections:
            if s(event): return True
        return False

    def end(self):
        for s in self.selections:
            if hasattr(s, 'end'): s.end()

##__________________________________________________________________||
class LambdaStr(object):
    """select events to which a lambda returns True.

    A lambda should be given as a string to __init__ and will be
    evaluated in begin(). This is because a lambda is not picklable.

    In the multiprocessing mode, __init__() is called in the main
    process. Then, the instance will be pickled and sent to
    subprocesses. begin() will be called in the subprocesses.

    """
    def __init__(self, lambda_str, name = None):
        if name is not None: self.name = name
        self.lambda_str = lambda_str

    def begin(self, event):
        self.func = eval('lambda ' + self.lambda_str)

    def __call__(self, event):
        try:
            return self.func(event)
        except:
            print self.lambda_str
            raise

    def end(self):
        self.func = None

##__________________________________________________________________||
class VarMin(object):
    """select events with the value of a specified variable greater than or
    equal to a specified minimum value

    """

    def __init__(self, varName, minValue, closed = True, name = None):
        if name is not None: self.name = name
        self.varName = varName
        self.minValue = minValue
        self.closed = closed

    def __call__(self, event):
        val = getattr(event, self.varName)[0]
        if self.minValue < val: return True
        if self.closed:
            if self.minValue == val: return True
        return False

##__________________________________________________________________||
class VarMax(object):
    """select events with the value of a specified variable less than or
    equal to a specified maximum value

    """

    def __init__(self, varName, maxValue, closed = False, name = None):
        if name is not None: self.name = name
        self.varName = varName
        self.maxValue = maxValue
        self.closed = closed

    def __call__(self, event):
        val = getattr(event, self.varName)[0]
        if val < self.maxValue: return True
        if self.closed:
            if val == self.maxValue: return True
        return False

##__________________________________________________________________||
class VarValue(object):
    """select events with the value of a specified variable equal to a
    specified value

    """

    def __init__(self, varName, value, name = None):
        if name is not None: self.name = name
        self.varName = varName
        self.value = value

    def __call__(self, event):
        return getattr(event, self.varName)[0] == self.value

##__________________________________________________________________||
class VarIn(object):
    """select events with the value of a specified variable an element of
    a specified list

    """

    def __init__(self, varName, valueList, name = None):
        if name is not None: self.name = name
        self.varName = varName
        self.valueList = valueList

    def __call__(self, event):
        return getattr(event, self.varName)[0] in self.valueList

##__________________________________________________________________||
class PD_HLT(object):
    def __init__(self):
        self.itsdict = {
            'MET': (  # "HLT_PFMET90_PFMHT90_IDTight"
                "HLT_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight",
                "HLT_PFMETNoMu120_JetIdCleaned_PFMHTNoMu120_IDTight",
                ),
            'HTMHT': (
                "HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57",
                "HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63",
                "HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55",
                "HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58",
                "HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53",
                "HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54",
                "HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52",
                "HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53",
                "HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51",
                "HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52",
                ),
            'JetHT': ('HLT_PFHT800', ),
            'SingleMuon': (
                'HLT_IsoMu17_eta2p1',
                'HLT_IsoMu20',
                'HLT_IsoMu24_eta2p1'
                ),
            'SingleElectron': (
                "HLT_Ele22_WPLoose_Gsf",
                "HLT_Ele23_WPLoose_Gsf",
                "HLT_Ele27_eta2p1_WPLoose_Gsf",
                ),
            'SinglePhoton': (
                "HLT_Photon120",
                "HLT_Photon125",
                "HLT_Photon175",
                )
        }

    def __call__(self, event):
        if not event.PrimaryDataset[0] in self.itsdict: return True
        hltpaths = self.itsdict[event.PrimaryDataset[0]]
        if all([getattr(event, p)[0] == 0 for p in hltpaths]): return False
        return True

##__________________________________________________________________||
class AlphaTCut(object):
    def __call__(self, event):
        if 200 <= event.ht40[0] < 250 and 0.65 <= event.alphaT[0]: return True
        elif 250 <= event.ht40[0] < 300 and 0.60 <= event.alphaT[0]: return True
        elif 300 <= event.ht40[0] < 350 and 0.55 <= event.alphaT[0]: return True
        elif 350 <= event.ht40[0] < 400 and 0.53 <= event.alphaT[0]: return True
        elif 400 <= event.ht40[0] < 800 and 0.52 <= event.alphaT[0]: return True
        return False

##__________________________________________________________________||
class HT_HLTAlphaT(object):
    def __call__(self, event):
        if 200 <= event.ht40[0] < 250:
            if event.HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57[0]: return True
            if event.HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63[0]: return True
        if 250 <= event.ht40[0] < 300:
            if event.HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55[0]: return True
            if event.HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58[0]: return True
        if 300 <= event.ht40[0] < 350:
            if event.HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53[0]: return True
            if event.HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54[0]: return True
        if 350 <= event.ht40[0] < 400:
            if event.HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52[0]: return True
            if event.HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53[0]: return True
        if 400 <= event.ht40[0] < 800:
            if event.HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51[0]: return True
            if event.HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52[0]: return True
        return False

##__________________________________________________________________||
class HT_SingleMuon(object):
    def __call__(self, event):
        if event.HLT_IsoMu17_eta2p1[0]: return True
        if event.HLT_IsoMu20[0]: return True
        if event.HLT_IsoMu24_eta2p1[0]: return True
        return False

##__________________________________________________________________||
def event_selection_str(eventSelection):
    out = event_selection_io(eventSelection)
    return out.getvalue()

##__________________________________________________________________||
def event_selection_io(eventSelection, out = None, shown = [ ]):

    if out is None:
        import StringIO
        out = StringIO.StringIO()

    import inspect

    def print_name(es):
        ret = '<'
        if hasattr(es, 'name'):
            ret += str(es.name)
        ret += (':')
        if inspect.isfunction(es):
            ret += es.__name__
        else:
            ret += es.__class__.__name__
        ret += '>'
        return ret
        
    out.write('##__________________________________________________________________||\n')
    out.write('# ' + print_name(eventSelection) + '\n')
    if inspect.isfunction(eventSelection):
        if eventSelection not in shown:
            out.write(inspect.getsource(eventSelection) + '\n')
            shown.append(eventSelection)
        return out

    if hasattr(eventSelection, '__dict__') and eventSelection.__dict__:
        out.write('# __dict__ = ')
        out.write(str(eventSelection.__dict__) + '\n')

    if eventSelection.__class__ not in shown:
        out.write('\n')
        out.write(inspect.getsource(eventSelection.__class__))
        shown.append(eventSelection.__class__)

    if isinstance(eventSelection, EventSelectionAll):
        out.write('\n')
        out.write('# ' + print_name(eventSelection) + ' = ')
        out.write(' AND '.join([print_name(e) for e in eventSelection.selections]))
        out.write('\n\n')
        for e in eventSelection.selections:
            event_selection_io(e, out)
            out.write('\n')

    if isinstance(eventSelection, EventSelectionAny):
        out.write('\n')
        out.write('# ' + print_name(eventSelection) + ' = ')
        out.write(' OR '.join([print_name(e) for e in eventSelection.selections]))
        out.write('\n\n')
        for e in eventSelection.selections:
            event_selection_io(e, out)
            out.write('\n')

    return out

def SignalLooseSelection(datamc,pd,hlt):

    SignalLoose = EventSelectionAll(name = 'SignalLoose')

    ##______________________________________________________________||
    ## Signal loose
    SignalLoose.add(LambdaStr("ev : ev.cutflow[0] == 'Signal'", name = 'cutflowSignal'))
    if datamc == 'data' and pd:
        SignalLoose.add(LambdaStr("ev : ev.PrimaryDataset[0] in ('MET', 'HTMHT', 'JetHT')", name = 'PDMetHtmhtJetht'))
    SignalLoose.add(LambdaStr("ev : ev.ht40[0] >= 200", name = 'HTGT200'))

    SignalLooseBintypes = EventSelectionAny(name = 'SignalLooseBintypes')
    SignalLoose.add(SignalLooseBintypes)

    SignalLooseMonojet = EventSelectionAll(name = 'SignalLooseMonojet')
    SignalLooseAsymjet = EventSelectionAll(name = 'SignalLooseAsymjet')
    SignalLooseSymjet = EventSelectionAll(name = 'SignalLooseSymjet')
    SignalLooseHighht = EventSelectionAll(name = 'SignalLooseHighht')

    SignalLooseBintypes.add(SignalLooseMonojet)
    SignalLooseBintypes.add(SignalLooseAsymjet)
    SignalLooseBintypes.add(SignalLooseSymjet)
    SignalLooseBintypes.add(SignalLooseHighht)

    ## Signal loose - monojet
    SignalLooseMonojet.add(LambdaStr("ev : ev.bintype[0] == 'monojet'", name = 'bintype_monojet'))
    if datamc == 'data' and pd:
        SignalLooseMonojet.add(LambdaStr("ev : ev.PrimaryDataset[0] == 'MET'", name = 'PD_MET'))

    ## Signal loose - asymjet
    SignalLooseAsymjet.add(LambdaStr("ev : ev.bintype[0] == 'asymjet'", name = 'bintype_asymjet'))
    if datamc == 'data' and pd:
        SignalLooseAsymjet.add(LambdaStr("ev : ev.PrimaryDataset[0] == 'HTMHT'", name = 'PD_HTMHT'))
    SignalLooseAsymjet.add(LambdaStr("ev : 0.5 <= ev.alphaT[0]", name = 'alphaTLT0p5'))

    ## Signal loose - symjet
    SignalLooseSymjet.add(LambdaStr("ev : ev.bintype[0] == 'symjet'", name = 'bintype_symjet'))
    if datamc == 'data' and pd:
        SignalLooseSymjet.add(LambdaStr("ev : ev.PrimaryDataset[0] == 'HTMHT'", name = 'PD_HTMHT'))
    SignalLooseSymjet.add(LambdaStr("ev : 0.5 <= ev.alphaT[0]", name = 'alphaTLT0p5'))

    ## Signal loose - highht
    SignalLooseHighht.add(LambdaStr("ev : ev.bintype[0] == 'highht'", name = 'bintype_highht'))
    if datamc == 'data' and pd:
        SignalLooseHighht.add(LambdaStr("ev : ev.PrimaryDataset[0] == 'JetHT'", name = 'PD_JetHT'))
    SignalLooseHighht.add(LambdaStr("ev : 130 <= ev.mht40_pt[0]", name = 'MHTGT130'))

    return SignalLoose

def SignalFinalSelection(datamc,pd,hlt):

    SignalFinal = EventSelectionAll(name = 'SignalFinal')

    ##______________________________________________________________||
    ## Signal final
    SignalFinal.add(LambdaStr("ev : ev.cutflow[0] == 'Signal'", name = 'cutflowSignal'))
    SignalFinal.add(LambdaStr("ev : ev.nIsoTracksVeto[0] <= 0", name = 'isoTrackVeto'))

    SignalBintypes = EventSelectionAny(name = 'SignalBintypes')
    SignalFinal.add(SignalBintypes)

    SignalFinalMonojet = EventSelectionAll(name = 'SignalFinalMonojet')
    SignalFinalAsymjet = EventSelectionAll(name = 'SignalFinalAsymjet')
    SignalFinalSymjet = EventSelectionAll(name = 'SignalFinalSymjet')
    SignalFinalHighht = EventSelectionAll(name = 'SignalFinalHighht')

    SignalBintypes.add(SignalFinalMonojet)
    SignalBintypes.add(SignalFinalAsymjet)
    SignalBintypes.add(SignalFinalSymjet)
    SignalBintypes.add(SignalFinalHighht)

    ## Signal final - monojet
    SignalFinalMonojet.add(LambdaStr("ev : ev.bintype[0] == 'monojet'", name = 'bintype_monojet'))

    ## Signal final - asymjet
    SignalFinalAsymjet.add(LambdaStr("ev : ev.bintype[0] == 'asymjet'", name = 'bintype_asymjet'))
    if datamc == 'data' and hlt:
        SignalFinalAsymjet.add(HT_HLTAlphaT())
    SignalFinalAsymjet.add(AlphaTCut())
    SignalFinalAsymjet.add(LambdaStr("ev : 0.5 <= ev.biasedDPhi[0]", name = 'biasedDPhiGT0p5'))

    ## Signal final - symjet
    SignalFinalSymjet.add(LambdaStr("ev : ev.bintype[0] == 'symjet'", name = 'bintype_symjet'))
    if datamc == 'data' and hlt:
        SignalFinalSymjet.add(HT_HLTAlphaT())
    SignalFinalSymjet.add(AlphaTCut())
    SignalFinalSymjet.add(LambdaStr("ev : 0.5 <= ev.biasedDPhi[0]", name = 'biasedDPhiGT0p5'))

    ## Signal final - highht
    SignalFinalHighht.add(LambdaStr("ev : ev.bintype[0] == 'highht'", name = 'bintype_highht'))
    SignalFinalHighht.add(LambdaStr("ev : 0.5 <= ev.biasedDPhi[0]", name = 'biasedDPhiGT0p5'))

    return SignalFinal
 
def SingleMuLooseSelection(datamc,pd,hlt):

    SingleMuLoose = EventSelectionAll(name = 'SingleMuLoose')

    ##______________________________________________________________||
    ## SingleMu loose
    SingleMuLoose.add(LambdaStr("ev : ev.cutflow[0] == 'SingleMu'", name = 'cutflowSingleMu'))
    if datamc == 'data' and pd:
        SingleMuLoose.add(LambdaStr("ev : ev.PrimaryDataset[0] == 'SingleMuon'", name = 'PDSingleMuon'))

    return SingleMuLoose

def SingleMuFinalSelection(datamc,pd,hlt):

    SingleMuFinal = EventSelectionAll(name = 'SingleMuFinal')

    ##______________________________________________________________||
    ## SingleMu final
    SingleMuFinal.add(LambdaStr("ev : ev.cutflow[0] == 'SingleMu'", name = 'cutflowSingleMu'))
    SingleMuFinal.add(LambdaStr("ev : ev.muon_relIso03[0] < 0.12", name = 'relIso03LT0p12'))
    if hlt:
        SingleMuFinal.add(HT_SingleMuon())
    SingleMuFinal.add(LambdaStr("ev : ev.nIsoTracksNoMuVeto[0] <= 0", name = 'isoTrackNoMuVeto'))
    if metnohf:
        SingleMuFinal.add(LambdaStr("ev : 30 <= ev.mtwNoHF[0] < 125", name = 'mtwNoHF'))
    else:
        SingleMuFinal.add(LambdaStr("ev : 30 <= ev.mtw[0] < 125", name = 'mtwNoHF'))
    SingleMuFinal.add(LambdaStr("ev : ev.minDelRJetMu[0] >= 0.5", name = 'minDelRJetMu'))

    return SingleMuFinal


def DoubleMuLooseSelection(datamc,pd,hlt):

    DoubleMuLoose = EventSelectionAll(name = 'DoubleMuLoose')

    ##______________________________________________________________||
    ## DoubleMu loose
    DoubleMuLoose.add(LambdaStr("ev : ev.cutflow[0] == 'DoubleMu'", name = 'cutflowDoubleMu'))
    if datamc == 'data' and pd:
        DoubleMuLoose.add(LambdaStr("ev : ev.PrimaryDataset[0] == 'SingleMuon'", name = 'PDSingleMuon'))

    return DoubleMuLoose

def DoubleMuFinalSelection(datamc,pd,hlt):

    DoubleMuFinal = EventSelectionAll(name = 'DoubleMuFinal')

    ##______________________________________________________________||
    ## DoubleMu final
    DoubleMuFinal.add(LambdaStr("ev : ev.cutflow[0] == 'DoubleMu'", name = 'cutflowDoubleMu'))
    DoubleMuFinal.add(LambdaStr("ev : ev.muon_relIso03[0] < 0.12", name = 'relIso03LT0p12'))
    DoubleMuFinal.add(LambdaStr("ev : ev.muon_relIso03[1] < 0.12", name = 'relIso03LT0p12'))
    if hlt:
        DoubleMuFinal.add(HT_SingleMuon())
    DoubleMuFinal.add(LambdaStr("ev : ev.nIsoTracksNoMuVeto[0] <= 0", name = 'isoTrackNoMuVeto'))
    DoubleMuFinal.add(LambdaStr("ev : 66.2 <= ev.mll[0] < 116.2", name = 'mll'))
    DoubleMuFinal.add(LambdaStr("ev : ev.minDelRJetMu[0] >= 0.5", name = 'minDelRJetMu'))

    return DoubleMuFinal

def SingleEleLooseSelection(datamc,pd,hlt):

    SingleEleLoose = EventSelectionAll(name = 'SingleEleLoose')

    ##______________________________________________________________||
    # SingleEle loose
    SingleEleLoose.add(LambdaStr("ev : ev.cutflow[0] == 'SingleEle'", name = 'cutflowSingleEle'))
    if datamc == 'data' and pd:
        SingleEleLoose.add(LambdaStr("ev : ev.PrimaryDataset[0] == 'SingleElectron'", name = 'PDSingleElectron'))

    return SingleEleLoose

def SingleEleFinalSelection(datamc,pd,hlt):

    SingleEleFinal = EventSelectionAll(name = 'SingleEleFinal')

    ##______________________________________________________________||
    # SingleEle final
    SingleEleFinal.add(LambdaStr("ev : ev.cutflow[0] == 'SingleEle'", name = 'cutflowSingleEle'))
    SingleEleFinal.add(LambdaStr("ev : -1.479 < ev.ele_eta[0] < 1.479", name = 'eleBarrel'))
    SingleEleFinal.add(LambdaStr("ev : ev.ele_relIso03[0] < 0.0354", name = 'eleRelIso03'))
    SingleEleFinal.add(LambdaStr("ev : ev.nIsoTracksNoEleVeto[0] <= 0", name = 'isoTrackNoEleVeto'))
    if metnohf:
        SingleEleFinal.add(LambdaStr("ev : 30 <= ev.mtwNoHF[0] < 125", name = 'mtwNoHF'))
    else:
        SingleEleFinal.add(LambdaStr("ev : 30 <= ev.mtw[0] < 125", name = 'mtwNoHF'))
    SingleEleFinal.add(LambdaStr("ev : ev.minDelRJetEle[0] >= 0.5", name = 'minDelRJetEle'))

    return SingleEleFinal 

def DoubleEleLooseSelection(datamc,pd,hlt):

    DoubleEleLoose = EventSelectionAll(name = 'DoubleEleLoose')

    ##______________________________________________________________||
    # DoubleEle loose
    DoubleEleLoose.add(LambdaStr("ev : ev.cutflow[0] == 'DoubleEle'", name = 'cutflowDoubleEle'))
    if datamc == 'data' and pd:
        DoubleEleLoose.add(LambdaStr("ev : ev.PrimaryDataset[0] == 'SingleElectron'", name = 'PDSingleElectron'))

    return DoubleEleLoose

def DoubleEleFinalSelection(datamc,pd,hlt):

    DoubleEleFinal = EventSelectionAll(name = 'DoubleEleFinal')

    ##______________________________________________________________||
    # DoubleEle final
    DoubleEleFinal.add(LambdaStr("ev : ev.cutflow[0] == 'DoubleEle'", name = 'cutflowDoubleEle'))
    DoubleEleFinal.add(LambdaStr("ev : -1.479 < ev.ele_eta[0] < 1.479", name = 'eleBarrel'))
    DoubleEleFinal.add(LambdaStr("ev : -1.479 < ev.ele_eta[1] < 1.479", name = 'eleBarrel'))
    DoubleEleFinal.add(LambdaStr("ev : ev.ele_relIso03[0] < 0.0354", name = 'eleRelIso03'))
    DoubleEleFinal.add(LambdaStr("ev : ev.ele_relIso03[1] < 0.0354", name = 'eleRelIso03'))
    DoubleEleFinal.add(LambdaStr("ev : ev.nIsoTracksNoEleVeto[0] <= 0", name = 'isoTrackNoEleVeto'))
    DoubleEleFinal.add(LambdaStr("ev : 66.2 <= ev.mll[0] < 116.2", name = 'mll'))
    DoubleEleFinal.add(LambdaStr("ev : ev.minDelRJetEle[0] >= 0.5", name = 'minDelRJetEle'))

    return DoubleEleFinal

def SinglePhotonLooseSelection(datamc,pd,hlt):

    SinglePhotonLoose = EventSelectionAll(name = 'SinglePhotonLoose')

    ##______________________________________________________________||
    # SinglePhoton loose
    SinglePhotonLoose.add(LambdaStr("ev : ev.cutflow[0] == 'SinglePhoton'", name = 'cutflowSinglePhoton'))
    if datamc == 'data' and pd:
        SinglePhotonLoose.add(LambdaStr("ev : ev.PrimaryDataset[0] == 'SinglePhoton'", name = 'PDSinglePhoton'))

    SinglePhotonLooseBintypes = EventSelectionAny(name = 'SinglePhotonLooseBintypes')
    SinglePhotonLoose.add(SinglePhotonLooseBintypes)

    SinglePhotonLooseMonojet = EventSelectionAll(name = 'SinglePhotonLooseMonojet')
    SinglePhotonLooseAsymjet = EventSelectionAll(name = 'SinglePhotonLooseAsymjet')
    SinglePhotonLooseSymjet = EventSelectionAll(name = 'SinglePhotonLooseSymjet')
    SinglePhotonLooseHighht = EventSelectionAll(name = 'SinglePhotonLooseHighht')

    SinglePhotonLooseBintypes.add(SinglePhotonLooseMonojet)
    SinglePhotonLooseBintypes.add(SinglePhotonLooseAsymjet)
    SinglePhotonLooseBintypes.add(SinglePhotonLooseSymjet)
    SinglePhotonLooseBintypes.add(SinglePhotonLooseHighht)

    ## SinglePhoton loose - monojet
    SinglePhotonLooseMonojet.add(LambdaStr("ev : ev.bintype[0] == 'monojet'", name = 'bintype_monojet'))

    ## SinglePhoton loose - asymjet
    SinglePhotonLooseAsymjet.add(LambdaStr("ev : ev.bintype[0] == 'asymjet'", name = 'bintype_asymjet'))
    SinglePhotonLooseAsymjet.add(LambdaStr("ev : 0.5 <= ev.alphaT[0]", name = 'alphaTLT0p5'))

    ## SinglePhoton loose- symjet
    SinglePhotonLooseSymjet.add(LambdaStr("ev : ev.bintype[0] == 'symjet'", name = 'bintype_symjet'))
    SinglePhotonLooseSymjet.add(LambdaStr("ev : 0.5 <= ev.alphaT[0]", name = 'alphaTLT0p5'))

    ## SinglePhoton loose- highht
    SinglePhotonLooseHighht.add(LambdaStr("ev : ev.bintype[0] == 'highht'", name = 'bintype_highht'))
    SinglePhotonLooseHighht.add(LambdaStr("ev : 130 <= ev.mht40_pt[0]", name = 'MHTGT130'))

    return SinglePhotonLoose

def SinglePhotonFinalSelection(datamc,pd,hlt):

    SinglePhotonFinal = EventSelectionAll(name = 'SinglePhotonFinal')

    ##______________________________________________________________||
    # SinglePhoton final
    SinglePhotonFinal.add(LambdaStr("ev : ev.cutflow[0] == 'SinglePhoton'", name = 'cutflowSinglePhoton'))
    SinglePhotonFinal.add(LambdaStr("ev : ev.nIsoTracksVeto[0] <= 0", name = 'isoTrackVeto'))
    SinglePhotonFinal.add(LambdaStr("ev : ev.minDelRJetPhoton[0] >= 1.0", name = 'minDelRJetPhoton'))

    SinglePhotonFinalBintypes = EventSelectionAny(name = 'SinglePhotonFinalBintypes')
    SinglePhotonFinal.add(SinglePhotonFinalBintypes)

    SinglePhotonFinalMonojet = EventSelectionAll(name = 'SinglePhotonFinalMonojet')
    SinglePhotonFinalAsymjet = EventSelectionAll(name = 'SinglePhotonFinalAsymjet')
    SinglePhotonFinalSymjet = EventSelectionAll(name = 'SinglePhotonFinalSymjet')
    SinglePhotonFinalHighht = EventSelectionAll(name = 'SinglePhotonFinalHighht')

    SinglePhotonFinalBintypes.add(SinglePhotonFinalMonojet)
    SinglePhotonFinalBintypes.add(SinglePhotonFinalAsymjet)
    SinglePhotonFinalBintypes.add(SinglePhotonFinalSymjet)
    SinglePhotonFinalBintypes.add(SinglePhotonFinalHighht)

    ## SinglePhoton final - monojet
    SinglePhotonFinalMonojet.add(LambdaStr("ev : ev.bintype[0] == 'monojet'", name = 'bintype_monojet'))

    ## SinglePhoton final - asymjet
    SinglePhotonFinalAsymjet.add(LambdaStr("ev : ev.bintype[0] == 'asymjet'", name = 'bintype_asymjet'))
    SinglePhotonFinalAsymjet.add(AlphaTCut())

    ## SinglePhoton - symjet
    SinglePhotonFinalSymjet.add(LambdaStr("ev : ev.bintype[0] == 'symjet'", name = 'bintype_symjet'))
    SinglePhotonFinalSymjet.add(AlphaTCut())

    ## SinglePhoton final - highht
    SinglePhotonFinalHighht.add(LambdaStr("ev : ev.bintype[0] == 'highht'", name = 'bintype_highht'))

    return SinglePhotonFinal


##__________________________________________________________________||
def event_selection(datamc, level,
                    hlt = False, pd = False, met_filters = False, metnohf = False):
    """
    Args:

    datamc: "data" or "mc"

    leve: "noselection" "baseline", "loose", "final"

    hlt: True or False

    pd: True or False

    met_filters: True or False

    metnohf: True or False

    """

    eventSelection = EventSelectionAll(name = 'All')

    if level == 'noselection': return eventSelection

    if datamc == 'data' and hlt and pd:
        eventSelection.add(PD_HLT())

    ##______________________________________________________________||
    # Baseline
    eventSelection.add(LambdaStr("ev : ev.nVert[0] >= 1", name = 'nVertGTOne'))
    eventSelection.add(LambdaStr("ev : ev.nJet100[0] >= 1", name = 'nJetGTOne'))
    eventSelection.add(LambdaStr("ev : ev.ht40[0] >= 150", name = 'HTGT150'))

    if level == 'baseline': return eventSelection

    ##______________________________________________________________||
    # cutflows loose
    cutflowsLoose = EventSelectionAny(name = 'cutflowsLoose')
    eventSelection.add(cutflowsLoose)

    SignalLoose = SignalLooseSelection(datamc,pd,hlt)
    SingleMuLoose = SingleMuLooseSelection(datamc,pd,hlt)
    DoubleMuLoose = DoubleMuLooseSelection(datamc,pd,hlt)
    SingleEleLoose = SingleEleLooseSelection(datamc,pd,hlt)
    DoubleEleLoose = DoubleEleLooseSelection(datamc,pd,hlt)
    SinglePhotonLoose = SinglePhotonLooseSelection(datamc,pd,hlt)
    cutflowsLoose.add(SignalLoose)
    cutflowsLoose.add(SingleMuLoose)
    cutflowsLoose.add(DoubleMuLoose)
    cutflowsLoose.add(SingleEleLoose)
    cutflowsLoose.add(DoubleEleLoose)
    cutflowsLoose.add(SinglePhotonLoose)

    if level == 'loose': return eventSelection

    ##______________________________________________________________||
    if met_filters:
        eventSelection.add(LambdaStr("ev : ev.Flag_goodVertices[0] == 1", name = 'goodVertex'))
        eventSelection.add(LambdaStr("ev : ev.Flag_CSCTightHaloFilter[0] ==1", name = 'CSCTightHaloFilter'))
        if datamc == 'data':
            eventSelection.add(LambdaStr("ev : ev.hbheFilterNew[0] == 1", name = 'hbheFilterNew'))
        else:
            eventSelection.add(LambdaStr("ev : ev.Flag_HBHENoiseFilter[0] == 1", name = 'HBHENoiseFilter'))

    ##______________________________________________________________||
    eventSelection.add(LambdaStr("ev : ev.nJet40Fwd[0] == 0", name = 'FwJetVeto'))
    eventSelection.add(LambdaStr("ev : ev.nJet40failedId[0] == 0", name = 'JetIDVeto'))
    eventSelection.add(LambdaStr("ev : ev.ht40[0] >= 200", name = 'HTGT200'))

    ##______________________________________________________________||
    if metnohf:
        eventSelection.add(LambdaStr("ev : ev.MhtOverMetNoXNoHF[0] < 1.25", name = 'MhtOverMetNoXNoHF'))
    else:
        eventSelection.add(LambdaStr("ev : ev.MhtOverMetNoX] < 1.25", name = 'MhtOverMetNoX'))

    ##______________________________________________________________||
    cutflowsFinal = EventSelectionAny(name = 'cutflowsFinal')
    eventSelection.add(cutflowsFinal)

    SignalFinal = SignalFinalSelection(datamc,pd,hlt)
    SingleMuFinal = SingleMuFinalSelection(datamc,pd,hlt)
    DoubleMuFinal = DoubleMuFinalSelection(datamc,pd,hlt)
    SingleEleFinal = SingleEleFinalSelection(datamc,pd,hlt)
    DoubleEleFinal = DoubleEleFinalSelection(datamc,pd,hlt)
    SinglePhotonFinal = SinglePhotonFinalSelection(datamc,pd,hlt)
    cutflowsFinal.add(SignalFinal)
    cutflowsFinal.add(SingleMuFinal)
    cutflowsFinal.add(DoubleMuFinal)
    cutflowsFinal.add(SingleEleFinal)
    cutflowsFinal.add(DoubleEleFinal)
    cutflowsFinal.add(SinglePhotonFinal)

    'final'
    return eventSelection

##__________________________________________________________________||
