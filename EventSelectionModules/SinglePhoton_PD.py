from .LambdaStr import LambdaStr
from .AlwaysTrue import AlwaysTrue

##__________________________________________________________________||
def SinglePhoton_PD(AllClass, AnyClass, datamc, **kargs):
    if not datamc == 'data': return AlwaysTrue(name = 'SingleMu_PD')
    return LambdaStr("ev : ev.PrimaryDataset[0] == 'SinglePhoton'", name = 'SinglePhoton_PD')

##__________________________________________________________________||
