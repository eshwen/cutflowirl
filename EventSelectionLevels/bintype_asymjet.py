from .Modules.LambdaStr import LambdaStr

##__________________________________________________________________||
def bintype_asymjet(AllClass, AnyClass, **kargs):
    return LambdaStr("ev : ev.bintypeId[0] == 2 # 'asymjet'", name = 'bintype_asymjet')

##__________________________________________________________________||
