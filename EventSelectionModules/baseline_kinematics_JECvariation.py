from .LambdaStr import LambdaStr

##__________________________________________________________________||
def baseline_kinematics_JECvariation(AllClass, AnyClass, **kargs):
    ret = AllClass(name = 'baseline_kinematics_JECvariation')
    ret.add(LambdaStr("ev : ev.nJet100JECUp[0] >= 1", name = 'nJetGTOne'))
    ret.add(LambdaStr("ev : ev.ht40JECUp[0] >= 150", name = 'HTGT150'))
    return ret

##__________________________________________________________________||
