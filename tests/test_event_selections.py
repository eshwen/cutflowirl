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
        self.do_arg(arg008, es_arg008)
        self.do_arg(arg009, es_arg009)
        self.do_arg(arg010, es_arg010)
        self.do_arg(arg011, es_arg011)
        self.do_arg(arg012, es_arg012)
        self.do_arg(arg013, es_arg013)
        self.do_arg(arg014, es_arg014)
        self.do_arg(arg015, es_arg015)
        self.do_arg(arg100, es_arg100)
        self.do_arg(arg101, es_arg101)
        self.do_arg(arg102, es_arg102)
        self.do_arg(arg103, es_arg103)
        self.do_arg(arg104, es_arg104)
        self.do_arg(arg105, es_arg105)
        self.do_arg(arg106, es_arg106)
        self.do_arg(arg107, es_arg107)
        self.do_arg(arg108, es_arg108)
        self.do_arg(arg109, es_arg109)
        self.do_arg(arg110, es_arg110)
        self.do_arg(arg111, es_arg111)
        self.do_arg(arg112, es_arg112)
        self.do_arg(arg113, es_arg113)
        self.do_arg(arg114, es_arg114)
        self.do_arg(arg115, es_arg115)

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
        self.print_ev_for(arg008, 'arg008')
        self.print_ev_for(arg009, 'arg009')
        self.print_ev_for(arg010, 'arg010')
        self.print_ev_for(arg011, 'arg011')
        self.print_ev_for(arg012, 'arg012')
        self.print_ev_for(arg013, 'arg013')
        self.print_ev_for(arg014, 'arg014')
        self.print_ev_for(arg015, 'arg015')
        self.print_ev_for(arg100, 'arg100')
        self.print_ev_for(arg101, 'arg101')
        self.print_ev_for(arg102, 'arg102')
        self.print_ev_for(arg103, 'arg103')
        self.print_ev_for(arg104, 'arg104')
        self.print_ev_for(arg105, 'arg105')
        self.print_ev_for(arg106, 'arg106')
        self.print_ev_for(arg107, 'arg107')
        self.print_ev_for(arg108, 'arg108')
        self.print_ev_for(arg109, 'arg109')
        self.print_ev_for(arg110, 'arg110')
        self.print_ev_for(arg111, 'arg111')
        self.print_ev_for(arg112, 'arg112')
        self.print_ev_for(arg113, 'arg113')
        self.print_ev_for(arg114, 'arg114')
        self.print_ev_for(arg115, 'arg115')

    def print_ev_for(self, arg, argName):
        print '\n'
        print 'es_' + argName + "='''" + test_event_selection_str(event_selection(**arg)) + "'''"

##__________________________________________________________________||
arg000 = dict(datamc = 'data', level = 'final', hlt = False, pd = False, met_filters = False, metnohf = False )
arg001 = dict(datamc = 'data', level = 'final', hlt = False, pd = False, met_filters = False, metnohf = True  )
arg002 = dict(datamc = 'data', level = 'final', hlt = False, pd = False, met_filters = True,  metnohf = False )
arg003 = dict(datamc = 'data', level = 'final', hlt = False, pd = False, met_filters = True,  metnohf = True  )
arg004 = dict(datamc = 'data', level = 'final', hlt = False, pd = True,  met_filters = False, metnohf = False )
arg005 = dict(datamc = 'data', level = 'final', hlt = False, pd = True,  met_filters = False, metnohf = True  )
arg006 = dict(datamc = 'data', level = 'final', hlt = False, pd = True,  met_filters = True,  metnohf = False )
arg007 = dict(datamc = 'data', level = 'final', hlt = False, pd = True,  met_filters = True,  metnohf = True  )
arg008 = dict(datamc = 'data', level = 'final', hlt = True,  pd = False, met_filters = False, metnohf = False )
arg009 = dict(datamc = 'data', level = 'final', hlt = True,  pd = False, met_filters = False, metnohf = True  )
arg010 = dict(datamc = 'data', level = 'final', hlt = True,  pd = False, met_filters = True,  metnohf = False )
arg011 = dict(datamc = 'data', level = 'final', hlt = True,  pd = False, met_filters = True,  metnohf = True  )
arg012 = dict(datamc = 'data', level = 'final', hlt = True,  pd = True,  met_filters = False, metnohf = False )
arg013 = dict(datamc = 'data', level = 'final', hlt = True,  pd = True,  met_filters = False, metnohf = True  )
arg014 = dict(datamc = 'data', level = 'final', hlt = True,  pd = True,  met_filters = True,  metnohf = False )
arg015 = dict(datamc = 'data', level = 'final', hlt = True,  pd = True,  met_filters = True,  metnohf = True  )
arg100 = dict(datamc = 'mc', level = 'final', hlt = False, pd = False, met_filters = False, metnohf = False )
arg101 = dict(datamc = 'mc', level = 'final', hlt = False, pd = False, met_filters = False, metnohf = True  )
arg102 = dict(datamc = 'mc', level = 'final', hlt = False, pd = False, met_filters = True,  metnohf = False )
arg103 = dict(datamc = 'mc', level = 'final', hlt = False, pd = False, met_filters = True,  metnohf = True  )
arg104 = dict(datamc = 'mc', level = 'final', hlt = False, pd = True,  met_filters = False, metnohf = False )
arg105 = dict(datamc = 'mc', level = 'final', hlt = False, pd = True,  met_filters = False, metnohf = True  )
arg106 = dict(datamc = 'mc', level = 'final', hlt = False, pd = True,  met_filters = True,  metnohf = False )
arg107 = dict(datamc = 'mc', level = 'final', hlt = False, pd = True,  met_filters = True,  metnohf = True  )
arg108 = dict(datamc = 'mc', level = 'final', hlt = True,  pd = False, met_filters = False, metnohf = False )
arg109 = dict(datamc = 'mc', level = 'final', hlt = True,  pd = False, met_filters = False, metnohf = True  )
arg110 = dict(datamc = 'mc', level = 'final', hlt = True,  pd = False, met_filters = True,  metnohf = False )
arg111 = dict(datamc = 'mc', level = 'final', hlt = True,  pd = False, met_filters = True,  metnohf = True  )
arg112 = dict(datamc = 'mc', level = 'final', hlt = True,  pd = True,  met_filters = False, metnohf = False )
arg113 = dict(datamc = 'mc', level = 'final', hlt = True,  pd = True,  met_filters = False, metnohf = True  )
arg114 = dict(datamc = 'mc', level = 'final', hlt = True,  pd = True,  met_filters = True,  metnohf = False )
arg115 = dict(datamc = 'mc', level = 'final', hlt = True,  pd = True,  met_filters = True,  metnohf = True  )

##__________________________________________________________________||
es_arg000='''<All:EventSelectionAll>
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
    <SignalLoose:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
      <SignalLooseBintypes:EventSelectionAny>
        <SignalLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
    <SingleMuLoose:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
    <DoubleMuLoose:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
    <SingleEleLoose:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
    <DoubleEleLoose:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
    <SinglePhotonLoose:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <SinglePhotonLooseBintypes:EventSelectionAny>
        <SinglePhotonLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <MhtOverMetNoX:LambdaStr> ev : ev.MhtOverMetNoX[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
    <SignalFinal:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <SignalBintypes:EventSelectionAny>
        <SignalFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
    <SingleMuFinal:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mtw:LambdaStr> ev : 30 <= ev.mtw[0] < 125
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <DoubleMuFinal:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[1] < 0.12
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <SingleEleFinal:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mtw:LambdaStr> ev : 30 <= ev.mtw[0] < 125
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <DoubleEleFinal:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[1] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[1] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <SinglePhotonFinal:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <minDelRJetPhoton:LambdaStr> ev : ev.minDelRJetPhoton[0] >= 1.0
      <SinglePhotonFinalBintypes:EventSelectionAny>
        <SinglePhotonFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
        <SinglePhotonFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
        <SinglePhotonFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
'''


