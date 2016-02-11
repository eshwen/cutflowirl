from .Modules.LambdaStr import LambdaStr
from .Modules.AlwaysTrue import AlwaysTrue

##__________________________________________________________________||
def PD_SinglePhoton(AllClass, AnyClass, datamc, **kargs):
    if not datamc == 'data': return AlwaysTrue()
    return LambdaStr("ev : ev.PrimaryDataset[0] == 'SinglePhoton'", name = 'PD_SinglePhoton')

##__________________________________________________________________||
