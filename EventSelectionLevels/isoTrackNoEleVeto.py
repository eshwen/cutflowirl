from .Modules.LambdaStr import LambdaStr

##__________________________________________________________________||
def isoTrackNoEleVeto(AllClass, AnyClass, **kargs):
    return LambdaStr("ev : ev.nIsoTracksNoEleVeto[0] <= 0", name = 'isoTrackNoEleVeto')

##__________________________________________________________________||