es_arg001='''<All:EventSelectionAll>
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
    <SignalLoose:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
      <SignalLooseBintypes:EventSelectionAny>
        <SignalLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
    <SingleMuLoose:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
    <DoubleMuLoose:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
    <SingleEleLoose:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
    <DoubleEleLoose:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
    <SinglePhotonLoose:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <SinglePhotonLooseBintypes:EventSelectionAny>
        <SinglePhotonLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <MhtOverMetNoXNoHF:LambdaStr> ev : ev.MhtOverMetNoXNoHF[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
    <SignalFinal:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <SignalBintypes:EventSelectionAny>
        <SignalFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
    <SingleMuFinal:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mtwNoHF:LambdaStr> ev : 30 <= ev.mtwNoHF[0] < 125
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <DoubleMuFinal:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[1] < 0.12
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <SingleEleFinal:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mtwNoHF:LambdaStr> ev : 30 <= ev.mtwNoHF[0] < 125
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <DoubleEleFinal:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[1] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[1] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <SinglePhotonFinal:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <minDelRJetPhoton:LambdaStr> ev : ev.minDelRJetPhoton[0] >= 1.0
      <SinglePhotonFinalBintypes:EventSelectionAny>
        <SinglePhotonFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
        <SinglePhotonFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
        <SinglePhotonFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
'''


es_arg002='''<All:EventSelectionAll>
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
    <SignalLoose:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
      <SignalLooseBintypes:EventSelectionAny>
        <SignalLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
    <SingleMuLoose:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
    <DoubleMuLoose:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
    <SingleEleLoose:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
    <DoubleEleLoose:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
    <SinglePhotonLoose:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <SinglePhotonLooseBintypes:EventSelectionAny>
        <SinglePhotonLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
  <MetFilters:EventSelectionAll>
    <goodVertex:LambdaStr> ev : ev.Flag_goodVertices[0] == 1
    <CSCTightHaloFilter:LambdaStr> ev : ev.Flag_CSCTightHaloFilter[0] ==1
    <hbheFilterNew:LambdaStr> ev : ev.hbheFilterNew[0] == 1
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <MhtOverMetNoX:LambdaStr> ev : ev.MhtOverMetNoX[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
    <SignalFinal:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <SignalBintypes:EventSelectionAny>
        <SignalFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
    <SingleMuFinal:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mtw:LambdaStr> ev : 30 <= ev.mtw[0] < 125
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <DoubleMuFinal:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[1] < 0.12
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <SingleEleFinal:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mtw:LambdaStr> ev : 30 <= ev.mtw[0] < 125
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <DoubleEleFinal:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[1] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[1] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <SinglePhotonFinal:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <minDelRJetPhoton:LambdaStr> ev : ev.minDelRJetPhoton[0] >= 1.0
      <SinglePhotonFinalBintypes:EventSelectionAny>
        <SinglePhotonFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
        <SinglePhotonFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
        <SinglePhotonFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
'''


es_arg003='''<All:EventSelectionAll>
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
    <SignalLoose:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
      <SignalLooseBintypes:EventSelectionAny>
        <SignalLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
    <SingleMuLoose:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
    <DoubleMuLoose:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
    <SingleEleLoose:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
    <DoubleEleLoose:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
    <SinglePhotonLoose:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <SinglePhotonLooseBintypes:EventSelectionAny>
        <SinglePhotonLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
  <MetFilters:EventSelectionAll>
    <goodVertex:LambdaStr> ev : ev.Flag_goodVertices[0] == 1
    <CSCTightHaloFilter:LambdaStr> ev : ev.Flag_CSCTightHaloFilter[0] ==1
    <hbheFilterNew:LambdaStr> ev : ev.hbheFilterNew[0] == 1
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <MhtOverMetNoXNoHF:LambdaStr> ev : ev.MhtOverMetNoXNoHF[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
    <SignalFinal:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <SignalBintypes:EventSelectionAny>
        <SignalFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
    <SingleMuFinal:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mtwNoHF:LambdaStr> ev : 30 <= ev.mtwNoHF[0] < 125
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <DoubleMuFinal:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[1] < 0.12
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <SingleEleFinal:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mtwNoHF:LambdaStr> ev : 30 <= ev.mtwNoHF[0] < 125
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <DoubleEleFinal:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[1] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[1] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <SinglePhotonFinal:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <minDelRJetPhoton:LambdaStr> ev : ev.minDelRJetPhoton[0] >= 1.0
      <SinglePhotonFinalBintypes:EventSelectionAny>
        <SinglePhotonFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
        <SinglePhotonFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
        <SinglePhotonFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
'''


es_arg004='''<All:EventSelectionAll>
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
    <SignalLoose:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <PDMetHtmhtJetht:LambdaStr> ev : ev.PrimaryDataset[0] in ('MET', 'HTMHT', 'JetHT')
      <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
      <SignalLooseBintypes:EventSelectionAny>
        <SignalLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
          <PD_MET:LambdaStr> ev : ev.PrimaryDataset[0] == 'MET'
        <SignalLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <PD_HTMHT:LambdaStr> ev : ev.PrimaryDataset[0] == 'HTMHT'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <PD_HTMHT:LambdaStr> ev : ev.PrimaryDataset[0] == 'HTMHT'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <PD_JetHT:LambdaStr> ev : ev.PrimaryDataset[0] == 'JetHT'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
    <SingleMuLoose:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
      <PDSingleMuon:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleMuon'
    <DoubleMuLoose:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
      <PDSingleMuon:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleMuon'
    <SingleEleLoose:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
      <PDSingleElectron:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleElectron'
    <DoubleEleLoose:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
      <PDSingleElectron:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleElectron'
    <SinglePhotonLoose:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <PDSinglePhoton:LambdaStr> ev : ev.PrimaryDataset[0] == 'SinglePhoton'
      <SinglePhotonLooseBintypes:EventSelectionAny>
        <SinglePhotonLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <MhtOverMetNoX:LambdaStr> ev : ev.MhtOverMetNoX[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
    <SignalFinal:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <SignalBintypes:EventSelectionAny>
        <SignalFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
    <SingleMuFinal:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mtw:LambdaStr> ev : 30 <= ev.mtw[0] < 125
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <DoubleMuFinal:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[1] < 0.12
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <SingleEleFinal:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mtw:LambdaStr> ev : 30 <= ev.mtw[0] < 125
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <DoubleEleFinal:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[1] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[1] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <SinglePhotonFinal:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <minDelRJetPhoton:LambdaStr> ev : ev.minDelRJetPhoton[0] >= 1.0
      <SinglePhotonFinalBintypes:EventSelectionAny>
        <SinglePhotonFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
        <SinglePhotonFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
        <SinglePhotonFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
'''


es_arg005='''<All:EventSelectionAll>
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
    <SignalLoose:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <PDMetHtmhtJetht:LambdaStr> ev : ev.PrimaryDataset[0] in ('MET', 'HTMHT', 'JetHT')
      <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
      <SignalLooseBintypes:EventSelectionAny>
        <SignalLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
          <PD_MET:LambdaStr> ev : ev.PrimaryDataset[0] == 'MET'
        <SignalLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <PD_HTMHT:LambdaStr> ev : ev.PrimaryDataset[0] == 'HTMHT'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <PD_HTMHT:LambdaStr> ev : ev.PrimaryDataset[0] == 'HTMHT'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <PD_JetHT:LambdaStr> ev : ev.PrimaryDataset[0] == 'JetHT'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
    <SingleMuLoose:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
      <PDSingleMuon:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleMuon'
    <DoubleMuLoose:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
      <PDSingleMuon:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleMuon'
    <SingleEleLoose:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
      <PDSingleElectron:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleElectron'
    <DoubleEleLoose:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
      <PDSingleElectron:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleElectron'
    <SinglePhotonLoose:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <PDSinglePhoton:LambdaStr> ev : ev.PrimaryDataset[0] == 'SinglePhoton'
      <SinglePhotonLooseBintypes:EventSelectionAny>
        <SinglePhotonLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <MhtOverMetNoXNoHF:LambdaStr> ev : ev.MhtOverMetNoXNoHF[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
    <SignalFinal:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <SignalBintypes:EventSelectionAny>
        <SignalFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
    <SingleMuFinal:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mtwNoHF:LambdaStr> ev : 30 <= ev.mtwNoHF[0] < 125
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <DoubleMuFinal:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[1] < 0.12
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <SingleEleFinal:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mtwNoHF:LambdaStr> ev : 30 <= ev.mtwNoHF[0] < 125
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <DoubleEleFinal:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[1] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[1] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <SinglePhotonFinal:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <minDelRJetPhoton:LambdaStr> ev : ev.minDelRJetPhoton[0] >= 1.0
      <SinglePhotonFinalBintypes:EventSelectionAny>
        <SinglePhotonFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
        <SinglePhotonFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
        <SinglePhotonFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
'''


