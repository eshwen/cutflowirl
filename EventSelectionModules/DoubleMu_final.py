from .LambdaStr import LambdaStr
from .SingleMu_HLT import SingleMu_HLT

##__________________________________________________________________||
def DoubleMu_final(AllClass, AnyClass, hlt, **kargs):

    ret = AllClass(name = 'DoubleMu_final')

    ret.add(LambdaStr("ev : ev.nMuonsIsolated[0] == 2", name = 'nMuonsIsolated'))

    if hlt:
        ret.add(SingleMu_HLT(AllClass, AnyClass))
    ret.add(LambdaStr("ev : ev.nIsoTracksNoMuVeto[0] <= 0", name = 'isoTrackNoMuVeto'))
    ret.add(LambdaStr("ev : 66.2 <= ev.mll[0] < 116.2", name = 'mll'))
    ret.add(LambdaStr("ev : ev.minDelRJetMu[0] >= 0.5", name = 'minDelRJetMu'))

    return ret

##__________________________________________________________________||
