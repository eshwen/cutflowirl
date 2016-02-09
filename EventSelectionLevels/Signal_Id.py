from .Modules.LambdaStr import LambdaStr

##__________________________________________________________________||
def Signal_Id(AllClass, AnyClass, datamc, **kargs):
    return LambdaStr("ev : ev.cutflowId[0] == 1 # 'Signal'", name = 'Signal_Id')

##__________________________________________________________________||
