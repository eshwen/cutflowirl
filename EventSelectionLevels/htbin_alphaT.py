from .FactoryDispatcher import FactoryDispatcher

##__________________________________________________________________||
def htbin_alphaT(AllClass, AnyClass, **kargs):

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
        level = level, **kargs)


##__________________________________________________________________||
