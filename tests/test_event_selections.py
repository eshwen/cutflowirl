from ..event_selections import *
import unittest

##__________________________________________________________________||
def test_event_selection_str(eventSelection):
    out = test_event_selection_io(eventSelection)
    return out.getvalue()

##__________________________________________________________________||
def test_event_selection_io(eventSelection, out = None, prep = ''):

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
            test_event_selection_io(e, out, prep + '  ')
        return out

    if isinstance(eventSelection, EventSelectionAny):
        out.write(print_name(eventSelection))
        out.write('\n')
        for e in eventSelection.selections:
            test_event_selection_io(e, out, prep + '  ')
        return out

    out.write(print_name(eventSelection))
    out.write('\n')
    return out

##__________________________________________________________________||
class Test_event_selection(unittest.TestCase):
    def test_call(self):
        ## self.print_ev_all()

        self.do_arg(arg000, es_arg000)
        self.do_arg(arg001, es_arg001)
        self.do_arg(arg002, es_arg002)
        self.do_arg(arg003, es_arg003)
        self.do_arg(arg004, es_arg004)
        self.do_arg(arg005, es_arg005)
        self.do_arg(arg006, es_arg006)
        self.do_arg(arg007, es_arg007)
        self.do_arg(arg100, es_arg100)
        self.do_arg(arg101, es_arg101)
        self.do_arg(arg102, es_arg102)
        self.do_arg(arg103, es_arg103)
        self.do_arg(arg104, es_arg104)
        self.do_arg(arg105, es_arg105)
        self.do_arg(arg106, es_arg106)
        self.do_arg(arg107, es_arg107)
        self.do_arg(arg200, es_arg200)
        self.do_arg(arg201, es_arg201)
        self.do_arg(arg202, es_arg202)
        self.do_arg(arg203, es_arg203)
        self.do_arg(arg204, es_arg204)

    def do_arg(self, arg, es_arg):
        es = event_selection(**arg)
        self.assertEqual(es_arg.split('\n'), test_event_selection_str(es).split('\n'))

    def print_ev_all(self):
        self.print_ev_for(arg000, 'arg000')
        self.print_ev_for(arg001, 'arg001')
        self.print_ev_for(arg002, 'arg002')
        self.print_ev_for(arg003, 'arg003')
        self.print_ev_for(arg004, 'arg004')
        self.print_ev_for(arg005, 'arg005')
        self.print_ev_for(arg006, 'arg006')
        self.print_ev_for(arg007, 'arg007')
        self.print_ev_for(arg100, 'arg100')
        self.print_ev_for(arg101, 'arg101')
        self.print_ev_for(arg102, 'arg102')
        self.print_ev_for(arg103, 'arg103')
        self.print_ev_for(arg104, 'arg104')
        self.print_ev_for(arg105, 'arg105')
        self.print_ev_for(arg106, 'arg106')
        self.print_ev_for(arg107, 'arg107')
        self.print_ev_for(arg200, 'arg200')
        self.print_ev_for(arg201, 'arg201')
        self.print_ev_for(arg202, 'arg202')
        self.print_ev_for(arg203, 'arg203')
        self.print_ev_for(arg204, 'arg204')

    def print_ev_for(self, arg, argName):
        print '\n'
        print 'es_' + argName + "='''" + test_event_selection_str(event_selection(**arg)) + "'''"

##__________________________________________________________________||
arg000 = dict(datamc = 'data', hlt = False, pd = False, metnohf = False )
arg001 = dict(datamc = 'data', hlt = False, pd = False, metnohf = True  )
arg002 = dict(datamc = 'data', hlt = False, pd = True,  metnohf = False )
arg003 = dict(datamc = 'data', hlt = False, pd = True,  metnohf = True  )
arg004 = dict(datamc = 'data', hlt = True,  pd = False, metnohf = False )
arg005 = dict(datamc = 'data', hlt = True,  pd = False, metnohf = True  )
arg006 = dict(datamc = 'data', hlt = True,  pd = True,  metnohf = False )
arg007 = dict(datamc = 'data', hlt = True,  pd = True,  metnohf = True  )
arg100 = dict(datamc = 'mc', hlt = False, pd = False, metnohf = False )
arg101 = dict(datamc = 'mc', hlt = False, pd = False, metnohf = True  )
arg102 = dict(datamc = 'mc', hlt = False, pd = True,  metnohf = False )
arg103 = dict(datamc = 'mc', hlt = False, pd = True,  metnohf = True  )
arg104 = dict(datamc = 'mc', hlt = True,  pd = False, metnohf = False )
arg105 = dict(datamc = 'mc', hlt = True,  pd = False, metnohf = True  )
arg106 = dict(datamc = 'mc', hlt = True,  pd = True,  metnohf = False )
arg107 = dict(datamc = 'mc', hlt = True,  pd = True,  metnohf = True  )
arg200 = dict(datamc = 'data', levels = ('baseline', 'loose'), cutflows = ('Signal', 'SingleEle'), hlt = False, pd = False, metnohf = False )
arg201 = dict(datamc = 'data', levels = ('baseline', 'loose', 'final'), cutflows = ('Signal', 'SingleEle'), hlt = False, pd = False, metnohf = False )
arg202 = dict(datamc = 'data', levels = ('baseline', 'loose'), cutflows = ( ), hlt = False, pd = False, metnohf = False )
arg203 = dict(datamc = 'data', levels = ('baseline', 'loose', 'final'), cutflows = ( ), hlt = False, pd = False, metnohf = False )
arg204 = dict(datamc = 'data', levels = ('final'), cutflows = ('Signal', 'SingleEle'), hlt = False, pd = False, metnohf = False )

##__________________________________________________________________||
es_arg000='''<All:EventSelectionAll>
  <PD_HLT:EventSelectionAny>
    <MET:EventSelectionAll>
      <PDMET:LambdaStr> ev : ev.PrimaryDataset[0] == 'MET'
      <MET_HLT:EventSelectionAny>
        <HLT_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight:LambdaStr> ev : ev.HLT_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight[0]
        <HLT_PFMETNoMu120_JetIdCleaned_PFMHTNoMu120_IDTight:LambdaStr> ev : ev.HLT_PFMETNoMu120_JetIdCleaned_PFMHTNoMu120_IDTight[0]
    <HTMHT:EventSelectionAll>
      <PDHTMHT:LambdaStr> ev : ev.PrimaryDataset[0] == 'HTMHT'
      <HTMHT_HLT:EventSelectionAny>
        <HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57:LambdaStr> ev : ev.HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57[0]
        <HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63:LambdaStr> ev : ev.HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63[0]
        <HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55:LambdaStr> ev : ev.HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55[0]
        <HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58:LambdaStr> ev : ev.HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58[0]
        <HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53:LambdaStr> ev : ev.HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53[0]
        <HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54:LambdaStr> ev : ev.HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54[0]
        <HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52:LambdaStr> ev : ev.HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52[0]
        <HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53:LambdaStr> ev : ev.HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53[0]
        <HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51:LambdaStr> ev : ev.HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51[0]
        <HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52:LambdaStr> ev : ev.HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52[0]
    <JetHT:EventSelectionAll>
      <PDJetHT:LambdaStr> ev : ev.PrimaryDataset[0] == 'JetHT'
      <JetHT_HLT:EventSelectionAny>
        <HLT_PFHT800:LambdaStr> ev : ev.HLT_PFHT800[0]
    <SingleMuon:EventSelectionAll>
      <PDSingleMuon:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleMuon'
      <SingleMuon_HLT:EventSelectionAny>
        <HLT_IsoMu17_eta2p1:LambdaStr> ev : ev.HLT_IsoMu17_eta2p1[0]
        <HLT_IsoMu20:LambdaStr> ev : ev.HLT_IsoMu20[0]
        <HLT_IsoMu24_eta2p1:LambdaStr> ev : ev.HLT_IsoMu24_eta2p1[0]
    <SingleElectron:EventSelectionAll>
      <PDSingleElectron:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleElectron'
      <SingleElectron_HLT:EventSelectionAny>
        <HLT_Ele22_WPLoose_Gsf:LambdaStr> ev : ev.HLT_Ele22_WPLoose_Gsf[0]
        <HLT_Ele23_WPLoose_Gsf:LambdaStr> ev : ev.HLT_Ele23_WPLoose_Gsf[0]
        <HLT_Ele27_eta2p1_WPLoose_Gsf:LambdaStr> ev : ev.HLT_Ele27_eta2p1_WPLoose_Gsf[0]
    <SinglePhoton:EventSelectionAll>
      <PDSinglePhoton:LambdaStr> ev : ev.PrimaryDataset[0] == 'SinglePhoton'
      <SinglePhoton_HLT:EventSelectionAny>
        <HLT_Photon120:LambdaStr> ev : ev.HLT_Photon120[0]
        <HLT_Photon125:LambdaStr> ev : ev.HLT_Photon125[0]
        <HLT_Photon175:LambdaStr> ev : ev.HLT_Photon175[0]
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
    <SignalLoose:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflowId[0] == 1 # 'Signal'
      <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
      <SignalLooseBintypes:EventSelectionAny>
        <SignalLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SignalLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <AlphaTCutLoose:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT300to800:EventSelectionAll>
              <HTin300to800:LambdaStr> ev : 300 <= ev.ht40[0] < 800
              <alphaTGT0p55:LambdaStr> ev : 0.50 <= ev.alphaT[0]
        <SignalLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <AlphaTCutLoose:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT300to800:EventSelectionAll>
              <HTin300to800:LambdaStr> ev : 300 <= ev.ht40[0] < 800
              <alphaTGT0p55:LambdaStr> ev : 0.50 <= ev.alphaT[0]
        <SignalLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
    <SingleMuLoose:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflowId[0] == 2 # 'SingleMu'
    <DoubleMuLoose:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflowId[0] == 3 # 'DoubleMu'
    <SingleEleLoose:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflowId[0] == 4 # 'SingleEle'
    <DoubleEleLoose:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflowId[0] == 5 # 'DoubleEle'
    <SinglePhotonLoose:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflowId[0] == 6 # 'SinglePhoton'
      <SinglePhotonLooseBintypes:EventSelectionAny>
        <SinglePhotonLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SinglePhotonLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
  <MetFilters:EventSelectionAll>
    <goodVertex:LambdaStr> ev : ev.Flag_goodVertices[0] == 1
    <CSCTightHaloFilter:LambdaStr> ev : ev.Flag_CSCTightHaloFilter[0] ==1
    <eeBadScFilter:LambdaStr> ev : ev.Flag_eeBadScFilter[0] ==1
    <HBHENoiseFilter:LambdaStr> ev : ev.Flag_HBHENoiseFilter[0] == 1
    <HBHENoiseIsoFilter:LambdaStr> ev : ev.Flag_HBHENoiseIsoFilter[0] == 1
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <LeadJetEtaLT2p5:LambdaStr> ev : -2.5 < ev.jet_eta[0] < 2.5
    <LeadJetChHEFGT0p1:LambdaStr> ev : ev.jet_chHEF[0] >= 0.1
    <MhtOverMetNoX:LambdaStr> ev : ev.MhtOverMetNoX[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
    <SignalFinal:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflowId[0] == 1 # 'Signal'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <SignalBintypes:EventSelectionAny>
        <SignalFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SignalFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
    <SingleMuFinal:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflowId[0] == 2 # 'SingleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mtw:LambdaStr> ev : 30 <= ev.mtw[0] < 125
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <DoubleMuFinal:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflowId[0] == 3 # 'DoubleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[1] < 0.12
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <SingleEleFinal:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflowId[0] == 4 # 'SingleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mtw:LambdaStr> ev : 30 <= ev.mtw[0] < 125
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <DoubleEleFinal:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflowId[0] == 5 # 'DoubleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[1] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[1] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <SinglePhotonFinal:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflowId[0] == 6 # 'SinglePhoton'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <minDelRJetPhoton:LambdaStr> ev : ev.minDelRJetPhoton[0] >= 1.0
      <SinglePhotonFinalBintypes:EventSelectionAny>
        <SinglePhotonFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SinglePhotonFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
        <SinglePhotonFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
        <SinglePhotonFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
'''


