
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
def PD_HLT(AllClass = EventSelectionAll, AnyClass = EventSelectionAny):

    ret = AnyClass(name = 'PD_HLT')

    pd = AllClass(name = 'MET')
    pd.add(LambdaStr("ev : ev.PrimaryDataset[0] == 'MET'", name = 'PDMET'))
    hlt = AnyClass(name = 'MET_HLT')
    ## hlt.add(LambdaStr("ev : ev.HLT_PFMET90_PFMHT90_IDTight[0]", name = 'HLT_PFMET90_PFMHT90_IDTight'))
    hlt.add(LambdaStr("ev : ev.HLT_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight[0]", name = 'HLT_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight'))
    hlt.add(LambdaStr("ev : ev.HLT_PFMETNoMu120_JetIdCleaned_PFMHTNoMu120_IDTight[0]", name = 'HLT_PFMETNoMu120_JetIdCleaned_PFMHTNoMu120_IDTight'))
    pd.add(hlt)
    ret.add(pd)

    pd = AllClass(name = 'HTMHT')
    pd.add(LambdaStr("ev : ev.PrimaryDataset[0] == 'HTMHT'", name = 'PDHTMHT'))
    hlt = AnyClass(name = 'HTMHT_HLT')
    hlt.add(LambdaStr("ev : ev.HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57[0]", name = 'HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57'))
    hlt.add(LambdaStr("ev : ev.HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63[0]", name = 'HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63'))
    hlt.add(LambdaStr("ev : ev.HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55[0]", name = 'HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55'))
    hlt.add(LambdaStr("ev : ev.HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58[0]", name = 'HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58'))
    hlt.add(LambdaStr("ev : ev.HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53[0]", name = 'HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53'))
    hlt.add(LambdaStr("ev : ev.HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54[0]", name = 'HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54'))
    hlt.add(LambdaStr("ev : ev.HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52[0]", name = 'HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52'))
    hlt.add(LambdaStr("ev : ev.HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53[0]", name = 'HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53'))
    hlt.add(LambdaStr("ev : ev.HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51[0]", name = 'HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51'))
    hlt.add(LambdaStr("ev : ev.HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52[0]", name = 'HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52'))
    pd.add(hlt)
    ret.add(pd)

    pd = AllClass(name = 'JetHT')
    pd.add(LambdaStr("ev : ev.PrimaryDataset[0] == 'JetHT'", name = 'PDJetHT'))
    hlt = AnyClass(name = 'JetHT_HLT')
    hlt.add(LambdaStr("ev : ev.HLT_PFHT800[0]", name = 'HLT_PFHT800'))
    pd.add(hlt)
    ret.add(pd)

    pd = AllClass(name = 'SingleMuon')
    pd.add(LambdaStr("ev : ev.PrimaryDataset[0] == 'SingleMuon'", name = 'PDSingleMuon'))
    hlt = AnyClass(name = 'SingleMuon_HLT')
    hlt.add(LambdaStr("ev : ev.HLT_IsoMu17_eta2p1[0]", name = 'HLT_IsoMu17_eta2p1'))
    hlt.add(LambdaStr("ev : ev.HLT_IsoMu20[0]", name = 'HLT_IsoMu20'))
    hlt.add(LambdaStr("ev : ev.HLT_IsoMu24_eta2p1[0]", name = 'HLT_IsoMu24_eta2p1'))
    pd.add(hlt)
    ret.add(pd)

    pd = AllClass(name = 'SingleElectron')
    pd.add(LambdaStr("ev : ev.PrimaryDataset[0] == 'SingleElectron'", name = 'PDSingleElectron'))
    hlt = AnyClass(name = 'SingleElectron_HLT')
    hlt.add(LambdaStr("ev : ev.HLT_Ele22_WPLoose_Gsf[0]", name = 'HLT_Ele22_WPLoose_Gsf'))
    hlt.add(LambdaStr("ev : ev.HLT_Ele23_WPLoose_Gsf[0]", name = 'HLT_Ele23_WPLoose_Gsf'))
    hlt.add(LambdaStr("ev : ev.HLT_Ele27_eta2p1_WPLoose_Gsf[0]", name = 'HLT_Ele27_eta2p1_WPLoose_Gsf'))
    pd.add(hlt)
    ret.add(pd)

    pd = AllClass(name = 'SinglePhoton')
    pd.add(LambdaStr("ev : ev.PrimaryDataset[0] == 'SinglePhoton'", name = 'PDSinglePhoton'))
    hlt = AnyClass(name = 'SinglePhoton_HLT')
    hlt.add(LambdaStr("ev : ev.HLT_Photon120[0]", name = 'HLT_Photon120'))
    hlt.add(LambdaStr("ev : ev.HLT_Photon125[0]", name = 'HLT_Photon125'))
    hlt.add(LambdaStr("ev : ev.HLT_Photon175[0]", name = 'HLT_Photon175'))
    pd.add(hlt)
    ret.add(pd)

    return ret

