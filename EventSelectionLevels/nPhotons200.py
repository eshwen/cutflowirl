from .Modules.LambdaStr import LambdaStr

##__________________________________________________________________||
def nPhotons200(AllClass, AnyClass, n, **kargs):
    return LambdaStr('ev : ev.nPhotons200[0] == {}'.format(n), name = 'nPhotons200')

##__________________________________________________________________||
