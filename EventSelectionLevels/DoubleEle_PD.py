from .Modules.LambdaStr import LambdaStr
from .Modules.AlwaysTrue import AlwaysTrue

##__________________________________________________________________||
def DoubleEle_PD(AllClass, AnyClass, datamc, **kargs):
    if not datamc == 'data': return AlwaysTrue(name = 'DoubleEle_PD')
    return LambdaStr("ev : ev.PrimaryDataset[0] == 'SingleElectron'", name = 'DoubleEle_PD')

##__________________________________________________________________||
