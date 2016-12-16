
##__________________________________________________________________||
htbin_alphaT_loose_JECvar = dict(
    Any = (dict(All = ('htbin_200_JECvar', ('alphaT_JECvar', dict(v = 0.60)))),
           dict(All = ('htbin_250_JECvar', ('alphaT_JECvar', dict(v = 0.55)))),
           dict(All = ('htbin_300_JECvar', ('alphaT_JECvar', dict(v = 0.50)))),
           dict(All = ('htbin_350_JECvar', ('alphaT_JECvar', dict(v = 0.50)))),
           dict(All = ('htbin_400_JECvar', ('alphaT_JECvar', dict(v = 0.50)))),
           dict(All = ('htbin_600_JECvar', ('alphaT_JECvar', dict(v = 0.50)))),
           dict(All = ('htbin_800_JECvar', ))
    )
)

htbin_alphaT_veryLoose_JECvar = dict(
    Any = (dict(All = ('htbin_200_JECvar', ('alphaT_JECvar', dict(v = 0.50)))),
           dict(All = ('htbin_250_JECvar', ('alphaT_JECvar', dict(v = 0.50)))),
           dict(All = ('htbin_300_JECvar', ('alphaT_JECvar', dict(v = 0.50)))),
           dict(All = ('htbin_350_JECvar', ('alphaT_JECvar', dict(v = 0.50)))),
           dict(All = ('htbin_400_JECvar', ('alphaT_JECvar', dict(v = 0.50)))),
           dict(All = ('htbin_600_JECvar', ('alphaT_JECvar', dict(v = 0.50)))),
           dict(All = ('htbin_800_JECvar', ))
    )
)

htbin_alphaTPt_loose_JECvar = dict(
    Any = (dict(All = ('htbin_200_JECvar', ('alphaTPt_JECvar', dict(v = 0.60)))),
           dict(All = ('htbin_250_JECvar', ('alphaTPt_JECvar', dict(v = 0.55)))),
           dict(All = ('htbin_300_JECvar', ('alphaTPt_JECvar', dict(v = 0.50)))),
           dict(All = ('htbin_350_JECvar', ('alphaTPt_JECvar', dict(v = 0.50)))),
           dict(All = ('htbin_400_JECvar', ('alphaTPt_JECvar', dict(v = 0.50)))),
           dict(All = ('htbin_600_JECvar', ('alphaTPt_JECvar', dict(v = 0.50)))),
           dict(All = ('htbin_800_JECvar', ))
    )
)

htbin_alphaTPt_veryLoose_JECvar = dict(
    Any = (dict(All = ('htbin_200_JECvar', ('alphaTPt_JECvar', dict(v = 0.50)))),
           dict(All = ('htbin_250_JECvar', ('alphaTPt_JECvar', dict(v = 0.50)))),
           dict(All = ('htbin_300_JECvar', ('alphaTPt_JECvar', dict(v = 0.50)))),
           dict(All = ('htbin_350_JECvar', ('alphaTPt_JECvar', dict(v = 0.50)))),
           dict(All = ('htbin_400_JECvar', ('alphaTPt_JECvar', dict(v = 0.50)))),
           dict(All = ('htbin_600_JECvar', ('alphaTPt_JECvar', dict(v = 0.50)))),
           dict(All = ('htbin_800_JECvar', ))
    )
)

biasedDPhi_loose_JECvar = dict(
    All = (('biasedDPhi_JECvar', dict(v = 0.50)),),
)

