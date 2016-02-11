from .Modules.LambdaStr import LambdaStr

##__________________________________________________________________||
def cutflow_SinglePhoton(AllClass, AnyClass, datamc, **kargs):
    return LambdaStr("ev : ev.cutflowId[0] == 6 # 'SinglePhoton'", name = 'cutflow_SinglePhoton')

##__________________________________________________________________||
