from .Modules.LambdaStr import LambdaStr

##__________________________________________________________________||
def bintype_symjet(AllClass, AnyClass, **kargs):
    return LambdaStr("ev : ev.bintypeId[0] == 3 # 'symjet'", name = 'bintype_symjet')

##__________________________________________________________________||
