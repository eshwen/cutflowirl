from .Modules.LambdaStr import LambdaStr

##__________________________________________________________________||
def SinglePhoton_loose(AllClass, AnyClass, datamc, **kargs):

    ret = AllClass(name = 'SinglePhoton_loose')

    bintypes = AnyClass(name = 'SinglePhotonLooseBintypes')
    ret.add(bintypes)

    monojet = AllClass(name = 'SinglePhotonLooseMonojet')
    asymjet = AllClass(name = 'SinglePhotonLooseAsymjet')
    symjet = AllClass(name = 'SinglePhotonLooseSymjet')
    highht = AllClass(name = 'SinglePhotonLooseHighht')

    bintypes.add(monojet)
    bintypes.add(asymjet)
    bintypes.add(symjet)
    bintypes.add(highht)

    ## monojet
    monojet.add(LambdaStr("ev : ev.bintypeId[0] == 1 # 'monojet'", name = 'bintype_monojet'))

    ## asymjet
    asymjet.add(LambdaStr("ev : ev.bintypeId[0] == 2 # 'asymjet'", name = 'bintype_asymjet'))

    ## symjet
    symjet.add(LambdaStr("ev : ev.bintypeId[0] == 3 # 'symjet'", name = 'bintype_symjet'))

    ## highht
    highht.add(LambdaStr("ev : ev.bintypeId[0] == 4 # 'highht'", name = 'bintype_highht'))
    highht.add(LambdaStr("ev : 130 <= ev.mht40_pt[0]", name = 'MHTGT130'))

    return ret

##__________________________________________________________________||
