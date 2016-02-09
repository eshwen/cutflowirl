from .Modules.LambdaStr import LambdaStr
from .htbin_alphaT_loose import htbin_alphaT_loose

##__________________________________________________________________||
def Signal_loose(AllClass, AnyClass, datamc, **kargs):

    ret = AllClass(name = 'Signal_loose')

    ret.add(LambdaStr("ev : ev.ht40[0] >= 200", name = 'HTGT200'))

    bintypes = AnyClass(name = 'SignalLooseBintypes')
    ret.add(bintypes)

    monojet = AllClass(name = 'SignalLooseMonojet')
    asymjet = AllClass(name = 'SignalLooseAsymjet')
    symjet = AllClass(name = 'SignalLooseSymjet')
    highht = AllClass(name = 'SignalLooseHighht')

    bintypes.add(monojet)
    bintypes.add(asymjet)
    bintypes.add(symjet)
    bintypes.add(highht)

    ## monojet
    monojet.add(LambdaStr("ev : ev.bintypeId[0] == 1 # 'monojet'", name = 'bintype_monojet'))

    ## asymjet
    asymjet.add(LambdaStr("ev : ev.bintypeId[0] == 2 # 'asymjet'", name = 'bintype_asymjet'))
    asymjet.add(htbin_alphaT_loose(AllClass, AnyClass))

    ## symjet
    symjet.add(LambdaStr("ev : ev.bintypeId[0] == 3 # 'symjet'", name = 'bintype_symjet'))
    symjet.add(htbin_alphaT_loose(AllClass, AnyClass))

    ## highht
    highht.add(LambdaStr("ev : ev.bintypeId[0] == 4 # 'highht'", name = 'bintype_highht'))
    highht.add(LambdaStr("ev : 130 <= ev.mht40_pt[0]", name = 'MHTGT130'))

    return ret

##__________________________________________________________________||
