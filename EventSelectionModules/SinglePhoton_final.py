from .LambdaStr import LambdaStr
from .AlphaTCut import AlphaTCut

##__________________________________________________________________||
def SinglePhoton_final(AllClass, AnyClass, datamc, **kargs):

    ret = AllClass(name = 'SinglePhoton_final')

    ret.add(LambdaStr("ev : ev.gamma_pt[0] >= 200", name = 'gamma_pt'))
    ret.add(LambdaStr("ev : ev.nIsoTracksVeto[0] <= 0", name = 'isoTrackVeto'))
    ret.add(LambdaStr("ev : ev.minDelRJetPhoton[0] >= 1.0", name = 'minDelRJetPhoton'))

    bintypes = AnyClass(name = 'SinglePhotonFinalBintypes')
    ret.add(bintypes)

    monojet = AllClass(name = 'SinglePhotonFinalMonojet')
    asymjet = AllClass(name = 'SinglePhotonFinalAsymjet')
    symjet = AllClass(name = 'SinglePhotonFinalSymjet')
    highht = AllClass(name = 'SinglePhotonFinalHighht')

    bintypes.add(monojet)
    bintypes.add(asymjet)
    bintypes.add(symjet)
    bintypes.add(highht)

    ## monojet
    monojet.add(LambdaStr("ev : ev.bintypeId[0] == 1 # 'monojet'", name = 'bintype_monojet'))

    ## asymjet
    asymjet.add(LambdaStr("ev : ev.bintypeId[0] == 2 # 'asymjet'", name = 'bintype_asymjet'))
    asymjet.add(AlphaTCut(AllClass, AnyClass))

    ## symjet
    symjet.add(LambdaStr("ev : ev.bintypeId[0] == 3 # 'symjet'", name = 'bintype_symjet'))
    symjet.add(AlphaTCut(AllClass, AnyClass))

    ## highht
    highht.add(LambdaStr("ev : ev.bintypeId[0] == 4 # 'highht'", name = 'bintype_highht'))

    return ret

##__________________________________________________________________||
