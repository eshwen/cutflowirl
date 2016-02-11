from .Modules.LambdaStr import LambdaStr
from .Modules.AlwaysTrue import AlwaysTrue

##__________________________________________________________________||
def PD_MET(AllClass, AnyClass, datamc, **kargs):
    if not datamc == 'data': return AlwaysTrue()
    return LambdaStr("ev : ev.PrimaryDataset[0] == 'MET'", name = 'PD_MET')

##__________________________________________________________________||
