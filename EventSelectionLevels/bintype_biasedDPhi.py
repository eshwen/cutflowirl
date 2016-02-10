from .Modules.LambdaStr import LambdaStr
from .AlternativeSequences import AlternativeSequences

##__________________________________________________________________||
def bintype_biasedDPhi(AllClass, AnyClass, **kargs):
    kargs = kargs.copy()
    kargs.update(dict(
        name = 'bintype_biasedDPhi',
        sequences = (
            dict(name = 'monojet', levels =('bintype_monojet', 'biasedDPhi20')),
            dict(name = 'asymjet', levels =('bintype_asymjet', 'biasedDPhi')),
            dict(name = 'symjet', levels =('bintype_symjet', 'biasedDPhi')),
            dict(name = 'highht', levels =('bintype_highht', 'biasedDPhi')),
        )))

    return AlternativeSequences(AllClass, AnyClass, **kargs)
##__________________________________________________________________||
