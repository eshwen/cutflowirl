from .LambdaStr import LambdaStr

##__________________________________________________________________||
def clean_jets(AllClass, AnyClass, metnohf, **kargs):
    ret = AllClass(name = 'clean_jets')
    ret.add(LambdaStr("ev : ev.nJet40failedId[0] == 0", name = 'JetIDVeto'))
    ret.add(LambdaStr("ev : -2.5 < ev.jet_eta[0] < 2.5", name = 'LeadJetEtaLT2p5'))
    ret.add(LambdaStr("ev : ev.jet_chHEF[0] >= 0.1", name = 'LeadJetChHEFGT0p1'))
    return ret
##__________________________________________________________________||
