from .LambdaStr import LambdaStr

##__________________________________________________________________||
def baseline_kinematics_loose(AllClass, AnyClass, **kargs):
    ret = AllClass(name = 'baseline_kinematics_loose')
    ret.add(LambdaStr("ev : ev.nJet100[0] >= 1", name = 'nJetGTOne'))
    ret.add(LambdaStr("ev : ev.ht40[0] >= 150", name = 'HTGT150'))
    return ret

##__________________________________________________________________||
