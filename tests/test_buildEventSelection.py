from ..buildEventSelection import buildEventSelection
from ..EventSelectionLevels.Modules.EventSelectionAll import EventSelectionAll
import unittest

##__________________________________________________________________||
class Test_buildEventSelection(unittest.TestCase):

    def setUp(self):

        kargs = dict(
            arg1 = 10,
            arg2 = 20,
            levels = (
                ('test_level1', dict(arg2 = 2, arg3 = 3)),
                'test_level2',
            ))

        self.obj = buildEventSelection(**kargs)

    def test_obj(self):
        self.assertIsInstance(self.obj, EventSelectionAll)
        self.assertEqual('All', self.obj.name)
        self.assertEqual(2, len(self.obj.selections))

    def test_level1(self):
        level = self.obj.selections[0]
        self.assertEqual('test_level1', level.name)
        self.assertEqual({'arg1': 10, 'arg2': 2, 'arg3': 3}, level.kargs)

    def test_level2(self):
        level = self.obj.selections[1]
        self.assertEqual('test_level2', level.name)
        self.assertEqual({'arg1': 10, 'arg2': 20}, level.kargs)

##__________________________________________________________________||
