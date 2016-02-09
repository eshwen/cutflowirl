from .Modules.LambdaStr import LambdaStr

##__________________________________________________________________||
def AlphaTCut(AllClass, AnyClass):

    ret = AnyClass(name = 'AlphaTCut')

    htbin = AllClass(name = 'HT200to250')
    htbin.add(LambdaStr("ev : ev.htbin[0] == 200", name = 'HTin200to250'))
    htbin.add(LambdaStr("ev : 0.65 <= ev.alphaT[0]", name = 'alphaTGT0p65'))
    ret.add(htbin)

    htbin = AllClass(name = 'HT250to300')
    htbin.add(LambdaStr("ev : ev.htbin[0] == 250", name = 'HTin250to300'))
    htbin.add(LambdaStr("ev : 0.60 <= ev.alphaT[0]", name = 'alphaTGT0p60'))
    ret.add(htbin)

    htbin = AllClass(name = 'HT300to350')
    htbin.add(LambdaStr("ev : ev.htbin[0] == 300", name = 'HTin300to350'))
    htbin.add(LambdaStr("ev : 0.55 <= ev.alphaT[0]", name = 'alphaTGT0p55'))
    ret.add(htbin)

    htbin = AllClass(name = 'HT350to400')
    htbin.add(LambdaStr("ev : ev.htbin[0] == 350", name = 'HTin350to400'))
    htbin.add(LambdaStr("ev : 0.53 <= ev.alphaT[0]", name = 'alphaTGT0p53'))
    ret.add(htbin)

    htbin = AllClass(name = 'HT400to800')
    htbin.add(LambdaStr("ev : ev.htbin[0] in (400, 600)", name = 'HTin400to800'))
    htbin.add(LambdaStr("ev : 0.52 <= ev.alphaT[0]", name = 'alphaTGT0p52'))
    ret.add(htbin)

    htbin = AllClass(name = 'HT800toInf')
    htbin.add(LambdaStr("ev : ev.htbin[0] == 800", name = 'HTGT800'))
    ret.add(htbin)

    return ret

##__________________________________________________________________||
