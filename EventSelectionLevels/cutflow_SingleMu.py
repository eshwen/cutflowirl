from .Modules.LambdaStr import LambdaStr

##__________________________________________________________________||
def cutflow_SingleMu(AllClass, AnyClass, datamc, **kargs):
    return LambdaStr("ev : ev.cutflowId[0] == 2 # 'SingleMu'", name = 'cutflow_SingleMu')

##__________________________________________________________________||
