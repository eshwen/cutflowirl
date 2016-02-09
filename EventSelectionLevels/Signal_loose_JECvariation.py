from .Modules.LambdaStr import LambdaStr
from .AlphaTCutLoose_JECvariation import AlphaTCutLoose_JECvariation

##__________________________________________________________________||
def Signal_loose_JECvariation(AllClass, AnyClass, datamc, **kargs):

    ret = AllClass(name = 'Signal_loose_JECvariation')

    ret.add(LambdaStr("ev : ev.ht40JECUp[0] >= 200", name = 'HTGT200'))

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
    monojet.add(LambdaStr("ev : 1 in (ev.bintypeId[0], ev.bintypeIdJECUp[0], ev.bintypeIdJECDown[0]) # 'monojet'", name = 'bintype_monojet'))

    ## asymjet
    asymjet.add(LambdaStr("ev : 2 in (ev.bintypeId[0], ev.bintypeIdJECUp[0], ev.bintypeIdJECDown[0]) # 'asymjet'", name = 'bintype_asymjet'))
    asymjet.add(AlphaTCutLoose_JECvariation(AllClass, AnyClass))

    ## symjet
    symjet.add(LambdaStr("ev : 3 in (ev.bintypeId[0], ev.bintypeIdJECUp[0], ev.bintypeIdJECDown[0]) # 'symjet'", name = 'bintype_symjet'))
    symjet.add(AlphaTCutLoose_JECvariation(AllClass, AnyClass))

    ## highht
    highht.add(LambdaStr("ev : 4 in (ev.bintypeId[0], ev.bintypeIdJECUp[0], ev.bintypeIdJECDown[0]) # 'highht'", name = 'bintype_highht'))
    highht.add(LambdaStr("ev : 130 <= max(ev.mht40_pt[0], ev.mht40JECUp_pt[0], ev.mht40JECDown_pt[0])", name = 'MHTGT130'))

    return ret

##__________________________________________________________________||