##__________________________________________________________________||
event_selection_path_cfg_tree_production = dict(All = (
    'nJet100_JECvar',
    'ht40_loose_JECvar',
    dict(Any = (
        'isMC',
        dict(All = (
            'isData',
            dict(Any = (dict(All = ('PD_MET', 'cutflow_Signal')),
                        dict(All = ('PD_HTMHT', 'cutflow_Signal')),
                        dict(All = ('PD_JetHT', 'cutflow_Signal')),
                        dict(All = ('PD_SingleMuon',
                                    dict(Any = ('cutflow_SingleMu',
                                                'cutflow_DoubleMu',
                                                dict(All = ("ev : ev.nMuonsVeto[0] >= 1", "ev : ev.nPhotonsVeto[0] == 0")),
                                    )))),
                        dict(All = ('PD_SingleElectron',
                                    dict(Any = ('cutflow_SingleEle',
                                                'cutflow_DoubleEle',
                                    )))),
                        dict(All = ('PD_SinglePhoton', 'cutflow_SinglePhoton')),
                        dict(All = ('PD_DoubleEG', 'cutflow_SinglePhoton')),
            )),
        )),
    )),
    dict(Any = (
        dict(All = (
            'cutflow_Signal',
            'ht_JECvar',
            'mht_loose_JECvar',
            dict(Any = (
                'bintype_monojet_JECvar',
                'bintype_asymjet_JECvar',
                'bintype_symjet_JECvar',
                'bintype_highht_JECvar',
            )),
            dict(Any = (
                'bintype_monojet_JECvar',
                biasedDPhi_loose_JECvar,
                dict(All = (
                    dict(Not = biasedDPhi_loose_JECvar),
                    dict(Any = (
                        dict(All = ('bintype_asymjet_JECvar', htbin_alphaT_veryLoose_JECvar)),
                        dict(All = ('bintype_asymjet_JECvar', htbin_alphaTPt_veryLoose_JECvar)),
                        dict(All = ('bintype_symjet_JECvar', htbin_alphaT_veryLoose_JECvar)),
                        dict(All = ('bintype_symjet_JECvar', htbin_alphaTPt_veryLoose_JECvar)),
                        dict(All = ('bintype_highht_JECvar',)),
                    )),
                )),
            )),
        )),
        'cutflow_SingleMu',
        'cutflow_DoubleMu',
        'cutflow_SingleEle',
        'cutflow_DoubleEle',
        'cutflow_SinglePhoton',
        dict(name = 'BaselineMu', All = ("ev : ev.nMuonsVeto[0] >= 1", "ev : ev.nPhotonsVeto[0] == 0")),
    )),
))


##__________________________________________________________________||
hlt_singlemuon = dict(Any = (
    'HLT_IsoMu17_eta2p1',
    'HLT_IsoMu20',
    # dict(Any = ('isMC',
    #             dict(All = ('isData', 'HLT_IsoTkMu20')),
    # )),
    'HLT_IsoMu24_eta2p1',
))

hlt_alphat = dict(Any = (
    'HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57',
    'HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55',
    'HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53',
    'HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52',
    'HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51',
))

hlt_alphat_secondary = dict(Any = (
    'HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63',
    'HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58',
    'HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54',
    'HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53',
    'HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52',
))