es_arg006='''<All:EventSelectionAll>
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
    <SignalLoose:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <PDMetHtmhtJetht:LambdaStr> ev : ev.PrimaryDataset[0] in ('MET', 'HTMHT', 'JetHT')
      <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
      <SignalLooseBintypes:EventSelectionAny>
        <SignalLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
          <PD_MET:LambdaStr> ev : ev.PrimaryDataset[0] == 'MET'
        <SignalLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <PD_HTMHT:LambdaStr> ev : ev.PrimaryDataset[0] == 'HTMHT'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <PD_HTMHT:LambdaStr> ev : ev.PrimaryDataset[0] == 'HTMHT'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <PD_JetHT:LambdaStr> ev : ev.PrimaryDataset[0] == 'JetHT'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
    <SingleMuLoose:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
      <PDSingleMuon:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleMuon'
    <DoubleMuLoose:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
      <PDSingleMuon:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleMuon'
    <SingleEleLoose:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
      <PDSingleElectron:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleElectron'
    <DoubleEleLoose:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
      <PDSingleElectron:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleElectron'
    <SinglePhotonLoose:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <PDSinglePhoton:LambdaStr> ev : ev.PrimaryDataset[0] == 'SinglePhoton'
      <SinglePhotonLooseBintypes:EventSelectionAny>
        <SinglePhotonLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
  <MetFilters:EventSelectionAll>
    <goodVertex:LambdaStr> ev : ev.Flag_goodVertices[0] == 1
    <CSCTightHaloFilter:LambdaStr> ev : ev.Flag_CSCTightHaloFilter[0] ==1
    <hbheFilterNew:LambdaStr> ev : ev.hbheFilterNew[0] == 1
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <MhtOverMetNoX:LambdaStr> ev : ev.MhtOverMetNoX[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
    <SignalFinal:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <SignalBintypes:EventSelectionAny>
        <SignalFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
    <SingleMuFinal:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mtw:LambdaStr> ev : 30 <= ev.mtw[0] < 125
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <DoubleMuFinal:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[1] < 0.12
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <SingleEleFinal:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mtw:LambdaStr> ev : 30 <= ev.mtw[0] < 125
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <DoubleEleFinal:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[1] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[1] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <SinglePhotonFinal:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <minDelRJetPhoton:LambdaStr> ev : ev.minDelRJetPhoton[0] >= 1.0
      <SinglePhotonFinalBintypes:EventSelectionAny>
        <SinglePhotonFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
        <SinglePhotonFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
        <SinglePhotonFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
'''


es_arg007='''<All:EventSelectionAll>
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
    <SignalLoose:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <PDMetHtmhtJetht:LambdaStr> ev : ev.PrimaryDataset[0] in ('MET', 'HTMHT', 'JetHT')
      <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
      <SignalLooseBintypes:EventSelectionAny>
        <SignalLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
          <PD_MET:LambdaStr> ev : ev.PrimaryDataset[0] == 'MET'
        <SignalLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <PD_HTMHT:LambdaStr> ev : ev.PrimaryDataset[0] == 'HTMHT'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <PD_HTMHT:LambdaStr> ev : ev.PrimaryDataset[0] == 'HTMHT'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <PD_JetHT:LambdaStr> ev : ev.PrimaryDataset[0] == 'JetHT'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
    <SingleMuLoose:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
      <PDSingleMuon:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleMuon'
    <DoubleMuLoose:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
      <PDSingleMuon:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleMuon'
    <SingleEleLoose:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
      <PDSingleElectron:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleElectron'
    <DoubleEleLoose:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
      <PDSingleElectron:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleElectron'
    <SinglePhotonLoose:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <PDSinglePhoton:LambdaStr> ev : ev.PrimaryDataset[0] == 'SinglePhoton'
      <SinglePhotonLooseBintypes:EventSelectionAny>
        <SinglePhotonLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
  <MetFilters:EventSelectionAll>
    <goodVertex:LambdaStr> ev : ev.Flag_goodVertices[0] == 1
    <CSCTightHaloFilter:LambdaStr> ev : ev.Flag_CSCTightHaloFilter[0] ==1
    <hbheFilterNew:LambdaStr> ev : ev.hbheFilterNew[0] == 1
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <MhtOverMetNoXNoHF:LambdaStr> ev : ev.MhtOverMetNoXNoHF[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
    <SignalFinal:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <SignalBintypes:EventSelectionAny>
        <SignalFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
    <SingleMuFinal:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mtwNoHF:LambdaStr> ev : 30 <= ev.mtwNoHF[0] < 125
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <DoubleMuFinal:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[1] < 0.12
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <SingleEleFinal:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mtwNoHF:LambdaStr> ev : 30 <= ev.mtwNoHF[0] < 125
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <DoubleEleFinal:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[1] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[1] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <SinglePhotonFinal:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <minDelRJetPhoton:LambdaStr> ev : ev.minDelRJetPhoton[0] >= 1.0
      <SinglePhotonFinalBintypes:EventSelectionAny>
        <SinglePhotonFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
        <SinglePhotonFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
        <SinglePhotonFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
'''


es_arg008='''<All:EventSelectionAll>
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
    <SignalLoose:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
      <SignalLooseBintypes:EventSelectionAny>
        <SignalLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
    <SingleMuLoose:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
    <DoubleMuLoose:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
    <SingleEleLoose:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
    <DoubleEleLoose:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
    <SinglePhotonLoose:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <SinglePhotonLooseBintypes:EventSelectionAny>
        <SinglePhotonLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <MhtOverMetNoX:LambdaStr> ev : ev.MhtOverMetNoX[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
    <SignalFinal:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <SignalBintypes:EventSelectionAny>
        <SignalFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:HT_HLTAlphaT>
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:HT_HLTAlphaT>
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
    <SingleMuFinal:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <:HLT_SingleMuon>
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mtw:LambdaStr> ev : 30 <= ev.mtw[0] < 125
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <DoubleMuFinal:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[1] < 0.12
      <:HLT_SingleMuon>
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <SingleEleFinal:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mtw:LambdaStr> ev : 30 <= ev.mtw[0] < 125
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <DoubleEleFinal:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[1] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[1] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <SinglePhotonFinal:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <minDelRJetPhoton:LambdaStr> ev : ev.minDelRJetPhoton[0] >= 1.0
      <SinglePhotonFinalBintypes:EventSelectionAny>
        <SinglePhotonFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
        <SinglePhotonFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
        <SinglePhotonFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
'''


es_arg009='''<All:EventSelectionAll>
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
    <SignalLoose:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
      <SignalLooseBintypes:EventSelectionAny>
        <SignalLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
    <SingleMuLoose:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
    <DoubleMuLoose:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
    <SingleEleLoose:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
    <DoubleEleLoose:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
    <SinglePhotonLoose:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <SinglePhotonLooseBintypes:EventSelectionAny>
        <SinglePhotonLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <MhtOverMetNoXNoHF:LambdaStr> ev : ev.MhtOverMetNoXNoHF[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
    <SignalFinal:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <SignalBintypes:EventSelectionAny>
        <SignalFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:HT_HLTAlphaT>
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:HT_HLTAlphaT>
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
    <SingleMuFinal:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <:HLT_SingleMuon>
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mtwNoHF:LambdaStr> ev : 30 <= ev.mtwNoHF[0] < 125
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <DoubleMuFinal:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[1] < 0.12
      <:HLT_SingleMuon>
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <SingleEleFinal:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mtwNoHF:LambdaStr> ev : 30 <= ev.mtwNoHF[0] < 125
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <DoubleEleFinal:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[1] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[1] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <SinglePhotonFinal:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <minDelRJetPhoton:LambdaStr> ev : ev.minDelRJetPhoton[0] >= 1.0
      <SinglePhotonFinalBintypes:EventSelectionAny>
        <SinglePhotonFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
        <SinglePhotonFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
        <SinglePhotonFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
'''