es_arg001='''<All:EventSelectionAll>
  <PD_HLT:EventSelectionAny>
    <MET:EventSelectionAll>
      <PDMET:LambdaStr> ev : ev.PrimaryDataset[0] == 'MET'
      <MET_HLT:EventSelectionAny>
        <HLT_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight:LambdaStr> ev : ev.HLT_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight[0]
        <HLT_PFMETNoMu120_JetIdCleaned_PFMHTNoMu120_IDTight:LambdaStr> ev : ev.HLT_PFMETNoMu120_JetIdCleaned_PFMHTNoMu120_IDTight[0]
    <HTMHT:EventSelectionAll>
      <PDHTMHT:LambdaStr> ev : ev.PrimaryDataset[0] == 'HTMHT'
      <HTMHT_HLT:EventSelectionAny>
        <HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57:LambdaStr> ev : ev.HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57[0]
        <HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63:LambdaStr> ev : ev.HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63[0]
        <HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55:LambdaStr> ev : ev.HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55[0]
        <HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58:LambdaStr> ev : ev.HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58[0]
        <HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53:LambdaStr> ev : ev.HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53[0]
        <HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54:LambdaStr> ev : ev.HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54[0]
        <HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52:LambdaStr> ev : ev.HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52[0]
        <HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53:LambdaStr> ev : ev.HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53[0]
        <HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51:LambdaStr> ev : ev.HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51[0]
        <HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52:LambdaStr> ev : ev.HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52[0]
    <JetHT:EventSelectionAll>
      <PDJetHT:LambdaStr> ev : ev.PrimaryDataset[0] == 'JetHT'
      <JetHT_HLT:EventSelectionAny>
        <HLT_PFHT800:LambdaStr> ev : ev.HLT_PFHT800[0]
    <SingleMuon:EventSelectionAll>
      <PDSingleMuon:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleMuon'
      <SingleMuon_HLT:EventSelectionAny>
        <HLT_IsoMu17_eta2p1:LambdaStr> ev : ev.HLT_IsoMu17_eta2p1[0]
        <HLT_IsoMu20:LambdaStr> ev : ev.HLT_IsoMu20[0]
        <HLT_IsoMu24_eta2p1:LambdaStr> ev : ev.HLT_IsoMu24_eta2p1[0]
    <SingleElectron:EventSelectionAll>
      <PDSingleElectron:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleElectron'
      <SingleElectron_HLT:EventSelectionAny>
        <HLT_Ele22_WPLoose_Gsf:LambdaStr> ev : ev.HLT_Ele22_WPLoose_Gsf[0]
        <HLT_Ele23_WPLoose_Gsf:LambdaStr> ev : ev.HLT_Ele23_WPLoose_Gsf[0]
        <HLT_Ele27_eta2p1_WPLoose_Gsf:LambdaStr> ev : ev.HLT_Ele27_eta2p1_WPLoose_Gsf[0]
    <SinglePhoton:EventSelectionAll>
      <PDSinglePhoton:LambdaStr> ev : ev.PrimaryDataset[0] == 'SinglePhoton'
      <SinglePhoton_HLT:EventSelectionAny>
        <HLT_Photon120:LambdaStr> ev : ev.HLT_Photon120[0]
        <HLT_Photon125:LambdaStr> ev : ev.HLT_Photon125[0]
        <HLT_Photon175:LambdaStr> ev : ev.HLT_Photon175[0]
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
    <SignalLoose:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflowId[0] == 1 # 'Signal'
      <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
      <SignalLooseBintypes:EventSelectionAny>
        <SignalLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SignalLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <AlphaTCutLoose:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT300to800:EventSelectionAll>
              <HTin300to800:LambdaStr> ev : 300 <= ev.ht40[0] < 800
              <alphaTGT0p55:LambdaStr> ev : 0.50 <= ev.alphaT[0]
        <SignalLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <AlphaTCutLoose:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT300to800:EventSelectionAll>
              <HTin300to800:LambdaStr> ev : 300 <= ev.ht40[0] < 800
              <alphaTGT0p55:LambdaStr> ev : 0.50 <= ev.alphaT[0]
        <SignalLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
    <SingleMuLoose:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflowId[0] == 2 # 'SingleMu'
    <DoubleMuLoose:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflowId[0] == 3 # 'DoubleMu'
    <SingleEleLoose:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflowId[0] == 4 # 'SingleEle'
    <DoubleEleLoose:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflowId[0] == 5 # 'DoubleEle'
    <SinglePhotonLoose:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflowId[0] == 6 # 'SinglePhoton'
      <SinglePhotonLooseBintypes:EventSelectionAny>
        <SinglePhotonLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SinglePhotonLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
  <MetFilters:EventSelectionAll>
    <goodVertex:LambdaStr> ev : ev.Flag_goodVertices[0] == 1
    <CSCTightHaloFilter:LambdaStr> ev : ev.Flag_CSCTightHaloFilter[0] ==1
    <eeBadScFilter:LambdaStr> ev : ev.Flag_eeBadScFilter[0] ==1
    <HBHENoiseFilter:LambdaStr> ev : ev.Flag_HBHENoiseFilter[0] == 1
    <HBHENoiseIsoFilter:LambdaStr> ev : ev.Flag_HBHENoiseIsoFilter[0] == 1
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <LeadJetEtaLT2p5:LambdaStr> ev : -2.5 < ev.jet_eta[0] < 2.5
    <LeadJetChHEFGT0p1:LambdaStr> ev : ev.jet_chHEF[0] >= 0.1
    <MhtOverMetNoXNoHF:LambdaStr> ev : ev.MhtOverMetNoXNoHF[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
    <SignalFinal:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflowId[0] == 1 # 'Signal'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <SignalBintypes:EventSelectionAny>
        <SignalFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SignalFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
    <SingleMuFinal:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflowId[0] == 2 # 'SingleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mtwNoHF:LambdaStr> ev : 30 <= ev.mtwNoHF[0] < 125
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <DoubleMuFinal:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflowId[0] == 3 # 'DoubleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[1] < 0.12
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <SingleEleFinal:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflowId[0] == 4 # 'SingleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mtwNoHF:LambdaStr> ev : 30 <= ev.mtwNoHF[0] < 125
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <DoubleEleFinal:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflowId[0] == 5 # 'DoubleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[1] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[1] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <SinglePhotonFinal:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflowId[0] == 6 # 'SinglePhoton'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <minDelRJetPhoton:LambdaStr> ev : ev.minDelRJetPhoton[0] >= 1.0
      <SinglePhotonFinalBintypes:EventSelectionAny>
        <SinglePhotonFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SinglePhotonFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
        <SinglePhotonFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
        <SinglePhotonFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
'''


es_arg002='''<All:EventSelectionAll>
  <PD_HLT:EventSelectionAny>
    <MET:EventSelectionAll>
      <PDMET:LambdaStr> ev : ev.PrimaryDataset[0] == 'MET'
      <MET_HLT:EventSelectionAny>
        <HLT_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight:LambdaStr> ev : ev.HLT_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight[0]
        <HLT_PFMETNoMu120_JetIdCleaned_PFMHTNoMu120_IDTight:LambdaStr> ev : ev.HLT_PFMETNoMu120_JetIdCleaned_PFMHTNoMu120_IDTight[0]
    <HTMHT:EventSelectionAll>
      <PDHTMHT:LambdaStr> ev : ev.PrimaryDataset[0] == 'HTMHT'
      <HTMHT_HLT:EventSelectionAny>
        <HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57:LambdaStr> ev : ev.HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57[0]
        <HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63:LambdaStr> ev : ev.HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63[0]
        <HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55:LambdaStr> ev : ev.HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55[0]
        <HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58:LambdaStr> ev : ev.HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58[0]
        <HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53:LambdaStr> ev : ev.HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53[0]
        <HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54:LambdaStr> ev : ev.HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54[0]
        <HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52:LambdaStr> ev : ev.HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52[0]
        <HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53:LambdaStr> ev : ev.HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53[0]
        <HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51:LambdaStr> ev : ev.HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51[0]
        <HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52:LambdaStr> ev : ev.HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52[0]
    <JetHT:EventSelectionAll>
      <PDJetHT:LambdaStr> ev : ev.PrimaryDataset[0] == 'JetHT'
      <JetHT_HLT:EventSelectionAny>
        <HLT_PFHT800:LambdaStr> ev : ev.HLT_PFHT800[0]
    <SingleMuon:EventSelectionAll>
      <PDSingleMuon:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleMuon'
      <SingleMuon_HLT:EventSelectionAny>
        <HLT_IsoMu17_eta2p1:LambdaStr> ev : ev.HLT_IsoMu17_eta2p1[0]
        <HLT_IsoMu20:LambdaStr> ev : ev.HLT_IsoMu20[0]
        <HLT_IsoMu24_eta2p1:LambdaStr> ev : ev.HLT_IsoMu24_eta2p1[0]
    <SingleElectron:EventSelectionAll>
      <PDSingleElectron:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleElectron'
      <SingleElectron_HLT:EventSelectionAny>
        <HLT_Ele22_WPLoose_Gsf:LambdaStr> ev : ev.HLT_Ele22_WPLoose_Gsf[0]
        <HLT_Ele23_WPLoose_Gsf:LambdaStr> ev : ev.HLT_Ele23_WPLoose_Gsf[0]
        <HLT_Ele27_eta2p1_WPLoose_Gsf:LambdaStr> ev : ev.HLT_Ele27_eta2p1_WPLoose_Gsf[0]
    <SinglePhoton:EventSelectionAll>
      <PDSinglePhoton:LambdaStr> ev : ev.PrimaryDataset[0] == 'SinglePhoton'
      <SinglePhoton_HLT:EventSelectionAny>
        <HLT_Photon120:LambdaStr> ev : ev.HLT_Photon120[0]
        <HLT_Photon125:LambdaStr> ev : ev.HLT_Photon125[0]
        <HLT_Photon175:LambdaStr> ev : ev.HLT_Photon175[0]
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
    <SignalLoose:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflowId[0] == 1 # 'Signal'
      <PDMetHtmhtJetht:LambdaStr> ev : ev.PrimaryDataset[0] in ('MET', 'HTMHT', 'JetHT')
      <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
      <SignalLooseBintypes:EventSelectionAny>
        <SignalLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SignalLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <AlphaTCutLoose:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT300to800:EventSelectionAll>
              <HTin300to800:LambdaStr> ev : 300 <= ev.ht40[0] < 800
              <alphaTGT0p55:LambdaStr> ev : 0.50 <= ev.alphaT[0]
        <SignalLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <AlphaTCutLoose:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT300to800:EventSelectionAll>
              <HTin300to800:LambdaStr> ev : 300 <= ev.ht40[0] < 800
              <alphaTGT0p55:LambdaStr> ev : 0.50 <= ev.alphaT[0]
        <SignalLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
    <SingleMuLoose:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflowId[0] == 2 # 'SingleMu'
      <PDSingleMuon:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleMuon'
    <DoubleMuLoose:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflowId[0] == 3 # 'DoubleMu'
      <PDSingleMuon:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleMuon'
    <SingleEleLoose:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflowId[0] == 4 # 'SingleEle'
      <PDSingleElectron:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleElectron'
    <DoubleEleLoose:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflowId[0] == 5 # 'DoubleEle'
      <PDSingleElectron:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleElectron'
    <SinglePhotonLoose:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflowId[0] == 6 # 'SinglePhoton'
      <PDSinglePhoton:LambdaStr> ev : ev.PrimaryDataset[0] == 'SinglePhoton'
      <SinglePhotonLooseBintypes:EventSelectionAny>
        <SinglePhotonLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SinglePhotonLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
  <MetFilters:EventSelectionAll>
    <goodVertex:LambdaStr> ev : ev.Flag_goodVertices[0] == 1
    <CSCTightHaloFilter:LambdaStr> ev : ev.Flag_CSCTightHaloFilter[0] ==1
    <eeBadScFilter:LambdaStr> ev : ev.Flag_eeBadScFilter[0] ==1
    <HBHENoiseFilter:LambdaStr> ev : ev.Flag_HBHENoiseFilter[0] == 1
    <HBHENoiseIsoFilter:LambdaStr> ev : ev.Flag_HBHENoiseIsoFilter[0] == 1
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <LeadJetEtaLT2p5:LambdaStr> ev : -2.5 < ev.jet_eta[0] < 2.5
    <LeadJetChHEFGT0p1:LambdaStr> ev : ev.jet_chHEF[0] >= 0.1
    <MhtOverMetNoX:LambdaStr> ev : ev.MhtOverMetNoX[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
    <SignalFinal:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflowId[0] == 1 # 'Signal'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <SignalBintypes:EventSelectionAny>
        <SignalFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SignalFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
    <SingleMuFinal:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflowId[0] == 2 # 'SingleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mtw:LambdaStr> ev : 30 <= ev.mtw[0] < 125
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <DoubleMuFinal:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflowId[0] == 3 # 'DoubleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[1] < 0.12
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <SingleEleFinal:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflowId[0] == 4 # 'SingleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mtw:LambdaStr> ev : 30 <= ev.mtw[0] < 125
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <DoubleEleFinal:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflowId[0] == 5 # 'DoubleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[1] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[1] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <SinglePhotonFinal:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflowId[0] == 6 # 'SinglePhoton'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <minDelRJetPhoton:LambdaStr> ev : ev.minDelRJetPhoton[0] >= 1.0
      <SinglePhotonFinalBintypes:EventSelectionAny>
        <SinglePhotonFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SinglePhotonFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
        <SinglePhotonFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
        <SinglePhotonFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
'''


