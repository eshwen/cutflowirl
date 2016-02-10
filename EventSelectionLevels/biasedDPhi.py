from .Modules.LambdaStr import LambdaStr

##__________________________________________________________________||
def biasedDPhi(AllClass, AnyClass, **kargs):
    return LambdaStr("ev : 0.5 <= ev.biasedDPhi[0]", name = 'biasedDPhi')

##__________________________________________________________________||