##__________________________________________________________________||
def AlphaTCutLoose(AllClass = EventSelectionAll, AnyClass = EventSelectionAny):

    ret = AnyClass(name = 'AlphaTCutLoose')

    htbin = AllClass(name = 'HT200to250')
    htbin.add(LambdaStr("ev : 200 <= ev.ht40[0] < 250", name = 'HTin200to250'))
    htbin.add(LambdaStr("ev : 0.60 <= ev.alphaT[0]", name = 'alphaTGT0p65'))
    ret.add(htbin)

    htbin = AllClass(name = 'HT250to300')
    htbin.add(LambdaStr("ev : 250 <= ev.ht40[0] < 300", name = 'HTin250to300'))
    htbin.add(LambdaStr("ev : 0.55 <= ev.alphaT[0]", name = 'alphaTGT0p60'))
    ret.add(htbin)

    htbin = AllClass(name = 'HT300to800')
    htbin.add(LambdaStr("ev : 300 <= ev.ht40[0] < 800", name = 'HTin300to800'))
    htbin.add(LambdaStr("ev : 0.50 <= ev.alphaT[0]", name = 'alphaTGT0p55'))
    ret.add(htbin)

    return ret

##__________________________________________________________________||
def AlphaTCut(AllClass = EventSelectionAll, AnyClass = EventSelectionAny):

    ret = AnyClass(name = 'AlphaTCut')

    htbin = AllClass(name = 'HT200to250')
    htbin.add(LambdaStr("ev : 200 <= ev.ht40[0] < 250", name = 'HTin200to250'))
    htbin.add(LambdaStr("ev : 0.65 <= ev.alphaT[0]", name = 'alphaTGT0p65'))
    ret.add(htbin)

    htbin = AllClass(name = 'HT250to300')
    htbin.add(LambdaStr("ev : 250 <= ev.ht40[0] < 300", name = 'HTin250to300'))
    htbin.add(LambdaStr("ev : 0.60 <= ev.alphaT[0]", name = 'alphaTGT0p60'))
    ret.add(htbin)

    htbin = AllClass(name = 'HT300to350')
    htbin.add(LambdaStr("ev : 300 <= ev.ht40[0] < 350", name = 'HTin300to350'))
    htbin.add(LambdaStr("ev : 0.55 <= ev.alphaT[0]", name = 'alphaTGT0p55'))
    ret.add(htbin)

    htbin = AllClass(name = 'HT350to400')
    htbin.add(LambdaStr("ev : 350 <= ev.ht40[0] < 400", name = 'HTin350to400'))
    htbin.add(LambdaStr("ev : 0.53 <= ev.alphaT[0]", name = 'alphaTGT0p53'))
    ret.add(htbin)

    htbin = AllClass(name = 'HT400to800')
    htbin.add(LambdaStr("ev : 400 <= ev.ht40[0] < 800", name = 'HTin400to800'))
    htbin.add(LambdaStr("ev : 0.52 <= ev.alphaT[0]", name = 'alphaTGT0p52'))
    ret.add(htbin)

    return ret

##__________________________________________________________________||
def HT_HLTAlphaT(AllClass = EventSelectionAll, AnyClass = EventSelectionAny):

    ret = AnyClass(name = 'HT_HLTAlphaT')

    htbin = AllClass(name = 'HT200to250')
    htbin.add(LambdaStr("ev : 200 <= ev.ht40[0] < 250", name = 'HTin200to250'))
    hlt = AnyClass(name = 'HLTAlphaTHT200')
    hlt.add(LambdaStr("ev : ev.HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57[0]", name = 'HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57'))
    hlt.add(LambdaStr("ev : ev.HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63[0]", name = 'HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63'))
    htbin.add(hlt)
    ret.add(htbin)

    htbin = AllClass(name = 'HT250to300')
    htbin.add(LambdaStr("ev : 250 <= ev.ht40[0] < 300", name = 'HTin250to300'))
    hlt = AnyClass(name = 'HLTAlphaTHT250')
    hlt.add(LambdaStr("ev : ev.HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55[0]", name = 'HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55'))
    hlt.add(LambdaStr("ev : ev.HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58[0]", name = 'HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58'))
    htbin.add(hlt)
    ret.add(htbin)

    htbin = AllClass(name = 'HT300to350')
    htbin.add(LambdaStr("ev : 300 <= ev.ht40[0] < 350", name = 'HTin300to350'))
    hlt = AnyClass(name = 'HLTAlphaTHT300')
    hlt.add(LambdaStr("ev : ev.HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53[0]", name = 'HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53'))
    hlt.add(LambdaStr("ev : ev.HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54[0]", name = 'HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54'))
    htbin.add(hlt)
    ret.add(htbin)

    htbin = AllClass(name = 'HT350to400')
    htbin.add(LambdaStr("ev : 350 <= ev.ht40[0] < 400", name = 'HTin350to400'))
    hlt = AnyClass(name = 'HLTAlphaTHT350')
    hlt.add(LambdaStr("ev : ev.HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52[0]", name = 'HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52'))
    hlt.add(LambdaStr("ev : ev.HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53[0]", name = 'HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53'))
    htbin.add(hlt)
    ret.add(htbin)

    htbin = AllClass(name = 'HT400to800')
    htbin.add(LambdaStr("ev : 400 <= ev.ht40[0] < 800", name = 'HTin400to800'))
    hlt = AnyClass(name = 'HLTAlphaTHT400')
    hlt.add(LambdaStr("ev : ev.HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51[0]", name = 'HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51'))
    hlt.add(LambdaStr("ev : ev.HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52[0]", name = 'HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52'))
    htbin.add(hlt)
    ret.add(htbin)

    return ret

