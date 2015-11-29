from .LambdaStr import LambdaStr

##__________________________________________________________________||
def baseline_kinematics_JECvariation(AllClass, AnyClass, **kargs):
    ret = AllClass(name = 'baseline_kinematics_JECvariation')
    ret.add(LambdaStr("ev : ev.nJetJECDown100[0] >= 1", name = 'nJetGTOne'))
    ret.add(LambdaStr("ev : ev.ht40JECDown[0] >= 150", name = 'HTGT150'))
    return ret

##__________________________________________________________________||
