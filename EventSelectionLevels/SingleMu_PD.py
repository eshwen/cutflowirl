from .Modules.LambdaStr import LambdaStr
from .Modules.AlwaysTrue import AlwaysTrue

##__________________________________________________________________||
def SingleMu_PD(AllClass, AnyClass, datamc, **kargs):
    if not datamc == 'data': return AlwaysTrue(name = 'SingleMu_PD')
    return LambdaStr("ev : ev.PrimaryDataset[0] == 'SingleMuon'", name = 'SingleMu_PD')

##__________________________________________________________________||
