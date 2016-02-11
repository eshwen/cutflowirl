from .Modules.LambdaStr import LambdaStr

##__________________________________________________________________||
def minDelRJetMu(AllClass, AnyClass, **kargs):
    return LambdaStr("ev : ev.minDelRJetMu[0] >= 0.5", name = 'minDelRJetMu')

##__________________________________________________________________||
