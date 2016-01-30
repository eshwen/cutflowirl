from .LambdaStr import LambdaStr

##__________________________________________________________________||
def SingleEle_final(AllClass, AnyClass, metnohf, **kargs):

    ret = AllClass(name = 'SingleEle_final')

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
