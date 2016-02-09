import imp

##__________________________________________________________________||
def cutflows(AllClass, AnyClass, **kargs):

    ret = AnyClass(name = 'cutflows')

    ##______________________________________________________________||
    top_module_name = 'EventSelectionLevels'
    f, filename, description = imp.find_module(top_module_name)
    top_module = imp.load_module(top_module_name, f, filename, description)

    ##______________________________________________________________||
    kargs_for_cutflow = kargs.copy()
    del kargs_for_cutflow['cutflows']

    ##______________________________________________________________||
    cutflows = kargs['cutflows']
    for cutflow in cutflows:
        if isinstance(cutflow, basestring):
            cutflow_name, options = cutflow,  { }
        else:
            cutflow_name, options = cutflow

        cutflow_args_0 = options['kargs'] if 'kargs' in options else { }
        cutflow_args = kargs_for_cutflow.copy()
        cutflow_args.update(cutflow_args_0)

        if 'levels' in options:
            selection = AllClass(name = cutflow_name)
            ret.add(selection)

            levels = options['levels']
            for level in levels:
                if isinstance(level, basestring):
                    level_name, level_kargs_0 = level, { }
                else:
                    level_name, level_kargs_0 = level

                level_args = cutflow_args.copy()
                level_args.update(level_kargs_0)

                module_name_base = "{}_{}".format(cutflow_name, level_name)
                module_name = "{}.{}".format(top_module_name, module_name_base)
                f, filename, description = imp.find_module(module_name_base, top_module.__path__)
                module = imp.load_module(module_name, f, filename, description)
                func = getattr(module, module_name_base)
                selection_level = func(AllClass, AnyClass, **level_args)
                selection.add(selection_level)

        else:
            f, filename, description = imp.find_module(cutflow_name, top_module.__path__)
            module = imp.load_module(cutflow_name, f, filename, description)
            func = getattr(module, cutflow_name)
            selection = func(AllClass, AnyClass, **cutflow_args)
            ret.add(selection)

    return ret

##__________________________________________________________________||
