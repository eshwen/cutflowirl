from .Modules.LambdaStr import LambdaStr

##__________________________________________________________________||
def isoTrackNoMuVeto(AllClass, AnyClass, **kargs):
    return LambdaStr("ev : ev.nIsoTracksNoMuVeto[0] <= 0", name = 'isoTrackNoMuVeto')

##__________________________________________________________________||