es_arg003='''<All:EventSelectionAll>
  <PD_HLT:EventSelectionAny>
    <MET:EventSelectionAll>
      <PDMET:LambdaStr> ev : ev.PrimaryDataset[0] == 'MET'
      <MET_HLT:EventSelectionAny>
        <HLT_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight:LambdaStr> ev : ev.HLT_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight[0]
        <HLT_PFMETNoMu120_JetIdCleaned_PFMHTNoMu120_IDTight:LambdaStr> ev : ev.HLT_PFMETNoMu120_JetIdCleaned_PFMHTNoMu120_IDTight[0]
    <HTMHT:EventSelectionAll>
      <PDHTMHT:LambdaStr> ev : ev.PrimaryDataset[0] == 'HTMHT'
      <HTMHT_HLT:EventSelectionAny>
        <HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57:LambdaStr> ev : ev.HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57[0]
        <HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63:LambdaStr> ev : ev.HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63[0]
        <HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55:LambdaStr> ev : ev.HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55[0]
        <HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58:LambdaStr> ev : ev.HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58[0]
        <HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53:LambdaStr> ev : ev.HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53[0]
        <HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54:LambdaStr> ev : ev.HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54[0]
        <HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52:LambdaStr> ev : ev.HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52[0]
        <HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53:LambdaStr> ev : ev.HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53[0]
        <HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51:LambdaStr> ev : ev.HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51[0]
        <HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52:LambdaStr> ev : ev.HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52[0]
    <JetHT:EventSelectionAll>
      <PDJetHT:LambdaStr> ev : ev.PrimaryDataset[0] == 'JetHT'
      <JetHT_HLT:EventSelectionAny>
        <HLT_PFHT800:LambdaStr> ev : ev.HLT_PFHT800[0]
    <SingleMuon:EventSelectionAll>
      <PDSingleMuon:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleMuon'
      <SingleMuon_HLT:EventSelectionAny>
        <HLT_IsoMu17_eta2p1:LambdaStr> ev : ev.HLT_IsoMu17_eta2p1[0]
        <HLT_IsoMu20:LambdaStr> ev : ev.HLT_IsoMu20[0]
        <HLT_IsoMu24_eta2p1:LambdaStr> ev : ev.HLT_IsoMu24_eta2p1[0]
    <SingleElectron:EventSelectionAll>
      <PDSingleElectron:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleElectron'
      <SingleElectron_HLT:EventSelectionAny>
        <HLT_Ele22_WPLoose_Gsf:LambdaStr> ev : ev.HLT_Ele22_WPLoose_Gsf[0]
        <HLT_Ele23_WPLoose_Gsf:LambdaStr> ev : ev.HLT_Ele23_WPLoose_Gsf[0]
        <HLT_Ele27_eta2p1_WPLoose_Gsf:LambdaStr> ev : ev.HLT_Ele27_eta2p1_WPLoose_Gsf[0]
    <SinglePhoton:EventSelectionAll>
      <PDSinglePhoton:LambdaStr> ev : ev.PrimaryDataset[0] == 'SinglePhoton'
      <SinglePhoton_HLT:EventSelectionAny>
        <HLT_Photon120:LambdaStr> ev : ev.HLT_Photon120[0]
        <HLT_Photon125:LambdaStr> ev : ev.HLT_Photon125[0]
        <HLT_Photon175:LambdaStr> ev : ev.HLT_Photon175[0]
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
    <SignalLoose:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflowId[0] == 1 # 'Signal'
      <PDMetHtmhtJetht:LambdaStr> ev : ev.PrimaryDataset[0] in ('MET', 'HTMHT', 'JetHT')
      <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
      <SignalLooseBintypes:EventSelectionAny>
        <SignalLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SignalLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <AlphaTCutLoose:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT300to800:EventSelectionAll>
              <HTin300to800:LambdaStr> ev : 300 <= ev.ht40[0] < 800
              <alphaTGT0p55:LambdaStr> ev : 0.50 <= ev.alphaT[0]
        <SignalLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <AlphaTCutLoose:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT300to800:EventSelectionAll>
              <HTin300to800:LambdaStr> ev : 300 <= ev.ht40[0] < 800
              <alphaTGT0p55:LambdaStr> ev : 0.50 <= ev.alphaT[0]
        <SignalLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
    <SingleMuLoose:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflowId[0] == 2 # 'SingleMu'
      <PDSingleMuon:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleMuon'
    <DoubleMuLoose:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflowId[0] == 3 # 'DoubleMu'
      <PDSingleMuon:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleMuon'
    <SingleEleLoose:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflowId[0] == 4 # 'SingleEle'
      <PDSingleElectron:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleElectron'
    <DoubleEleLoose:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflowId[0] == 5 # 'DoubleEle'
      <PDSingleElectron:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleElectron'
    <SinglePhotonLoose:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflowId[0] == 6 # 'SinglePhoton'
      <PDSinglePhoton:LambdaStr> ev : ev.PrimaryDataset[0] == 'SinglePhoton'
      <SinglePhotonLooseBintypes:EventSelectionAny>
        <SinglePhotonLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SinglePhotonLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
  <MetFilters:EventSelectionAll>
    <goodVertex:LambdaStr> ev : ev.Flag_goodVertices[0] == 1
    <CSCTightHaloFilter:LambdaStr> ev : ev.Flag_CSCTightHaloFilter[0] ==1
    <eeBadScFilter:LambdaStr> ev : ev.Flag_eeBadScFilter[0] ==1
    <HBHENoiseFilter:LambdaStr> ev : ev.Flag_HBHENoiseFilter[0] == 1
    <HBHENoiseIsoFilter:LambdaStr> ev : ev.Flag_HBHENoiseIsoFilter[0] == 1
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <LeadJetEtaLT2p5:LambdaStr> ev : -2.5 < ev.jet_eta[0] < 2.5
    <LeadJetChHEFGT0p1:LambdaStr> ev : ev.jet_chHEF[0] >= 0.1
    <MhtOverMetNoXNoHF:LambdaStr> ev : ev.MhtOverMetNoXNoHF[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
    <SignalFinal:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflowId[0] == 1 # 'Signal'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <SignalBintypes:EventSelectionAny>
        <SignalFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SignalFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
    <SingleMuFinal:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflowId[0] == 2 # 'SingleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mtwNoHF:LambdaStr> ev : 30 <= ev.mtwNoHF[0] < 125
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <DoubleMuFinal:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflowId[0] == 3 # 'DoubleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[1] < 0.12
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <SingleEleFinal:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflowId[0] == 4 # 'SingleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mtwNoHF:LambdaStr> ev : 30 <= ev.mtwNoHF[0] < 125
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <DoubleEleFinal:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflowId[0] == 5 # 'DoubleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[1] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[1] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <SinglePhotonFinal:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflowId[0] == 6 # 'SinglePhoton'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <minDelRJetPhoton:LambdaStr> ev : ev.minDelRJetPhoton[0] >= 1.0
      <SinglePhotonFinalBintypes:EventSelectionAny>
        <SinglePhotonFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SinglePhotonFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
        <SinglePhotonFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
        <SinglePhotonFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
'''


es_arg004='''<All:EventSelectionAll>
  <PD_HLT:EventSelectionAny>
    <MET:EventSelectionAll>
      <PDMET:LambdaStr> ev : ev.PrimaryDataset[0] == 'MET'
      <MET_HLT:EventSelectionAny>
        <HLT_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight:LambdaStr> ev : ev.HLT_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight[0]
        <HLT_PFMETNoMu120_JetIdCleaned_PFMHTNoMu120_IDTight:LambdaStr> ev : ev.HLT_PFMETNoMu120_JetIdCleaned_PFMHTNoMu120_IDTight[0]
    <HTMHT:EventSelectionAll>
      <PDHTMHT:LambdaStr> ev : ev.PrimaryDataset[0] == 'HTMHT'
      <HTMHT_HLT:EventSelectionAny>
        <HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57:LambdaStr> ev : ev.HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57[0]
        <HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63:LambdaStr> ev : ev.HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63[0]
        <HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55:LambdaStr> ev : ev.HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55[0]
        <HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58:LambdaStr> ev : ev.HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58[0]
        <HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53:LambdaStr> ev : ev.HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53[0]
        <HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54:LambdaStr> ev : ev.HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54[0]
        <HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52:LambdaStr> ev : ev.HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52[0]
        <HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53:LambdaStr> ev : ev.HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53[0]
        <HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51:LambdaStr> ev : ev.HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51[0]
        <HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52:LambdaStr> ev : ev.HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52[0]
    <JetHT:EventSelectionAll>
      <PDJetHT:LambdaStr> ev : ev.PrimaryDataset[0] == 'JetHT'
      <JetHT_HLT:EventSelectionAny>
        <HLT_PFHT800:LambdaStr> ev : ev.HLT_PFHT800[0]
    <SingleMuon:EventSelectionAll>
      <PDSingleMuon:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleMuon'
      <SingleMuon_HLT:EventSelectionAny>
        <HLT_IsoMu17_eta2p1:LambdaStr> ev : ev.HLT_IsoMu17_eta2p1[0]
        <HLT_IsoMu20:LambdaStr> ev : ev.HLT_IsoMu20[0]
        <HLT_IsoMu24_eta2p1:LambdaStr> ev : ev.HLT_IsoMu24_eta2p1[0]
    <SingleElectron:EventSelectionAll>
      <PDSingleElectron:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleElectron'
      <SingleElectron_HLT:EventSelectionAny>
        <HLT_Ele22_WPLoose_Gsf:LambdaStr> ev : ev.HLT_Ele22_WPLoose_Gsf[0]
        <HLT_Ele23_WPLoose_Gsf:LambdaStr> ev : ev.HLT_Ele23_WPLoose_Gsf[0]
        <HLT_Ele27_eta2p1_WPLoose_Gsf:LambdaStr> ev : ev.HLT_Ele27_eta2p1_WPLoose_Gsf[0]
    <SinglePhoton:EventSelectionAll>
      <PDSinglePhoton:LambdaStr> ev : ev.PrimaryDataset[0] == 'SinglePhoton'
      <SinglePhoton_HLT:EventSelectionAny>
        <HLT_Photon120:LambdaStr> ev : ev.HLT_Photon120[0]
        <HLT_Photon125:LambdaStr> ev : ev.HLT_Photon125[0]
        <HLT_Photon175:LambdaStr> ev : ev.HLT_Photon175[0]
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
    <SignalLoose:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflowId[0] == 1 # 'Signal'
      <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
      <SignalLooseBintypes:EventSelectionAny>
        <SignalLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SignalLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <AlphaTCutLoose:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT300to800:EventSelectionAll>
              <HTin300to800:LambdaStr> ev : 300 <= ev.ht40[0] < 800
              <alphaTGT0p55:LambdaStr> ev : 0.50 <= ev.alphaT[0]
        <SignalLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <AlphaTCutLoose:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT300to800:EventSelectionAll>
              <HTin300to800:LambdaStr> ev : 300 <= ev.ht40[0] < 800
              <alphaTGT0p55:LambdaStr> ev : 0.50 <= ev.alphaT[0]
        <SignalLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
    <SingleMuLoose:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflowId[0] == 2 # 'SingleMu'
    <DoubleMuLoose:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflowId[0] == 3 # 'DoubleMu'
    <SingleEleLoose:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflowId[0] == 4 # 'SingleEle'
    <DoubleEleLoose:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflowId[0] == 5 # 'DoubleEle'
    <SinglePhotonLoose:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflowId[0] == 6 # 'SinglePhoton'
      <SinglePhotonLooseBintypes:EventSelectionAny>
        <SinglePhotonLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SinglePhotonLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
  <MetFilters:EventSelectionAll>
    <goodVertex:LambdaStr> ev : ev.Flag_goodVertices[0] == 1
    <CSCTightHaloFilter:LambdaStr> ev : ev.Flag_CSCTightHaloFilter[0] ==1
    <eeBadScFilter:LambdaStr> ev : ev.Flag_eeBadScFilter[0] ==1
    <HBHENoiseFilter:LambdaStr> ev : ev.Flag_HBHENoiseFilter[0] == 1
    <HBHENoiseIsoFilter:LambdaStr> ev : ev.Flag_HBHENoiseIsoFilter[0] == 1
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <LeadJetEtaLT2p5:LambdaStr> ev : -2.5 < ev.jet_eta[0] < 2.5
    <LeadJetChHEFGT0p1:LambdaStr> ev : ev.jet_chHEF[0] >= 0.1
    <MhtOverMetNoX:LambdaStr> ev : ev.MhtOverMetNoX[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
    <SignalFinal:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflowId[0] == 1 # 'Signal'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <SignalBintypes:EventSelectionAny>
        <SignalFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SignalFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <HT_HLTAlphaT:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <HLTAlphaTHT200:EventSelectionAny>
                <HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57:LambdaStr> ev : ev.HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57[0]
                <HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63:LambdaStr> ev : ev.HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <HLTAlphaTHT250:EventSelectionAny>
                <HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55:LambdaStr> ev : ev.HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55[0]
                <HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58:LambdaStr> ev : ev.HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <HLTAlphaTHT300:EventSelectionAny>
                <HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53:LambdaStr> ev : ev.HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53[0]
                <HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54:LambdaStr> ev : ev.HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <HLTAlphaTHT350:EventSelectionAny>
                <HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52:LambdaStr> ev : ev.HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52[0]
                <HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53:LambdaStr> ev : ev.HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <HLTAlphaTHT400:EventSelectionAny>
                <HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51:LambdaStr> ev : ev.HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51[0]
                <HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52:LambdaStr> ev : ev.HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52[0]
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <HT_HLTAlphaT:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <HLTAlphaTHT200:EventSelectionAny>
                <HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57:LambdaStr> ev : ev.HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57[0]
                <HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63:LambdaStr> ev : ev.HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <HLTAlphaTHT250:EventSelectionAny>
                <HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55:LambdaStr> ev : ev.HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55[0]
                <HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58:LambdaStr> ev : ev.HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <HLTAlphaTHT300:EventSelectionAny>
                <HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53:LambdaStr> ev : ev.HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53[0]
                <HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54:LambdaStr> ev : ev.HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <HLTAlphaTHT350:EventSelectionAny>
                <HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52:LambdaStr> ev : ev.HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52[0]
                <HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53:LambdaStr> ev : ev.HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <HLTAlphaTHT400:EventSelectionAny>
                <HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51:LambdaStr> ev : ev.HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51[0]
                <HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52:LambdaStr> ev : ev.HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52[0]
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
    <SingleMuFinal:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflowId[0] == 2 # 'SingleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <HLT_SingleMuon:EventSelectionAny>
        <HLT_IsoMu17_eta2p1:LambdaStr> ev : ev.HLT_IsoMu17_eta2p1[0]
        <HLT_IsoMu20:LambdaStr> ev : ev.HLT_IsoMu20[0]
        <HLT_IsoMu24_eta2p1:LambdaStr> ev : ev.HLT_IsoMu24_eta2p1[0]
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mtw:LambdaStr> ev : 30 <= ev.mtw[0] < 125
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <DoubleMuFinal:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflowId[0] == 3 # 'DoubleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[1] < 0.12
      <HLT_SingleMuon:EventSelectionAny>
        <HLT_IsoMu17_eta2p1:LambdaStr> ev : ev.HLT_IsoMu17_eta2p1[0]
        <HLT_IsoMu20:LambdaStr> ev : ev.HLT_IsoMu20[0]
        <HLT_IsoMu24_eta2p1:LambdaStr> ev : ev.HLT_IsoMu24_eta2p1[0]
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <SingleEleFinal:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflowId[0] == 4 # 'SingleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mtw:LambdaStr> ev : 30 <= ev.mtw[0] < 125
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <DoubleEleFinal:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflowId[0] == 5 # 'DoubleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[1] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[1] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <SinglePhotonFinal:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflowId[0] == 6 # 'SinglePhoton'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <minDelRJetPhoton:LambdaStr> ev : ev.minDelRJetPhoton[0] >= 1.0
      <SinglePhotonFinalBintypes:EventSelectionAny>
        <SinglePhotonFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SinglePhotonFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
        <SinglePhotonFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
        <SinglePhotonFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
'''


