from .Modules.LambdaStr import LambdaStr

##__________________________________________________________________||
def baseline_kinematics(AllClass, AnyClass, metnohf = False, **kargs):
    ret = AllClass(name = 'baseline_kinematics')
    ret.add(LambdaStr("ev : ev.nJet100[0] >= 1", name = 'nJetGTOne'))
    ret.add(LambdaStr("ev : ev.ht40[0] >= 200", name = 'HTGT200'))
    ret.add(LambdaStr("ev : ev.nJet40Fwd[0] == 0", name = 'FwJetVeto'))

    if metnohf:
        ret.add(LambdaStr("ev : ev.MhtOverMetNoXNoHF[0] < 1.25", name = 'MhtOverMetNoXNoHF'))
    else:
        ret.add(LambdaStr("ev : ev.MhtOverMetNoX[0] < 1.25", name = 'MhtOverMetNoX'))
    return ret
##__________________________________________________________________||
