from .LambdaStr import LambdaStr

##__________________________________________________________________||
def BaselineMu_Id(AllClass, AnyClass, **kargs):
    ret = AllClass(name = 'BaselineMu_Id')
    ret.add(LambdaStr("ev : ev.nMuonsVeto[0] >= 1"))
    ret.add(LambdaStr("ev : ev.nPhotonsVeto[0] == 0"))
    return ret

##__________________________________________________________________||
