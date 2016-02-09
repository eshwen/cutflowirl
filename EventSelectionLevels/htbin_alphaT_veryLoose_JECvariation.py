from .Modules.LambdaStr import LambdaStr

##__________________________________________________________________||
def htbin_alphaT_veryLoose_JECvariation(AllClass, AnyClass):

    ret = AnyClass(name = 'htbin_alphaT_veryLoose_JECvariation')

    htbin = AllClass(name = 'HT200to800')
    htbin.add(LambdaStr("ev : ev.htbin[0] in (200, 250, 300, 350, 400, 600)", name = 'HTin200to800'))
    htbin.add(LambdaStr("ev : 0.50 <= max(ev.alphaT[0], ev.alphaTJECUp[0], ev.alphaTJECDown[0])", name = ''))
    ret.add(htbin)

    htbin = AllClass(name = 'HT800toInf')
    htbin.add(LambdaStr("ev : ev.htbin[0] == 800", name = 'HTGT800'))
    ret.add(htbin)

    return ret

##__________________________________________________________________||
