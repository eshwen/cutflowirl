from .Modules.LambdaStr import LambdaStr

##__________________________________________________________________||
def cutflow_Signal(AllClass, AnyClass, datamc, **kargs):
    return LambdaStr("ev : ev.cutflowId[0] == 1 # 'Signal'", name = 'cutflow_Signal')

##__________________________________________________________________||