es_arg005='''<All:EventSelectionAll>
  <PD_HLT:EventSelectionAny>
    <MET:EventSelectionAll>
      <PDMET:LambdaStr> ev : ev.PrimaryDataset[0] == 'MET'
      <MET_HLT:EventSelectionAny>
        <HLT_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight:LambdaStr> ev : ev.HLT_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight[0]
        <HLT_PFMETNoMu120_JetIdCleaned_PFMHTNoMu120_IDTight:LambdaStr> ev : ev.HLT_PFMETNoMu120_JetIdCleaned_PFMHTNoMu120_IDTight[0]
    <HTMHT:EventSelectionAll>
      <PDHTMHT:LambdaStr> ev : ev.PrimaryDataset[0] == 'HTMHT'
      <HTMHT_HLT:EventSelectionAny>
        <HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57:LambdaStr> ev : ev.HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57[0]
        <HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63:LambdaStr> ev : ev.HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63[0]
        <HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55:LambdaStr> ev : ev.HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55[0]
        <HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58:LambdaStr> ev : ev.HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58[0]
        <HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53:LambdaStr> ev : ev.HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53[0]
        <HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54:LambdaStr> ev : ev.HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54[0]
        <HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52:LambdaStr> ev : ev.HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52[0]
        <HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53:LambdaStr> ev : ev.HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53[0]
        <HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51:LambdaStr> ev : ev.HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51[0]
        <HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52:LambdaStr> ev : ev.HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52[0]
    <JetHT:EventSelectionAll>
      <PDJetHT:LambdaStr> ev : ev.PrimaryDataset[0] == 'JetHT'
      <JetHT_HLT:EventSelectionAny>
        <HLT_PFHT800:LambdaStr> ev : ev.HLT_PFHT800[0]
    <SingleMuon:EventSelectionAll>
      <PDSingleMuon:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleMuon'
      <SingleMuon_HLT:EventSelectionAny>
        <HLT_IsoMu17_eta2p1:LambdaStr> ev : ev.HLT_IsoMu17_eta2p1[0]
        <HLT_IsoMu20:LambdaStr> ev : ev.HLT_IsoMu20[0]
        <HLT_IsoMu24_eta2p1:LambdaStr> ev : ev.HLT_IsoMu24_eta2p1[0]
    <SingleElectron:EventSelectionAll>
      <PDSingleElectron:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleElectron'
      <SingleElectron_HLT:EventSelectionAny>
        <HLT_Ele22_WPLoose_Gsf:LambdaStr> ev : ev.HLT_Ele22_WPLoose_Gsf[0]
        <HLT_Ele23_WPLoose_Gsf:LambdaStr> ev : ev.HLT_Ele23_WPLoose_Gsf[0]
        <HLT_Ele27_eta2p1_WPLoose_Gsf:LambdaStr> ev : ev.HLT_Ele27_eta2p1_WPLoose_Gsf[0]
    <SinglePhoton:EventSelectionAll>
      <PDSinglePhoton:LambdaStr> ev : ev.PrimaryDataset[0] == 'SinglePhoton'
      <SinglePhoton_HLT:EventSelectionAny>
        <HLT_Photon120:LambdaStr> ev : ev.HLT_Photon120[0]
        <HLT_Photon125:LambdaStr> ev : ev.HLT_Photon125[0]
        <HLT_Photon175:LambdaStr> ev : ev.HLT_Photon175[0]
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
    <SignalLoose:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflowId[0] == 1 # 'Signal'
      <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
      <SignalLooseBintypes:EventSelectionAny>
        <SignalLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SignalLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <AlphaTCutLoose:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT300to800:EventSelectionAll>
              <HTin300to800:LambdaStr> ev : 300 <= ev.ht40[0] < 800
              <alphaTGT0p55:LambdaStr> ev : 0.50 <= ev.alphaT[0]
        <SignalLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <AlphaTCutLoose:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT300to800:EventSelectionAll>
              <HTin300to800:LambdaStr> ev : 300 <= ev.ht40[0] < 800
              <alphaTGT0p55:LambdaStr> ev : 0.50 <= ev.alphaT[0]
        <SignalLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
    <SingleMuLoose:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflowId[0] == 2 # 'SingleMu'
    <DoubleMuLoose:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflowId[0] == 3 # 'DoubleMu'
    <SingleEleLoose:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflowId[0] == 4 # 'SingleEle'
    <DoubleEleLoose:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflowId[0] == 5 # 'DoubleEle'
    <SinglePhotonLoose:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflowId[0] == 6 # 'SinglePhoton'
      <SinglePhotonLooseBintypes:EventSelectionAny>
        <SinglePhotonLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SinglePhotonLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
  <MetFilters:EventSelectionAll>
    <goodVertex:LambdaStr> ev : ev.Flag_goodVertices[0] == 1
    <CSCTightHaloFilter:LambdaStr> ev : ev.Flag_CSCTightHaloFilter[0] ==1
    <eeBadScFilter:LambdaStr> ev : ev.Flag_eeBadScFilter[0] ==1
    <HBHENoiseFilter:LambdaStr> ev : ev.Flag_HBHENoiseFilter[0] == 1
    <HBHENoiseIsoFilter:LambdaStr> ev : ev.Flag_HBHENoiseIsoFilter[0] == 1
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <LeadJetEtaLT2p5:LambdaStr> ev : -2.5 < ev.jet_eta[0] < 2.5
    <LeadJetChHEFGT0p1:LambdaStr> ev : ev.jet_chHEF[0] >= 0.1
    <MhtOverMetNoXNoHF:LambdaStr> ev : ev.MhtOverMetNoXNoHF[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
    <SignalFinal:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflowId[0] == 1 # 'Signal'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <SignalBintypes:EventSelectionAny>
        <SignalFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SignalFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <HT_HLTAlphaT:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <HLTAlphaTHT200:EventSelectionAny>
                <HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57:LambdaStr> ev : ev.HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57[0]
                <HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63:LambdaStr> ev : ev.HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <HLTAlphaTHT250:EventSelectionAny>
                <HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55:LambdaStr> ev : ev.HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55[0]
                <HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58:LambdaStr> ev : ev.HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <HLTAlphaTHT300:EventSelectionAny>
                <HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53:LambdaStr> ev : ev.HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53[0]
                <HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54:LambdaStr> ev : ev.HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <HLTAlphaTHT350:EventSelectionAny>
                <HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52:LambdaStr> ev : ev.HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52[0]
                <HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53:LambdaStr> ev : ev.HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <HLTAlphaTHT400:EventSelectionAny>
                <HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51:LambdaStr> ev : ev.HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51[0]
                <HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52:LambdaStr> ev : ev.HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52[0]
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <HT_HLTAlphaT:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <HLTAlphaTHT200:EventSelectionAny>
                <HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57:LambdaStr> ev : ev.HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57[0]
                <HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63:LambdaStr> ev : ev.HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <HLTAlphaTHT250:EventSelectionAny>
                <HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55:LambdaStr> ev : ev.HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55[0]
                <HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58:LambdaStr> ev : ev.HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <HLTAlphaTHT300:EventSelectionAny>
                <HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53:LambdaStr> ev : ev.HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53[0]
                <HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54:LambdaStr> ev : ev.HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <HLTAlphaTHT350:EventSelectionAny>
                <HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52:LambdaStr> ev : ev.HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52[0]
                <HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53:LambdaStr> ev : ev.HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <HLTAlphaTHT400:EventSelectionAny>
                <HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51:LambdaStr> ev : ev.HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51[0]
                <HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52:LambdaStr> ev : ev.HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52[0]
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
    <SingleMuFinal:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflowId[0] == 2 # 'SingleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <HLT_SingleMuon:EventSelectionAny>
        <HLT_IsoMu17_eta2p1:LambdaStr> ev : ev.HLT_IsoMu17_eta2p1[0]
        <HLT_IsoMu20:LambdaStr> ev : ev.HLT_IsoMu20[0]
        <HLT_IsoMu24_eta2p1:LambdaStr> ev : ev.HLT_IsoMu24_eta2p1[0]
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mtwNoHF:LambdaStr> ev : 30 <= ev.mtwNoHF[0] < 125
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <DoubleMuFinal:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflowId[0] == 3 # 'DoubleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[1] < 0.12
      <HLT_SingleMuon:EventSelectionAny>
        <HLT_IsoMu17_eta2p1:LambdaStr> ev : ev.HLT_IsoMu17_eta2p1[0]
        <HLT_IsoMu20:LambdaStr> ev : ev.HLT_IsoMu20[0]
        <HLT_IsoMu24_eta2p1:LambdaStr> ev : ev.HLT_IsoMu24_eta2p1[0]
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <SingleEleFinal:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflowId[0] == 4 # 'SingleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mtwNoHF:LambdaStr> ev : 30 <= ev.mtwNoHF[0] < 125
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <DoubleEleFinal:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflowId[0] == 5 # 'DoubleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[1] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[1] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <SinglePhotonFinal:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflowId[0] == 6 # 'SinglePhoton'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <minDelRJetPhoton:LambdaStr> ev : ev.minDelRJetPhoton[0] >= 1.0
      <SinglePhotonFinalBintypes:EventSelectionAny>
        <SinglePhotonFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SinglePhotonFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
        <SinglePhotonFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
        <SinglePhotonFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
'''