##__________________________________________________________________||
def HLT_SingleMuon(AllClass = EventSelectionAll, AnyClass = EventSelectionAny):
    ret = AnyClass(name = 'HLT_SingleMuon')
    ret.add(LambdaStr("ev : ev.HLT_IsoMu17_eta2p1[0]", name = 'HLT_IsoMu17_eta2p1'))
    ret.add(LambdaStr("ev : ev.HLT_IsoMu20[0]", name = 'HLT_IsoMu20'))
    ret.add(LambdaStr("ev : ev.HLT_IsoMu24_eta2p1[0]", name = 'HLT_IsoMu24_eta2p1'))
    return ret

##__________________________________________________________________||
def event_selection_str(eventSelection):
    out = event_selection_io(eventSelection)
    return out.getvalue()

##__________________________________________________________________||
def event_selection_io(eventSelection, out = None, prep = ''):

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

    out.write(prep)

    if isinstance(eventSelection, LambdaStr):
        out.write(print_name(eventSelection))
        out.write(' ')
        out.write(eventSelection.lambda_str)
        out.write('\n')
        return out

    if isinstance(eventSelection, EventSelectionAll):
        out.write(print_name(eventSelection))
        out.write('\n')
        for e in eventSelection.selections:
            event_selection_io(e, out, prep + '  ')
        return out

    if isinstance(eventSelection, EventSelectionAny):
        out.write(print_name(eventSelection))
        out.write('\n')
        for e in eventSelection.selections:
            event_selection_io(e, out, prep + '  ')
        return out

    out.write(print_name(eventSelection))
    out.write('\n')

    return out

##__________________________________________________________________||
def BaselineSelection(AllClass = EventSelectionAll, AnyClass = EventSelectionAny):

    ret = AllClass(name = 'Baseline')

    ret.add(LambdaStr("ev : ev.nJet100[0] >= 1", name = 'nJetGTOne'))
    ret.add(LambdaStr("ev : ev.ht40[0] >= 150", name = 'HTGT150'))

    return ret

##__________________________________________________________________||
def MetFilters(datamc,
               AllClass = EventSelectionAll, AnyClass = EventSelectionAny):

    ret = AllClass(name = 'MetFilters')

    ret.add(LambdaStr("ev : ev.Flag_goodVertices[0] == 1", name = 'goodVertex'))
    ret.add(LambdaStr("ev : ev.Flag_CSCTightHaloFilter[0] ==1", name = 'CSCTightHaloFilter'))
    ret.add(LambdaStr("ev : ev.Flag_eeBadScFilter[0] ==1", name = 'eeBadScFilter'))
    ret.add(LambdaStr("ev : ev.Flag_HBHENoiseFilter[0] == 1", name = 'HBHENoiseFilter'))
    if datamc == 'data':
        ret.add(LambdaStr("ev : ev.Flag_HBHENoiseIsoFilter[0] == 1", name = 'HBHENoiseIsoFilter'))

    return ret

##__________________________________________________________________||
def UniquePromptPhotonPhaseSpaceInQCDandGJets(AllClass = EventSelectionAll, AnyClass = EventSelectionAny):

    ret = AllClass(name = 'UniquePromptPhotonPhaseSpaceInQCDandGJets')

    processes = AnyClass(name = 'GenProcesses')
    ret.add(processes)

    qcd = AllClass(name = 'GenProcessQCD')
    gjets = AllClass(name = 'GenProcessGJets')
    other = AllClass(name = 'GenProcessesNoQCDorGJets')

    processes.add(qcd)
    processes.add(gjets)
    processes.add(other)

    ## QCD
    qcd.add(LambdaStr("ev : ev.GenProcess[0] == 'QCD'", name = 'process_QCD'))
    qcd.add(LambdaStr("ev : ev.nPromptDirectGenPhotons[0] == 0", name = 'nPromptDirectGenPhotonsEQ0'))

    ## GJets
    gjets.add(LambdaStr("ev : ev.GenProcess[0] == 'GJets'", name = 'process_GJets'))
    gjets.add(LambdaStr("ev : ev.nPromptDirectGenPhotons[0] >= 1", name = 'nPromptDirectGenPhotonsGE1'))

    ## Other
    other.add(LambdaStr("ev : ev.GenProcess[0] not in ('QCD', 'GJets')", name = 'process_not_QCD_or_GJets'))

    return ret

