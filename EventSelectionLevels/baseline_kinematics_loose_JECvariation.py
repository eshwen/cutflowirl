from .FactoryDispatcher import FactoryDispatcher

##__________________________________________________________________||
def baseline_kinematics_loose_JECvariation(**kargs):
    lambdaStrDict = {
        'nJet100_JECvar' : 'ev : ev.nJet100JECUp[0] >= 1',
        'ht40_loose_JECvar' : 'ev : ev.ht40JECUp[0] >= 150',
    }

    level = dict(name = 'baseline_kinematics_loose_JECvariation',
                 lambdaStrDict = lambdaStrDict,
                 All = (dict(factory = 'LambdaStrFromDictFactory', key = 'nJet100_JECvar'),
                        dict(factory = 'LambdaStrFromDictFactory', key = 'ht40_loose_JECvar'),
                 )
                )
    return FactoryDispatcher(level = level, **kargs)

##__________________________________________________________________||
