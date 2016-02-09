from .Modules.LambdaStr import LambdaStr

##__________________________________________________________________||
def bintype_mht_JECvariation(AllClass, AnyClass, **kargs):

    ret = AllClass(name = 'bintype_mht_JECvariation')
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

    ## symjet
    symjet.add(LambdaStr("ev : 3 in (ev.bintypeId[0], ev.bintypeIdJECUp[0], ev.bintypeIdJECDown[0]) # 'symjet'", name = 'bintype_symjet'))

    ## highht
    highht.add(LambdaStr("ev : 4 in (ev.bintypeId[0], ev.bintypeIdJECUp[0], ev.bintypeIdJECDown[0]) # 'highht'", name = 'bintype_highht'))
    highht.add(LambdaStr("ev : 130 <= max(ev.mht40_pt[0], ev.mht40JECUp_pt[0], ev.mht40JECDown_pt[0])", name = 'MHTGT130'))

    return ret

##__________________________________________________________________||
