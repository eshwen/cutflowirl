from .LambdaStr import LambdaStr

##__________________________________________________________________||
def baseline_kinematics(AllClass, AnyClass, metnohf, **kargs):

    ret = AllClass(name = 'baseline_kinematics')

    ret.add(LambdaStr("ev : ev.nJet40Fwd[0] == 0", name = 'FwJetVeto'))
    ret.add(LambdaStr("ev : ev.nJet40failedId[0] == 0", name = 'JetIDVeto'))
    ret.add(LambdaStr("ev : ev.ht40[0] >= 200", name = 'HTGT200'))
    ret.add(LambdaStr("ev : -2.5 < ev.jet_eta[0] < 2.5", name = 'LeadJetEtaLT2p5'))
    ret.add(LambdaStr("ev : ev.jet_chHEF[0] >= 0.1", name = 'LeadJetChHEFGT0p1'))

    if metnohf:
        ret.add(LambdaStr("ev : ev.MhtOverMetNoXNoHF[0] < 1.25", name = 'MhtOverMetNoXNoHF'))
    else:
        ret.add(LambdaStr("ev : ev.MhtOverMetNoX[0] < 1.25", name = 'MhtOverMetNoX'))

    return ret
##__________________________________________________________________||
