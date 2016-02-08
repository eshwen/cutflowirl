import imp

##__________________________________________________________________||
def AlternativeSequences(AllClass, AnyClass, name = 'AlternativeSequences', **kargs):

    ret = AnyClass(name = name)

    ##______________________________________________________________||
    top_module_name = 'EventSelectionModules'
    f, filename, description = imp.find_module(top_module_name)
    top_module = imp.load_module(top_module_name, f, filename, description)

    ##______________________________________________________________||
    kargs_for_sequence = kargs.copy()
    del kargs_for_sequence['sequences']

    ##______________________________________________________________||
    sequences = kargs['sequences']
    for sequence in sequences:
        if isinstance(sequence, basestring):
            sequence_name, options = sequence,  { }
        else:
            sequence_name, options = sequence

        sequence_args_0 = options['kargs'] if 'kargs' in options else { }
        sequence_args = kargs_for_sequence.copy()
        sequence_args.update(sequence_args_0)

        if 'levels' in options:
            selection = AllClass(name = sequence_name)
            ret.add(selection)

            levels = options['levels']
            for level in levels:
                if isinstance(level, basestring):
                    level_name, level_kargs_0 = level, { }
                else:
                    level_name, level_kargs_0 = level

                level_args = sequence_args.copy()
                level_args.update(level_kargs_0)

                module_name_base = "{}_{}".format(sequence_name, level_name)
                module_name = "{}.{}".format(top_module_name, module_name_base)
                f, filename, description = imp.find_module(module_name_base, top_module.__path__)
                module = imp.load_module(module_name, f, filename, description)
                func = getattr(module, module_name_base)
                selection_level = func(AllClass, AnyClass, **level_args)
                selection.add(selection_level)

        else:
            f, filename, description = imp.find_module(sequence_name, top_module.__path__)
            module = imp.load_module(sequence_name, f, filename, description)
            func = getattr(module, sequence_name)
            selection = func(AllClass, AnyClass, **sequence_args)
            ret.add(selection)

    return ret

##__________________________________________________________________||