es_arg006='''<All:EventSelectionAll>
  <PD_HLT:EventSelectionAny>
    <MET:EventSelectionAll>
      <PDMET:LambdaStr> ev : ev.PrimaryDataset[0] == 'MET'
      <MET_HLT:EventSelectionAny>
        <HLT_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight:LambdaStr> ev : ev.HLT_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight[0]
        <HLT_PFMETNoMu120_JetIdCleaned_PFMHTNoMu120_IDTight:LambdaStr> ev : ev.HLT_PFMETNoMu120_JetIdCleaned_PFMHTNoMu120_IDTight[0]
    <HTMHT:EventSelectionAll>
      <PDHTMHT:LambdaStr> ev : ev.PrimaryDataset[0] == 'HTMHT'
      <HTMHT_HLT:EventSelectionAny>
        <HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57:LambdaStr> ev : ev.HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57[0]
        <HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63:LambdaStr> ev : ev.HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63[0]
        <HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55:LambdaStr> ev : ev.HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55[0]
        <HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58:LambdaStr> ev : ev.HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58[0]
        <HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53:LambdaStr> ev : ev.HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53[0]
        <HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54:LambdaStr> ev : ev.HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54[0]
        <HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52:LambdaStr> ev : ev.HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52[0]
        <HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53:LambdaStr> ev : ev.HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53[0]
        <HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51:LambdaStr> ev : ev.HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51[0]
        <HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52:LambdaStr> ev : ev.HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52[0]
    <JetHT:EventSelectionAll>
      <PDJetHT:LambdaStr> ev : ev.PrimaryDataset[0] == 'JetHT'
      <JetHT_HLT:EventSelectionAny>
        <HLT_PFHT800:LambdaStr> ev : ev.HLT_PFHT800[0]
    <SingleMuon:EventSelectionAll>
      <PDSingleMuon:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleMuon'
      <SingleMuon_HLT:EventSelectionAny>
        <HLT_IsoMu17_eta2p1:LambdaStr> ev : ev.HLT_IsoMu17_eta2p1[0]
        <HLT_IsoMu20:LambdaStr> ev : ev.HLT_IsoMu20[0]
        <HLT_IsoMu24_eta2p1:LambdaStr> ev : ev.HLT_IsoMu24_eta2p1[0]
    <SingleElectron:EventSelectionAll>
      <PDSingleElectron:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleElectron'
      <SingleElectron_HLT:EventSelectionAny>
        <HLT_Ele22_WPLoose_Gsf:LambdaStr> ev : ev.HLT_Ele22_WPLoose_Gsf[0]
        <HLT_Ele23_WPLoose_Gsf:LambdaStr> ev : ev.HLT_Ele23_WPLoose_Gsf[0]
        <HLT_Ele27_eta2p1_WPLoose_Gsf:LambdaStr> ev : ev.HLT_Ele27_eta2p1_WPLoose_Gsf[0]
    <SinglePhoton:EventSelectionAll>
      <PDSinglePhoton:LambdaStr> ev : ev.PrimaryDataset[0] == 'SinglePhoton'
      <SinglePhoton_HLT:EventSelectionAny>
        <HLT_Photon120:LambdaStr> ev : ev.HLT_Photon120[0]
        <HLT_Photon125:LambdaStr> ev : ev.HLT_Photon125[0]
        <HLT_Photon175:LambdaStr> ev : ev.HLT_Photon175[0]
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
    <SignalLoose:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflowId[0] == 1 # 'Signal'
      <PDMetHtmhtJetht:LambdaStr> ev : ev.PrimaryDataset[0] in ('MET', 'HTMHT', 'JetHT')
      <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
      <SignalLooseBintypes:EventSelectionAny>
        <SignalLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SignalLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <AlphaTCutLoose:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT300to800:EventSelectionAll>
              <HTin300to800:LambdaStr> ev : 300 <= ev.ht40[0] < 800
              <alphaTGT0p55:LambdaStr> ev : 0.50 <= ev.alphaT[0]
        <SignalLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <AlphaTCutLoose:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT300to800:EventSelectionAll>
              <HTin300to800:LambdaStr> ev : 300 <= ev.ht40[0] < 800
              <alphaTGT0p55:LambdaStr> ev : 0.50 <= ev.alphaT[0]
        <SignalLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
    <SingleMuLoose:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflowId[0] == 2 # 'SingleMu'
      <PDSingleMuon:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleMuon'
    <DoubleMuLoose:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflowId[0] == 3 # 'DoubleMu'
      <PDSingleMuon:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleMuon'
    <SingleEleLoose:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflowId[0] == 4 # 'SingleEle'
      <PDSingleElectron:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleElectron'
    <DoubleEleLoose:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflowId[0] == 5 # 'DoubleEle'
      <PDSingleElectron:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleElectron'
    <SinglePhotonLoose:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflowId[0] == 6 # 'SinglePhoton'
      <PDSinglePhoton:LambdaStr> ev : ev.PrimaryDataset[0] == 'SinglePhoton'
      <SinglePhotonLooseBintypes:EventSelectionAny>
        <SinglePhotonLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SinglePhotonLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
  <MetFilters:EventSelectionAll>
    <goodVertex:LambdaStr> ev : ev.Flag_goodVertices[0] == 1
    <CSCTightHaloFilter:LambdaStr> ev : ev.Flag_CSCTightHaloFilter[0] ==1
    <eeBadScFilter:LambdaStr> ev : ev.Flag_eeBadScFilter[0] ==1
    <HBHENoiseFilter:LambdaStr> ev : ev.Flag_HBHENoiseFilter[0] == 1
    <HBHENoiseIsoFilter:LambdaStr> ev : ev.Flag_HBHENoiseIsoFilter[0] == 1
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <LeadJetEtaLT2p5:LambdaStr> ev : -2.5 < ev.jet_eta[0] < 2.5
    <LeadJetChHEFGT0p1:LambdaStr> ev : ev.jet_chHEF[0] >= 0.1
    <MhtOverMetNoX:LambdaStr> ev : ev.MhtOverMetNoX[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
    <SignalFinal:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflowId[0] == 1 # 'Signal'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <SignalBintypes:EventSelectionAny>
        <SignalFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SignalFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <HT_HLTAlphaT:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <HLTAlphaTHT200:EventSelectionAny>
                <HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57:LambdaStr> ev : ev.HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57[0]
                <HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63:LambdaStr> ev : ev.HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <HLTAlphaTHT250:EventSelectionAny>
                <HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55:LambdaStr> ev : ev.HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55[0]
                <HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58:LambdaStr> ev : ev.HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <HLTAlphaTHT300:EventSelectionAny>
                <HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53:LambdaStr> ev : ev.HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53[0]
                <HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54:LambdaStr> ev : ev.HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <HLTAlphaTHT350:EventSelectionAny>
                <HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52:LambdaStr> ev : ev.HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52[0]
                <HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53:LambdaStr> ev : ev.HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <HLTAlphaTHT400:EventSelectionAny>
                <HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51:LambdaStr> ev : ev.HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51[0]
                <HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52:LambdaStr> ev : ev.HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52[0]
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <HT_HLTAlphaT:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <HLTAlphaTHT200:EventSelectionAny>
                <HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57:LambdaStr> ev : ev.HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57[0]
                <HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63:LambdaStr> ev : ev.HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <HLTAlphaTHT250:EventSelectionAny>
                <HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55:LambdaStr> ev : ev.HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55[0]
                <HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58:LambdaStr> ev : ev.HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <HLTAlphaTHT300:EventSelectionAny>
                <HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53:LambdaStr> ev : ev.HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53[0]
                <HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54:LambdaStr> ev : ev.HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <HLTAlphaTHT350:EventSelectionAny>
                <HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52:LambdaStr> ev : ev.HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52[0]
                <HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53:LambdaStr> ev : ev.HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <HLTAlphaTHT400:EventSelectionAny>
                <HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51:LambdaStr> ev : ev.HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51[0]
                <HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52:LambdaStr> ev : ev.HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52[0]
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
    <SingleMuFinal:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflowId[0] == 2 # 'SingleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <HLT_SingleMuon:EventSelectionAny>
        <HLT_IsoMu17_eta2p1:LambdaStr> ev : ev.HLT_IsoMu17_eta2p1[0]
        <HLT_IsoMu20:LambdaStr> ev : ev.HLT_IsoMu20[0]
        <HLT_IsoMu24_eta2p1:LambdaStr> ev : ev.HLT_IsoMu24_eta2p1[0]
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mtw:LambdaStr> ev : 30 <= ev.mtw[0] < 125
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <DoubleMuFinal:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflowId[0] == 3 # 'DoubleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[1] < 0.12
      <HLT_SingleMuon:EventSelectionAny>
        <HLT_IsoMu17_eta2p1:LambdaStr> ev : ev.HLT_IsoMu17_eta2p1[0]
        <HLT_IsoMu20:LambdaStr> ev : ev.HLT_IsoMu20[0]
        <HLT_IsoMu24_eta2p1:LambdaStr> ev : ev.HLT_IsoMu24_eta2p1[0]
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <SingleEleFinal:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflowId[0] == 4 # 'SingleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mtw:LambdaStr> ev : 30 <= ev.mtw[0] < 125
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <DoubleEleFinal:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflowId[0] == 5 # 'DoubleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[1] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[1] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <SinglePhotonFinal:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflowId[0] == 6 # 'SinglePhoton'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <minDelRJetPhoton:LambdaStr> ev : ev.minDelRJetPhoton[0] >= 1.0
      <SinglePhotonFinalBintypes:EventSelectionAny>
        <SinglePhotonFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SinglePhotonFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
        <SinglePhotonFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
        <SinglePhotonFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
'''


es_arg007='''<All:EventSelectionAll>
  <PD_HLT:EventSelectionAny>
    <MET:EventSelectionAll>
      <PDMET:LambdaStr> ev : ev.PrimaryDataset[0] == 'MET'
      <MET_HLT:EventSelectionAny>
        <HLT_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight:LambdaStr> ev : ev.HLT_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight[0]
        <HLT_PFMETNoMu120_JetIdCleaned_PFMHTNoMu120_IDTight:LambdaStr> ev : ev.HLT_PFMETNoMu120_JetIdCleaned_PFMHTNoMu120_IDTight[0]
    <HTMHT:EventSelectionAll>
      <PDHTMHT:LambdaStr> ev : ev.PrimaryDataset[0] == 'HTMHT'
      <HTMHT_HLT:EventSelectionAny>
        <HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57:LambdaStr> ev : ev.HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57[0]
        <HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63:LambdaStr> ev : ev.HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63[0]
        <HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55:LambdaStr> ev : ev.HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55[0]
        <HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58:LambdaStr> ev : ev.HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58[0]
        <HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53:LambdaStr> ev : ev.HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53[0]
        <HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54:LambdaStr> ev : ev.HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54[0]
        <HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52:LambdaStr> ev : ev.HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52[0]
        <HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53:LambdaStr> ev : ev.HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53[0]
        <HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51:LambdaStr> ev : ev.HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51[0]
        <HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52:LambdaStr> ev : ev.HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52[0]
    <JetHT:EventSelectionAll>
      <PDJetHT:LambdaStr> ev : ev.PrimaryDataset[0] == 'JetHT'
      <JetHT_HLT:EventSelectionAny>
        <HLT_PFHT800:LambdaStr> ev : ev.HLT_PFHT800[0]
    <SingleMuon:EventSelectionAll>
      <PDSingleMuon:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleMuon'
      <SingleMuon_HLT:EventSelectionAny>
        <HLT_IsoMu17_eta2p1:LambdaStr> ev : ev.HLT_IsoMu17_eta2p1[0]
        <HLT_IsoMu20:LambdaStr> ev : ev.HLT_IsoMu20[0]
        <HLT_IsoMu24_eta2p1:LambdaStr> ev : ev.HLT_IsoMu24_eta2p1[0]
    <SingleElectron:EventSelectionAll>
      <PDSingleElectron:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleElectron'
      <SingleElectron_HLT:EventSelectionAny>
        <HLT_Ele22_WPLoose_Gsf:LambdaStr> ev : ev.HLT_Ele22_WPLoose_Gsf[0]
        <HLT_Ele23_WPLoose_Gsf:LambdaStr> ev : ev.HLT_Ele23_WPLoose_Gsf[0]
        <HLT_Ele27_eta2p1_WPLoose_Gsf:LambdaStr> ev : ev.HLT_Ele27_eta2p1_WPLoose_Gsf[0]
    <SinglePhoton:EventSelectionAll>
      <PDSinglePhoton:LambdaStr> ev : ev.PrimaryDataset[0] == 'SinglePhoton'
      <SinglePhoton_HLT:EventSelectionAny>
        <HLT_Photon120:LambdaStr> ev : ev.HLT_Photon120[0]
        <HLT_Photon125:LambdaStr> ev : ev.HLT_Photon125[0]
        <HLT_Photon175:LambdaStr> ev : ev.HLT_Photon175[0]
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
    <SignalLoose:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflowId[0] == 1 # 'Signal'
      <PDMetHtmhtJetht:LambdaStr> ev : ev.PrimaryDataset[0] in ('MET', 'HTMHT', 'JetHT')
      <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
      <SignalLooseBintypes:EventSelectionAny>
        <SignalLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SignalLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <AlphaTCutLoose:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT300to800:EventSelectionAll>
              <HTin300to800:LambdaStr> ev : 300 <= ev.ht40[0] < 800
              <alphaTGT0p55:LambdaStr> ev : 0.50 <= ev.alphaT[0]
        <SignalLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <AlphaTCutLoose:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT300to800:EventSelectionAll>
              <HTin300to800:LambdaStr> ev : 300 <= ev.ht40[0] < 800
              <alphaTGT0p55:LambdaStr> ev : 0.50 <= ev.alphaT[0]
        <SignalLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
    <SingleMuLoose:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflowId[0] == 2 # 'SingleMu'
      <PDSingleMuon:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleMuon'
    <DoubleMuLoose:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflowId[0] == 3 # 'DoubleMu'
      <PDSingleMuon:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleMuon'
    <SingleEleLoose:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflowId[0] == 4 # 'SingleEle'
      <PDSingleElectron:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleElectron'
    <DoubleEleLoose:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflowId[0] == 5 # 'DoubleEle'
      <PDSingleElectron:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleElectron'
    <SinglePhotonLoose:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflowId[0] == 6 # 'SinglePhoton'
      <PDSinglePhoton:LambdaStr> ev : ev.PrimaryDataset[0] == 'SinglePhoton'
      <SinglePhotonLooseBintypes:EventSelectionAny>
        <SinglePhotonLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SinglePhotonLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
  <MetFilters:EventSelectionAll>
    <goodVertex:LambdaStr> ev : ev.Flag_goodVertices[0] == 1
    <CSCTightHaloFilter:LambdaStr> ev : ev.Flag_CSCTightHaloFilter[0] ==1
    <eeBadScFilter:LambdaStr> ev : ev.Flag_eeBadScFilter[0] ==1
    <HBHENoiseFilter:LambdaStr> ev : ev.Flag_HBHENoiseFilter[0] == 1
    <HBHENoiseIsoFilter:LambdaStr> ev : ev.Flag_HBHENoiseIsoFilter[0] == 1
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <LeadJetEtaLT2p5:LambdaStr> ev : -2.5 < ev.jet_eta[0] < 2.5
    <LeadJetChHEFGT0p1:LambdaStr> ev : ev.jet_chHEF[0] >= 0.1
    <MhtOverMetNoXNoHF:LambdaStr> ev : ev.MhtOverMetNoXNoHF[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
    <SignalFinal:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflowId[0] == 1 # 'Signal'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <SignalBintypes:EventSelectionAny>
        <SignalFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SignalFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <HT_HLTAlphaT:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <HLTAlphaTHT200:EventSelectionAny>
                <HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57:LambdaStr> ev : ev.HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57[0]
                <HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63:LambdaStr> ev : ev.HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <HLTAlphaTHT250:EventSelectionAny>
                <HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55:LambdaStr> ev : ev.HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55[0]
                <HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58:LambdaStr> ev : ev.HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <HLTAlphaTHT300:EventSelectionAny>
                <HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53:LambdaStr> ev : ev.HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53[0]
                <HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54:LambdaStr> ev : ev.HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <HLTAlphaTHT350:EventSelectionAny>
                <HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52:LambdaStr> ev : ev.HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52[0]
                <HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53:LambdaStr> ev : ev.HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <HLTAlphaTHT400:EventSelectionAny>
                <HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51:LambdaStr> ev : ev.HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51[0]
                <HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52:LambdaStr> ev : ev.HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52[0]
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <HT_HLTAlphaT:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <HLTAlphaTHT200:EventSelectionAny>
                <HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57:LambdaStr> ev : ev.HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57[0]
                <HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63:LambdaStr> ev : ev.HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <HLTAlphaTHT250:EventSelectionAny>
                <HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55:LambdaStr> ev : ev.HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55[0]
                <HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58:LambdaStr> ev : ev.HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <HLTAlphaTHT300:EventSelectionAny>
                <HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53:LambdaStr> ev : ev.HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53[0]
                <HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54:LambdaStr> ev : ev.HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <HLTAlphaTHT350:EventSelectionAny>
                <HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52:LambdaStr> ev : ev.HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52[0]
                <HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53:LambdaStr> ev : ev.HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <HLTAlphaTHT400:EventSelectionAny>
                <HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51:LambdaStr> ev : ev.HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51[0]
                <HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52:LambdaStr> ev : ev.HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52[0]
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
    <SingleMuFinal:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflowId[0] == 2 # 'SingleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <HLT_SingleMuon:EventSelectionAny>
        <HLT_IsoMu17_eta2p1:LambdaStr> ev : ev.HLT_IsoMu17_eta2p1[0]
        <HLT_IsoMu20:LambdaStr> ev : ev.HLT_IsoMu20[0]
        <HLT_IsoMu24_eta2p1:LambdaStr> ev : ev.HLT_IsoMu24_eta2p1[0]
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mtwNoHF:LambdaStr> ev : 30 <= ev.mtwNoHF[0] < 125
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <DoubleMuFinal:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflowId[0] == 3 # 'DoubleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[1] < 0.12
      <HLT_SingleMuon:EventSelectionAny>
        <HLT_IsoMu17_eta2p1:LambdaStr> ev : ev.HLT_IsoMu17_eta2p1[0]
        <HLT_IsoMu20:LambdaStr> ev : ev.HLT_IsoMu20[0]
        <HLT_IsoMu24_eta2p1:LambdaStr> ev : ev.HLT_IsoMu24_eta2p1[0]
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <SingleEleFinal:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflowId[0] == 4 # 'SingleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mtwNoHF:LambdaStr> ev : 30 <= ev.mtwNoHF[0] < 125
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <DoubleEleFinal:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflowId[0] == 5 # 'DoubleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[1] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[1] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <SinglePhotonFinal:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflowId[0] == 6 # 'SinglePhoton'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <minDelRJetPhoton:LambdaStr> ev : ev.minDelRJetPhoton[0] >= 1.0
      <SinglePhotonFinalBintypes:EventSelectionAny>
        <SinglePhotonFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SinglePhotonFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
        <SinglePhotonFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
        <SinglePhotonFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
'''


