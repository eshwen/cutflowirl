from .Modules.LambdaStr import LambdaStr

##__________________________________________________________________||
def baseline_kinematics_loose_JECvariation(AllClass, AnyClass, **kargs):
    ret = AllClass(name = 'baseline_kinematics_loose_JECvariation')
    ret.add(LambdaStr("ev : ev.nJet100JECUp[0] >= 1", name = 'nJet100_JECvar'))
    ret.add(LambdaStr("ev : ev.ht40JECUp[0] >= 150", name = 'ht40_loose_JECvar'))
    return ret

##__________________________________________________________________||
