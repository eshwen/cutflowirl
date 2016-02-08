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

        sequence_args_0 = sequence['kargs'] if 'kargs' in sequence else { }
        sequence_args = kargs_for_sequence.copy()
        sequence_args.update(sequence_args_0)

        sequence_name = sequence['name'] if 'name' in sequence else None

        selection = AllClass(name = sequence_name)
        ret.add(selection)

        if not 'levels' in sequence: continue

        levels = sequence['levels']
        for level in levels:
            if isinstance(level, basestring):
                level_name, level_kargs_0 = level, { }
            else:
                level_name, level_kargs_0 = level

            level_args = sequence_args.copy()
            level_args.update(level_kargs_0)

            module_name = "{}.{}".format(top_module_name, level_name)
            f, filename, description = imp.find_module(level_name, top_module.__path__)
            module = imp.load_module(module_name, f, filename, description)
            func = getattr(module, level_name)
            selection_level = func(AllClass, AnyClass, **level_args)
            selection.add(selection_level)

    return ret

##__________________________________________________________________||
