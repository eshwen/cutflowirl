from ...EventSelectionLevels.FactoryDispatcher import FactoryDispatcher
from ...EventSelectionLevels.Modules.EventSelectionAll import EventSelectionAll
from ...EventSelectionLevels.Modules.EventSelectionAny import EventSelectionAny
from ...EventSelectionLevels.Modules.EventSelectionNot import EventSelectionNot
from ...EventSelectionLevels.Modules.LambdaStr import LambdaStr
import unittest
import copy

##__________________________________________________________________||
class Test_FactoryDispatcher(unittest.TestCase):

    def setUp(self):
        self.lambdaStrDict = {
            'JSON': "ev : ev.inCertifiedLumiSections[0]",
            'nMuonsIsolated': 'ev : ev.nMuonsIsolated[0] == {n}'
        }

    def test_string(self):
        kargs = dict(arg1 = 10, arg2 = 20,
                     lambdaStrDict = self.lambdaStrDict,
                     LambdaStrClass = LambdaStr)
        path_cfg = 'JSON'
        obj = FactoryDispatcher(path_cfg = path_cfg, **kargs)
        self.assertIsInstance(obj, LambdaStr)
        self.assertEqual('JSON', obj.name)
        self.assertEqual('ev : ev.inCertifiedLumiSections[0]', obj.lambda_str)

    def test_tuple(self):
        kargs = dict(arg1 = 10, arg2 = 20,
                     lambdaStrDict = self.lambdaStrDict,
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
