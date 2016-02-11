from .Modules.LambdaStr import LambdaStr

##__________________________________________________________________||
def cutflow_DoubleMu(AllClass, AnyClass, datamc, **kargs):
    return LambdaStr("ev : ev.cutflowId[0] == 3 # 'DoubleMu'", name = 'cutflow_DoubleMu')

##__________________________________________________________________||