es_arg100='''<All:EventSelectionAll>
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
    <SignalLoose:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflowId[0] == 1 # 'Signal'
      <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
      <SignalLooseBintypes:EventSelectionAny>
        <SignalLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SignalLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <AlphaTCutLoose:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT300to800:EventSelectionAll>
              <HTin300to800:LambdaStr> ev : 300 <= ev.ht40[0] < 800
              <alphaTGT0p55:LambdaStr> ev : 0.50 <= ev.alphaT[0]
        <SignalLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <AlphaTCutLoose:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT300to800:EventSelectionAll>
              <HTin300to800:LambdaStr> ev : 300 <= ev.ht40[0] < 800
              <alphaTGT0p55:LambdaStr> ev : 0.50 <= ev.alphaT[0]
        <SignalLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
    <SingleMuLoose:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflowId[0] == 2 # 'SingleMu'
    <DoubleMuLoose:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflowId[0] == 3 # 'DoubleMu'
    <SingleEleLoose:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflowId[0] == 4 # 'SingleEle'
    <DoubleEleLoose:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflowId[0] == 5 # 'DoubleEle'
    <SinglePhotonLoose:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflowId[0] == 6 # 'SinglePhoton'
      <SinglePhotonLooseBintypes:EventSelectionAny>
        <SinglePhotonLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SinglePhotonLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
  <MetFilters:EventSelectionAll>
    <goodVertex:LambdaStr> ev : ev.Flag_goodVertices[0] == 1
    <CSCTightHaloFilter:LambdaStr> ev : ev.Flag_CSCTightHaloFilter[0] ==1
    <eeBadScFilter:LambdaStr> ev : ev.Flag_eeBadScFilter[0] ==1
    <HBHENoiseFilter:LambdaStr> ev : ev.Flag_HBHENoiseFilter[0] == 1
  <UniquePromptPhotonPhaseSpaceInQCDandGJets:EventSelectionAll>
    <GenProcesses:EventSelectionAny>
      <GenProcessQCD:EventSelectionAll>
        <process_QCD:LambdaStr> ev : ev.GenProcess[0] == 'QCD'
        <nPromptDirectGenPhotonsEQ0:LambdaStr> ev : ev.nPromptDirectGenPhotons[0] == 0
      <GenProcessGJets:EventSelectionAll>
        <process_GJets:LambdaStr> ev : ev.GenProcess[0] == 'GJets'
        <nPromptDirectGenPhotonsGE1:LambdaStr> ev : ev.nPromptDirectGenPhotons[0] >= 1
      <GenProcessesNoQCDorGJets:EventSelectionAll>
        <process_not_QCD_or_GJets:LambdaStr> ev : ev.GenProcess[0] not in ('QCD', 'GJets')
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <LeadJetEtaLT2p5:LambdaStr> ev : -2.5 < ev.jet_eta[0] < 2.5
    <LeadJetChHEFGT0p1:LambdaStr> ev : ev.jet_chHEF[0] >= 0.1
    <MhtOverMetNoX:LambdaStr> ev : ev.MhtOverMetNoX[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
    <SignalFinal:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflowId[0] == 1 # 'Signal'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <SignalBintypes:EventSelectionAny>
        <SignalFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SignalFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
    <SingleMuFinal:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflowId[0] == 2 # 'SingleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mtw:LambdaStr> ev : 30 <= ev.mtw[0] < 125
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <DoubleMuFinal:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflowId[0] == 3 # 'DoubleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[1] < 0.12
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <SingleEleFinal:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflowId[0] == 4 # 'SingleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mtw:LambdaStr> ev : 30 <= ev.mtw[0] < 125
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <DoubleEleFinal:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflowId[0] == 5 # 'DoubleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[1] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[1] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <SinglePhotonFinal:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflowId[0] == 6 # 'SinglePhoton'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <minDelRJetPhoton:LambdaStr> ev : ev.minDelRJetPhoton[0] >= 1.0
      <SinglePhotonFinalBintypes:EventSelectionAny>
        <SinglePhotonFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SinglePhotonFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
        <SinglePhotonFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
        <SinglePhotonFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
'''


es_arg101='''<All:EventSelectionAll>
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
    <SignalLoose:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflowId[0] == 1 # 'Signal'
      <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
      <SignalLooseBintypes:EventSelectionAny>
        <SignalLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SignalLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <AlphaTCutLoose:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT300to800:EventSelectionAll>
              <HTin300to800:LambdaStr> ev : 300 <= ev.ht40[0] < 800
              <alphaTGT0p55:LambdaStr> ev : 0.50 <= ev.alphaT[0]
        <SignalLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <AlphaTCutLoose:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT300to800:EventSelectionAll>
              <HTin300to800:LambdaStr> ev : 300 <= ev.ht40[0] < 800
              <alphaTGT0p55:LambdaStr> ev : 0.50 <= ev.alphaT[0]
        <SignalLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
    <SingleMuLoose:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflowId[0] == 2 # 'SingleMu'
    <DoubleMuLoose:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflowId[0] == 3 # 'DoubleMu'
    <SingleEleLoose:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflowId[0] == 4 # 'SingleEle'
    <DoubleEleLoose:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflowId[0] == 5 # 'DoubleEle'
    <SinglePhotonLoose:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflowId[0] == 6 # 'SinglePhoton'
      <SinglePhotonLooseBintypes:EventSelectionAny>
        <SinglePhotonLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SinglePhotonLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
  <MetFilters:EventSelectionAll>
    <goodVertex:LambdaStr> ev : ev.Flag_goodVertices[0] == 1
    <CSCTightHaloFilter:LambdaStr> ev : ev.Flag_CSCTightHaloFilter[0] ==1
    <eeBadScFilter:LambdaStr> ev : ev.Flag_eeBadScFilter[0] ==1
    <HBHENoiseFilter:LambdaStr> ev : ev.Flag_HBHENoiseFilter[0] == 1
  <UniquePromptPhotonPhaseSpaceInQCDandGJets:EventSelectionAll>
    <GenProcesses:EventSelectionAny>
      <GenProcessQCD:EventSelectionAll>
        <process_QCD:LambdaStr> ev : ev.GenProcess[0] == 'QCD'
        <nPromptDirectGenPhotonsEQ0:LambdaStr> ev : ev.nPromptDirectGenPhotons[0] == 0
      <GenProcessGJets:EventSelectionAll>
        <process_GJets:LambdaStr> ev : ev.GenProcess[0] == 'GJets'
        <nPromptDirectGenPhotonsGE1:LambdaStr> ev : ev.nPromptDirectGenPhotons[0] >= 1
      <GenProcessesNoQCDorGJets:EventSelectionAll>
        <process_not_QCD_or_GJets:LambdaStr> ev : ev.GenProcess[0] not in ('QCD', 'GJets')
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <LeadJetEtaLT2p5:LambdaStr> ev : -2.5 < ev.jet_eta[0] < 2.5
    <LeadJetChHEFGT0p1:LambdaStr> ev : ev.jet_chHEF[0] >= 0.1
    <MhtOverMetNoXNoHF:LambdaStr> ev : ev.MhtOverMetNoXNoHF[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
    <SignalFinal:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflowId[0] == 1 # 'Signal'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <SignalBintypes:EventSelectionAny>
        <SignalFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SignalFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
    <SingleMuFinal:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflowId[0] == 2 # 'SingleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mtwNoHF:LambdaStr> ev : 30 <= ev.mtwNoHF[0] < 125
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <DoubleMuFinal:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflowId[0] == 3 # 'DoubleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[1] < 0.12
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <SingleEleFinal:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflowId[0] == 4 # 'SingleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mtwNoHF:LambdaStr> ev : 30 <= ev.mtwNoHF[0] < 125
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <DoubleEleFinal:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflowId[0] == 5 # 'DoubleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[1] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[1] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <SinglePhotonFinal:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflowId[0] == 6 # 'SinglePhoton'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <minDelRJetPhoton:LambdaStr> ev : ev.minDelRJetPhoton[0] >= 1.0
      <SinglePhotonFinalBintypes:EventSelectionAny>
        <SinglePhotonFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SinglePhotonFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
        <SinglePhotonFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
        <SinglePhotonFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
'''


es_arg102='''<All:EventSelectionAll>
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
    <SignalLoose:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflowId[0] == 1 # 'Signal'
      <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
      <SignalLooseBintypes:EventSelectionAny>
        <SignalLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SignalLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <AlphaTCutLoose:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT300to800:EventSelectionAll>
              <HTin300to800:LambdaStr> ev : 300 <= ev.ht40[0] < 800
              <alphaTGT0p55:LambdaStr> ev : 0.50 <= ev.alphaT[0]
        <SignalLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <AlphaTCutLoose:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT300to800:EventSelectionAll>
              <HTin300to800:LambdaStr> ev : 300 <= ev.ht40[0] < 800
              <alphaTGT0p55:LambdaStr> ev : 0.50 <= ev.alphaT[0]
        <SignalLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
    <SingleMuLoose:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflowId[0] == 2 # 'SingleMu'
    <DoubleMuLoose:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflowId[0] == 3 # 'DoubleMu'
    <SingleEleLoose:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflowId[0] == 4 # 'SingleEle'
    <DoubleEleLoose:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflowId[0] == 5 # 'DoubleEle'
    <SinglePhotonLoose:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflowId[0] == 6 # 'SinglePhoton'
      <SinglePhotonLooseBintypes:EventSelectionAny>
        <SinglePhotonLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SinglePhotonLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
  <MetFilters:EventSelectionAll>
    <goodVertex:LambdaStr> ev : ev.Flag_goodVertices[0] == 1
    <CSCTightHaloFilter:LambdaStr> ev : ev.Flag_CSCTightHaloFilter[0] ==1
    <eeBadScFilter:LambdaStr> ev : ev.Flag_eeBadScFilter[0] ==1
    <HBHENoiseFilter:LambdaStr> ev : ev.Flag_HBHENoiseFilter[0] == 1
  <UniquePromptPhotonPhaseSpaceInQCDandGJets:EventSelectionAll>
    <GenProcesses:EventSelectionAny>
      <GenProcessQCD:EventSelectionAll>
        <process_QCD:LambdaStr> ev : ev.GenProcess[0] == 'QCD'
        <nPromptDirectGenPhotonsEQ0:LambdaStr> ev : ev.nPromptDirectGenPhotons[0] == 0
      <GenProcessGJets:EventSelectionAll>
        <process_GJets:LambdaStr> ev : ev.GenProcess[0] == 'GJets'
        <nPromptDirectGenPhotonsGE1:LambdaStr> ev : ev.nPromptDirectGenPhotons[0] >= 1
      <GenProcessesNoQCDorGJets:EventSelectionAll>
        <process_not_QCD_or_GJets:LambdaStr> ev : ev.GenProcess[0] not in ('QCD', 'GJets')
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <LeadJetEtaLT2p5:LambdaStr> ev : -2.5 < ev.jet_eta[0] < 2.5
    <LeadJetChHEFGT0p1:LambdaStr> ev : ev.jet_chHEF[0] >= 0.1
    <MhtOverMetNoX:LambdaStr> ev : ev.MhtOverMetNoX[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
    <SignalFinal:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflowId[0] == 1 # 'Signal'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <SignalBintypes:EventSelectionAny>
        <SignalFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SignalFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
    <SingleMuFinal:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflowId[0] == 2 # 'SingleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mtw:LambdaStr> ev : 30 <= ev.mtw[0] < 125
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <DoubleMuFinal:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflowId[0] == 3 # 'DoubleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[1] < 0.12
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <SingleEleFinal:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflowId[0] == 4 # 'SingleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mtw:LambdaStr> ev : 30 <= ev.mtw[0] < 125
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <DoubleEleFinal:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflowId[0] == 5 # 'DoubleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[1] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[1] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <SinglePhotonFinal:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflowId[0] == 6 # 'SinglePhoton'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <minDelRJetPhoton:LambdaStr> ev : ev.minDelRJetPhoton[0] >= 1.0
      <SinglePhotonFinalBintypes:EventSelectionAny>
        <SinglePhotonFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SinglePhotonFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
        <SinglePhotonFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
        <SinglePhotonFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
'''