es_arg010='''<All:EventSelectionAll>
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
    <SignalLoose:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
      <SignalLooseBintypes:EventSelectionAny>
        <SignalLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
    <SingleMuLoose:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
    <DoubleMuLoose:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
    <SingleEleLoose:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
    <DoubleEleLoose:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
    <SinglePhotonLoose:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <SinglePhotonLooseBintypes:EventSelectionAny>
        <SinglePhotonLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
  <MetFilters:EventSelectionAll>
    <goodVertex:LambdaStr> ev : ev.Flag_goodVertices[0] == 1
    <CSCTightHaloFilter:LambdaStr> ev : ev.Flag_CSCTightHaloFilter[0] ==1
    <hbheFilterNew:LambdaStr> ev : ev.hbheFilterNew[0] == 1
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <MhtOverMetNoX:LambdaStr> ev : ev.MhtOverMetNoX[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
    <SignalFinal:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <SignalBintypes:EventSelectionAny>
        <SignalFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:HT_HLTAlphaT>
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:HT_HLTAlphaT>
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
    <SingleMuFinal:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <:HLT_SingleMuon>
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mtw:LambdaStr> ev : 30 <= ev.mtw[0] < 125
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <DoubleMuFinal:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[1] < 0.12
      <:HLT_SingleMuon>
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <SingleEleFinal:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mtw:LambdaStr> ev : 30 <= ev.mtw[0] < 125
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <DoubleEleFinal:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[1] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[1] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <SinglePhotonFinal:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <minDelRJetPhoton:LambdaStr> ev : ev.minDelRJetPhoton[0] >= 1.0
      <SinglePhotonFinalBintypes:EventSelectionAny>
        <SinglePhotonFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
        <SinglePhotonFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
        <SinglePhotonFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
'''


es_arg011='''<All:EventSelectionAll>
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
    <SignalLoose:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
      <SignalLooseBintypes:EventSelectionAny>
        <SignalLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
    <SingleMuLoose:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
    <DoubleMuLoose:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
    <SingleEleLoose:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
    <DoubleEleLoose:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
    <SinglePhotonLoose:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <SinglePhotonLooseBintypes:EventSelectionAny>
        <SinglePhotonLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
  <MetFilters:EventSelectionAll>
    <goodVertex:LambdaStr> ev : ev.Flag_goodVertices[0] == 1
    <CSCTightHaloFilter:LambdaStr> ev : ev.Flag_CSCTightHaloFilter[0] ==1
    <hbheFilterNew:LambdaStr> ev : ev.hbheFilterNew[0] == 1
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <MhtOverMetNoXNoHF:LambdaStr> ev : ev.MhtOverMetNoXNoHF[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
    <SignalFinal:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <SignalBintypes:EventSelectionAny>
        <SignalFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:HT_HLTAlphaT>
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:HT_HLTAlphaT>
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
    <SingleMuFinal:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <:HLT_SingleMuon>
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mtwNoHF:LambdaStr> ev : 30 <= ev.mtwNoHF[0] < 125
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <DoubleMuFinal:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[1] < 0.12
      <:HLT_SingleMuon>
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <SingleEleFinal:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mtwNoHF:LambdaStr> ev : 30 <= ev.mtwNoHF[0] < 125
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <DoubleEleFinal:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[1] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[1] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <SinglePhotonFinal:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <minDelRJetPhoton:LambdaStr> ev : ev.minDelRJetPhoton[0] >= 1.0
      <SinglePhotonFinalBintypes:EventSelectionAny>
        <SinglePhotonFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
        <SinglePhotonFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
        <SinglePhotonFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
'''


es_arg012='''<All:EventSelectionAll>
  <:PD_HLT>
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
    <SignalLoose:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <PDMetHtmhtJetht:LambdaStr> ev : ev.PrimaryDataset[0] in ('MET', 'HTMHT', 'JetHT')
      <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
      <SignalLooseBintypes:EventSelectionAny>
        <SignalLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
          <PD_MET:LambdaStr> ev : ev.PrimaryDataset[0] == 'MET'
        <SignalLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <PD_HTMHT:LambdaStr> ev : ev.PrimaryDataset[0] == 'HTMHT'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <PD_HTMHT:LambdaStr> ev : ev.PrimaryDataset[0] == 'HTMHT'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <PD_JetHT:LambdaStr> ev : ev.PrimaryDataset[0] == 'JetHT'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
    <SingleMuLoose:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
      <PDSingleMuon:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleMuon'
    <DoubleMuLoose:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
      <PDSingleMuon:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleMuon'
    <SingleEleLoose:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
      <PDSingleElectron:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleElectron'
    <DoubleEleLoose:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
      <PDSingleElectron:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleElectron'
    <SinglePhotonLoose:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <PDSinglePhoton:LambdaStr> ev : ev.PrimaryDataset[0] == 'SinglePhoton'
      <SinglePhotonLooseBintypes:EventSelectionAny>
        <SinglePhotonLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <MhtOverMetNoX:LambdaStr> ev : ev.MhtOverMetNoX[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
    <SignalFinal:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <SignalBintypes:EventSelectionAny>
        <SignalFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:HT_HLTAlphaT>
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:HT_HLTAlphaT>
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
    <SingleMuFinal:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <:HLT_SingleMuon>
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mtw:LambdaStr> ev : 30 <= ev.mtw[0] < 125
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <DoubleMuFinal:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[1] < 0.12
      <:HLT_SingleMuon>
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <SingleEleFinal:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mtw:LambdaStr> ev : 30 <= ev.mtw[0] < 125
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <DoubleEleFinal:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[1] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[1] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <SinglePhotonFinal:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <minDelRJetPhoton:LambdaStr> ev : ev.minDelRJetPhoton[0] >= 1.0
      <SinglePhotonFinalBintypes:EventSelectionAny>
        <SinglePhotonFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
        <SinglePhotonFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
        <SinglePhotonFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
'''


es_arg013='''<All:EventSelectionAll>
  <:PD_HLT>
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
    <SignalLoose:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <PDMetHtmhtJetht:LambdaStr> ev : ev.PrimaryDataset[0] in ('MET', 'HTMHT', 'JetHT')
      <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
      <SignalLooseBintypes:EventSelectionAny>
        <SignalLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
          <PD_MET:LambdaStr> ev : ev.PrimaryDataset[0] == 'MET'
        <SignalLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <PD_HTMHT:LambdaStr> ev : ev.PrimaryDataset[0] == 'HTMHT'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <PD_HTMHT:LambdaStr> ev : ev.PrimaryDataset[0] == 'HTMHT'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <PD_JetHT:LambdaStr> ev : ev.PrimaryDataset[0] == 'JetHT'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
    <SingleMuLoose:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
      <PDSingleMuon:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleMuon'
    <DoubleMuLoose:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
      <PDSingleMuon:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleMuon'
    <SingleEleLoose:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
      <PDSingleElectron:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleElectron'
    <DoubleEleLoose:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
      <PDSingleElectron:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleElectron'
    <SinglePhotonLoose:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <PDSinglePhoton:LambdaStr> ev : ev.PrimaryDataset[0] == 'SinglePhoton'
      <SinglePhotonLooseBintypes:EventSelectionAny>
        <SinglePhotonLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <MhtOverMetNoXNoHF:LambdaStr> ev : ev.MhtOverMetNoXNoHF[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
    <SignalFinal:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <SignalBintypes:EventSelectionAny>
        <SignalFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:HT_HLTAlphaT>
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:HT_HLTAlphaT>
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
    <SingleMuFinal:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <:HLT_SingleMuon>
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mtwNoHF:LambdaStr> ev : 30 <= ev.mtwNoHF[0] < 125
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <DoubleMuFinal:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[1] < 0.12
      <:HLT_SingleMuon>
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <SingleEleFinal:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mtwNoHF:LambdaStr> ev : 30 <= ev.mtwNoHF[0] < 125
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <DoubleEleFinal:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[1] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[1] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <SinglePhotonFinal:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <minDelRJetPhoton:LambdaStr> ev : ev.minDelRJetPhoton[0] >= 1.0
      <SinglePhotonFinalBintypes:EventSelectionAny>
        <SinglePhotonFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
        <SinglePhotonFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
        <SinglePhotonFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
'''


