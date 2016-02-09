from .Modules.LambdaStr import LambdaStr
from .Modules.AlwaysTrue import AlwaysTrue

##__________________________________________________________________||
def BaselineMu_PD(AllClass, AnyClass, datamc, **kargs):
    if not datamc == 'data': return AlwaysTrue(name = 'BaselineMu_PD')
    return LambdaStr("ev : ev.PrimaryDataset[0] == 'SingleMuon'", name = 'BaselineMu_PD')

##__________________________________________________________________||
