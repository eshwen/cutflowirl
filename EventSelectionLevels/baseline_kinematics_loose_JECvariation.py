from .FactoryDispatcher import FactoryDispatcher

##__________________________________________________________________||
def baseline_kinematics_loose_JECvariation(**kargs):
    level = dict(name = 'baseline_kinematics_loose_JECvariation',
                 All = (dict(factory = 'LambdaStrFromDictFactory', key = 'nJet100_JECvar'),
                        dict(factory = 'LambdaStrFromDictFactory', key = 'ht40_loose_JECvar'),
                 )
                )
    return FactoryDispatcher(level = level, **kargs)

##__________________________________________________________________||
