from .FactoryDispatcher import FactoryDispatcher

##__________________________________________________________________||
def baseline_kinematics_loose_JECvariation(**kargs):
    level = dict(name = 'baseline_kinematics_loose_JECvariation',
                 All = (dict(factory = 'LambdaStrFactory', lambda_str = "ev : ev.nJet100JECUp[0] >= 1", name = 'nJet100_JECvar'),
                        dict(factory = 'LambdaStrFactory', lambda_str = "ev : ev.ht40JECUp[0] >= 150", name = 'ht40_loose_JECvar'),
                 )
                )
    return FactoryDispatcher(level = level, **kargs)

##__________________________________________________________________||
