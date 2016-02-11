from .Modules.LambdaStr import LambdaStr

##__________________________________________________________________||
def isoTrackVeto(AllClass, AnyClass, **kargs):
    return LambdaStr("ev : ev.nIsoTracksVeto[0] <= 0", name = 'isoTrackVeto')

##__________________________________________________________________||
