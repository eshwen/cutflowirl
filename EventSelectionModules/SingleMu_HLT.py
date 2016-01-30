from .LambdaStr import LambdaStr

##__________________________________________________________________||
def SingleMu_HLT(AllClass, AnyClass, **kargs):
    ret = AnyClass(name = 'SingleMu_HLT')
    ret.add(LambdaStr("ev : ev.HLT_IsoMu17_eta2p1[0]", name = 'HLT_IsoMu17_eta2p1'))
    ret.add(LambdaStr("ev : ev.HLT_IsoMu20[0]", name = 'HLT_IsoMu20'))
    ret.add(LambdaStr("ev : ev.HLT_IsoMu24_eta2p1[0]", name = 'HLT_IsoMu24_eta2p1'))
    return ret

##__________________________________________________________________||
