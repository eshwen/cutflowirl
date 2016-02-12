# Tai Sakuma <tai.sakuma@cern.ch>
import imp

##__________________________________________________________________||
def AllFactory(AllClass, AnyClass, levels, name = None, **kargs):

    ret = AllClass(name = name)

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

        module = find_module(level_name)

        func = getattr(module, level_name)

        selection = func(AllClass, AnyClass, **level_kargs)

        ret.add(selection)

    return ret

##__________________________________________________________________||
def find_module(name):

    top_module_name = 'EventSelectionLevels'
    f, filename, description = imp.find_module(top_module_name)
    top_module = imp.load_module(top_module_name, f, filename, description)
    ##______________________________________________________________||

    module_name = "{}.{}".format(top_module_name, name)
    # e.g., 'EventSelectionLevels.baseline_kinematics'

    f, filename, description = imp.find_module(name, top_module.__path__)
    module = imp.load_module(module_name, f, filename, description)

    return module

##__________________________________________________________________||
