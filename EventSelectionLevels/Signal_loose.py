from .Modules.LambdaStr import LambdaStr

##__________________________________________________________________||
def Signal_loose(AllClass, AnyClass, datamc, **kargs):
    ret = AllClass(name = 'Signal_loose')
    ret.add(LambdaStr("ev : ev.ht40[0] >= 200", name = 'HTGT200'))
    return ret

##__________________________________________________________________||
