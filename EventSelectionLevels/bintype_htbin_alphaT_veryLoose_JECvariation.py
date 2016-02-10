from .AlternativeSequences import AlternativeSequences

##__________________________________________________________________||
def bintype_htbin_alphaT_veryLoose_JECvariation(AllClass, AnyClass, **kargs):
    kargs = kargs.copy()
    kargs.update(dict(
        name = 'bintype_htbin_alphaT_veryLoose_JECvariation',
        sequences = (
            dict(name = 'monojet', levels =('bintype_monojet_JECvariation', )),
            dict(name = 'asymjet', levels =('bintype_asymjet_JECvariation', 'htbin_alphaT_veryLoose_JECvariation')),
            dict(name = 'symjet', levels =('bintype_symjet_JECvariation', 'htbin_alphaT_veryLoose_JECvariation')),
            dict(name = 'highht', levels =('bintype_highht_JECvariation', )),
        )))

    return AlternativeSequences(AllClass, AnyClass, **kargs)

##__________________________________________________________________||
