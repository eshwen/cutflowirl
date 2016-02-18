# Tai Sakuma <tai.sakuma@cern.ch>
from .EventSelectionModules.EventSelectionAll import EventSelectionAll
from .EventSelectionModules.EventSelectionAny import EventSelectionAny
from .EventSelectionModules.EventSelectionNot import EventSelectionNot
from .EventSelectionModules.LambdaStr import LambdaStr
from .EventSelectionFactories.FactoryDispatcher import FactoryDispatcher
from .eventSelectionAliasDict import eventSelectionAliasDict

import os, sys

##__________________________________________________________________||
thisDir = os.path.dirname(os.path.realpath(__file__))
if not thisDir in sys.path: sys.path.append(thisDir)

##__________________________________________________________________||
def buildEventSelection(**kargs):

    if 'aliasDict' not in kargs: kargs['aliasDict'] = eventSelectionAliasDict

    return FactoryDispatcher(
        AllClass = EventSelectionAll,
        AnyClass = EventSelectionAny,
        NotClass = EventSelectionNot,
        LambdaStrClass = LambdaStr,
        **kargs)

##__________________________________________________________________||
