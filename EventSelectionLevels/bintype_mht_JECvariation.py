from .AlternativeSequences import AlternativeSequences

##__________________________________________________________________||
def bintype_mht_JECvariation(AllClass, AnyClass, **kargs):
    kargs = kargs.copy()
    kargs.update(dict(
        name = 'bintype_htbin_alphaT_veryLoose_JECvariation',
        sequences = (
            dict(name = 'monojet', levels =('bintype_monojet_JECvariation', )),
            dict(name = 'asymjet', levels =('bintype_asymjet_JECvariation', )),
            dict(name = 'symjet', levels =('bintype_symjet_JECvariation', )),
            dict(name = 'highht', levels =('bintype_highht_JECvariation', 'mht_JECvariation')),
        )))

    return AlternativeSequences(AllClass, AnyClass, **kargs)

##__________________________________________________________________||
