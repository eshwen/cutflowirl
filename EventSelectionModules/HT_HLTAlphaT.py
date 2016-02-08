from .LambdaStr import LambdaStr

##__________________________________________________________________||
def HT_HLTAlphaT(AllClass, AnyClass, **kargs):

    ret = AnyClass(name = 'HT_HLTAlphaT')

    htbin = AllClass(name = 'HT200to250')
    htbin.add(LambdaStr("ev : 200 <= ev.ht40[0] < 250", name = 'HTin200to250'))
    hlt = AnyClass(name = 'HLTAlphaTHT200')
    hlt.add(LambdaStr("ev : ev.HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57[0]", name = 'HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57'))
    hlt.add(LambdaStr("ev : ev.HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63[0]", name = 'HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63'))
    htbin.add(hlt)
    ret.add(htbin)

    htbin = AllClass(name = 'HT250to300')
    htbin.add(LambdaStr("ev : 250 <= ev.ht40[0] < 300", name = 'HTin250to300'))
    hlt = AnyClass(name = 'HLTAlphaTHT250')
    hlt.add(LambdaStr("ev : ev.HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55[0]", name = 'HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55'))
    hlt.add(LambdaStr("ev : ev.HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58[0]", name = 'HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58'))
    htbin.add(hlt)
    ret.add(htbin)

    htbin = AllClass(name = 'HT300to350')
    htbin.add(LambdaStr("ev : 300 <= ev.ht40[0] < 350", name = 'HTin300to350'))
    hlt = AnyClass(name = 'HLTAlphaTHT300')
    hlt.add(LambdaStr("ev : ev.HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53[0]", name = 'HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53'))
    hlt.add(LambdaStr("ev : ev.HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54[0]", name = 'HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54'))
    htbin.add(hlt)
    ret.add(htbin)

    htbin = AllClass(name = 'HT350to400')
    htbin.add(LambdaStr("ev : 350 <= ev.ht40[0] < 400", name = 'HTin350to400'))
    hlt = AnyClass(name = 'HLTAlphaTHT350')
    hlt.add(LambdaStr("ev : ev.HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52[0]", name = 'HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52'))
    hlt.add(LambdaStr("ev : ev.HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53[0]", name = 'HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53'))
    htbin.add(hlt)
    ret.add(htbin)

    htbin = AllClass(name = 'HT400to800')
    htbin.add(LambdaStr("ev : 400 <= ev.ht40[0] < 800", name = 'HTin400to800'))
    hlt = AnyClass(name = 'HLTAlphaTHT400')
    hlt.add(LambdaStr("ev : ev.HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51[0]", name = 'HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51'))
    hlt.add(LambdaStr("ev : ev.HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52[0]", name = 'HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52'))
    htbin.add(hlt)
    ret.add(htbin)

    return ret

##__________________________________________________________________||
