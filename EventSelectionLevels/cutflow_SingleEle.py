from .Modules.LambdaStr import LambdaStr

##__________________________________________________________________||
def cutflow_SingleEle(AllClass, AnyClass, datamc, **kargs):
    return LambdaStr("ev : ev.cutflowId[0] == 4 # 'SingleEle'", name = 'cutflow_SingleEle')

##__________________________________________________________________||
