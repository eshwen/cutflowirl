from .Modules.LambdaStr import LambdaStr

##__________________________________________________________________||
def htbin_alphaT_loose_JECvariation(AllClass, AnyClass, **kargs):

    ret = AnyClass(name = 'htbin_alphaT_loose_JECvariation')

    htbin = AllClass(name = 'HT200to250')
    htbin.add(LambdaStr("ev : 200 <= ev.ht40JECUp[0]", name = ''))
    htbin.add(LambdaStr("ev : ev.ht40JECDown[0] < 250", name = ''))
    htbin.add(LambdaStr("ev : 0.60 <= max(ev.alphaT[0], ev.alphaTJECUp[0], ev.alphaTJECDown[0])", name = ''))
    ret.add(htbin)

    htbin = AllClass(name = 'HT250to300')
    htbin.add(LambdaStr("ev : 250 <= ev.ht40JECUp[0]", name = ''))
    htbin.add(LambdaStr("ev : ev.ht40JECDown[0] < 300", name = ''))
    htbin.add(LambdaStr("ev : 0.55 <= max(ev.alphaT[0], ev.alphaTJECUp[0], ev.alphaTJECDown[0])", name = ''))
    ret.add(htbin)

    htbin = AllClass(name = 'HT300to800')
    htbin.add(LambdaStr("ev : 300 <= ev.ht40JECUp[0]", name = ''))
    htbin.add(LambdaStr("ev : ev.ht40JECDown[0] < 800", name = ''))
    htbin.add(LambdaStr("ev : 0.50 <= max(ev.alphaT[0], ev.alphaTJECUp[0], ev.alphaTJECDown[0])", name = ''))
    ret.add(htbin)

    htbin = AllClass(name = 'HT800toInf')
    htbin.add(LambdaStr("ev : 800 <= ev.ht40JECUp[0]", name = ''))
    ret.add(htbin)

    return ret

##__________________________________________________________________||
