from .Modules.LambdaStr import LambdaStr

##__________________________________________________________________||
def mht_JECvariation(AllClass, AnyClass, **kargs):
    return LambdaStr("ev : 130 <= max(ev.mht40_pt[0], ev.mht40JECUp_pt[0], ev.mht40JECDown_pt[0])", name = 'mht_JECvariation')

##__________________________________________________________________||