es_arg014='''<All:EventSelectionAll>
  <:PD_HLT>
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
    <SignalLoose:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <PDMetHtmhtJetht:LambdaStr> ev : ev.PrimaryDataset[0] in ('MET', 'HTMHT', 'JetHT')
      <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
      <SignalLooseBintypes:EventSelectionAny>
        <SignalLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
          <PD_MET:LambdaStr> ev : ev.PrimaryDataset[0] == 'MET'
        <SignalLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <PD_HTMHT:LambdaStr> ev : ev.PrimaryDataset[0] == 'HTMHT'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <PD_HTMHT:LambdaStr> ev : ev.PrimaryDataset[0] == 'HTMHT'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <PD_JetHT:LambdaStr> ev : ev.PrimaryDataset[0] == 'JetHT'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
    <SingleMuLoose:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
      <PDSingleMuon:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleMuon'
    <DoubleMuLoose:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
      <PDSingleMuon:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleMuon'
    <SingleEleLoose:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
      <PDSingleElectron:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleElectron'
    <DoubleEleLoose:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
      <PDSingleElectron:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleElectron'
    <SinglePhotonLoose:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <PDSinglePhoton:LambdaStr> ev : ev.PrimaryDataset[0] == 'SinglePhoton'
      <SinglePhotonLooseBintypes:EventSelectionAny>
        <SinglePhotonLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
  <MetFilters:EventSelectionAll>
    <goodVertex:LambdaStr> ev : ev.Flag_goodVertices[0] == 1
    <CSCTightHaloFilter:LambdaStr> ev : ev.Flag_CSCTightHaloFilter[0] ==1
    <hbheFilterNew:LambdaStr> ev : ev.hbheFilterNew[0] == 1
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <MhtOverMetNoX:LambdaStr> ev : ev.MhtOverMetNoX[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
    <SignalFinal:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <SignalBintypes:EventSelectionAny>
        <SignalFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:HT_HLTAlphaT>
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:HT_HLTAlphaT>
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
    <SingleMuFinal:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <:HLT_SingleMuon>
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mtw:LambdaStr> ev : 30 <= ev.mtw[0] < 125
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <DoubleMuFinal:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[1] < 0.12
      <:HLT_SingleMuon>
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <SingleEleFinal:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mtw:LambdaStr> ev : 30 <= ev.mtw[0] < 125
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <DoubleEleFinal:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[1] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[1] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <SinglePhotonFinal:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <minDelRJetPhoton:LambdaStr> ev : ev.minDelRJetPhoton[0] >= 1.0
      <SinglePhotonFinalBintypes:EventSelectionAny>
        <SinglePhotonFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
        <SinglePhotonFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
        <SinglePhotonFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
'''


es_arg015='''<All:EventSelectionAll>
  <:PD_HLT>
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
    <SignalLoose:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <PDMetHtmhtJetht:LambdaStr> ev : ev.PrimaryDataset[0] in ('MET', 'HTMHT', 'JetHT')
      <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
      <SignalLooseBintypes:EventSelectionAny>
        <SignalLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
          <PD_MET:LambdaStr> ev : ev.PrimaryDataset[0] == 'MET'
        <SignalLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <PD_HTMHT:LambdaStr> ev : ev.PrimaryDataset[0] == 'HTMHT'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <PD_HTMHT:LambdaStr> ev : ev.PrimaryDataset[0] == 'HTMHT'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <PD_JetHT:LambdaStr> ev : ev.PrimaryDataset[0] == 'JetHT'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
    <SingleMuLoose:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
      <PDSingleMuon:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleMuon'
    <DoubleMuLoose:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
      <PDSingleMuon:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleMuon'
    <SingleEleLoose:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
      <PDSingleElectron:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleElectron'
    <DoubleEleLoose:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
      <PDSingleElectron:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleElectron'
    <SinglePhotonLoose:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <PDSinglePhoton:LambdaStr> ev : ev.PrimaryDataset[0] == 'SinglePhoton'
      <SinglePhotonLooseBintypes:EventSelectionAny>
        <SinglePhotonLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
  <MetFilters:EventSelectionAll>
    <goodVertex:LambdaStr> ev : ev.Flag_goodVertices[0] == 1
    <CSCTightHaloFilter:LambdaStr> ev : ev.Flag_CSCTightHaloFilter[0] ==1
    <hbheFilterNew:LambdaStr> ev : ev.hbheFilterNew[0] == 1
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <MhtOverMetNoXNoHF:LambdaStr> ev : ev.MhtOverMetNoXNoHF[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
    <SignalFinal:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <SignalBintypes:EventSelectionAny>
        <SignalFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:HT_HLTAlphaT>
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:HT_HLTAlphaT>
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
    <SingleMuFinal:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <:HLT_SingleMuon>
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mtwNoHF:LambdaStr> ev : 30 <= ev.mtwNoHF[0] < 125
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <DoubleMuFinal:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[1] < 0.12
      <:HLT_SingleMuon>
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <SingleEleFinal:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mtwNoHF:LambdaStr> ev : 30 <= ev.mtwNoHF[0] < 125
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <DoubleEleFinal:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[1] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[1] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <SinglePhotonFinal:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <minDelRJetPhoton:LambdaStr> ev : ev.minDelRJetPhoton[0] >= 1.0
      <SinglePhotonFinalBintypes:EventSelectionAny>
        <SinglePhotonFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
        <SinglePhotonFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
        <SinglePhotonFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
'''


es_arg100='''<All:EventSelectionAll>
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
    <SignalLoose:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
      <SignalLooseBintypes:EventSelectionAny>
        <SignalLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
    <SingleMuLoose:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
    <DoubleMuLoose:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
    <SingleEleLoose:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
    <DoubleEleLoose:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
    <SinglePhotonLoose:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <SinglePhotonLooseBintypes:EventSelectionAny>
        <SinglePhotonLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <MhtOverMetNoX:LambdaStr> ev : ev.MhtOverMetNoX[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
    <SignalFinal:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <SignalBintypes:EventSelectionAny>
        <SignalFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
    <SingleMuFinal:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mtw:LambdaStr> ev : 30 <= ev.mtw[0] < 125
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <DoubleMuFinal:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[1] < 0.12
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <SingleEleFinal:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mtw:LambdaStr> ev : 30 <= ev.mtw[0] < 125
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <DoubleEleFinal:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[1] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[1] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <SinglePhotonFinal:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <minDelRJetPhoton:LambdaStr> ev : ev.minDelRJetPhoton[0] >= 1.0
      <SinglePhotonFinalBintypes:EventSelectionAny>
        <SinglePhotonFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
        <SinglePhotonFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
        <SinglePhotonFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
'''


es_arg101='''<All:EventSelectionAll>
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
    <SignalLoose:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
      <SignalLooseBintypes:EventSelectionAny>
        <SignalLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
    <SingleMuLoose:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
    <DoubleMuLoose:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
    <SingleEleLoose:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
    <DoubleEleLoose:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
    <SinglePhotonLoose:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <SinglePhotonLooseBintypes:EventSelectionAny>
        <SinglePhotonLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <MhtOverMetNoXNoHF:LambdaStr> ev : ev.MhtOverMetNoXNoHF[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
    <SignalFinal:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <SignalBintypes:EventSelectionAny>
        <SignalFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
    <SingleMuFinal:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mtwNoHF:LambdaStr> ev : 30 <= ev.mtwNoHF[0] < 125
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <DoubleMuFinal:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[1] < 0.12
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <SingleEleFinal:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mtwNoHF:LambdaStr> ev : 30 <= ev.mtwNoHF[0] < 125
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <DoubleEleFinal:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[1] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[1] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <SinglePhotonFinal:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <minDelRJetPhoton:LambdaStr> ev : ev.minDelRJetPhoton[0] >= 1.0
      <SinglePhotonFinalBintypes:EventSelectionAny>
        <SinglePhotonFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
        <SinglePhotonFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
        <SinglePhotonFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
'''


