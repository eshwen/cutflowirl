from .LambdaStr import LambdaStr
from .AlphaTCut import AlphaTCut

##__________________________________________________________________||
def Signal_final(AllClass, AnyClass, **kargs):

    ret = AllClass(name = 'Signal_final')

    ret.add(LambdaStr("ev : ev.nIsoTracksVeto[0] <= 0", name = 'isoTrackVeto'))

    bintypes = AnyClass(name = 'SignalBintypes')
    ret.add(bintypes)

    monojet = AllClass(name = 'SignalFinalMonojet')
    asymjet = AllClass(name = 'SignalFinalAsymjet')
    symjet = AllClass(name = 'SignalFinalSymjet')
    highht = AllClass(name = 'SignalFinalHighht')

    bintypes.add(monojet)
    bintypes.add(asymjet)
    bintypes.add(symjet)
    bintypes.add(highht)

    ## monojet
    monojet.add(LambdaStr("ev : ev.bintypeId[0] == 1 # 'monojet'", name = 'bintype_monojet'))

    ## asymjet
    asymjet.add(LambdaStr("ev : ev.bintypeId[0] == 2 # 'asymjet'", name = 'bintype_asymjet'))
    asymjet.add(AlphaTCut(AllClass, AnyClass))
    asymjet.add(LambdaStr("ev : 0.5 <= ev.biasedDPhi[0]", name = 'biasedDPhiGT0p5'))

    ## symjet
    symjet.add(LambdaStr("ev : ev.bintypeId[0] == 3 # 'symjet'", name = 'bintype_symjet'))
    symjet.add(AlphaTCut(AllClass, AnyClass))
    symjet.add(LambdaStr("ev : 0.5 <= ev.biasedDPhi[0]", name = 'biasedDPhiGT0p5'))

    ## highht
    highht.add(LambdaStr("ev : ev.bintypeId[0] == 4 # 'highht'", name = 'bintype_highht'))
    highht.add(LambdaStr("ev : 0.5 <= ev.biasedDPhi[0]", name = 'biasedDPhiGT0p5'))

    return ret

##__________________________________________________________________||