##__________________________________________________________________||
def CommonFinalSelection(metnohf,
                         AllClass = EventSelectionAll, AnyClass = EventSelectionAny):

    ret = AllClass(name = 'CommonFinal')

    ret.add(LambdaStr("ev : ev.nJet40Fwd[0] == 0", name = 'FwJetVeto'))
    ret.add(LambdaStr("ev : ev.nJet40failedId[0] == 0", name = 'JetIDVeto'))
    ret.add(LambdaStr("ev : ev.ht40[0] >= 200", name = 'HTGT200'))
    ret.add(LambdaStr("ev : -2.5 < ev.jet_eta[0] < 2.5", name = 'LeadJetEtaLT2p5'))
    ret.add(LambdaStr("ev : ev.jet_chHEF[0] >= 0.1", name = 'LeadJetChHEFGT0p1'))

    if metnohf:
        ret.add(LambdaStr("ev : ev.MhtOverMetNoXNoHF[0] < 1.25", name = 'MhtOverMetNoXNoHF'))
    else:
        ret.add(LambdaStr("ev : ev.MhtOverMetNoX[0] < 1.25", name = 'MhtOverMetNoX'))

    return ret

##__________________________________________________________________||
def SignalPD(AllClass = EventSelectionAll, AnyClass = EventSelectionAny):
    ret = AllClass(name = 'SignalPD')
    ret.add(LambdaStr("ev : ev.cutflowId[0] == 1 # 'Signal'", name = 'cutflowSignal'))
    ret.add(LambdaStr("ev : ev.PrimaryDataset[0] in ('MET', 'HTMHT', 'JetHT')", name = 'PDMetHtmhtJetht'))
    return ret

##__________________________________________________________________||
def SignalLooseSelection(AllClass = EventSelectionAll, AnyClass = EventSelectionAny):

    ret = AllClass(name = 'SignalLoose')

    ret.add(LambdaStr("ev : ev.cutflowId[0] == 1 # 'Signal'", name = 'cutflowSignal'))
    ret.add(LambdaStr("ev : ev.ht40[0] >= 200", name = 'HTGT200'))

    bintypes = AnyClass(name = 'SignalLooseBintypes')
    ret.add(bintypes)

    monojet = AllClass(name = 'SignalLooseMonojet')
    asymjet = AllClass(name = 'SignalLooseAsymjet')
    symjet = AllClass(name = 'SignalLooseSymjet')
    highht = AllClass(name = 'SignalLooseHighht')

    bintypes.add(monojet)
    bintypes.add(asymjet)
    bintypes.add(symjet)
    bintypes.add(highht)

    ## monojet
    monojet.add(LambdaStr("ev : ev.bintypeId[0] == 1 # 'monojet'", name = 'bintype_monojet'))

    ## asymjet
    asymjet.add(LambdaStr("ev : ev.bintypeId[0] == 2 # 'asymjet'", name = 'bintype_asymjet'))
    asymjet.add(AlphaTCutLoose())

    ## symjet
    symjet.add(LambdaStr("ev : ev.bintypeId[0] == 3 # 'symjet'", name = 'bintype_symjet'))
    symjet.add(AlphaTCutLoose())

    ## highht
    highht.add(LambdaStr("ev : ev.bintypeId[0] == 4 # 'highht'", name = 'bintype_highht'))
    highht.add(LambdaStr("ev : 130 <= ev.mht40_pt[0]", name = 'MHTGT130'))

    return ret

