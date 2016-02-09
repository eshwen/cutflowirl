from .Modules.LambdaStr import LambdaStr
from .Modules.AlwaysTrue import AlwaysTrue

##__________________________________________________________________||
def SingleEle_PD(AllClass, AnyClass, datamc, **kargs):
    if not datamc == 'data': return AlwaysTrue(name = 'SingleEle_PD')
    return LambdaStr("ev : ev.PrimaryDataset[0] == 'SingleElectron'", name = 'SingleEle_PD')

##__________________________________________________________________||
