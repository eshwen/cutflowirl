from .EventSelectionModules.EventSelectionAll import EventSelectionAll
from .EventSelectionModules.EventSelectionAny import EventSelectionAny

import imp
import os, sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

##__________________________________________________________________||
def buildEventSelection(levels, AllClass = EventSelectionAll, AnyClass = EventSelectionAny, **kargs):
    """
    """

    ##______________________________________________________________||
    eventSelection = AllClass(name = 'All')

    ##______________________________________________________________||
    top_module_name = 'EventSelectionModules'
    f, filename, description = imp.find_module(top_module_name)
    top_module = imp.load_module(top_module_name, f, filename, description)

    ##______________________________________________________________||
    for level in levels:
        if isinstance(level, basestring):
            level_name, level_kargs_0 = level, { }
        else:
            level_name, level_kargs_0 = level

        # e.g., level_name = 'baseline_kinematics'
        #       level_kargs_0 = {'arg1': 1, 'arg2': 2}

        level_kargs = kargs.copy()
        level_kargs.update(level_kargs_0)
        # e.g., level_args = {'arg1': 1, 'arg2': 2, 'datamc': 'data'}

        module_name = "{}.{}".format(top_module_name, level_name)
        # e.g., 'EventSelectionModules.baseline_kinematics'

        f, filename, description = imp.find_module(level_name, top_module.__path__)

        module = imp.load_module(module_name, f, filename, description)

        func = getattr(module, level_name)

        selection = func(AllClass, AnyClass, **level_kargs)

        eventSelection.add(selection)
    
    ##______________________________________________________________||
    return eventSelection

##__________________________________________________________________||
