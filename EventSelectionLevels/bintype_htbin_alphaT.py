from .AlternativeSequences import AlternativeSequences

##__________________________________________________________________||
def bintype_htbin_alphaT(AllClass, AnyClass, **kargs):
    kargs = kargs.copy()
    kargs.update(dict(
        name = 'bintype_htbin_alphaT',
        sequences = (
            dict(name = 'monojet', levels =('bintype_monojet', )),
            dict(name = 'asymjet', levels =('bintype_asymjet', 'htbin_alphaT')),
            dict(name = 'symjet', levels =('bintype_symjet', 'htbin_alphaT')),
            dict(name = 'highht', levels =('bintype_highht', )),
        )))

    return AlternativeSequences(AllClass, AnyClass, **kargs)

##__________________________________________________________________||
