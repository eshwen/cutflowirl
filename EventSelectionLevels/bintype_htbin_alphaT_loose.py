from .Modules.LambdaStr import LambdaStr
from .AnyFactory import AnyFactory

##__________________________________________________________________||
def bintype_htbin_alphaT_loose(AllClass, AnyClass, **kargs):
    kargs = kargs.copy()
    kargs.update(dict(
        name = 'bintype_htbin_alphaT_loose',
        sequences = (
            dict(name = 'monojet', levels =('bintype_monojet', )),
            dict(name = 'asymjet', levels =('bintype_asymjet', 'htbin_alphaT_loose')),
            dict(name = 'symjet', levels =('bintype_symjet', 'htbin_alphaT_loose')),
            dict(name = 'highht', levels =('bintype_highht', )),
        )))

    return AnyFactory(AllClass, AnyClass, **kargs)

##__________________________________________________________________||
