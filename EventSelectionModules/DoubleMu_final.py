from .LambdaStr import LambdaStr
from .SingleMu_HLT import SingleMu_HLT

##__________________________________________________________________||
def DoubleMu_final(AllClass, AnyClass, hlt, **kargs):

    ret = AllClass(name = 'DoubleMu_final')

    ret.add(LambdaStr("ev : ev.cutflowId[0] == 3 # 'DoubleMu'", name = 'cutflowDoubleMu'))
    ret.add(LambdaStr("ev : ev.muon_relIso03[0] < 0.12", name = 'relIso03LT0p12'))
    ret.add(LambdaStr("ev : ev.muon_relIso03[1] < 0.12", name = 'relIso03LT0p12'))
    if hlt:
        ret.add(SingleMu_HLT(AllClass, AnyClass))
    ret.add(LambdaStr("ev : ev.nIsoTracksNoMuVeto[0] <= 0", name = 'isoTrackNoMuVeto'))
    ret.add(LambdaStr("ev : 66.2 <= ev.mll[0] < 116.2", name = 'mll'))
    ret.add(LambdaStr("ev : ev.minDelRJetMu[0] >= 0.5", name = 'minDelRJetMu'))

    return ret

##__________________________________________________________________||
