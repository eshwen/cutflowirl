# Tai Sakuma <tai.sakuma@cern.ch>
import copy

##__________________________________________________________________||
def FactoryDispatcher(path_cfg, **kargs):

    if not isinstance(path_cfg, dict):
        aliasDict = kargs['aliasDict'] if 'aliasDict' in kargs else None
        path_cfg = expand_path_cfg(path_cfg, aliasDict = aliasDict)

    if isinstance(path_cfg, dict):
        if 'factory' in path_cfg:
            path_cfg_copy = path_cfg.copy()
            factoryName = path_cfg_copy.pop('factory')
            factory = find_factory(factoryName)
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
def expand_path_cfg(path_cfg, overriding_kargs = dict(), aliasDict = None):

    if isinstance(path_cfg, basestring):
        if aliasDict is not None and path_cfg in aliasDict:
            new_overriding_kargs = dict(alias = path_cfg)
            new_overriding_kargs.update(overriding_kargs)
            return expand_path_cfg(aliasDict[path_cfg], new_overriding_kargs, aliasDict)

        ret = dict(factory = 'LambdaStrFactory', lambda_str = path_cfg)

        overriding_kargs_copy = overriding_kargs.copy()
        if 'alias' in overriding_kargs: ret['name'] = overriding_kargs_copy.pop('alias')
        if 'name' in overriding_kargs: ret['name'] = overriding_kargs_copy.pop('name')
        ret.update(overriding_kargs_copy)

        return ret

    if not isinstance(path_cfg, dict):
        # assume tuple or list
        if isinstance(path_cfg[0], basestring) and isinstance(path_cfg[1], dict):
            new_overriding_kargs = path_cfg[1].copy()
            new_overriding_kargs.update(overriding_kargs)
            return expand_path_cfg(path_cfg[0], overriding_kargs = new_overriding_kargs, aliasDict = aliasDict)

        raise ValueError("cannot recognize the path_cfg")

    if isinstance(path_cfg, dict):
        if 'factory' in path_cfg: return path_cfg

        if not sum([k in path_cfg for k in ('All', 'Any', 'Not')]) <= 1:
            raise ValueError("Any pair of 'All', 'Any', 'Not' cannot be simultaneously given unless factory is given!")

        if 'All' in path_cfg:
            new_path_cfg = path_cfg.copy()
            new_path_cfg['factory'] = 'AllFactory'
            new_path_cfg['path_cfg_list'] = new_path_cfg.pop('All')
            return new_path_cfg

        if 'Any' in path_cfg:
            new_path_cfg = path_cfg.copy()
            new_path_cfg['factory'] = 'AnyFactory'
            new_path_cfg['path_cfg_list'] = new_path_cfg.pop('Any')
            return new_path_cfg

        if 'Not' in path_cfg:
            new_path_cfg = path_cfg.copy()
            new_path_cfg['factory'] = 'NotFactory'
            new_path_cfg['path_cfg'] = new_path_cfg.pop('Not')
            return new_path_cfg

    raise ValueError("cannot recognize the path_cfg")

##__________________________________________________________________||
def find_factory(name):
    import imp

    top_module_name = 'EventSelectionLevels'
    f, filename, description = imp.find_module(top_module_name)
    top_module = imp.load_module(top_module_name, f, filename, description)
    ##______________________________________________________________||

    module_name = "{}.{}".format(top_module_name, name)
    # e.g., 'EventSelectionLevels.baseline_kinematics'

    f, filename, description = imp.find_module(name, top_module.__path__)
    module = imp.load_module(module_name, f, filename, description)

    factory = getattr(module, name)

    return factory

##__________________________________________________________________||
