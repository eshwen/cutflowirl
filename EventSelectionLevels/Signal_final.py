from .Modules.LambdaStr import LambdaStr

##__________________________________________________________________||
def Signal_final(AllClass, AnyClass, **kargs):
    ret = AllClass(name = 'Signal_final')
    ret.add(LambdaStr("ev : ev.nIsoTracksVeto[0] <= 0", name = 'isoTrackVeto'))
    return ret

##__________________________________________________________________||
