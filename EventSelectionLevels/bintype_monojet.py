from .Modules.LambdaStr import LambdaStr

##__________________________________________________________________||
def bintype_monojet(AllClass, AnyClass, **kargs):
    return LambdaStr("ev : ev.bintypeId[0] == 1 # 'monojet'", name = 'bintype_monojet')

##__________________________________________________________________||
