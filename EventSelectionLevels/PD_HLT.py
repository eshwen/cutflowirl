from .FactoryDispatcher import FactoryDispatcher

##__________________________________________________________________||
def PD_HLT(**kargs):

    path_cfg = dict(Any = (
        dict(All = ('PD_MET', dict(Any = (
            # 'HLT_PFMET90_PFMHT90_IDTight',
            'HLT_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight',
            'HLT_PFMETNoMu120_JetIdCleaned_PFMHTNoMu120_IDTight',
        )))),
        dict(All = ('PD_HTMHT', dict(Any = (
            'HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57',
            'HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63',
            'HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55',
            'HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58',
            'HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53',
            'HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54',
            'HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52',
            'HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53',
            'HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51',
            'HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52',
        )))),
        dict(All = ('PD_JetHT', dict(Any = (
            'HLT_PFHT800',
        )))),
        dict(All = ('PD_SingleMuon', dict(Any = (
            'HLT_IsoMu17_eta2p1',
            'HLT_IsoMu20',
            'HLT_IsoTkMuMu20',
            'HLT_IsoMu24_eta2p1',
        )))),
        dict(All = ('PD_SingleElectron', dict(Any = (
            'HLT_Ele22_WPLoose_Gsf',
            'HLT_Ele23_WPLoose_Gsf',
            'HLT_Ele27_eta2p1_WPLoose_Gsf',
        )))),
        dict(All = ('PD_SinglePhoton', dict(Any = (
            'HLT_Photon120',
            'HLT_Photon125',
            'HLT_Photon175',
        )))),
        )
    )

    ## import pprint
    ## pprint.pprint(path_cfg)

    return FactoryDispatcher(path_cfg = path_cfg, **kargs)

##__________________________________________________________________||
