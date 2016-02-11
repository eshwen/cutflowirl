from .Modules.LambdaStr import LambdaStr

##__________________________________________________________________||
def minDelRJetPhoton(AllClass, AnyClass, **kargs):
    return LambdaStr("ev : ev.minDelRJetPhoton[0] >= 1.0", name = 'minDelRJetPhoton')

##__________________________________________________________________||
