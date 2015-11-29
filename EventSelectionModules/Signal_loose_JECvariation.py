from .LambdaStr import LambdaStr
from .AlphaTCutLoose_JECvariation import AlphaTCutLoose_JECvariation

##__________________________________________________________________||
def Signal_loose_JECvariation(AllClass, AnyClass, datamc, **kargs):

    ret = AllClass(name = 'Signal_loose_JECvariation')

    ret.add(LambdaStr("ev : ev.ht40JECDown[0] >= 200", name = 'HTGT200'))

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
    asymjet.add(AlphaTCutLoose_JECvariation(AllClass, AnyClass))

    ## symjet
    symjet.add(LambdaStr("ev : ev.bintypeId[0] == 3 # 'symjet'", name = 'bintype_symjet'))
    symjet.add(AlphaTCutLoose_JECvariation(AllClass, AnyClass))

    ## highht
    highht.add(LambdaStr("ev : ev.bintypeId[0] == 4 # 'highht'", name = 'bintype_highht'))
    highht.add(LambdaStr("ev : 130 <= min(ev.mht40_pt[0], ev.mht40JECUp_pt[0], ev.mht40JECDown_pt[0])", name = 'MHTGT130'))

    return ret

##__________________________________________________________________||
