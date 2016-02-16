from ...EventSelectionLevels.FactoryDispatcher import FactoryDispatcher
from ...EventSelectionLevels.FactoryDispatcher import expand_path_cfg
from ...EventSelectionLevels.Modules.EventSelectionAll import EventSelectionAll
from ...EventSelectionLevels.Modules.EventSelectionAny import EventSelectionAny
from ...EventSelectionLevels.Modules.EventSelectionNot import EventSelectionNot
from ...EventSelectionLevels.Modules.LambdaStr import LambdaStr
import unittest
import copy

##__________________________________________________________________||
class Test_FactoryDispatcher(unittest.TestCase):

    def setUp(self):
        self.aliasDict = {
            'JSON': "ev : ev.inCertifiedLumiSections[0]",
            'nMuonsIsolated': 'ev : ev.nMuonsIsolated[0] == {n}'
        }

    def test_string(self):
        kargs = dict(arg1 = 10, arg2 = 20,
                     aliasDict = self.aliasDict,
                     LambdaStrClass = LambdaStr)
        path_cfg = 'JSON'
        obj = FactoryDispatcher(path_cfg = path_cfg, **kargs)
        self.assertIsInstance(obj, LambdaStr)
        self.assertEqual('JSON', obj.name)
        self.assertEqual('ev : ev.inCertifiedLumiSections[0]', obj.lambda_str)

    def test_tuple(self):
        kargs = dict(arg1 = 10, arg2 = 20,
                     aliasDict = self.aliasDict,
                     LambdaStrClass = LambdaStr)
        path_cfg = ('nMuonsIsolated', dict(n = 1))
        obj = FactoryDispatcher(path_cfg = path_cfg, **kargs)
        self.assertIsInstance(obj, LambdaStr)
        self.assertEqual('nMuonsIsolated', obj.name)
        self.assertEqual('ev : ev.nMuonsIsolated[0] == 1', obj.lambda_str)

    def test_dict_factory(self):
        kargs = dict(arg1 = 10, arg2 = 20)
        path_cfg = dict(factory = 'test_level1')
        path_cfg_org = copy.deepcopy(path_cfg)
        obj = FactoryDispatcher(path_cfg = path_cfg, **kargs)
        self.assertEqual(path_cfg_org, path_cfg)
        self.assertEqual('test_level1', obj.name)
        self.assertEqual({'arg1': 10, 'arg2': 20}, obj.kargs)

    def test_dict_factory_with_args(self):
        kargs = dict(arg1 = 10, arg2 = 20)
        path_cfg = dict(factory = 'test_level1', arg2 = 2, arg3 = 3)
        path_cfg_org = copy.deepcopy(path_cfg)
        obj = FactoryDispatcher(path_cfg = path_cfg, **kargs)
        self.assertEqual(path_cfg_org, path_cfg)
        self.assertEqual('test_level1', obj.name)
        self.assertEqual({'arg1': 10, 'arg2': 2, 'arg3': 3}, obj.kargs)

    def test_dict_raise_multiple_All_Any_Not(self):
        kargs = dict(arg1 = 10, arg2 = 20)
        path_cfg = dict(All = (), Any = ())
        self.assertRaises(ValueError, FactoryDispatcher, path_cfg = path_cfg, **kargs)

        kargs = dict(arg1 = 10, arg2 = 20)
        path_cfg = dict(All = (), Not = ())
        self.assertRaises(ValueError, FactoryDispatcher, path_cfg = path_cfg, **kargs)

        kargs = dict(arg1 = 10, arg2 = 20)
        path_cfg = dict(Any = (), Not = ())
        self.assertRaises(ValueError, FactoryDispatcher, path_cfg = path_cfg, **kargs)

    def test_dict_raise_no_All_Any_Not(self):
        kargs = dict(arg1 = 10, arg2 = 20)
        path_cfg = dict()
        self.assertRaises(ValueError, FactoryDispatcher, path_cfg = path_cfg, **kargs)

    def test_dict_All(self):
        kargs = dict(
            arg1 = 10, arg2 = 20,
            AllClass = EventSelectionAll,
            AnyClass = EventSelectionAny
        )
        path_cfg = dict(All = (dict(factory = 'test_level1'), dict(factory = 'test_level2')), name = 'test_all', arg2 = 2, arg3 = 3)
        path_cfg_org = copy.deepcopy(path_cfg)
        obj = FactoryDispatcher(path_cfg = path_cfg, **kargs)
        self.assertEqual(path_cfg_org, path_cfg)
        self.assertIsInstance(obj, EventSelectionAll)
        self.assertEqual('test_all', obj.name)
        self.assertEqual(2, len(obj.selections))
        self.assertEqual('test_level1', obj.selections[0].name)
        self.assertEqual({'arg1': 10, 'arg2': 2, 'arg3': 3}, obj.selections[0].kargs)
        self.assertEqual('test_level2', obj.selections[1].name)
        self.assertEqual({'arg1': 10, 'arg2': 2, 'arg3': 3}, obj.selections[1].kargs)

    def test_dict_Any(self):
        kargs = dict(
            arg1 = 10, arg2 = 20,
            AllClass = EventSelectionAll,
            AnyClass = EventSelectionAny,
        )
        path_cfg = dict(Any = (dict(factory = 'test_level1'), dict(factory = 'test_level2')), name = 'test_any', arg2 = 2, arg3 = 3)
        path_cfg_org = copy.deepcopy(path_cfg)
        obj = FactoryDispatcher(path_cfg = path_cfg, **kargs)
        self.assertEqual(path_cfg_org, path_cfg)
        self.assertIsInstance(obj, EventSelectionAny)
        self.assertEqual('test_any', obj.name)
        self.assertEqual(2, len(obj.selections))
        self.assertEqual('test_level1', obj.selections[0].name)
        self.assertEqual({'arg1': 10, 'arg2': 2, 'arg3': 3}, obj.selections[0].kargs)
        self.assertEqual('test_level2', obj.selections[1].name)
        self.assertEqual({'arg1': 10, 'arg2': 2, 'arg3': 3}, obj.selections[1].kargs)

    def test_dict_Not(self):
         kargs = dict(
             arg1 = 10, arg2 = 20,
             AllClass = EventSelectionAll,
             AnyClass = EventSelectionAny,
             NotClass = EventSelectionNot,
         )
         path_cfg = dict(Not = dict(factory = 'test_level1'), name = 'not_test_level1', arg2 = 2, arg3 = 3)
         path_cfg_org = copy.deepcopy(path_cfg)
         obj = FactoryDispatcher(path_cfg = path_cfg, **kargs)
         self.assertEqual(path_cfg_org, path_cfg)
         self.assertIsInstance(obj, EventSelectionNot)
         self.assertEqual('not_test_level1', obj.name)
         self.assertEqual('test_level1', obj.selection.name)
         self.assertEqual({'arg1': 10, 'arg2': 2, 'arg3': 3}, obj.selection.kargs)

