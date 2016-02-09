from .Modules.LambdaStr import LambdaStr

##__________________________________________________________________||
def SinglePhoton_Id(AllClass, AnyClass, datamc, **kargs):
    return LambdaStr("ev : ev.cutflowId[0] == 6 # 'SinglePhoton'", name = 'SinglePhoton_Id')

##__________________________________________________________________||