##__________________________________________________________________||
def SignalFinalSelection(AllClass = EventSelectionAll, AnyClass = EventSelectionAny):

    ret = AllClass(name = 'SignalFinal')

    ret.add(LambdaStr("ev : ev.cutflowId[0] == 1 # 'Signal'", name = 'cutflowSignal'))
    ret.add(LambdaStr("ev : ev.nIsoTracksVeto[0] <= 0", name = 'isoTrackVeto'))

    bintypes = AnyClass(name = 'SignalBintypes')
    ret.add(bintypes)

    monojet = AllClass(name = 'SignalFinalMonojet')
    asymjet = AllClass(name = 'SignalFinalAsymjet')
    symjet = AllClass(name = 'SignalFinalSymjet')
    highht = AllClass(name = 'SignalFinalHighht')

    bintypes.add(monojet)
    bintypes.add(asymjet)
    bintypes.add(symjet)
    bintypes.add(highht)

    ## monojet
    monojet.add(LambdaStr("ev : ev.bintypeId[0] == 1 # 'monojet'", name = 'bintype_monojet'))

    ## asymjet
    asymjet.add(LambdaStr("ev : ev.bintypeId[0] == 2 # 'asymjet'", name = 'bintype_asymjet'))
    asymjet.add(AlphaTCut())
    asymjet.add(LambdaStr("ev : 0.5 <= ev.biasedDPhi[0]", name = 'biasedDPhiGT0p5'))

    ## symjet
    symjet.add(LambdaStr("ev : ev.bintypeId[0] == 3 # 'symjet'", name = 'bintype_symjet'))
    symjet.add(AlphaTCut())
    symjet.add(LambdaStr("ev : 0.5 <= ev.biasedDPhi[0]", name = 'biasedDPhiGT0p5'))

    ## highht
    highht.add(LambdaStr("ev : ev.bintypeId[0] == 4 # 'highht'", name = 'bintype_highht'))
    highht.add(LambdaStr("ev : 0.5 <= ev.biasedDPhi[0]", name = 'biasedDPhiGT0p5'))

    return ret
 
##__________________________________________________________________||
def SingleMuPD(AllClass = EventSelectionAll, AnyClass = EventSelectionAny):
    ret = AllClass(name = 'SingleMuPD')
    ret.add(LambdaStr("ev : ev.cutflowId[0] == 2 # 'SingleMu'", name = 'cutflowSingleMu'))
    ret.add(LambdaStr("ev : ev.PrimaryDataset[0] == 'SingleMuon'", name = 'PDSingleMuon'))
    return ret

##__________________________________________________________________||
def SingleMuLooseSelection(AllClass = EventSelectionAll, AnyClass = EventSelectionAny):

    ret = AllClass(name = 'SingleMuLoose')
    ret.add(LambdaStr("ev : ev.cutflowId[0] == 2 # 'SingleMu'", name = 'cutflowSingleMu'))
    return ret

##__________________________________________________________________||
def SingleMuFinalSelection(hlt, metnohf,
                           AllClass = EventSelectionAll, AnyClass = EventSelectionAny):

    ret = AllClass(name = 'SingleMuFinal')

    ret.add(LambdaStr("ev : ev.cutflowId[0] == 2 # 'SingleMu'", name = 'cutflowSingleMu'))
    ret.add(LambdaStr("ev : ev.muon_relIso03[0] < 0.12", name = 'relIso03LT0p12'))
    if hlt:
        ret.add(HLT_SingleMuon())
    ret.add(LambdaStr("ev : ev.nIsoTracksNoMuVeto[0] <= 0", name = 'isoTrackNoMuVeto'))
    if metnohf:
        ret.add(LambdaStr("ev : 30 <= ev.mtwNoHF[0] < 125", name = 'mtwNoHF'))
    else:
        ret.add(LambdaStr("ev : 30 <= ev.mtw[0] < 125", name = 'mtw'))
    ret.add(LambdaStr("ev : ev.minDelRJetMu[0] >= 0.5", name = 'minDelRJetMu'))

    return ret


##__________________________________________________________________||
def DoubleMuPD(AllClass = EventSelectionAll, AnyClass = EventSelectionAny):
    ret = AllClass(name = 'DoubleMuPD')
    ret.add(LambdaStr("ev : ev.cutflowId[0] == 3 # 'DoubleMu'", name = 'cutflowDoubleMu'))
    ret.add(LambdaStr("ev : ev.PrimaryDataset[0] == 'SingleMuon'", name = 'PDSingleMuon'))
    return ret

##__________________________________________________________________||
def DoubleMuLooseSelection(AllClass = EventSelectionAll, AnyClass = EventSelectionAny):

    ret = AllClass(name = 'DoubleMuLoose')
    ret.add(LambdaStr("ev : ev.cutflowId[0] == 3 # 'DoubleMu'", name = 'cutflowDoubleMu'))
    return ret

##__________________________________________________________________||
def DoubleMuFinalSelection(hlt,
                           AllClass = EventSelectionAll, AnyClass = EventSelectionAny):

    ret = AllClass(name = 'DoubleMuFinal')

    ret.add(LambdaStr("ev : ev.cutflowId[0] == 3 # 'DoubleMu'", name = 'cutflowDoubleMu'))
    ret.add(LambdaStr("ev : ev.muon_relIso03[0] < 0.12", name = 'relIso03LT0p12'))
    ret.add(LambdaStr("ev : ev.muon_relIso03[1] < 0.12", name = 'relIso03LT0p12'))
    if hlt:
        ret.add(HLT_SingleMuon())
    ret.add(LambdaStr("ev : ev.nIsoTracksNoMuVeto[0] <= 0", name = 'isoTrackNoMuVeto'))
    ret.add(LambdaStr("ev : 66.2 <= ev.mll[0] < 116.2", name = 'mll'))
    ret.add(LambdaStr("ev : ev.minDelRJetMu[0] >= 0.5", name = 'minDelRJetMu'))

    return ret

