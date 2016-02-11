from .Modules.LambdaStr import LambdaStr

##__________________________________________________________________||
def minDelRJetEle(AllClass, AnyClass, **kargs):
    return LambdaStr("ev : ev.minDelRJetEle[0] >= 0.5", name = 'minDelRJetEle')

##__________________________________________________________________||
