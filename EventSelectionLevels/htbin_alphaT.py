from .FactoryDispatcher import FactoryDispatcher
import copy

##__________________________________________________________________||
def htbin_alphaT(AllClass, AnyClass, **kargs):

    kargs_copy = copy.deepcopy(kargs)

    lambdaStrDict = {
        'htbin_200': "ev : ev.htbin[0] == 200",
        'htbin_250': "ev : ev.htbin[0] == 250",
        'htbin_300': "ev : ev.htbin[0] == 300",
        'htbin_350': "ev : ev.htbin[0] == 350",
        'htbin_400': "ev : ev.htbin[0] == 400",
        'htbin_600': "ev : ev.htbin[0] == 600",
        'htbin_800': "ev : ev.htbin[0] == 800",
        'alphaT': "ev : {v} <= ev.alphaT[0]",
    }

    kargs_copy['lambdaStrDict'].update(lambdaStrDict)

    level = dict(
        Any = (dict(All = ('htbin_200', ('alphaT', dict(v = 0.65)))),
               dict(All = ('htbin_250', ('alphaT', dict(v = 0.60)))),
               dict(All = ('htbin_300', ('alphaT', dict(v = 0.55)))),
               dict(All = ('htbin_350', ('alphaT', dict(v = 0.53)))),
               dict(All = ('htbin_400', ('alphaT', dict(v = 0.52)))),
               dict(All = ('htbin_600', ('alphaT', dict(v = 0.52)))),
               dict(All = ('htbin_800', ))
        )
    )

    return FactoryDispatcher(
        AllClass = AllClass, AnyClass = AnyClass,
        level = level, **kargs_copy)


##__________________________________________________________________||