es_arg102='''<All:EventSelectionAll>
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
    <SignalLoose:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
      <SignalLooseBintypes:EventSelectionAny>
        <SignalLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
    <SingleMuLoose:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
    <DoubleMuLoose:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
    <SingleEleLoose:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
    <DoubleEleLoose:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
    <SinglePhotonLoose:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <SinglePhotonLooseBintypes:EventSelectionAny>
        <SinglePhotonLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
  <MetFilters:EventSelectionAll>
    <goodVertex:LambdaStr> ev : ev.Flag_goodVertices[0] == 1
    <CSCTightHaloFilter:LambdaStr> ev : ev.Flag_CSCTightHaloFilter[0] ==1
    <HBHENoiseFilter:LambdaStr> ev : ev.Flag_HBHENoiseFilter[0] == 1
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <MhtOverMetNoX:LambdaStr> ev : ev.MhtOverMetNoX[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
    <SignalFinal:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <SignalBintypes:EventSelectionAny>
        <SignalFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
    <SingleMuFinal:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mtw:LambdaStr> ev : 30 <= ev.mtw[0] < 125
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <DoubleMuFinal:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[1] < 0.12
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <SingleEleFinal:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mtw:LambdaStr> ev : 30 <= ev.mtw[0] < 125
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <DoubleEleFinal:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[1] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[1] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <SinglePhotonFinal:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <minDelRJetPhoton:LambdaStr> ev : ev.minDelRJetPhoton[0] >= 1.0
      <SinglePhotonFinalBintypes:EventSelectionAny>
        <SinglePhotonFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
        <SinglePhotonFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
        <SinglePhotonFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
'''


es_arg103='''<All:EventSelectionAll>
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
    <SignalLoose:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
      <SignalLooseBintypes:EventSelectionAny>
        <SignalLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
    <SingleMuLoose:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
    <DoubleMuLoose:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
    <SingleEleLoose:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
    <DoubleEleLoose:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
    <SinglePhotonLoose:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <SinglePhotonLooseBintypes:EventSelectionAny>
        <SinglePhotonLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
  <MetFilters:EventSelectionAll>
    <goodVertex:LambdaStr> ev : ev.Flag_goodVertices[0] == 1
    <CSCTightHaloFilter:LambdaStr> ev : ev.Flag_CSCTightHaloFilter[0] ==1
    <HBHENoiseFilter:LambdaStr> ev : ev.Flag_HBHENoiseFilter[0] == 1
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <MhtOverMetNoXNoHF:LambdaStr> ev : ev.MhtOverMetNoXNoHF[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
    <SignalFinal:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <SignalBintypes:EventSelectionAny>
        <SignalFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
    <SingleMuFinal:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mtwNoHF:LambdaStr> ev : 30 <= ev.mtwNoHF[0] < 125
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <DoubleMuFinal:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[1] < 0.12
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <SingleEleFinal:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mtwNoHF:LambdaStr> ev : 30 <= ev.mtwNoHF[0] < 125
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <DoubleEleFinal:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[1] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[1] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <SinglePhotonFinal:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <minDelRJetPhoton:LambdaStr> ev : ev.minDelRJetPhoton[0] >= 1.0
      <SinglePhotonFinalBintypes:EventSelectionAny>
        <SinglePhotonFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
        <SinglePhotonFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
        <SinglePhotonFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
'''


es_arg104='''<All:EventSelectionAll>
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
    <SignalLoose:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
      <SignalLooseBintypes:EventSelectionAny>
        <SignalLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
    <SingleMuLoose:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
    <DoubleMuLoose:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
    <SingleEleLoose:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
    <DoubleEleLoose:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
    <SinglePhotonLoose:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <SinglePhotonLooseBintypes:EventSelectionAny>
        <SinglePhotonLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <MhtOverMetNoX:LambdaStr> ev : ev.MhtOverMetNoX[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
    <SignalFinal:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <SignalBintypes:EventSelectionAny>
        <SignalFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
    <SingleMuFinal:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mtw:LambdaStr> ev : 30 <= ev.mtw[0] < 125
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <DoubleMuFinal:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[1] < 0.12
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <SingleEleFinal:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mtw:LambdaStr> ev : 30 <= ev.mtw[0] < 125
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <DoubleEleFinal:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[1] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[1] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <SinglePhotonFinal:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <minDelRJetPhoton:LambdaStr> ev : ev.minDelRJetPhoton[0] >= 1.0
      <SinglePhotonFinalBintypes:EventSelectionAny>
        <SinglePhotonFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
        <SinglePhotonFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
        <SinglePhotonFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
'''


es_arg105='''<All:EventSelectionAll>
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
    <SignalLoose:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
      <SignalLooseBintypes:EventSelectionAny>
        <SignalLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
    <SingleMuLoose:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
    <DoubleMuLoose:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
    <SingleEleLoose:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
    <DoubleEleLoose:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
    <SinglePhotonLoose:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <SinglePhotonLooseBintypes:EventSelectionAny>
        <SinglePhotonLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <MhtOverMetNoXNoHF:LambdaStr> ev : ev.MhtOverMetNoXNoHF[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
    <SignalFinal:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <SignalBintypes:EventSelectionAny>
        <SignalFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
    <SingleMuFinal:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mtwNoHF:LambdaStr> ev : 30 <= ev.mtwNoHF[0] < 125
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <DoubleMuFinal:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[1] < 0.12
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <SingleEleFinal:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mtwNoHF:LambdaStr> ev : 30 <= ev.mtwNoHF[0] < 125
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <DoubleEleFinal:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[1] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[1] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <SinglePhotonFinal:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <minDelRJetPhoton:LambdaStr> ev : ev.minDelRJetPhoton[0] >= 1.0
      <SinglePhotonFinalBintypes:EventSelectionAny>
        <SinglePhotonFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
        <SinglePhotonFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
        <SinglePhotonFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
'''


es_arg106='''<All:EventSelectionAll>
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
    <SignalLoose:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
      <SignalLooseBintypes:EventSelectionAny>
        <SignalLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
    <SingleMuLoose:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
    <DoubleMuLoose:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
    <SingleEleLoose:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
    <DoubleEleLoose:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
    <SinglePhotonLoose:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <SinglePhotonLooseBintypes:EventSelectionAny>
        <SinglePhotonLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
  <MetFilters:EventSelectionAll>
    <goodVertex:LambdaStr> ev : ev.Flag_goodVertices[0] == 1
    <CSCTightHaloFilter:LambdaStr> ev : ev.Flag_CSCTightHaloFilter[0] ==1
    <HBHENoiseFilter:LambdaStr> ev : ev.Flag_HBHENoiseFilter[0] == 1
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <MhtOverMetNoX:LambdaStr> ev : ev.MhtOverMetNoX[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
    <SignalFinal:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <SignalBintypes:EventSelectionAny>
        <SignalFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
    <SingleMuFinal:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mtw:LambdaStr> ev : 30 <= ev.mtw[0] < 125
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <DoubleMuFinal:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[1] < 0.12
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <SingleEleFinal:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mtw:LambdaStr> ev : 30 <= ev.mtw[0] < 125
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <DoubleEleFinal:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[1] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[1] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <SinglePhotonFinal:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <minDelRJetPhoton:LambdaStr> ev : ev.minDelRJetPhoton[0] >= 1.0
      <SinglePhotonFinalBintypes:EventSelectionAny>
        <SinglePhotonFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
        <SinglePhotonFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
        <SinglePhotonFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
'''


es_arg107='''<All:EventSelectionAll>
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
    <SignalLoose:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
      <SignalLooseBintypes:EventSelectionAny>
        <SignalLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
    <SingleMuLoose:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
    <DoubleMuLoose:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
    <SingleEleLoose:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
    <DoubleEleLoose:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
    <SinglePhotonLoose:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <SinglePhotonLooseBintypes:EventSelectionAny>
        <SinglePhotonLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
  <MetFilters:EventSelectionAll>
    <goodVertex:LambdaStr> ev : ev.Flag_goodVertices[0] == 1
    <CSCTightHaloFilter:LambdaStr> ev : ev.Flag_CSCTightHaloFilter[0] ==1
    <HBHENoiseFilter:LambdaStr> ev : ev.Flag_HBHENoiseFilter[0] == 1
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <MhtOverMetNoXNoHF:LambdaStr> ev : ev.MhtOverMetNoXNoHF[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
    <SignalFinal:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <SignalBintypes:EventSelectionAny>
        <SignalFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
    <SingleMuFinal:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mtwNoHF:LambdaStr> ev : 30 <= ev.mtwNoHF[0] < 125
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <DoubleMuFinal:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[1] < 0.12
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <SingleEleFinal:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mtwNoHF:LambdaStr> ev : 30 <= ev.mtwNoHF[0] < 125
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <DoubleEleFinal:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[1] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[1] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <SinglePhotonFinal:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <minDelRJetPhoton:LambdaStr> ev : ev.minDelRJetPhoton[0] >= 1.0
      <SinglePhotonFinalBintypes:EventSelectionAny>
        <SinglePhotonFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
        <SinglePhotonFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
        <SinglePhotonFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
'''


