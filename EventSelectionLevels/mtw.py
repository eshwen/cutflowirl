from .Modules.LambdaStr import LambdaStr

##__________________________________________________________________||
def mtw(AllClass, AnyClass, metnohf, **kargs):
    if metnohf: return LambdaStr("ev : 30 <= ev.mtwNoHF[0] < 125", name = 'mtw')
    return LambdaStr("ev : 30 <= ev.mtw[0] < 125", name = 'mtw')

##__________________________________________________________________||
