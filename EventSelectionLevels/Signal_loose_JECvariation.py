from .Modules.LambdaStr import LambdaStr

##__________________________________________________________________||
def Signal_loose_JECvariation(AllClass, AnyClass, datamc, **kargs):
    ret = AllClass(name = 'Signal_loose_JECvariation')
    ret.add(LambdaStr("ev : ev.ht40JECUp[0] >= 200", name = 'HTGT200'))
    return ret

##__________________________________________________________________||