##__________________________________________________________________||
def SingleElePD(AllClass = EventSelectionAll, AnyClass = EventSelectionAny):
    ret = AllClass(name = 'SingleElePD')
    ret.add(LambdaStr("ev : ev.cutflowId[0] == 4 # 'SingleEle'", name = 'cutflowSingleEle'))
    ret.add(LambdaStr("ev : ev.PrimaryDataset[0] == 'SingleElectron'", name = 'PDSingleElectron'))
    return ret

##__________________________________________________________________||
def SingleEleLooseSelection(AllClass = EventSelectionAll, AnyClass = EventSelectionAny):

    ret = AllClass(name = 'SingleEleLoose')
    ret.add(LambdaStr("ev : ev.cutflowId[0] == 4 # 'SingleEle'", name = 'cutflowSingleEle'))
    return ret

##__________________________________________________________________||
def SingleEleFinalSelection(metnohf,
                            AllClass = EventSelectionAll, AnyClass = EventSelectionAny):

    ret = AllClass(name = 'SingleEleFinal')

    ret.add(LambdaStr("ev : ev.cutflowId[0] == 4 # 'SingleEle'", name = 'cutflowSingleEle'))
    ret.add(LambdaStr("ev : -1.479 < ev.ele_eta[0] < 1.479", name = 'eleBarrel'))
    ret.add(LambdaStr("ev : ev.ele_relIso03[0] < 0.0354", name = 'eleRelIso03'))
    ret.add(LambdaStr("ev : ev.nIsoTracksNoEleVeto[0] <= 0", name = 'isoTrackNoEleVeto'))
    if metnohf:
        ret.add(LambdaStr("ev : 30 <= ev.mtwNoHF[0] < 125", name = 'mtwNoHF'))
    else:
        ret.add(LambdaStr("ev : 30 <= ev.mtw[0] < 125", name = 'mtw'))
    ret.add(LambdaStr("ev : ev.minDelRJetEle[0] >= 0.5", name = 'minDelRJetEle'))

    return ret 

##__________________________________________________________________||
def DoubleElePD(AllClass = EventSelectionAll, AnyClass = EventSelectionAny):
    ret = AllClass(name = 'DoubleElePD')
    ret.add(LambdaStr("ev : ev.cutflowId[0] == 5 # 'DoubleEle'", name = 'cutflowDoubleEle'))
    ret.add(LambdaStr("ev : ev.PrimaryDataset[0] == 'SingleElectron'", name = 'PDSingleElectron'))
    return ret

##__________________________________________________________________||
def DoubleEleLooseSelection(AllClass = EventSelectionAll, AnyClass = EventSelectionAny):

    ret = AllClass(name = 'DoubleEleLoose')
    ret.add(LambdaStr("ev : ev.cutflowId[0] == 5 # 'DoubleEle'", name = 'cutflowDoubleEle'))
    return ret

##__________________________________________________________________||
def DoubleEleFinalSelection(AllClass = EventSelectionAll, AnyClass = EventSelectionAny):

    ret = AllClass(name = 'DoubleEleFinal')

    ret.add(LambdaStr("ev : ev.cutflowId[0] == 5 # 'DoubleEle'", name = 'cutflowDoubleEle'))
    ret.add(LambdaStr("ev : -1.479 < ev.ele_eta[0] < 1.479", name = 'eleBarrel'))
    ret.add(LambdaStr("ev : -1.479 < ev.ele_eta[1] < 1.479", name = 'eleBarrel'))
    ret.add(LambdaStr("ev : ev.ele_relIso03[0] < 0.0354", name = 'eleRelIso03'))
    ret.add(LambdaStr("ev : ev.ele_relIso03[1] < 0.0354", name = 'eleRelIso03'))
    ret.add(LambdaStr("ev : ev.nIsoTracksNoEleVeto[0] <= 0", name = 'isoTrackNoEleVeto'))
    ret.add(LambdaStr("ev : 66.2 <= ev.mll[0] < 116.2", name = 'mll'))
    ret.add(LambdaStr("ev : ev.minDelRJetEle[0] >= 0.5", name = 'minDelRJetEle'))

    return ret

##__________________________________________________________________||
def SinglePhotonPD(AllClass = EventSelectionAll, AnyClass = EventSelectionAny):
    ret = AllClass(name = 'SinglePhotonPD')
    ret.add(LambdaStr("ev : ev.cutflowId[0] == 6 # 'SinglePhoton'", name = 'cutflowSinglePhoton'))
    ret.add(LambdaStr("ev : ev.PrimaryDataset[0] == 'SinglePhoton'", name = 'PDSinglePhoton'))
    return ret

