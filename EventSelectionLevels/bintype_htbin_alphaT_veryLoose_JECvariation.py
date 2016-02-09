from .Modules.LambdaStr import LambdaStr
from .htbin_alphaT_veryLoose_JECvariation import htbin_alphaT_veryLoose_JECvariation

##__________________________________________________________________||
def bintype_htbin_alphaT_veryLoose_JECvariation(AllClass, AnyClass, **kargs):

    ret = AllClass(name = 'bintype_htbin_alphaT_veryLoose_JECvariation')
    bintypes = AnyClass(name = 'bintypes')
    ret.add(bintypes)

    monojet = AllClass(name = 'monojet')
    asymjet = AllClass(name = 'asymjet')
    symjet = AllClass(name = 'symjet')
    highht = AllClass(name = 'highht')

    bintypes.add(monojet)
    bintypes.add(asymjet)
    bintypes.add(symjet)
    bintypes.add(highht)

    ## monojet
    monojet.add(LambdaStr("ev : 1 in (ev.bintypeId[0], ev.bintypeIdJECUp[0], ev.bintypeIdJECDown[0]) # 'monojet'", name = 'bintype_monojet'))

    ## asymjet
    asymjet.add(LambdaStr("ev : 2 in (ev.bintypeId[0], ev.bintypeIdJECUp[0], ev.bintypeIdJECDown[0]) # 'asymjet'", name = 'bintype_asymjet'))
    asymjet.add(htbin_alphaT_veryLoose_JECvariation(AllClass, AnyClass))

    ## symjet
    symjet.add(LambdaStr("ev : 3 in (ev.bintypeId[0], ev.bintypeIdJECUp[0], ev.bintypeIdJECDown[0]) # 'symjet'", name = 'bintype_symjet'))
    symjet.add(htbin_alphaT_veryLoose_JECvariation(AllClass, AnyClass))

    ## highht
    highht.add(LambdaStr("ev : 4 in (ev.bintypeId[0], ev.bintypeIdJECUp[0], ev.bintypeIdJECDown[0]) # 'highht'", name = 'bintype_highht'))

    return ret

##__________________________________________________________________||
