from .LambdaStr import LambdaStr

##__________________________________________________________________||
def SingleEle_Id(AllClass, AnyClass, datamc, **kargs):
    return LambdaStr("ev : ev.cutflowId[0] == 4 # 'SingleEle'", name = 'SingleEle_Id')

##__________________________________________________________________||
