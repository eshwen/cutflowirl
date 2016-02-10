from .Modules.LambdaStr import LambdaStr

##__________________________________________________________________||
def bintype_monojet_JECvariation(AllClass, AnyClass, **kargs):
    return LambdaStr("ev : 1 in (ev.bintypeId[0], ev.bintypeIdJECUp[0], ev.bintypeIdJECDown[0]) # 'monojet'", name = 'bintype_monojet_JECvariation')

##__________________________________________________________________||
