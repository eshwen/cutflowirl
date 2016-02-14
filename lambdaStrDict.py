
##__________________________________________________________________||
lambdaStrDict = {
    'ht40_loose_JECvar': 'ev : ev.ht40JECUp[0] >= 150',
    'nJet100_JECvar': 'ev : ev.nJet100JECUp[0] >= 1',
    'ht_JECvar': "ev : ev.ht40JECUp[0] >= 200",
    'mht_JECvar': "ev : 130 <= max(ev.mht40_pt[0], ev.mht40JECUp_pt[0], ev.mht40JECDown_pt[0])",
    'bintype_monojet_JECvar': "ev : 1 in (ev.bintypeId[0], ev.bintypeIdJECUp[0], ev.bintypeIdJECDown[0]) # 'monojet'",
    'bintype_asymjet_JECvar': "ev : 2 in (ev.bintypeId[0], ev.bintypeIdJECUp[0], ev.bintypeIdJECDown[0]) # 'asymjet'",
    'bintype_symjet_JECvar': "ev : 3 in (ev.bintypeId[0], ev.bintypeIdJECUp[0], ev.bintypeIdJECDown[0]) # 'symjet'",
    'bintype_highht_JECvar': "ev : 4 in (ev.bintypeId[0], ev.bintypeIdJECUp[0], ev.bintypeIdJECDown[0]) # 'highht'",
    'cutflow_Signal': "ev : ev.cutflowId[0] == 1 # 'Signal'",
    'cutflow_SingleMu': "ev : ev.cutflowId[0] == 2 # 'SingleMu'",
    'cutflow_DoubleMu': "ev : ev.cutflowId[0] == 3 # 'DoubleMu'",
    'cutflow_SingleEle': "ev : ev.cutflowId[0] == 4 # 'SingleEle'",
    'cutflow_DoubleEle': "ev : ev.cutflowId[0] == 5 # 'DoubleEle'",
    'cutflow_SinglePhoton': "ev : ev.cutflowId[0] == 6 # 'SinglePhoton'",
    'PD_MET': "ev : ev.PrimaryDataset[0] == 'MET'",
    'PD_HTMHT': "ev : ev.PrimaryDataset[0] == 'HTMHT'",
    'PD_JetHT': "ev : ev.PrimaryDataset[0] == 'JetHT'",
    'PD_SingleElectron': "ev : ev.PrimaryDataset[0] == 'SingleElectron'",
    'PD_SingleMuon': "ev : ev.PrimaryDataset[0] == 'SingleMuon'",
    'PD_SinglePhoton': "ev : ev.PrimaryDataset[0] == 'SinglePhoton'",
}

##__________________________________________________________________||
