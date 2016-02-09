from .Modules.LambdaStr import LambdaStr

##__________________________________________________________________||
def unique_promptPhoton_phaseSpace_in_QCD_and_GJets(AllClass, AnyClass, **kargs):

    ret = AllClass(name = 'unique_promptPhoton_phaseSpace_in_QCD_and_GJets')

    processes = AnyClass(name = 'GenProcesses')
    ret.add(processes)

    qcd = AllClass(name = 'GenProcessQCD')
    gjets = AllClass(name = 'GenProcessGJets')
    other = AllClass(name = 'GenProcessesNoQCDorGJets')

    processes.add(qcd)
    processes.add(gjets)
    processes.add(other)

    ## QCD
    qcd.add(LambdaStr("ev : ev.GenProcess[0] == 'QCD'", name = 'process_QCD'))
    qcd.add(LambdaStr("ev : ev.nPromptDirectGenPhotons[0] == 0", name = 'nPromptDirectGenPhotonsEQ0'))

    ## GJets
    gjets.add(LambdaStr("ev : ev.GenProcess[0] == 'GJets'", name = 'process_GJets'))
    gjets.add(LambdaStr("ev : ev.nPromptDirectGenPhotons[0] >= 1", name = 'nPromptDirectGenPhotonsGE1'))

    ## Other
    other.add(LambdaStr("ev : ev.GenProcess[0] not in ('QCD', 'GJets')", name = 'process_not_QCD_or_GJets'))

    return ret

##__________________________________________________________________||
