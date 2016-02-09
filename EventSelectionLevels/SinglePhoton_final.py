from .Modules.LambdaStr import LambdaStr

##__________________________________________________________________||
def SinglePhoton_final(AllClass, AnyClass, datamc, **kargs):
    ret = AllClass(name = 'SinglePhoton_final')
    ret.add(LambdaStr("ev : ev.gamma_pt[0] >= 200", name = 'gamma_pt'))
    ret.add(LambdaStr("ev : ev.nIsoTracksVeto[0] <= 0", name = 'isoTrackVeto'))
    ret.add(LambdaStr("ev : ev.minDelRJetPhoton[0] >= 1.0", name = 'minDelRJetPhoton'))
    return ret

##__________________________________________________________________||
