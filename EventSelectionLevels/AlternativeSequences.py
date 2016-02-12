# Tai Sakuma <tai.sakuma@cern.ch>
import imp
from .AllFactory import AllFactory

##__________________________________________________________________||
def AlternativeSequences(AllClass, AnyClass, levels, name = 'AlternativeSequences', **kargs):

    ret = AnyClass(name = name)

    for level in levels:

        level_args = kargs.copy()
        level_args.update(level)

        if 'name' not in level_args: level_args['name'] = None

        ret.add(AllFactory(AllClass = AllClass, AnyClass = AnyClass, **level_args))

    return ret

##__________________________________________________________________||
