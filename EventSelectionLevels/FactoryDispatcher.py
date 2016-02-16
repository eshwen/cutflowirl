# Tai Sakuma <tai.sakuma@cern.ch>
import copy

##__________________________________________________________________||
def FactoryDispatcher(path_cfg, **kargs):

    if not isinstance(path_cfg, dict):
        path_cfg = expand_path_cfg(path_cfg, **kargs)

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
def expand_path_cfg(path_cfg, **kargs):

    if isinstance(path_cfg, dict): return path_cfg

    if isinstance(path_cfg, basestring):
        if 'aliasDict' in kargs and path_cfg in kargs['aliasDict']:
            kargs_copy = copy.deepcopy(kargs)
            kargs_copy.update(alias = path_cfg)
            return expand_path_cfg(kargs['aliasDict'][path_cfg], **kargs_copy)
        lambda_str = path_cfg.format(**kargs)
        ret = dict(factory = 'LambdaStrFactory', lambda_str = lambda_str)
        if 'alias' in kargs: ret['name'] = kargs['alias'] 
        if 'name' in kargs: ret['name'] = kargs['name'] 
        return ret

    # assume tuple or list
    if isinstance(path_cfg[0], basestring) and isinstance(path_cfg[1], dict):
        kargs_copy = copy.deepcopy(kargs)
        kargs_copy.update(path_cfg[1])
        return expand_path_cfg(path_cfg[0], **kargs_copy)

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