es_arg103='''<All:EventSelectionAll>
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
    <SignalLoose:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflowId[0] == 1 # 'Signal'
      <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
      <SignalLooseBintypes:EventSelectionAny>
        <SignalLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SignalLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <AlphaTCutLoose:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT300to800:EventSelectionAll>
              <HTin300to800:LambdaStr> ev : 300 <= ev.ht40[0] < 800
              <alphaTGT0p55:LambdaStr> ev : 0.50 <= ev.alphaT[0]
        <SignalLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <AlphaTCutLoose:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT300to800:EventSelectionAll>
              <HTin300to800:LambdaStr> ev : 300 <= ev.ht40[0] < 800
              <alphaTGT0p55:LambdaStr> ev : 0.50 <= ev.alphaT[0]
        <SignalLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
    <SingleMuLoose:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflowId[0] == 2 # 'SingleMu'
    <DoubleMuLoose:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflowId[0] == 3 # 'DoubleMu'
    <SingleEleLoose:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflowId[0] == 4 # 'SingleEle'
    <DoubleEleLoose:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflowId[0] == 5 # 'DoubleEle'
    <SinglePhotonLoose:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflowId[0] == 6 # 'SinglePhoton'
      <SinglePhotonLooseBintypes:EventSelectionAny>
        <SinglePhotonLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SinglePhotonLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
  <MetFilters:EventSelectionAll>
    <goodVertex:LambdaStr> ev : ev.Flag_goodVertices[0] == 1
    <CSCTightHaloFilter:LambdaStr> ev : ev.Flag_CSCTightHaloFilter[0] ==1
    <eeBadScFilter:LambdaStr> ev : ev.Flag_eeBadScFilter[0] ==1
    <HBHENoiseFilter:LambdaStr> ev : ev.Flag_HBHENoiseFilter[0] == 1
  <UniquePromptPhotonPhaseSpaceInQCDandGJets:EventSelectionAll>
    <GenProcesses:EventSelectionAny>
      <GenProcessQCD:EventSelectionAll>
        <process_QCD:LambdaStr> ev : ev.GenProcess[0] == 'QCD'
        <nPromptDirectGenPhotonsEQ0:LambdaStr> ev : ev.nPromptDirectGenPhotons[0] == 0
      <GenProcessGJets:EventSelectionAll>
        <process_GJets:LambdaStr> ev : ev.GenProcess[0] == 'GJets'
        <nPromptDirectGenPhotonsGE1:LambdaStr> ev : ev.nPromptDirectGenPhotons[0] >= 1
      <GenProcessesNoQCDorGJets:EventSelectionAll>
        <process_not_QCD_or_GJets:LambdaStr> ev : ev.GenProcess[0] not in ('QCD', 'GJets')
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <LeadJetEtaLT2p5:LambdaStr> ev : -2.5 < ev.jet_eta[0] < 2.5
    <LeadJetChHEFGT0p1:LambdaStr> ev : ev.jet_chHEF[0] >= 0.1
    <MhtOverMetNoXNoHF:LambdaStr> ev : ev.MhtOverMetNoXNoHF[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
    <SignalFinal:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflowId[0] == 1 # 'Signal'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <SignalBintypes:EventSelectionAny>
        <SignalFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SignalFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
    <SingleMuFinal:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflowId[0] == 2 # 'SingleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mtwNoHF:LambdaStr> ev : 30 <= ev.mtwNoHF[0] < 125
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <DoubleMuFinal:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflowId[0] == 3 # 'DoubleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[1] < 0.12
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <SingleEleFinal:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflowId[0] == 4 # 'SingleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mtwNoHF:LambdaStr> ev : 30 <= ev.mtwNoHF[0] < 125
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <DoubleEleFinal:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflowId[0] == 5 # 'DoubleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[1] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[1] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <SinglePhotonFinal:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflowId[0] == 6 # 'SinglePhoton'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <minDelRJetPhoton:LambdaStr> ev : ev.minDelRJetPhoton[0] >= 1.0
      <SinglePhotonFinalBintypes:EventSelectionAny>
        <SinglePhotonFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SinglePhotonFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
        <SinglePhotonFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
        <SinglePhotonFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
'''


es_arg104='''<All:EventSelectionAll>
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
    <SignalLoose:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflowId[0] == 1 # 'Signal'
      <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
      <SignalLooseBintypes:EventSelectionAny>
        <SignalLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SignalLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <AlphaTCutLoose:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT300to800:EventSelectionAll>
              <HTin300to800:LambdaStr> ev : 300 <= ev.ht40[0] < 800
              <alphaTGT0p55:LambdaStr> ev : 0.50 <= ev.alphaT[0]
        <SignalLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <AlphaTCutLoose:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT300to800:EventSelectionAll>
              <HTin300to800:LambdaStr> ev : 300 <= ev.ht40[0] < 800
              <alphaTGT0p55:LambdaStr> ev : 0.50 <= ev.alphaT[0]
        <SignalLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
    <SingleMuLoose:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflowId[0] == 2 # 'SingleMu'
    <DoubleMuLoose:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflowId[0] == 3 # 'DoubleMu'
    <SingleEleLoose:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflowId[0] == 4 # 'SingleEle'
    <DoubleEleLoose:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflowId[0] == 5 # 'DoubleEle'
    <SinglePhotonLoose:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflowId[0] == 6 # 'SinglePhoton'
      <SinglePhotonLooseBintypes:EventSelectionAny>
        <SinglePhotonLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SinglePhotonLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
  <MetFilters:EventSelectionAll>
    <goodVertex:LambdaStr> ev : ev.Flag_goodVertices[0] == 1
    <CSCTightHaloFilter:LambdaStr> ev : ev.Flag_CSCTightHaloFilter[0] ==1
    <eeBadScFilter:LambdaStr> ev : ev.Flag_eeBadScFilter[0] ==1
    <HBHENoiseFilter:LambdaStr> ev : ev.Flag_HBHENoiseFilter[0] == 1
  <UniquePromptPhotonPhaseSpaceInQCDandGJets:EventSelectionAll>
    <GenProcesses:EventSelectionAny>
      <GenProcessQCD:EventSelectionAll>
        <process_QCD:LambdaStr> ev : ev.GenProcess[0] == 'QCD'
        <nPromptDirectGenPhotonsEQ0:LambdaStr> ev : ev.nPromptDirectGenPhotons[0] == 0
      <GenProcessGJets:EventSelectionAll>
        <process_GJets:LambdaStr> ev : ev.GenProcess[0] == 'GJets'
        <nPromptDirectGenPhotonsGE1:LambdaStr> ev : ev.nPromptDirectGenPhotons[0] >= 1
      <GenProcessesNoQCDorGJets:EventSelectionAll>
        <process_not_QCD_or_GJets:LambdaStr> ev : ev.GenProcess[0] not in ('QCD', 'GJets')
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <LeadJetEtaLT2p5:LambdaStr> ev : -2.5 < ev.jet_eta[0] < 2.5
    <LeadJetChHEFGT0p1:LambdaStr> ev : ev.jet_chHEF[0] >= 0.1
    <MhtOverMetNoX:LambdaStr> ev : ev.MhtOverMetNoX[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
    <SignalFinal:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflowId[0] == 1 # 'Signal'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <SignalBintypes:EventSelectionAny>
        <SignalFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SignalFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
    <SingleMuFinal:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflowId[0] == 2 # 'SingleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <HLT_SingleMuon:EventSelectionAny>
        <HLT_IsoMu17_eta2p1:LambdaStr> ev : ev.HLT_IsoMu17_eta2p1[0]
        <HLT_IsoMu20:LambdaStr> ev : ev.HLT_IsoMu20[0]
        <HLT_IsoMu24_eta2p1:LambdaStr> ev : ev.HLT_IsoMu24_eta2p1[0]
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mtw:LambdaStr> ev : 30 <= ev.mtw[0] < 125
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <DoubleMuFinal:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflowId[0] == 3 # 'DoubleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[1] < 0.12
      <HLT_SingleMuon:EventSelectionAny>
        <HLT_IsoMu17_eta2p1:LambdaStr> ev : ev.HLT_IsoMu17_eta2p1[0]
        <HLT_IsoMu20:LambdaStr> ev : ev.HLT_IsoMu20[0]
        <HLT_IsoMu24_eta2p1:LambdaStr> ev : ev.HLT_IsoMu24_eta2p1[0]
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <SingleEleFinal:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflowId[0] == 4 # 'SingleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mtw:LambdaStr> ev : 30 <= ev.mtw[0] < 125
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <DoubleEleFinal:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflowId[0] == 5 # 'DoubleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[1] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[1] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <SinglePhotonFinal:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflowId[0] == 6 # 'SinglePhoton'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <minDelRJetPhoton:LambdaStr> ev : ev.minDelRJetPhoton[0] >= 1.0
      <SinglePhotonFinalBintypes:EventSelectionAny>
        <SinglePhotonFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SinglePhotonFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
        <SinglePhotonFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
        <SinglePhotonFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
'''


es_arg105='''<All:EventSelectionAll>
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
    <SignalLoose:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflowId[0] == 1 # 'Signal'
      <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
      <SignalLooseBintypes:EventSelectionAny>
        <SignalLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SignalLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <AlphaTCutLoose:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT300to800:EventSelectionAll>
              <HTin300to800:LambdaStr> ev : 300 <= ev.ht40[0] < 800
              <alphaTGT0p55:LambdaStr> ev : 0.50 <= ev.alphaT[0]
        <SignalLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <AlphaTCutLoose:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT300to800:EventSelectionAll>
              <HTin300to800:LambdaStr> ev : 300 <= ev.ht40[0] < 800
              <alphaTGT0p55:LambdaStr> ev : 0.50 <= ev.alphaT[0]
        <SignalLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
    <SingleMuLoose:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflowId[0] == 2 # 'SingleMu'
    <DoubleMuLoose:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflowId[0] == 3 # 'DoubleMu'
    <SingleEleLoose:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflowId[0] == 4 # 'SingleEle'
    <DoubleEleLoose:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflowId[0] == 5 # 'DoubleEle'
    <SinglePhotonLoose:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflowId[0] == 6 # 'SinglePhoton'
      <SinglePhotonLooseBintypes:EventSelectionAny>
        <SinglePhotonLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SinglePhotonLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
  <MetFilters:EventSelectionAll>
    <goodVertex:LambdaStr> ev : ev.Flag_goodVertices[0] == 1
    <CSCTightHaloFilter:LambdaStr> ev : ev.Flag_CSCTightHaloFilter[0] ==1
    <eeBadScFilter:LambdaStr> ev : ev.Flag_eeBadScFilter[0] ==1
    <HBHENoiseFilter:LambdaStr> ev : ev.Flag_HBHENoiseFilter[0] == 1
  <UniquePromptPhotonPhaseSpaceInQCDandGJets:EventSelectionAll>
    <GenProcesses:EventSelectionAny>
      <GenProcessQCD:EventSelectionAll>
        <process_QCD:LambdaStr> ev : ev.GenProcess[0] == 'QCD'
        <nPromptDirectGenPhotonsEQ0:LambdaStr> ev : ev.nPromptDirectGenPhotons[0] == 0
      <GenProcessGJets:EventSelectionAll>
        <process_GJets:LambdaStr> ev : ev.GenProcess[0] == 'GJets'
        <nPromptDirectGenPhotonsGE1:LambdaStr> ev : ev.nPromptDirectGenPhotons[0] >= 1
      <GenProcessesNoQCDorGJets:EventSelectionAll>
        <process_not_QCD_or_GJets:LambdaStr> ev : ev.GenProcess[0] not in ('QCD', 'GJets')
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <LeadJetEtaLT2p5:LambdaStr> ev : -2.5 < ev.jet_eta[0] < 2.5
    <LeadJetChHEFGT0p1:LambdaStr> ev : ev.jet_chHEF[0] >= 0.1
    <MhtOverMetNoXNoHF:LambdaStr> ev : ev.MhtOverMetNoXNoHF[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
    <SignalFinal:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflowId[0] == 1 # 'Signal'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <SignalBintypes:EventSelectionAny>
        <SignalFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SignalFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
    <SingleMuFinal:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflowId[0] == 2 # 'SingleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <HLT_SingleMuon:EventSelectionAny>
        <HLT_IsoMu17_eta2p1:LambdaStr> ev : ev.HLT_IsoMu17_eta2p1[0]
        <HLT_IsoMu20:LambdaStr> ev : ev.HLT_IsoMu20[0]
        <HLT_IsoMu24_eta2p1:LambdaStr> ev : ev.HLT_IsoMu24_eta2p1[0]
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mtwNoHF:LambdaStr> ev : 30 <= ev.mtwNoHF[0] < 125
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <DoubleMuFinal:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflowId[0] == 3 # 'DoubleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[1] < 0.12
      <HLT_SingleMuon:EventSelectionAny>
        <HLT_IsoMu17_eta2p1:LambdaStr> ev : ev.HLT_IsoMu17_eta2p1[0]
        <HLT_IsoMu20:LambdaStr> ev : ev.HLT_IsoMu20[0]
        <HLT_IsoMu24_eta2p1:LambdaStr> ev : ev.HLT_IsoMu24_eta2p1[0]
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <SingleEleFinal:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflowId[0] == 4 # 'SingleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mtwNoHF:LambdaStr> ev : 30 <= ev.mtwNoHF[0] < 125
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <DoubleEleFinal:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflowId[0] == 5 # 'DoubleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[1] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[1] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <SinglePhotonFinal:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflowId[0] == 6 # 'SinglePhoton'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <minDelRJetPhoton:LambdaStr> ev : ev.minDelRJetPhoton[0] >= 1.0
      <SinglePhotonFinalBintypes:EventSelectionAny>
        <SinglePhotonFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SinglePhotonFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
        <SinglePhotonFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
        <SinglePhotonFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
'''


