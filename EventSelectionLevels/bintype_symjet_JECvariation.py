from .Modules.LambdaStr import LambdaStr

##__________________________________________________________________||
def bintype_symjet_JECvariation(AllClass, AnyClass, **kargs):
    return LambdaStr("ev : 3 in (ev.bintypeId[0], ev.bintypeIdJECUp[0], ev.bintypeIdJECDown[0]) # 'symjet'", name = 'bintype_symjet_JECvariation')

##__________________________________________________________________||
