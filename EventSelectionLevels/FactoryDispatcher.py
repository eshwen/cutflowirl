# Tai Sakuma <tai.sakuma@cern.ch>

##__________________________________________________________________||
def FactoryDispatcher(path_cfg, **kargs):

    if isinstance(path_cfg, basestring):
        path_cfg = dict(factory = 'LambdaStrFromDictFactory', key = path_cfg)

    if not isinstance(path_cfg, dict):
        # assume tuple or list
        if isinstance(path_cfg[0], basestring) and isinstance(path_cfg[1], dict):
            key = path_cfg[0]
            path_cfg = path_cfg[1].copy()
            path_cfg.update(dict(factory = 'LambdaStrFromDictFactory', key = key))

    if isinstance(path_cfg, dict):
        if 'factory' in path_cfg:
            path_cfg_copy = path_cfg.copy()
            factoryName = path_cfg_copy.pop('factory')
            module = find_module(factoryName)
            factory = getattr(module, factoryName)
            kargs_copy = kargs.copy()
            kargs_copy.update(path_cfg_copy)
            return factory(**kargs_copy)

        if not sum([k in path_cfg for k in ('All', 'Any', 'Not')]) <= 1:
            raise ValueError("Any pair of 'All', 'Any', 'Not' cannot be simultaneously given unless factory is given!")

        if 'All' in path_cfg:
            path_cfg_copy = path_cfg.copy()
            name = path_cfg_copy.pop('name', None)
            ret = kargs['AllClass'](name = name)
            path_cfgs = path_cfg_copy.pop('All')
            kargs_copy = kargs.copy()
            kargs_copy.update(path_cfg_copy)
            for path_cfg in path_cfgs:
                ret.add(FactoryDispatcher(path_cfg, **kargs_copy))
            return ret

        if 'Any' in path_cfg:
            path_cfg_copy = path_cfg.copy()
            name = path_cfg_copy.pop('name', None)
            ret = kargs['AnyClass'](name = name)
            path_cfgs = path_cfg_copy.pop('Any')
            kargs_copy = kargs.copy()
            kargs_copy.update(path_cfg_copy)
            for path_cfg in path_cfgs:
                ret.add(FactoryDispatcher(path_cfg, **kargs_copy))
            return ret

        if 'Not' in path_cfg:
            path_cfg_copy = path_cfg.copy()
            name = path_cfg_copy.pop('name', None)
            path_cfg = path_cfg_copy.pop('Not')
            kargs_copy = kargs.copy()
            kargs_copy.update(path_cfg_copy)
            return kargs['NotClass'](selection = FactoryDispatcher(path_cfg, **kargs_copy), name = name)

        raise ValueError("cannot recognize the path_cfg")

    raise ValueError("cannot recognize the path_cfg")

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
