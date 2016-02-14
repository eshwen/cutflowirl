# Tai Sakuma <tai.sakuma@cern.ch>

##__________________________________________________________________||
def FactoryDispatcher(level, **kargs):

    if isinstance(level, basestring):
        if 'lambdaStrDict' in kargs:
            if level in kargs['lambdaStrDict']:
                level = dict(factory = 'LambdaStrFromDictFactory', key = level)
        else:
            factoryName = level
            module = find_module(factoryName)
            factory = getattr(module, factoryName)
            return factory(**kargs)

    if not isinstance(level, dict):
        if isinstance(level[0], basestring) and isinstance(level[1], dict):
            key = level[0]
            if 'lambdaStrDict' in kargs:
                if key in kargs['lambdaStrDict']:
                    level = level[1].copy()
                    level.update(dict(factory = 'LambdaStrFromDictFactory', key = key))
            else:
                factoryName = level[0]
                module = find_module(factoryName)
                factory = getattr(module, factoryName)
                kargs_copy = kargs.copy()
                kargs_copy.update(level[1])
                return factory(**kargs_copy)

    if isinstance(level, dict):
        if 'factory' in level:
            level_copy = level.copy()
            factoryName = level_copy.pop('factory')
            module = find_module(factoryName)
            factory = getattr(module, factoryName)
            kargs_copy = kargs.copy()
            kargs_copy.update(level_copy)
            return factory(**kargs_copy)

        if not sum([k in level for k in ('All', 'Any', 'Not')]) <= 1:
            raise ValueError("Any pair of 'All', 'Any', 'Not' cannot be simultaneously given unless factory is given!")

        if 'All' in level:
            level_copy = level.copy()
            name = level_copy.pop('name', None)
            ret = kargs['AllClass'](name = name)
            levels = level_copy.pop('All')
            kargs_copy = kargs.copy()
            kargs_copy.update(level_copy)
            for level in levels:
                ret.add(FactoryDispatcher(level, **kargs_copy))
            return ret

        if 'Any' in level:
            level_copy = level.copy()
            name = level_copy.pop('name', None)
            ret = kargs['AnyClass'](name = name)
            levels = level_copy.pop('Any')
            kargs_copy = kargs.copy()
            kargs_copy.update(level_copy)
            for level in levels:
                ret.add(FactoryDispatcher(level, **kargs_copy))
            return ret

        if 'Not' in level:
            level_copy = level.copy()
            name = level_copy.pop('name', None)
            level = level_copy.pop('Not')
            kargs_copy = kargs.copy()
            kargs_copy.update(level_copy)
            return kargs['NotClass'](selection = FactoryDispatcher(level, **kargs_copy), name = name)

        raise ValueError("cannot recognize the level")

    # assum tuple or list
    if isinstance(level[0], basestring) and isinstance(level[1], dict):
        factoryName = level[0]
        module = find_module(factoryName)
        factory = getattr(module, factoryName)
        kargs_copy = kargs.copy()
        kargs_copy.update(level[1])
        return factory(**kargs_copy)

    raise ValueError("cannot recognize the level")

##__________________________________________________________________||
def find_module(name):
    import imp

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
