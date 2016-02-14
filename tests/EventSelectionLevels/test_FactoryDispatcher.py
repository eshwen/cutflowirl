from ...EventSelectionLevels.FactoryDispatcher import FactoryDispatcher
from ...EventSelectionLevels.Modules.EventSelectionAll import EventSelectionAll
from ...EventSelectionLevels.Modules.EventSelectionAny import EventSelectionAny
from ...EventSelectionLevels.Modules.EventSelectionNot import EventSelectionNot
import unittest
import copy

##__________________________________________________________________||
class Test_FactoryDispatcher(unittest.TestCase):

    def test_string(self):
        kargs = dict(arg1 = 10, arg2 = 20)
        level = 'test_level1'
        obj = FactoryDispatcher(level = level, **kargs)
        self.assertEqual('test_level1', obj.name)
        self.assertEqual({'arg1': 10, 'arg2': 20}, obj.kargs)

    def test_tuple(self):
        kargs = dict(arg1 = 10, arg2 = 20)
        level = ('test_level1', dict(arg2 = 2, arg3 = 3))
        level_org = copy.deepcopy(level)
        obj = FactoryDispatcher(level = level, **kargs)
        self.assertEqual(level_org, level)
        self.assertEqual('test_level1', obj.name)
        self.assertEqual({'arg1': 10, 'arg2': 2,'arg3': 3}, obj.kargs)

    def test_dict_factory(self):
        kargs = dict(arg1 = 10, arg2 = 20)
        level = dict(factory = 'test_level1')
        level_org = copy.deepcopy(level)
        obj = FactoryDispatcher(level = level, **kargs)
        self.assertEqual(level_org, level)
        self.assertEqual('test_level1', obj.name)
        self.assertEqual({'arg1': 10, 'arg2': 20}, obj.kargs)

    def test_dict_factory_with_args(self):
        kargs = dict(arg1 = 10, arg2 = 20)
        level = dict(factory = 'test_level1', arg2 = 2, arg3 = 3)
        level_org = copy.deepcopy(level)
        obj = FactoryDispatcher(level = level, **kargs)
        self.assertEqual(level_org, level)
        self.assertEqual('test_level1', obj.name)
        self.assertEqual({'arg1': 10, 'arg2': 2, 'arg3': 3}, obj.kargs)

    def test_dict_raise_multiple_All_Any_Not(self):
        kargs = dict(arg1 = 10, arg2 = 20)
        level = dict(All = (), Any = ())
        self.assertRaises(ValueError, FactoryDispatcher, level = level, **kargs)

        kargs = dict(arg1 = 10, arg2 = 20)
        level = dict(All = (), Not = ())
        self.assertRaises(ValueError, FactoryDispatcher, level = level, **kargs)

        kargs = dict(arg1 = 10, arg2 = 20)
        level = dict(Any = (), Not = ())
        self.assertRaises(ValueError, FactoryDispatcher, level = level, **kargs)

    def test_dict_raise_no_All_Any_Not(self):
        kargs = dict(arg1 = 10, arg2 = 20)
        level = dict()
        self.assertRaises(ValueError, FactoryDispatcher, level = level, **kargs)

    def test_dict_All(self):
        kargs = dict(
            arg1 = 10, arg2 = 20,
            AllClass = EventSelectionAll,
            AnyClass = EventSelectionAny
        )
        level = dict(All = ('test_level1', 'test_level2'), name = 'test_all', arg2 = 2, arg3 = 3)
        level_org = copy.deepcopy(level)
        obj = FactoryDispatcher(level = level, **kargs)
        self.assertEqual(level_org, level)
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
        level = dict(Any = ('test_level1', 'test_level2'), name = 'test_any', arg2 = 2, arg3 = 3)
        level_org = copy.deepcopy(level)
        obj = FactoryDispatcher(level = level, **kargs)
        self.assertEqual(level_org, level)
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
         level = dict(Not = 'test_level1', name = 'not_test_level1', arg2 = 2, arg3 = 3)
         level_org = copy.deepcopy(level)
         obj = FactoryDispatcher(level = level, **kargs)
         self.assertEqual(level_org, level)
         self.assertIsInstance(obj, EventSelectionNot)
         self.assertEqual('not_test_level1', obj.name)
         self.assertEqual('test_level1', obj.selection.name)
         self.assertEqual({'arg1': 10, 'arg2': 2, 'arg3': 3}, obj.selection.kargs)

##__________________________________________________________________||
