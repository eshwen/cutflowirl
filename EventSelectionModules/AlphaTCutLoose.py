from .LambdaStr import LambdaStr

##__________________________________________________________________||
def AlphaTCutLoose(AllClass, AnyClass):

    ret = AnyClass(name = 'AlphaTCutLoose')

    htbin = AllClass(name = 'HT200to250')
    htbin.add(LambdaStr("ev : 200 <= ev.ht40[0] < 250", name = 'HTin200to250'))
    htbin.add(LambdaStr("ev : 0.60 <= ev.alphaT[0]", name = 'alphaTGT0p65'))
    ret.add(htbin)

    htbin = AllClass(name = 'HT250to300')
    htbin.add(LambdaStr("ev : 250 <= ev.ht40[0] < 300", name = 'HTin250to300'))
    htbin.add(LambdaStr("ev : 0.55 <= ev.alphaT[0]", name = 'alphaTGT0p60'))
    ret.add(htbin)

    htbin = AllClass(name = 'HT300to800')
    htbin.add(LambdaStr("ev : 300 <= ev.ht40[0] < 800", name = 'HTin300to800'))
    htbin.add(LambdaStr("ev : 0.50 <= ev.alphaT[0]", name = 'alphaTGT0p55'))
    ret.add(htbin)

    return ret

##__________________________________________________________________||