es_arg108='''<All:EventSelectionAll>
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
    <SignalLoose:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
      <SignalLooseBintypes:EventSelectionAny>
        <SignalLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
    <SingleMuLoose:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
    <DoubleMuLoose:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
    <SingleEleLoose:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
    <DoubleEleLoose:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
    <SinglePhotonLoose:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <SinglePhotonLooseBintypes:EventSelectionAny>
        <SinglePhotonLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <MhtOverMetNoX:LambdaStr> ev : ev.MhtOverMetNoX[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
    <SignalFinal:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <SignalBintypes:EventSelectionAny>
        <SignalFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
    <SingleMuFinal:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <:HLT_SingleMuon>
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mtw:LambdaStr> ev : 30 <= ev.mtw[0] < 125
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <DoubleMuFinal:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[1] < 0.12
      <:HLT_SingleMuon>
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <SingleEleFinal:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mtw:LambdaStr> ev : 30 <= ev.mtw[0] < 125
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <DoubleEleFinal:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[1] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[1] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <SinglePhotonFinal:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <minDelRJetPhoton:LambdaStr> ev : ev.minDelRJetPhoton[0] >= 1.0
      <SinglePhotonFinalBintypes:EventSelectionAny>
        <SinglePhotonFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
        <SinglePhotonFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
        <SinglePhotonFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
'''


es_arg109='''<All:EventSelectionAll>
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
    <SignalLoose:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
      <SignalLooseBintypes:EventSelectionAny>
        <SignalLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
    <SingleMuLoose:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
    <DoubleMuLoose:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
    <SingleEleLoose:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
    <DoubleEleLoose:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
    <SinglePhotonLoose:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <SinglePhotonLooseBintypes:EventSelectionAny>
        <SinglePhotonLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <MhtOverMetNoXNoHF:LambdaStr> ev : ev.MhtOverMetNoXNoHF[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
    <SignalFinal:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <SignalBintypes:EventSelectionAny>
        <SignalFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
    <SingleMuFinal:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <:HLT_SingleMuon>
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mtwNoHF:LambdaStr> ev : 30 <= ev.mtwNoHF[0] < 125
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <DoubleMuFinal:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[1] < 0.12
      <:HLT_SingleMuon>
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <SingleEleFinal:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mtwNoHF:LambdaStr> ev : 30 <= ev.mtwNoHF[0] < 125
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <DoubleEleFinal:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[1] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[1] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <SinglePhotonFinal:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <minDelRJetPhoton:LambdaStr> ev : ev.minDelRJetPhoton[0] >= 1.0
      <SinglePhotonFinalBintypes:EventSelectionAny>
        <SinglePhotonFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
        <SinglePhotonFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
        <SinglePhotonFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
'''


es_arg110='''<All:EventSelectionAll>
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
    <SignalLoose:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
      <SignalLooseBintypes:EventSelectionAny>
        <SignalLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
    <SingleMuLoose:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
    <DoubleMuLoose:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
    <SingleEleLoose:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
    <DoubleEleLoose:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
    <SinglePhotonLoose:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <SinglePhotonLooseBintypes:EventSelectionAny>
        <SinglePhotonLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
  <MetFilters:EventSelectionAll>
    <goodVertex:LambdaStr> ev : ev.Flag_goodVertices[0] == 1
    <CSCTightHaloFilter:LambdaStr> ev : ev.Flag_CSCTightHaloFilter[0] ==1
    <HBHENoiseFilter:LambdaStr> ev : ev.Flag_HBHENoiseFilter[0] == 1
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <MhtOverMetNoX:LambdaStr> ev : ev.MhtOverMetNoX[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
    <SignalFinal:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <SignalBintypes:EventSelectionAny>
        <SignalFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
    <SingleMuFinal:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <:HLT_SingleMuon>
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mtw:LambdaStr> ev : 30 <= ev.mtw[0] < 125
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <DoubleMuFinal:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[1] < 0.12
      <:HLT_SingleMuon>
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <SingleEleFinal:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mtw:LambdaStr> ev : 30 <= ev.mtw[0] < 125
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <DoubleEleFinal:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[1] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[1] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <SinglePhotonFinal:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <minDelRJetPhoton:LambdaStr> ev : ev.minDelRJetPhoton[0] >= 1.0
      <SinglePhotonFinalBintypes:EventSelectionAny>
        <SinglePhotonFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
        <SinglePhotonFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
        <SinglePhotonFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
'''


es_arg111='''<All:EventSelectionAll>
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
    <SignalLoose:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
      <SignalLooseBintypes:EventSelectionAny>
        <SignalLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
    <SingleMuLoose:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
    <DoubleMuLoose:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
    <SingleEleLoose:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
    <DoubleEleLoose:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
    <SinglePhotonLoose:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <SinglePhotonLooseBintypes:EventSelectionAny>
        <SinglePhotonLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
  <MetFilters:EventSelectionAll>
    <goodVertex:LambdaStr> ev : ev.Flag_goodVertices[0] == 1
    <CSCTightHaloFilter:LambdaStr> ev : ev.Flag_CSCTightHaloFilter[0] ==1
    <HBHENoiseFilter:LambdaStr> ev : ev.Flag_HBHENoiseFilter[0] == 1
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <MhtOverMetNoXNoHF:LambdaStr> ev : ev.MhtOverMetNoXNoHF[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
    <SignalFinal:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <SignalBintypes:EventSelectionAny>
        <SignalFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
    <SingleMuFinal:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <:HLT_SingleMuon>
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mtwNoHF:LambdaStr> ev : 30 <= ev.mtwNoHF[0] < 125
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <DoubleMuFinal:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[1] < 0.12
      <:HLT_SingleMuon>
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <SingleEleFinal:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mtwNoHF:LambdaStr> ev : 30 <= ev.mtwNoHF[0] < 125
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <DoubleEleFinal:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[1] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[1] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <SinglePhotonFinal:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <minDelRJetPhoton:LambdaStr> ev : ev.minDelRJetPhoton[0] >= 1.0
      <SinglePhotonFinalBintypes:EventSelectionAny>
        <SinglePhotonFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
        <SinglePhotonFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
        <SinglePhotonFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
'''


es_arg112='''<All:EventSelectionAll>
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
    <SignalLoose:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
      <SignalLooseBintypes:EventSelectionAny>
        <SignalLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
    <SingleMuLoose:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
    <DoubleMuLoose:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
    <SingleEleLoose:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
    <DoubleEleLoose:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
    <SinglePhotonLoose:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <SinglePhotonLooseBintypes:EventSelectionAny>
        <SinglePhotonLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <MhtOverMetNoX:LambdaStr> ev : ev.MhtOverMetNoX[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
    <SignalFinal:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <SignalBintypes:EventSelectionAny>
        <SignalFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
    <SingleMuFinal:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <:HLT_SingleMuon>
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mtw:LambdaStr> ev : 30 <= ev.mtw[0] < 125
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <DoubleMuFinal:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[1] < 0.12
      <:HLT_SingleMuon>
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <SingleEleFinal:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mtw:LambdaStr> ev : 30 <= ev.mtw[0] < 125
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <DoubleEleFinal:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[1] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[1] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <SinglePhotonFinal:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <minDelRJetPhoton:LambdaStr> ev : ev.minDelRJetPhoton[0] >= 1.0
      <SinglePhotonFinalBintypes:EventSelectionAny>
        <SinglePhotonFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
        <SinglePhotonFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
        <SinglePhotonFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
'''


