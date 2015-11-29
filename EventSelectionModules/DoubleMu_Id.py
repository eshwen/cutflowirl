from .LambdaStr import LambdaStr

##__________________________________________________________________||
def DoubleMu_Id(AllClass, AnyClass, datamc, **kargs):
    return LambdaStr("ev : ev.cutflowId[0] == 3 # 'DoubleMu'", name = 'DoubleMu_Id')

##__________________________________________________________________||
