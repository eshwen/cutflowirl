from .Modules.LambdaStr import LambdaStr

##__________________________________________________________________||
def nElectronsBarrel(AllClass, AnyClass, n, **kargs):
    return LambdaStr('ev : ev.nElectronsBarrel[0] == {}'.format(n), name = 'nElectronsBarrel')

##__________________________________________________________________||
