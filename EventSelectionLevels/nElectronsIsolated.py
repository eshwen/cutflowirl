from .Modules.LambdaStr import LambdaStr

##__________________________________________________________________||
def nElectronsIsolated(AllClass, AnyClass, n, **kargs):
    return LambdaStr('ev : ev.nElectronsIsolated[0] == {}'.format(n), name = 'nElectronsIsolated')

##__________________________________________________________________||