##__________________________________________________________________||
def SinglePhotonLooseSelection(AllClass = EventSelectionAll, AnyClass = EventSelectionAny):

    ret = AllClass(name = 'SinglePhotonLoose')

    ret.add(LambdaStr("ev : ev.cutflowId[0] == 6 # 'SinglePhoton'", name = 'cutflowSinglePhoton'))

    bintypes = AnyClass(name = 'SinglePhotonLooseBintypes')
    ret.add(bintypes)

    monojet = AllClass(name = 'SinglePhotonLooseMonojet')
    asymjet = AllClass(name = 'SinglePhotonLooseAsymjet')
    symjet = AllClass(name = 'SinglePhotonLooseSymjet')
    highht = AllClass(name = 'SinglePhotonLooseHighht')

    bintypes.add(monojet)
    bintypes.add(asymjet)
    bintypes.add(symjet)
    bintypes.add(highht)

    ## monojet
    monojet.add(LambdaStr("ev : ev.bintypeId[0] == 1 # 'monojet'", name = 'bintype_monojet'))

    ## asymjet
    asymjet.add(LambdaStr("ev : ev.bintypeId[0] == 2 # 'asymjet'", name = 'bintype_asymjet'))
    asymjet.add(LambdaStr("ev : 0.5 <= ev.alphaT[0]", name = 'alphaTLT0p5'))

    ## symjet
    symjet.add(LambdaStr("ev : ev.bintypeId[0] == 3 # 'symjet'", name = 'bintype_symjet'))
    symjet.add(LambdaStr("ev : 0.5 <= ev.alphaT[0]", name = 'alphaTLT0p5'))

    ## highht
    highht.add(LambdaStr("ev : ev.bintypeId[0] == 4 # 'highht'", name = 'bintype_highht'))
    highht.add(LambdaStr("ev : 130 <= ev.mht40_pt[0]", name = 'MHTGT130'))

    return ret

##__________________________________________________________________||
def SinglePhotonFinalSelection(AllClass = EventSelectionAll, AnyClass = EventSelectionAny):

    ret = AllClass(name = 'SinglePhotonFinal')

    ret.add(LambdaStr("ev : ev.cutflowId[0] == 6 # 'SinglePhoton'", name = 'cutflowSinglePhoton'))
    ret.add(LambdaStr("ev : ev.nIsoTracksVeto[0] <= 0", name = 'isoTrackVeto'))
    ret.add(LambdaStr("ev : ev.minDelRJetPhoton[0] >= 1.0", name = 'minDelRJetPhoton'))

    bintypes = AnyClass(name = 'SinglePhotonFinalBintypes')
    ret.add(bintypes)

    monojet = AllClass(name = 'SinglePhotonFinalMonojet')
    asymjet = AllClass(name = 'SinglePhotonFinalAsymjet')
    symjet = AllClass(name = 'SinglePhotonFinalSymjet')
    highht = AllClass(name = 'SinglePhotonFinalHighht')

    bintypes.add(monojet)
    bintypes.add(asymjet)
    bintypes.add(symjet)
    bintypes.add(highht)

    ## monojet
    monojet.add(LambdaStr("ev : ev.bintypeId[0] == 1 # 'monojet'", name = 'bintype_monojet'))

    ## asymjet
    asymjet.add(LambdaStr("ev : ev.bintypeId[0] == 2 # 'asymjet'", name = 'bintype_asymjet'))
    asymjet.add(AlphaTCut())

    ## symjet
    symjet.add(LambdaStr("ev : ev.bintypeId[0] == 3 # 'symjet'", name = 'bintype_symjet'))
    symjet.add(AlphaTCut())

    ## highht
    highht.add(LambdaStr("ev : ev.bintypeId[0] == 4 # 'highht'", name = 'bintype_highht'))

    return ret