##__________________________________________________________________||
pd_hlt = dict(Any = (
    dict(All = ('PD_MET', dict(Any = (
        # 'HLT_PFMET90_PFMHT90_IDTight',
        'HLT_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight',
        'HLT_PFMETNoMu120_JetIdCleaned_PFMHTNoMu120_IDTight',
    )))),
    dict(All = ('PD_HTMHT', dict(Any = (
        hlt_alphat, hlt_alphat_secondary
    )))),
    dict(All = ('PD_JetHT', dict(Any = (
        'HLT_PFHT800',
    )))),
    dict(All = ('PD_SingleMuon', hlt_singlemuon)),
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

##__________________________________________________________________||
htbin_alphaT = dict(
    Any = (dict(All = ('htbin_200', ('alphaT', dict(v = 0.65)))),
           dict(All = ('htbin_250', ('alphaT', dict(v = 0.60)))),
           dict(All = ('htbin_300', ('alphaT', dict(v = 0.55)))),
           dict(All = ('htbin_350', ('alphaT', dict(v = 0.53)))),
           dict(All = ('htbin_400', ('alphaT', dict(v = 0.52)))),
           dict(All = ('htbin_600', ('alphaT', dict(v = 0.52)))),
           dict(All = ('htbin_800', ))
    )
)

##__________________________________________________________________||
met_filters = dict(
    All = (
        "ev : ev.Flag_HBHENoiseFilter[0] == 1",
        "ev : ev.Flag_HBHENoiseIsoFilter[0] == 1",
        "ev : ev.Flag_EcalDeadCellTriggerPrimitiveFilter[0] == 1",
        "ev : ev.Flag_goodVertices[0] == 1",
        "ev : ev.Flag_eeBadScFilter[0] == 1",
        "ev : ev.Flag_globalTightHalo2016Filter[0] == 1",
        )
)

met_filters_data_only = dict(
    All = (
        'NotInBadEventList',
    ))

##__________________________________________________________________||
unique_promptPhoton_phaseSpace_in_QCD_and_GJets = dict(Any = (
    dict(All = ("ev : ev.GenProcess[0] == 'QCD'", "ev : ev.nPromptDirectGenPhotons[0] == 0")),
    dict(All = ("ev : ev.GenProcess[0] == 'GJets'", "ev : ev.nPromptDirectGenPhotons[0] >= 1")),
    dict(Not = dict(Any = ("ev : ev.GenProcess[0] == 'QCD'", "ev : ev.GenProcess[0] == 'GJets'"))),
))

##__________________________________________________________________||
unique_TTJets_phaseSpace = dict(Any = (
    dict(All = (
        'ev : ev.componentName[0] == "TTJets_madgraphMLM"',
        'ev : ev.lheHTnoT[0] < 600',
        'ev : ev.nLheElectrons[0] == 0',
        'ev : ev.nLheMuons[0] == 0',
        'ev : ev.nLheTaus[0] == 0',
    )),
    dict(All = (
        dict(Any = (
            'ev : ev.componentName[0] == "TTJets_DiLept_madgraphMLM"',
            'ev : ev.componentName[0] == "TTJets_SingleLeptFromT_madgraphMLM"',
            'ev : ev.componentName[0] == "TTJets_SingleLeptFromTbar_madgraphMLM"',
            'ev : ev.componentName[0] == "TTJets_DiLept_madgraphMLM_ext1"',
            'ev : ev.componentName[0] == "TTJets_SingleLeptFromT_madgraphMLM_ext1"',
            'ev : ev.componentName[0] == "TTJets_SingleLeptFromTbar_madgraphMLM_ext1"',
        )),
        'ev : ev.lheHTnoT[0] < 600',
    )),
    dict(All = (
        dict(Any = (
            'ev : ev.componentName[0] == "TTJets_HT600to800_madgraphMLM"',
            'ev : ev.componentName[0] == "TTJets_HT800to1200_madgraphMLM"',
            'ev : ev.componentName[0] == "TTJets_HT1200to2500_madgraphMLM"',
            'ev : ev.componentName[0] == "TTJets_HT2500toInf_madgraphMLM"',
        )),
        'ev : ev.lheHTnoT[0] >= 600',
    )),
    dict(Not = dict(Any = (
        'ev : ev.componentName[0] == "TTJets_madgraphMLM"',
            'ev : ev.componentName[0] == "TTJets_DiLept_madgraphMLM"',
            'ev : ev.componentName[0] == "TTJets_SingleLeptFromT_madgraphMLM"',
            'ev : ev.componentName[0] == "TTJets_SingleLeptFromTbar_madgraphMLM"',
            'ev : ev.componentName[0] == "TTJets_DiLept_madgraphMLM_ext1"',
            'ev : ev.componentName[0] == "TTJets_SingleLeptFromT_madgraphMLM_ext1"',
            'ev : ev.componentName[0] == "TTJets_SingleLeptFromTbar_madgraphMLM_ext1"',
            'ev : ev.componentName[0] == "TTJets_HT600to800_madgraphMLM"',
            'ev : ev.componentName[0] == "TTJets_HT800to1200_madgraphMLM"',
            'ev : ev.componentName[0] == "TTJets_HT1200to2500_madgraphMLM"',
            'ev : ev.componentName[0] == "TTJets_HT2500toInf_madgraphMLM"',
        ))),
    ))


##__________________________________________________________________||
def build_event_selection_path_cfg_standard(
        json = True,
        metnohf = False,
        hlt_for_mc = True,
):
    # Ideally, a dict should be put here. But now it is a function
    # because a path_cfg has to be generated in accordance with
    # arguments

    ret = dict(All = (
        dict(Any = (
            dict(All = (
                'isMC',
                unique_promptPhoton_phaseSpace_in_QCD_and_GJets,
                unique_TTJets_phaseSpace,
            )),
            dict(All = (
                'isData',
                'JSON' if json else 'True',
                pd_hlt,
            )),
        )),
        met_filters,
        dict(Any = (
            'isMC',
            dict(All = ('isData', met_filters_data_only)),
        )),
        ('nJet40failedId', dict(n = 0)),
        ('nJet40Fwd', dict(n = 0)),
        'ev : -2.5 < ev.jet_eta[0] < 2.5',
        'ev : ev.jet_chHEF[0] >= 0.1',
        'nJet100',
        'ht40',
        'mht',
        'MhtOverMetNoXNoHF' if metnohf else 'MhtOverMetNoX',
        dict(Any = (
            dict(All = ('bintype_monojet', 'biasedDPhi20')),
            dict(All = (
                dict(Any = ('bintype_asymjet', 'bintype_symjet', 'bintype_highht')),
                'biasedDPhi',
            )),
        )),
        dict(Any = (
            'isMC',
            dict(All = (
                'isData',
                dict(Any = (
                    dict(All = (
                        'cutflow_Signal',
                        dict(Any = (
                            dict(All =('bintype_monojet', 'PD_MET')),
                            dict(All =(dict(Any = ('bintype_asymjet', 'bintype_symjet')),
                                       dict(Any = (
                                           dict(All = ('PD_MET', dict(Not = hlt_alphat))),
                                           'PD_HTMHT'
                                       )))),
                            dict(All =('bintype_highht',
                                       dict(Any = (
                                           'PD_HTMHT',
                                           dict(All = ('PD_JetHT', dict(Not = hlt_alphat))),
                                       )))),
                        )))),
                    dict(All = ('cutflow_SingleMu', 'PD_SingleMuon')),
                    dict(All = ('cutflow_DoubleMu', 'PD_SingleMuon')),
                    dict(All = ('cutflow_SingleEle', 'PD_SingleElectron')),
                    dict(All = ('cutflow_DoubleEle', 'PD_SingleElectron')),
                    dict(All = ('cutflow_SinglePhoton', 'PD_SinglePhoton')),
                )),
            )),
        )),
        dict(name = 'cutflows',
             Any = (
                 dict(name = 'Signal',
                      All = (
                          'cutflow_Signal',
                          'isoTrackVeto',
                          dict(Any = (
                              'bintype_monojet',
                              dict(All =('bintype_asymjet', htbin_alphaT)),
                              dict(All =('bintype_symjet', htbin_alphaT)),
                              'bintype_highht',
                          )),
                      )),
                 dict(name = 'SingleMu',
                      All = (
                          'cutflow_SingleMu',
                          hlt_singlemuon if hlt_for_mc else 'True',
                          ('nMuonsIsolated', dict(n = 1)),
                          'isoTrackNoMuVeto',
                          'minDelRJetMu',
                          'mtwNoHF' if metnohf else 'mtw',
                      )),
                 dict(name = 'DoubleMu',
                      All = (
                          'cutflow_DoubleMu',
                          hlt_singlemuon if hlt_for_mc else 'True',
                          ('nMuonsIsolated', dict(n = 2)),
                          'isoTrackNoMuVeto',
                          'minDelRJetMu',
                          'mll',
                      )),
                 dict(name = 'SingleEle',
                      All = (
                          'cutflow_SingleEle',
                          ('nElectronsIsolated', dict(n = 1)),
                          ('nElectronsBarrel', dict(n = 1)),
                          'isoTrackNoEleVeto',
                          'minDelRJetEle',
                          'mtwNoHF' if metnohf else 'mtw',
                      )),
                 dict(name = 'DoubleEle',
                      All = (
                          'cutflow_DoubleEle',
                          ('nElectronsIsolated', dict(n = 2)),
                          ('nElectronsBarrel', dict(n = 2)),
                          'isoTrackNoEleVeto',
                          'minDelRJetEle',
                          'mll',
                      )),
                 dict(name = 'SinglePhoton',
                      All = (
                          'cutflow_SinglePhoton',
                          'isoTrackVeto',
                          dict(Any = (
                              'bintype_monojet',
                              dict(All =('bintype_asymjet', htbin_alphaT)),
                              dict(All =('bintype_symjet', htbin_alphaT)),
                              'bintype_highht',
                          )),
                          'minDelRJetPhoton',
                          ('nPhotons200', dict(n = 1)),
                      )),
             )),
    ))

    return ret

##__________________________________________________________________||

