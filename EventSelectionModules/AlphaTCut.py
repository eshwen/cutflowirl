from .LambdaStr import LambdaStr

##__________________________________________________________________||
def AlphaTCut(AllClass, AnyClass):

    ret = AnyClass(name = 'AlphaTCut')

    htbin = AllClass(name = 'HT200to250')
    htbin.add(LambdaStr("ev : 200 <= ev.ht40[0] < 250", name = 'HTin200to250'))
    htbin.add(LambdaStr("ev : 0.65 <= ev.alphaT[0]", name = 'alphaTGT0p65'))
    ret.add(htbin)

    htbin = AllClass(name = 'HT250to300')
    htbin.add(LambdaStr("ev : 250 <= ev.ht40[0] < 300", name = 'HTin250to300'))
    htbin.add(LambdaStr("ev : 0.60 <= ev.alphaT[0]", name = 'alphaTGT0p60'))
    ret.add(htbin)

    htbin = AllClass(name = 'HT300to350')
    htbin.add(LambdaStr("ev : 300 <= ev.ht40[0] < 350", name = 'HTin300to350'))
    htbin.add(LambdaStr("ev : 0.55 <= ev.alphaT[0]", name = 'alphaTGT0p55'))
    ret.add(htbin)

    htbin = AllClass(name = 'HT350to400')
    htbin.add(LambdaStr("ev : 350 <= ev.ht40[0] < 400", name = 'HTin350to400'))
    htbin.add(LambdaStr("ev : 0.53 <= ev.alphaT[0]", name = 'alphaTGT0p53'))
    ret.add(htbin)

    htbin = AllClass(name = 'HT400to800')
    htbin.add(LambdaStr("ev : 400 <= ev.ht40[0] < 800", name = 'HTin400to800'))
    htbin.add(LambdaStr("ev : 0.52 <= ev.alphaT[0]", name = 'alphaTGT0p52'))
    ret.add(htbin)

    return ret

##__________________________________________________________________||
