from .LambdaStr import LambdaStr
from .SingleMu_HLT import SingleMu_HLT

##__________________________________________________________________||
def SingleMu_final(AllClass, AnyClass, hlt, metnohf, **kargs):

    ret = AllClass(name = 'SingleMu_final')

    ret.add(LambdaStr("ev : ev.muon_relIso03[0] < 0.12", name = 'relIso03LT0p12'))
    if hlt:
        ret.add(SingleMu_HLT(AllClass, AnyClass))
    ret.add(LambdaStr("ev : ev.nIsoTracksNoMuVeto[0] <= 0", name = 'isoTrackNoMuVeto'))
    if metnohf:
        ret.add(LambdaStr("ev : 30 <= ev.mtwNoHF[0] < 125", name = 'mtwNoHF'))
    else:
        ret.add(LambdaStr("ev : 30 <= ev.mtw[0] < 125", name = 'mtw'))
    ret.add(LambdaStr("ev : ev.minDelRJetMu[0] >= 0.5", name = 'minDelRJetMu'))

    return ret

##__________________________________________________________________||
