# Tai Sakuma <tai.sakuma@cern.ch>
from .Modules.EventSelectionNot import EventSelectionNot
import imp

##__________________________________________________________________||
def Not(AllClass, AnyClass, level, name = 'Not', **kargs):

    if isinstance(level, basestring):
        level_name, level_kargs_0 = level, { }
    else:
        level_name, level_kargs_0 = level

    ##______________________________________________________________||
    kargs_for_level = kargs.copy()
    kargs_for_level.update(level_kargs_0)

    ##______________________________________________________________||
    top_module_name = 'EventSelectionLevels'
    f, filename, description = imp.find_module(top_module_name)
    top_module = imp.load_module(top_module_name, f, filename, description)

    module_name = "{}.{}".format(top_module_name, level_name)
    f, filename, description = imp.find_module(level_name, top_module.__path__)
    module = imp.load_module(module_name, f, filename, description)
    func = getattr(module, level_name)
    selection_level = func(AllClass, AnyClass, **kargs_for_level)

    return EventSelectionNot(selection_level, name)

##__________________________________________________________________||