##__________________________________________________________________||
def event_selection(datamc,
                    levels = (
                        'PD_HLT',
                        'baseline_kinematics',
                        'cutflows_loose',
                        'cutflows_PD',
                        'met_filters',
                        'unique_promptPhoton_phaseSpace_in_QCD_and_GJets',
                        'final'
                    ),
                    cutflows = (
                        'Signal',
                        'SingleMu',
                        'DoubleMu',
                        'SingleEle',
                        'DoubleEle',
                        'SinglePhoton'
                    ),
                    hlt = False, pd = False, metnohf = False,
                    AllClass = EventSelectionAll, AnyClass = EventSelectionAny):
    """
    Args:

    datamc: 'data' or 'mc'

    levels: a list or tuple of the names of selection levels to include.
            possible levels:
                'PD_HLT',
                'baseline_kinematics'
                'cutflows_loose'
                'cutflows_PD',
                'met_filters'
                'unique_promptPhoton_phaseSpace_in_QCD_and_GJets'
                'final'

    cutflows: a list or tuple of the names of cutflows
              e.g., ('Signal', 'SingleMu', 'DoubleMu', 'SingleEle', 'DoubleEle', 'SinglePhoton')

    hlt: True or False

    pd: True or False

    metnohf: True or False

    """

    eventSelection = AllClass(name = 'All')

    ##______________________________________________________________||
    if 'PD_HLT' in levels:
        if datamc == 'data':
            eventSelection.add(PD_HLT(AllClass = AllClass, AnyClass = AnyClass))

    ##______________________________________________________________||
    if 'baseline_kinematics' in levels:
        eventSelection.add(BaselineSelection(AllClass = AllClass, AnyClass = AnyClass))

    ##______________________________________________________________||
    if 'cutflows_PD' in levels:
        if datamc == 'data':

            ##______________________________________________________||
            cutflows_PD = AnyClass(name = 'cutflows_PD')
            eventSelection.add(cutflows_PD)

            if 'Signal'       in cutflows: cutflows_PD.add(SignalPD(AllClass = AllClass, AnyClass = AnyClass))
            if 'SingleMu'     in cutflows: cutflows_PD.add(SingleMuPD(AllClass = AllClass, AnyClass = AnyClass))
            if 'DoubleMu'     in cutflows: cutflows_PD.add(DoubleMuPD(AllClass = AllClass, AnyClass = AnyClass))
            if 'SingleEle'    in cutflows: cutflows_PD.add(SingleElePD(AllClass = AllClass, AnyClass = AnyClass))
            if 'DoubleEle'    in cutflows: cutflows_PD.add(DoubleElePD(AllClass = AllClass, AnyClass = AnyClass))
            if 'SinglePhoton' in cutflows: cutflows_PD.add(SinglePhotonPD(AllClass = AllClass, AnyClass = AnyClass))
                
    ##______________________________________________________________||
    if 'cutflows_loose' in levels:

        ##__________________________________________________________||
        cutflowsLoose = AnyClass(name = 'cutflowsLoose')
        eventSelection.add(cutflowsLoose)

        if 'Signal'       in cutflows: cutflowsLoose.add(SignalLooseSelection(AllClass = AllClass, AnyClass = AnyClass))
        if 'SingleMu'     in cutflows: cutflowsLoose.add(SingleMuLooseSelection(AllClass = AllClass, AnyClass = AnyClass))
        if 'DoubleMu'     in cutflows: cutflowsLoose.add(DoubleMuLooseSelection(AllClass = AllClass, AnyClass = AnyClass))
        if 'SingleEle'    in cutflows: cutflowsLoose.add(SingleEleLooseSelection(AllClass = AllClass, AnyClass = AnyClass))
        if 'DoubleEle'    in cutflows: cutflowsLoose.add(DoubleEleLooseSelection(AllClass = AllClass, AnyClass = AnyClass))
        if 'SinglePhoton' in cutflows: cutflowsLoose.add(SinglePhotonLooseSelection(AllClass = AllClass, AnyClass = AnyClass))

    ##______________________________________________________________||
    if "met_filters" in levels:
        eventSelection.add(MetFilters(datamc = datamc, AllClass = AllClass, AnyClass = AnyClass))

    ##______________________________________________________________||
    if 'unique_promptPhoton_phaseSpace_in_QCD_and_GJets' in levels:
        if datamc == 'mc':
            eventSelection.add(UniquePromptPhotonPhaseSpaceInQCDandGJets(AllClass = AllClass, AnyClass = AnyClass))

    ##______________________________________________________________||
    if "final" in levels:

        ##__________________________________________________________||
        eventSelection.add(CommonFinalSelection(metnohf = metnohf, AllClass = AllClass, AnyClass = AnyClass))

        ##__________________________________________________________||
        cutflowsFinal = AnyClass(name = 'cutflowsFinal')
        eventSelection.add(cutflowsFinal)

        if 'Signal'       in cutflows: cutflowsFinal.add(SignalFinalSelection(AllClass = AllClass, AnyClass = AnyClass))
        if 'SingleMu'     in cutflows: cutflowsFinal.add(SingleMuFinalSelection(hlt = hlt, metnohf = metnohf, AllClass = AllClass, AnyClass = AnyClass))
        if 'DoubleMu'     in cutflows: cutflowsFinal.add(DoubleMuFinalSelection(hlt = hlt, AllClass = AllClass, AnyClass = AnyClass))
        if 'SingleEle'    in cutflows: cutflowsFinal.add(SingleEleFinalSelection(metnohf = metnohf, AllClass = AllClass, AnyClass = AnyClass))
        if 'DoubleEle'    in cutflows: cutflowsFinal.add(DoubleEleFinalSelection(AllClass = AllClass, AnyClass = AnyClass))
        if 'SinglePhoton' in cutflows: cutflowsFinal.add(SinglePhotonFinalSelection(AllClass = AllClass, AnyClass = AnyClass))

    return eventSelection

##__________________________________________________________________||
