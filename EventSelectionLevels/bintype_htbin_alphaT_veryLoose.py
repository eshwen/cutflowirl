from .Modules.LambdaStr import LambdaStr
from .htbin_alphaT_veryLoose import htbin_alphaT_veryLoose

##__________________________________________________________________||
def bintype_htbin_alphaT_veryLoose(AllClass, AnyClass, **kargs):

    ret = AllClass(name = 'bintype_htbin_alphaT_veryLoose')
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
    monojet.add(LambdaStr("ev : ev.bintypeId[0] == 1 # 'monojet'", name = 'bintype_monojet'))

    ## asymjet
    asymjet.add(LambdaStr("ev : ev.bintypeId[0] == 2 # 'asymjet'", name = 'bintype_asymjet'))
    asymjet.add(htbin_alphaT_veryLoose(AllClass, AnyClass))

    ## symjet
    symjet.add(LambdaStr("ev : ev.bintypeId[0] == 3 # 'symjet'", name = 'bintype_symjet'))
    symjet.add(htbin_alphaT_veryLoose(AllClass, AnyClass))

    ## highht
    highht.add(LambdaStr("ev : ev.bintypeId[0] == 4 # 'highht'", name = 'bintype_highht'))

    return ret

##__________________________________________________________________||
