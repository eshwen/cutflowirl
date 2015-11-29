from .LambdaStr import LambdaStr
from .AlphaTCutLoose import AlphaTCutLoose

##__________________________________________________________________||
def SinglePhoton_loose_JECvariation(AllClass, AnyClass, datamc, **kargs):

    ret = AllClass(name = 'SinglePhoton_loose_JECvariation')

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
    asymjet.add(LambdaStr("ev : 0.5 <= min(ev.alphaT[0], ev.alphaTJECUp[0], ev.alphaTJECDown[0])", name = 'alphaTLT0p5'))

    ## symjet
    symjet.add(LambdaStr("ev : ev.bintypeId[0] == 3 # 'symjet'", name = 'bintype_symjet'))
    symjet.add(LambdaStr("ev : 0.5 <= min(ev.alphaT[0], ev.alphaTJECUp[0], ev.alphaTJECDown[0])", name = 'alphaTLT0p5'))

    ## highht
    highht.add(LambdaStr("ev : ev.bintypeId[0] == 4 # 'highht'", name = 'bintype_highht'))
    highht.add(LambdaStr("ev : 130 <= min(ev.mht40_pt[0], ev.mht40JECUp_pt[0], ev.mht40JECDown_pt[0])", name = 'MHTGT130'))

    return ret

##__________________________________________________________________||
