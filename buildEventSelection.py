# Tai Sakuma <tai.sakuma@cern.ch>
from .EventSelectionLevels.Modules.EventSelectionAll import EventSelectionAll
from .EventSelectionLevels.Modules.EventSelectionAny import EventSelectionAny
from .EventSelectionLevels.AllFactory import AllFactory

import os, sys

##__________________________________________________________________||
thisDir = os.path.dirname(os.path.realpath(__file__))
if not thisDir in sys.path: sys.path.append(thisDir)

##__________________________________________________________________||
def buildEventSelection(levels, name = 'All', AllClass = EventSelectionAll, AnyClass = EventSelectionAny, **kargs):
    return AllFactory(levels = levels, name = name, AllClass = AllClass, AnyClass = AnyClass, **kargs)

##__________________________________________________________________||
