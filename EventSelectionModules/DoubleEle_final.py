from .LambdaStr import LambdaStr

##__________________________________________________________________||
def DoubleEle_final(AllClass, AnyClass, datamc, **kargs):

    ret = AllClass(name = 'DoubleEle_final')

    ret.add(LambdaStr("ev : -1.479 < ev.ele_eta[0] < 1.479", name = 'eleBarrel'))
    ret.add(LambdaStr("ev : -1.479 < ev.ele_eta[1] < 1.479", name = 'eleBarrel'))
    ret.add(LambdaStr("ev : ev.ele_relIso03[0] < 0.0354", name = 'eleRelIso03'))
    ret.add(LambdaStr("ev : ev.ele_relIso03[1] < 0.0354", name = 'eleRelIso03'))
    ret.add(LambdaStr("ev : ev.nIsoTracksNoEleVeto[0] <= 0", name = 'isoTrackNoEleVeto'))
    ret.add(LambdaStr("ev : 66.2 <= ev.mll[0] < 116.2", name = 'mll'))
    ret.add(LambdaStr("ev : ev.minDelRJetEle[0] >= 0.5", name = 'minDelRJetEle'))

    return ret

##__________________________________________________________________||
