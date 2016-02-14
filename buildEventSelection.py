# Tai Sakuma <tai.sakuma@cern.ch>
from .EventSelectionLevels.Modules.EventSelectionAll import EventSelectionAll
from .EventSelectionLevels.Modules.EventSelectionAny import EventSelectionAny
from .EventSelectionLevels.Modules.EventSelectionNot import EventSelectionNot
from .EventSelectionLevels.Modules.LambdaStr import LambdaStr
from .EventSelectionLevels.AllFactory import AllFactory
from .EventSelectionLevels.FactoryDispatcher import FactoryDispatcher

import os, sys

##__________________________________________________________________||
thisDir = os.path.dirname(os.path.realpath(__file__))
if not thisDir in sys.path: sys.path.append(thisDir)

##__________________________________________________________________||
## def buildEventSelection(levels, name = 'All', AllClass = EventSelectionAll, AnyClass = EventSelectionAny, **kargs):
##    return AllFactory(levels = levels, name = name, AllClass = AllClass, AnyClass = AnyClass, **kargs)

##__________________________________________________________________||
def buildEventSelection(**kargs):
    return FactoryDispatcher(
        AllClass = EventSelectionAll,
        AnyClass = EventSelectionAny,
        NotClass = EventSelectionNot,
        LambdaStrClass = LambdaStr,
        **kargs)

##__________________________________________________________________||
