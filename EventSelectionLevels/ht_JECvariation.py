from .Modules.LambdaStr import LambdaStr

##__________________________________________________________________||
def ht_JECvariation(AllClass, AnyClass, datamc, **kargs):
    return LambdaStr("ev : ev.ht40JECUp[0] >= 200", name = 'ht_JECvariation')

##__________________________________________________________________||
