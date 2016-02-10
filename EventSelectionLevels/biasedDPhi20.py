from .Modules.LambdaStr import LambdaStr

##__________________________________________________________________||
def biasedDPhi20(AllClass, AnyClass, **kargs):
    return LambdaStr("ev : ev.biasedDPhi20[0] == -1 or 0.5 <= ev.biasedDPhi20[0]", name = 'biasedDPhi20')

##__________________________________________________________________||
