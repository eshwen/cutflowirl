from .LambdaStr import LambdaStr

##__________________________________________________________________||
def met_filters(AllClass, AnyClass, datamc, **kargs):

    ret = AllClass(name = 'met_filters')

    ret.add(LambdaStr("ev : ev.Flag_goodVertices[0] == 1", name = 'goodVertex'))
    ret.add(LambdaStr("ev : ev.Flag_CSCTightHaloFilter[0] ==1", name = 'CSCTightHaloFilter'))
    ret.add(LambdaStr("ev : ev.Flag_eeBadScFilter[0] ==1", name = 'eeBadScFilter'))
    ret.add(LambdaStr("ev : ev.Flag_HBHENoiseFilter[0] == 1", name = 'HBHENoiseFilter'))
    if datamc == 'data':
        ret.add(LambdaStr("ev : ev.Flag_HBHENoiseIsoFilter[0] == 1", name = 'HBHENoiseIsoFilter'))

    return ret

##__________________________________________________________________||