##__________________________________________________________________||
class Test_expand_path_cfg(unittest.TestCase):

    def setUp(self):
        self.aliasDict = {
            'alias1': 'ev : ev.var1[0] >= 10',
            'alias2': ('ev : ev.var2[0] >= 20', dict(name = 'name2')),
            'alias3': 'alias1',
            'alias4': 'alias3',
            'alias5': 'ev : ev.var4[0] == {n}',
            'alias6': ('ev : {low} <= ev.var5[0] < {high}', dict(low = 11, high = 20))
        }

    def test_alias1(self):

        extra_args = dict(arg1 = 10, arg2 = 20)
        kargs = dict(aliasDict = self.aliasDict)
        kargs.update(extra_args)

        path_cfg = 'alias1'

        actual = expand_path_cfg(path_cfg = path_cfg, **kargs)

        expected = dict(
            factory = 'LambdaStrFactory',
            lambda_str = 'ev : ev.var1[0] >= 10',
            name = 'alias1'
        )

        self.assertEqual(expected, actual)

    def test_alias1_with_name(self):

        extra_args = dict(arg1 = 10, arg2 = 20)
        kargs = dict(aliasDict = self.aliasDict)
        kargs.update(extra_args)

        path_cfg = ('alias1', dict(name = 'name1'))

        actual = expand_path_cfg(path_cfg = path_cfg, **kargs)

        expected = dict(
            factory = 'LambdaStrFactory',
            lambda_str = 'ev : ev.var1[0] >= 10',
            name = 'name1'
        )

        self.assertEqual(expected, actual)

    def test_alias2(self):

        extra_args = dict(arg1 = 10, arg2 = 20)
        kargs = dict(aliasDict = self.aliasDict)
        kargs.update(extra_args)

        path_cfg = 'alias2'

        actual = expand_path_cfg(path_cfg = path_cfg, **kargs)

        expected = dict(
            factory = 'LambdaStrFactory',
            lambda_str = 'ev : ev.var2[0] >= 20',
            name = 'name2' #  name has priority over alias
        )

        self.assertEqual(expected, actual)

    def test_alias2_with_name(self):

        extra_args = dict(arg1 = 10, arg2 = 20)
        kargs = dict(aliasDict = self.aliasDict)
        kargs.update(extra_args)

        path_cfg = ('alias2', dict(name = 'new_name2'))

        actual = expand_path_cfg(path_cfg = path_cfg, **kargs)

        expected = dict(
            factory = 'LambdaStrFactory',
            lambda_str = 'ev : ev.var2[0] >= 20',
            name = 'new_name2' # name can be overridden
        )

        self.assertEqual(expected, actual)

    def test_alias3(self):

        extra_args = dict(arg1 = 10, arg2 = 20)
        kargs = dict(aliasDict = self.aliasDict)
        kargs.update(extra_args)

        path_cfg = 'alias3'

        actual = expand_path_cfg(path_cfg = path_cfg, **kargs)

        expected = dict(
            factory = 'LambdaStrFactory',
            lambda_str = 'ev : ev.var1[0] >= 10',
            name = 'alias3' # the outermost alias has priority
        )

        self.assertEqual(expected, actual)

    def test_alias4(self):

        extra_args = dict(arg1 = 10, arg2 = 20)
        kargs = dict(aliasDict = self.aliasDict)
        kargs.update(extra_args)

        path_cfg = 'alias4'

        actual = expand_path_cfg(path_cfg = path_cfg, **kargs)

        expected = dict(
            factory = 'LambdaStrFactory',
            lambda_str = 'ev : ev.var1[0] >= 10',
            name = 'alias4' # the outermost alias has priority
        )

        self.assertEqual(expected, actual)

    def test_alias5(self):

        extra_args = dict(arg1 = 10, arg2 = 20)
        kargs = dict(aliasDict = self.aliasDict)
        kargs.update(extra_args)

        path_cfg = ('alias5', dict(n = 30))

        actual = expand_path_cfg(path_cfg = path_cfg, **kargs)

        expected = dict(
            factory = 'LambdaStrFactory',
            lambda_str = 'ev : ev.var4[0] == 30',
            name = 'alias5'
        )

        self.assertEqual(expected, actual)

    def test_alias6(self):

        extra_args = dict(arg1 = 10, arg2 = 20)
        kargs = dict(aliasDict = self.aliasDict)
        kargs.update(extra_args)

        path_cfg = 'alias6'

        actual = expand_path_cfg(path_cfg = path_cfg, **kargs)

        expected = dict(
            factory = 'LambdaStrFactory',
            lambda_str = 'ev : 11 <= ev.var5[0] < 20',
            name = 'alias6'
        )

        self.assertEqual(expected, actual)

    def test_alias6_with_option(self):

        extra_args = dict(arg1 = 10, arg2 = 20)
        kargs = dict(aliasDict = self.aliasDict)
        kargs.update(extra_args)

        path_cfg = ('alias6', dict(high = 30))

        actual = expand_path_cfg(path_cfg = path_cfg, **kargs)

        expected = dict(
            factory = 'LambdaStrFactory',
            lambda_str = 'ev : 11 <= ev.var5[0] < 30',
            name = 'alias6'
        )

        self.assertEqual(expected, actual)

    def test_string_lambda_str(self):

        extra_args = dict(arg1 = 10, arg2 = 20)
        kargs = dict(aliasDict = self.aliasDict)
        kargs.update(extra_args)

        path_cfg = 'ev : ev.nJets >= 2'

        actual = expand_path_cfg(path_cfg = path_cfg, **kargs)

        expected = dict(
            factory = 'LambdaStrFactory',
            lambda_str = 'ev : ev.nJets >= 2',
        )

        self.assertEqual(expected, actual)

    def test_string_lambda_str_format(self):

        extra_args = dict(arg1 = 10, arg2 = 20)
        kargs = dict(aliasDict = self.aliasDict)
        kargs.update(extra_args)

        path_cfg = 'ev : ev.nJets >= {n}'

        actual = expand_path_cfg(path_cfg = path_cfg, n = 2, **kargs)

        expected = dict(
            factory = 'LambdaStrFactory',
            lambda_str = 'ev : ev.nJets >= 2',
        )

        self.assertEqual(expected, actual)

##__________________________________________________________________||