es_arg106='''<All:EventSelectionAll>
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
    <SignalLoose:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflowId[0] == 1 # 'Signal'
      <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
      <SignalLooseBintypes:EventSelectionAny>
        <SignalLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SignalLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <AlphaTCutLoose:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT300to800:EventSelectionAll>
              <HTin300to800:LambdaStr> ev : 300 <= ev.ht40[0] < 800
              <alphaTGT0p55:LambdaStr> ev : 0.50 <= ev.alphaT[0]
        <SignalLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <AlphaTCutLoose:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT300to800:EventSelectionAll>
              <HTin300to800:LambdaStr> ev : 300 <= ev.ht40[0] < 800
              <alphaTGT0p55:LambdaStr> ev : 0.50 <= ev.alphaT[0]
        <SignalLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
    <SingleMuLoose:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflowId[0] == 2 # 'SingleMu'
    <DoubleMuLoose:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflowId[0] == 3 # 'DoubleMu'
    <SingleEleLoose:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflowId[0] == 4 # 'SingleEle'
    <DoubleEleLoose:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflowId[0] == 5 # 'DoubleEle'
    <SinglePhotonLoose:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflowId[0] == 6 # 'SinglePhoton'
      <SinglePhotonLooseBintypes:EventSelectionAny>
        <SinglePhotonLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SinglePhotonLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
  <MetFilters:EventSelectionAll>
    <goodVertex:LambdaStr> ev : ev.Flag_goodVertices[0] == 1
    <CSCTightHaloFilter:LambdaStr> ev : ev.Flag_CSCTightHaloFilter[0] ==1
    <eeBadScFilter:LambdaStr> ev : ev.Flag_eeBadScFilter[0] ==1
    <HBHENoiseFilter:LambdaStr> ev : ev.Flag_HBHENoiseFilter[0] == 1
  <UniquePromptPhotonPhaseSpaceInQCDandGJets:EventSelectionAll>
    <GenProcesses:EventSelectionAny>
      <GenProcessQCD:EventSelectionAll>
        <process_QCD:LambdaStr> ev : ev.GenProcess[0] == 'QCD'
        <nPromptDirectGenPhotonsEQ0:LambdaStr> ev : ev.nPromptDirectGenPhotons[0] == 0
      <GenProcessGJets:EventSelectionAll>
        <process_GJets:LambdaStr> ev : ev.GenProcess[0] == 'GJets'
        <nPromptDirectGenPhotonsGE1:LambdaStr> ev : ev.nPromptDirectGenPhotons[0] >= 1
      <GenProcessesNoQCDorGJets:EventSelectionAll>
        <process_not_QCD_or_GJets:LambdaStr> ev : ev.GenProcess[0] not in ('QCD', 'GJets')
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <LeadJetEtaLT2p5:LambdaStr> ev : -2.5 < ev.jet_eta[0] < 2.5
    <LeadJetChHEFGT0p1:LambdaStr> ev : ev.jet_chHEF[0] >= 0.1
    <MhtOverMetNoX:LambdaStr> ev : ev.MhtOverMetNoX[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
    <SignalFinal:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflowId[0] == 1 # 'Signal'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <SignalBintypes:EventSelectionAny>
        <SignalFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SignalFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
    <SingleMuFinal:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflowId[0] == 2 # 'SingleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <HLT_SingleMuon:EventSelectionAny>
        <HLT_IsoMu17_eta2p1:LambdaStr> ev : ev.HLT_IsoMu17_eta2p1[0]
        <HLT_IsoMu20:LambdaStr> ev : ev.HLT_IsoMu20[0]
        <HLT_IsoMu24_eta2p1:LambdaStr> ev : ev.HLT_IsoMu24_eta2p1[0]
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mtw:LambdaStr> ev : 30 <= ev.mtw[0] < 125
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <DoubleMuFinal:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflowId[0] == 3 # 'DoubleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[1] < 0.12
      <HLT_SingleMuon:EventSelectionAny>
        <HLT_IsoMu17_eta2p1:LambdaStr> ev : ev.HLT_IsoMu17_eta2p1[0]
        <HLT_IsoMu20:LambdaStr> ev : ev.HLT_IsoMu20[0]
        <HLT_IsoMu24_eta2p1:LambdaStr> ev : ev.HLT_IsoMu24_eta2p1[0]
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <SingleEleFinal:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflowId[0] == 4 # 'SingleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mtw:LambdaStr> ev : 30 <= ev.mtw[0] < 125
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <DoubleEleFinal:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflowId[0] == 5 # 'DoubleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[1] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[1] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <SinglePhotonFinal:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflowId[0] == 6 # 'SinglePhoton'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <minDelRJetPhoton:LambdaStr> ev : ev.minDelRJetPhoton[0] >= 1.0
      <SinglePhotonFinalBintypes:EventSelectionAny>
        <SinglePhotonFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SinglePhotonFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
        <SinglePhotonFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
        <SinglePhotonFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
'''


es_arg107='''<All:EventSelectionAll>
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
    <SignalLoose:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflowId[0] == 1 # 'Signal'
      <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
      <SignalLooseBintypes:EventSelectionAny>
        <SignalLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SignalLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <AlphaTCutLoose:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT300to800:EventSelectionAll>
              <HTin300to800:LambdaStr> ev : 300 <= ev.ht40[0] < 800
              <alphaTGT0p55:LambdaStr> ev : 0.50 <= ev.alphaT[0]
        <SignalLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <AlphaTCutLoose:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT300to800:EventSelectionAll>
              <HTin300to800:LambdaStr> ev : 300 <= ev.ht40[0] < 800
              <alphaTGT0p55:LambdaStr> ev : 0.50 <= ev.alphaT[0]
        <SignalLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
    <SingleMuLoose:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflowId[0] == 2 # 'SingleMu'
    <DoubleMuLoose:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflowId[0] == 3 # 'DoubleMu'
    <SingleEleLoose:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflowId[0] == 4 # 'SingleEle'
    <DoubleEleLoose:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflowId[0] == 5 # 'DoubleEle'
    <SinglePhotonLoose:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflowId[0] == 6 # 'SinglePhoton'
      <SinglePhotonLooseBintypes:EventSelectionAny>
        <SinglePhotonLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SinglePhotonLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
  <MetFilters:EventSelectionAll>
    <goodVertex:LambdaStr> ev : ev.Flag_goodVertices[0] == 1
    <CSCTightHaloFilter:LambdaStr> ev : ev.Flag_CSCTightHaloFilter[0] ==1
    <eeBadScFilter:LambdaStr> ev : ev.Flag_eeBadScFilter[0] ==1
    <HBHENoiseFilter:LambdaStr> ev : ev.Flag_HBHENoiseFilter[0] == 1
  <UniquePromptPhotonPhaseSpaceInQCDandGJets:EventSelectionAll>
    <GenProcesses:EventSelectionAny>
      <GenProcessQCD:EventSelectionAll>
        <process_QCD:LambdaStr> ev : ev.GenProcess[0] == 'QCD'
        <nPromptDirectGenPhotonsEQ0:LambdaStr> ev : ev.nPromptDirectGenPhotons[0] == 0
      <GenProcessGJets:EventSelectionAll>
        <process_GJets:LambdaStr> ev : ev.GenProcess[0] == 'GJets'
        <nPromptDirectGenPhotonsGE1:LambdaStr> ev : ev.nPromptDirectGenPhotons[0] >= 1
      <GenProcessesNoQCDorGJets:EventSelectionAll>
        <process_not_QCD_or_GJets:LambdaStr> ev : ev.GenProcess[0] not in ('QCD', 'GJets')
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <LeadJetEtaLT2p5:LambdaStr> ev : -2.5 < ev.jet_eta[0] < 2.5
    <LeadJetChHEFGT0p1:LambdaStr> ev : ev.jet_chHEF[0] >= 0.1
    <MhtOverMetNoXNoHF:LambdaStr> ev : ev.MhtOverMetNoXNoHF[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
    <SignalFinal:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflowId[0] == 1 # 'Signal'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <SignalBintypes:EventSelectionAny>
        <SignalFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SignalFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
    <SingleMuFinal:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflowId[0] == 2 # 'SingleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <HLT_SingleMuon:EventSelectionAny>
        <HLT_IsoMu17_eta2p1:LambdaStr> ev : ev.HLT_IsoMu17_eta2p1[0]
        <HLT_IsoMu20:LambdaStr> ev : ev.HLT_IsoMu20[0]
        <HLT_IsoMu24_eta2p1:LambdaStr> ev : ev.HLT_IsoMu24_eta2p1[0]
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mtwNoHF:LambdaStr> ev : 30 <= ev.mtwNoHF[0] < 125
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <DoubleMuFinal:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflowId[0] == 3 # 'DoubleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[1] < 0.12
      <HLT_SingleMuon:EventSelectionAny>
        <HLT_IsoMu17_eta2p1:LambdaStr> ev : ev.HLT_IsoMu17_eta2p1[0]
        <HLT_IsoMu20:LambdaStr> ev : ev.HLT_IsoMu20[0]
        <HLT_IsoMu24_eta2p1:LambdaStr> ev : ev.HLT_IsoMu24_eta2p1[0]
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <SingleEleFinal:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflowId[0] == 4 # 'SingleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mtwNoHF:LambdaStr> ev : 30 <= ev.mtwNoHF[0] < 125
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <DoubleEleFinal:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflowId[0] == 5 # 'DoubleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[1] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[1] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <SinglePhotonFinal:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflowId[0] == 6 # 'SinglePhoton'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <minDelRJetPhoton:LambdaStr> ev : ev.minDelRJetPhoton[0] >= 1.0
      <SinglePhotonFinalBintypes:EventSelectionAny>
        <SinglePhotonFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SinglePhotonFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
        <SinglePhotonFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
        <SinglePhotonFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
'''


es_arg200='''<All:EventSelectionAll>
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
    <SignalLoose:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflowId[0] == 1 # 'Signal'
      <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
      <SignalLooseBintypes:EventSelectionAny>
        <SignalLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SignalLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <AlphaTCutLoose:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT300to800:EventSelectionAll>
              <HTin300to800:LambdaStr> ev : 300 <= ev.ht40[0] < 800
              <alphaTGT0p55:LambdaStr> ev : 0.50 <= ev.alphaT[0]
        <SignalLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <AlphaTCutLoose:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT300to800:EventSelectionAll>
              <HTin300to800:LambdaStr> ev : 300 <= ev.ht40[0] < 800
              <alphaTGT0p55:LambdaStr> ev : 0.50 <= ev.alphaT[0]
        <SignalLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
    <SingleEleLoose:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflowId[0] == 4 # 'SingleEle'
'''


es_arg201='''<All:EventSelectionAll>
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
    <SignalLoose:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflowId[0] == 1 # 'Signal'
      <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
      <SignalLooseBintypes:EventSelectionAny>
        <SignalLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SignalLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <AlphaTCutLoose:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT300to800:EventSelectionAll>
              <HTin300to800:LambdaStr> ev : 300 <= ev.ht40[0] < 800
              <alphaTGT0p55:LambdaStr> ev : 0.50 <= ev.alphaT[0]
        <SignalLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <AlphaTCutLoose:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT300to800:EventSelectionAll>
              <HTin300to800:LambdaStr> ev : 300 <= ev.ht40[0] < 800
              <alphaTGT0p55:LambdaStr> ev : 0.50 <= ev.alphaT[0]
        <SignalLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
    <SingleEleLoose:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflowId[0] == 4 # 'SingleEle'
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <LeadJetEtaLT2p5:LambdaStr> ev : -2.5 < ev.jet_eta[0] < 2.5
    <LeadJetChHEFGT0p1:LambdaStr> ev : ev.jet_chHEF[0] >= 0.1
    <MhtOverMetNoX:LambdaStr> ev : ev.MhtOverMetNoX[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
    <SignalFinal:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflowId[0] == 1 # 'Signal'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <SignalBintypes:EventSelectionAny>
        <SignalFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SignalFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
    <SingleEleFinal:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflowId[0] == 4 # 'SingleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mtw:LambdaStr> ev : 30 <= ev.mtw[0] < 125
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
'''


es_arg202='''<All:EventSelectionAll>
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
'''


es_arg203='''<All:EventSelectionAll>
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <LeadJetEtaLT2p5:LambdaStr> ev : -2.5 < ev.jet_eta[0] < 2.5
    <LeadJetChHEFGT0p1:LambdaStr> ev : ev.jet_chHEF[0] >= 0.1
    <MhtOverMetNoX:LambdaStr> ev : ev.MhtOverMetNoX[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
'''


es_arg204='''<All:EventSelectionAll>
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <LeadJetEtaLT2p5:LambdaStr> ev : -2.5 < ev.jet_eta[0] < 2.5
    <LeadJetChHEFGT0p1:LambdaStr> ev : ev.jet_chHEF[0] >= 0.1
    <MhtOverMetNoX:LambdaStr> ev : ev.MhtOverMetNoX[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
    <SignalFinal:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflowId[0] == 1 # 'Signal'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <SignalBintypes:EventSelectionAny>
        <SignalFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintypeId[0] == 1 # 'monojet'
        <SignalFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintypeId[0] == 2 # 'asymjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintypeId[0] == 3 # 'symjet'
          <AlphaTCut:EventSelectionAny>
            <HT200to250:EventSelectionAll>
              <HTin200to250:LambdaStr> ev : 200 <= ev.ht40[0] < 250
              <alphaTGT0p65:LambdaStr> ev : 0.65 <= ev.alphaT[0]
            <HT250to300:EventSelectionAll>
              <HTin250to300:LambdaStr> ev : 250 <= ev.ht40[0] < 300
              <alphaTGT0p60:LambdaStr> ev : 0.60 <= ev.alphaT[0]
            <HT300to350:EventSelectionAll>
              <HTin300to350:LambdaStr> ev : 300 <= ev.ht40[0] < 350
              <alphaTGT0p55:LambdaStr> ev : 0.55 <= ev.alphaT[0]
            <HT350to400:EventSelectionAll>
              <HTin350to400:LambdaStr> ev : 350 <= ev.ht40[0] < 400
              <alphaTGT0p53:LambdaStr> ev : 0.53 <= ev.alphaT[0]
            <HT400to800:EventSelectionAll>
              <HTin400to800:LambdaStr> ev : 400 <= ev.ht40[0] < 800
              <alphaTGT0p52:LambdaStr> ev : 0.52 <= ev.alphaT[0]
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintypeId[0] == 4 # 'highht'
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
    <SingleEleFinal:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflowId[0] == 4 # 'SingleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mtw:LambdaStr> ev : 30 <= ev.mtw[0] < 125
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
'''
##__________________________________________________________________||
