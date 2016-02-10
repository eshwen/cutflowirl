from .Modules.LambdaStr import LambdaStr

##__________________________________________________________________||
def htbin_alphaT_loose(AllClass, AnyClass, **kargs):

    ret = AnyClass(name = 'htbin_alphaT_loose')

    htbin = AllClass(name = 'HT200to250')
    htbin.add(LambdaStr("ev : ev.htbin[0] == 200", name = 'HTin200to250'))
    htbin.add(LambdaStr("ev : 0.60 <= ev.alphaT[0]", name = 'alphaTGT0p65'))
    ret.add(htbin)

    htbin = AllClass(name = 'HT250to300')
    htbin.add(LambdaStr("ev : ev.htbin[0] == 250", name = 'HTin250to300'))
    htbin.add(LambdaStr("ev : 0.55 <= ev.alphaT[0]", name = 'alphaTGT0p60'))
    ret.add(htbin)

    htbin = AllClass(name = 'HT300to800')
    htbin.add(LambdaStr("ev : ev.htbin[0] in (300, 350, 400, 600)", name = 'HTin300to800'))
    htbin.add(LambdaStr("ev : 0.50 <= ev.alphaT[0]", name = 'alphaTGT0p55'))
    ret.add(htbin)

    htbin = AllClass(name = 'HT800toInf')
    htbin.add(LambdaStr("ev : ev.htbin[0] == 800", name = 'HTGT800'))
    ret.add(htbin)

    return ret

##__________________________________________________________________||
