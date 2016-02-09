from .Modules.LambdaStr import LambdaStr
from .Modules.AlwaysTrue import AlwaysTrue

##__________________________________________________________________||
def Signal_PD(AllClass, AnyClass, datamc, **kargs):
    if not datamc == 'data': return AlwaysTrue(name = 'Signal_PD')
    return LambdaStr("ev : ev.PrimaryDataset[0] in ('MET', 'HTMHT', 'JetHT')", name = 'Signal_PD')

##__________________________________________________________________||