es_arg113='''<All:EventSelectionAll>
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
    <SignalLoose:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
      <SignalLooseBintypes:EventSelectionAny>
        <SignalLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
    <SingleMuLoose:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
    <DoubleMuLoose:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
    <SingleEleLoose:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
    <DoubleEleLoose:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
    <SinglePhotonLoose:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <SinglePhotonLooseBintypes:EventSelectionAny>
        <SinglePhotonLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <MhtOverMetNoXNoHF:LambdaStr> ev : ev.MhtOverMetNoXNoHF[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
    <SignalFinal:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <SignalBintypes:EventSelectionAny>
        <SignalFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
    <SingleMuFinal:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <:HLT_SingleMuon>
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mtwNoHF:LambdaStr> ev : 30 <= ev.mtwNoHF[0] < 125
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <DoubleMuFinal:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[1] < 0.12
      <:HLT_SingleMuon>
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <SingleEleFinal:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mtwNoHF:LambdaStr> ev : 30 <= ev.mtwNoHF[0] < 125
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <DoubleEleFinal:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[1] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[1] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <SinglePhotonFinal:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <minDelRJetPhoton:LambdaStr> ev : ev.minDelRJetPhoton[0] >= 1.0
      <SinglePhotonFinalBintypes:EventSelectionAny>
        <SinglePhotonFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
        <SinglePhotonFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
        <SinglePhotonFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
'''


es_arg114='''<All:EventSelectionAll>
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
    <SignalLoose:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
      <SignalLooseBintypes:EventSelectionAny>
        <SignalLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
    <SingleMuLoose:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
    <DoubleMuLoose:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
    <SingleEleLoose:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
    <DoubleEleLoose:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
    <SinglePhotonLoose:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <SinglePhotonLooseBintypes:EventSelectionAny>
        <SinglePhotonLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
  <MetFilters:EventSelectionAll>
    <goodVertex:LambdaStr> ev : ev.Flag_goodVertices[0] == 1
    <CSCTightHaloFilter:LambdaStr> ev : ev.Flag_CSCTightHaloFilter[0] ==1
    <HBHENoiseFilter:LambdaStr> ev : ev.Flag_HBHENoiseFilter[0] == 1
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <MhtOverMetNoX:LambdaStr> ev : ev.MhtOverMetNoX[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
    <SignalFinal:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <SignalBintypes:EventSelectionAny>
        <SignalFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
    <SingleMuFinal:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <:HLT_SingleMuon>
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mtw:LambdaStr> ev : 30 <= ev.mtw[0] < 125
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <DoubleMuFinal:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[1] < 0.12
      <:HLT_SingleMuon>
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <SingleEleFinal:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mtw:LambdaStr> ev : 30 <= ev.mtw[0] < 125
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <DoubleEleFinal:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[1] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[1] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <SinglePhotonFinal:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <minDelRJetPhoton:LambdaStr> ev : ev.minDelRJetPhoton[0] >= 1.0
      <SinglePhotonFinalBintypes:EventSelectionAny>
        <SinglePhotonFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
        <SinglePhotonFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
        <SinglePhotonFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
'''


es_arg115='''<All:EventSelectionAll>
  <Baseline:EventSelectionAll>
    <nVertGTOne:LambdaStr> ev : ev.nVert[0] >= 1
    <nJetGTOne:LambdaStr> ev : ev.nJet100[0] >= 1
    <HTGT150:LambdaStr> ev : ev.ht40[0] >= 150
  <cutflowsLoose:EventSelectionAny>
    <SignalLoose:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
      <SignalLooseBintypes:EventSelectionAny>
        <SignalLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SignalLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
    <SingleMuLoose:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
    <DoubleMuLoose:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
    <SingleEleLoose:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
    <DoubleEleLoose:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
    <SinglePhotonLoose:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <SinglePhotonLooseBintypes:EventSelectionAny>
        <SinglePhotonLooseMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonLooseAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <alphaTLT0p5:LambdaStr> ev : 0.5 <= ev.alphaT[0]
        <SinglePhotonLooseHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <MHTGT130:LambdaStr> ev : 130 <= ev.mht40_pt[0]
  <MetFilters:EventSelectionAll>
    <goodVertex:LambdaStr> ev : ev.Flag_goodVertices[0] == 1
    <CSCTightHaloFilter:LambdaStr> ev : ev.Flag_CSCTightHaloFilter[0] ==1
    <HBHENoiseFilter:LambdaStr> ev : ev.Flag_HBHENoiseFilter[0] == 1
  <CommonFinal:EventSelectionAll>
    <FwJetVeto:LambdaStr> ev : ev.nJet40Fwd[0] == 0
    <JetIDVeto:LambdaStr> ev : ev.nJet40failedId[0] == 0
    <HTGT200:LambdaStr> ev : ev.ht40[0] >= 200
    <MhtOverMetNoXNoHF:LambdaStr> ev : ev.MhtOverMetNoXNoHF[0] < 1.25
  <cutflowsFinal:EventSelectionAny>
    <SignalFinal:EventSelectionAll>
      <cutflowSignal:LambdaStr> ev : ev.cutflow[0] == 'Signal'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <SignalBintypes:EventSelectionAny>
        <SignalFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SignalFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
        <SignalFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
          <biasedDPhiGT0p5:LambdaStr> ev : 0.5 <= ev.biasedDPhi[0]
    <SingleMuFinal:EventSelectionAll>
      <cutflowSingleMu:LambdaStr> ev : ev.cutflow[0] == 'SingleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <:HLT_SingleMuon>
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mtwNoHF:LambdaStr> ev : 30 <= ev.mtwNoHF[0] < 125
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <DoubleMuFinal:EventSelectionAll>
      <cutflowDoubleMu:LambdaStr> ev : ev.cutflow[0] == 'DoubleMu'
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[0] < 0.12
      <relIso03LT0p12:LambdaStr> ev : ev.muon_relIso03[1] < 0.12
      <:HLT_SingleMuon>
      <isoTrackNoMuVeto:LambdaStr> ev : ev.nIsoTracksNoMuVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetMu:LambdaStr> ev : ev.minDelRJetMu[0] >= 0.5
    <SingleEleFinal:EventSelectionAll>
      <cutflowSingleEle:LambdaStr> ev : ev.cutflow[0] == 'SingleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mtwNoHF:LambdaStr> ev : 30 <= ev.mtwNoHF[0] < 125
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <DoubleEleFinal:EventSelectionAll>
      <cutflowDoubleEle:LambdaStr> ev : ev.cutflow[0] == 'DoubleEle'
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[0] < 1.479
      <eleBarrel:LambdaStr> ev : -1.479 < ev.ele_eta[1] < 1.479
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[0] < 0.0354
      <eleRelIso03:LambdaStr> ev : ev.ele_relIso03[1] < 0.0354
      <isoTrackNoEleVeto:LambdaStr> ev : ev.nIsoTracksNoEleVeto[0] <= 0
      <mll:LambdaStr> ev : 66.2 <= ev.mll[0] < 116.2
      <minDelRJetEle:LambdaStr> ev : ev.minDelRJetEle[0] >= 0.5
    <SinglePhotonFinal:EventSelectionAll>
      <cutflowSinglePhoton:LambdaStr> ev : ev.cutflow[0] == 'SinglePhoton'
      <isoTrackVeto:LambdaStr> ev : ev.nIsoTracksVeto[0] <= 0
      <minDelRJetPhoton:LambdaStr> ev : ev.minDelRJetPhoton[0] >= 1.0
      <SinglePhotonFinalBintypes:EventSelectionAny>
        <SinglePhotonFinalMonojet:EventSelectionAll>
          <bintype_monojet:LambdaStr> ev : ev.bintype[0] == 'monojet'
        <SinglePhotonFinalAsymjet:EventSelectionAll>
          <bintype_asymjet:LambdaStr> ev : ev.bintype[0] == 'asymjet'
          <:AlphaTCut>
        <SinglePhotonFinalSymjet:EventSelectionAll>
          <bintype_symjet:LambdaStr> ev : ev.bintype[0] == 'symjet'
          <:AlphaTCut>
        <SinglePhotonFinalHighht:EventSelectionAll>
          <bintype_highht:LambdaStr> ev : ev.bintype[0] == 'highht'
'''

##__________________________________________________________________||
