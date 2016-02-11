from .Modules.LambdaStr import LambdaStr

##__________________________________________________________________||
def nMuonsIsolated(AllClass, AnyClass, n, **kargs):
    return LambdaStr('ev : ev.nMuonsIsolated[0] == {}'.format(n), name = 'nMuonsIsolated')

##__________________________________________________________________||
