from .Modules.LambdaStr import LambdaStr
from .AlternativeSequences import AlternativeSequences

##__________________________________________________________________||
def bintype_mht(AllClass, AnyClass, **kargs):
    kargs = kargs.copy()
    kargs.update(dict(
        name = 'bintype_mht',
        sequences = (
            dict(name = 'monojet', levels =('bintype_monojet', )),
            dict(name = 'asymjet', levels =('bintype_asymjet', )),
            dict(name = 'symjet', levels =('bintype_symjet', )),
            dict(name = 'highht', levels =('bintype_highht', 'mht')),
        )))

    return AlternativeSequences(AllClass, AnyClass, **kargs)

##__________________________________________________________________||
