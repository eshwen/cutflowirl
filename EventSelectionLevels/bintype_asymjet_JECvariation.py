from .Modules.LambdaStr import LambdaStr

##__________________________________________________________________||
def bintype_asymjet_JECvariation(AllClass, AnyClass, **kargs):
    return LambdaStr("ev : 2 in (ev.bintypeId[0], ev.bintypeIdJECUp[0], ev.bintypeIdJECDown[0]) # 'asymjet'", name = 'bintype_asymjet_JECvariation')

##__________________________________________________________________||
