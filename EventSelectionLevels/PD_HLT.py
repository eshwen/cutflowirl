from .Modules.LambdaStr import LambdaStr

##__________________________________________________________________||
def PD_HLT(AllClass, AnyClass, datamc, **kargs):

    if not datamc == 'data': return AllClass(name = 'PD_HLT')

    ret = AnyClass(name = 'PD_HLT')

    pd = AllClass(name = 'MET')
    pd.add(LambdaStr("ev : ev.PrimaryDataset[0] == 'MET'", name = 'PDMET'))
    hlt = AnyClass(name = 'MET_HLT')
    ## hlt.add(LambdaStr("ev : ev.HLT_PFMET90_PFMHT90_IDTight[0]", name = 'HLT_PFMET90_PFMHT90_IDTight'))
    hlt.add(LambdaStr("ev : ev.HLT_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight[0]", name = 'HLT_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight'))
    hlt.add(LambdaStr("ev : ev.HLT_PFMETNoMu120_JetIdCleaned_PFMHTNoMu120_IDTight[0]", name = 'HLT_PFMETNoMu120_JetIdCleaned_PFMHTNoMu120_IDTight'))
    pd.add(hlt)
    ret.add(pd)

    pd = AllClass(name = 'HTMHT')
    pd.add(LambdaStr("ev : ev.PrimaryDataset[0] == 'HTMHT'", name = 'PDHTMHT'))
    hlt = AnyClass(name = 'HTMHT_HLT')
    hlt.add(LambdaStr("ev : ev.HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57[0]", name = 'HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57'))
    hlt.add(LambdaStr("ev : ev.HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63[0]", name = 'HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63'))
    hlt.add(LambdaStr("ev : ev.HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55[0]", name = 'HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55'))
    hlt.add(LambdaStr("ev : ev.HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58[0]", name = 'HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58'))
    hlt.add(LambdaStr("ev : ev.HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53[0]", name = 'HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53'))
    hlt.add(LambdaStr("ev : ev.HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54[0]", name = 'HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54'))
    hlt.add(LambdaStr("ev : ev.HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52[0]", name = 'HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52'))
    hlt.add(LambdaStr("ev : ev.HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53[0]", name = 'HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53'))
    hlt.add(LambdaStr("ev : ev.HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51[0]", name = 'HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51'))
    hlt.add(LambdaStr("ev : ev.HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52[0]", name = 'HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52'))
    pd.add(hlt)
    ret.add(pd)

    pd = AllClass(name = 'JetHT')
    pd.add(LambdaStr("ev : ev.PrimaryDataset[0] == 'JetHT'", name = 'PDJetHT'))
    hlt = AnyClass(name = 'JetHT_HLT')
    hlt.add(LambdaStr("ev : ev.HLT_PFHT800[0]", name = 'HLT_PFHT800'))
    pd.add(hlt)
    ret.add(pd)

    pd = AllClass(name = 'SingleMuon')
    pd.add(LambdaStr("ev : ev.PrimaryDataset[0] == 'SingleMuon'", name = 'PDSingleMuon'))
    hlt = AnyClass(name = 'SingleMuon_HLT')
    hlt.add(LambdaStr("ev : ev.HLT_IsoMu17_eta2p1[0]", name = 'HLT_IsoMu17_eta2p1'))
    hlt.add(LambdaStr("ev : ev.HLT_IsoMu20[0]",        name = 'HLT_IsoMu20'))
    hlt.add(LambdaStr("ev : ev.HLT_IsoTkMuMu20[0]",    name = 'HLT_IsoTkMuMu20'))
    hlt.add(LambdaStr("ev : ev.HLT_IsoMu24_eta2p1[0]", name = 'HLT_IsoMu24_eta2p1'))
    pd.add(hlt)
    ret.add(pd)

    pd = AllClass(name = 'SingleElectron')
    pd.add(LambdaStr("ev : ev.PrimaryDataset[0] == 'SingleElectron'", name = 'PDSingleElectron'))
    hlt = AnyClass(name = 'SingleElectron_HLT')
    hlt.add(LambdaStr("ev : ev.HLT_Ele22_WPLoose_Gsf[0]", name = 'HLT_Ele22_WPLoose_Gsf'))
    hlt.add(LambdaStr("ev : ev.HLT_Ele23_WPLoose_Gsf[0]", name = 'HLT_Ele23_WPLoose_Gsf'))
    hlt.add(LambdaStr("ev : ev.HLT_Ele27_eta2p1_WPLoose_Gsf[0]", name = 'HLT_Ele27_eta2p1_WPLoose_Gsf'))
    pd.add(hlt)
    ret.add(pd)

    pd = AllClass(name = 'SinglePhoton')
    pd.add(LambdaStr("ev : ev.PrimaryDataset[0] == 'SinglePhoton'", name = 'PDSinglePhoton'))
    hlt = AnyClass(name = 'SinglePhoton_HLT')
    hlt.add(LambdaStr("ev : ev.HLT_Photon120[0]", name = 'HLT_Photon120'))
    hlt.add(LambdaStr("ev : ev.HLT_Photon125[0]", name = 'HLT_Photon125'))
    hlt.add(LambdaStr("ev : ev.HLT_Photon175[0]", name = 'HLT_Photon175'))
    pd.add(hlt)
    ret.add(pd)

    return ret

##__________________________________________________________________||
