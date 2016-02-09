from .Modules.LambdaStr import LambdaStr

##__________________________________________________________________||
def SingleMu_Id(AllClass, AnyClass, datamc, **kargs):
    return LambdaStr("ev : ev.cutflowId[0] == 2 # 'SingleMu'", name = 'SingleMu_Id')

##__________________________________________________________________||
