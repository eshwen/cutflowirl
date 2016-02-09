from .Modules.LambdaStr import LambdaStr
from .Modules.AlwaysTrue import AlwaysTrue

##__________________________________________________________________||
def DoubleMu_PD(AllClass, AnyClass, datamc, **kargs):
    if not datamc == 'data': return AlwaysTrue(name = 'DoubleMu_PD')
    return LambdaStr("ev : ev.PrimaryDataset[0] == 'SingleMuon'", name = 'DoubleMu_PD')

##__________________________________________________________________||
