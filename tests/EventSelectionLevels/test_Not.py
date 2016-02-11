# Tai Sakuma <tai.sakuma@cern.ch>
from ...EventSelectionLevels.Not import Not
from ...EventSelectionLevels.Modules.EventSelectionAll import EventSelectionAll
from ...EventSelectionLevels.Modules.EventSelectionAny import EventSelectionAny
from ...EventSelectionLevels.Modules.EventSelectionNot import EventSelectionNot
from ...EventSelectionLevels.Modules.LambdaStr import LambdaStr
from ...event_selection_str import event_selection_str
import unittest

##__________________________________________________________________||
class Test_Not(unittest.TestCase):

    def test_one(self):

        kargs = dict(
            name = 'test_not',
            arg1 = 10,
            arg2 = 20,
            level = ('test_cutflow1_level1', dict(arg2 = 2, arg3 = 3))
            )

        obj = Not(EventSelectionAll, EventSelectionAny, **kargs)
        self.assertEqual('test_not', obj.name)
        self.assertEqual('test_cutflow1_level1', obj.selection.name)
        self.assertEqual({'arg1': 10, 'arg2': 2, 'arg3': 3}, obj.selection.kargs)

        ## print event_selection_str(obj)

        self.assertIsInstance(obj, EventSelectionNot)

    def test_two(self):

        kargs = dict(
            name = 'test_not',
            arg1 = 10,
            arg2 = 20,
            level = 'test_cutflow1_level1'
            )

        obj = Not(EventSelectionAll, EventSelectionAny, **kargs)
        self.assertEqual('test_not', obj.name)
        self.assertEqual('test_cutflow1_level1', obj.selection.name)
        self.assertEqual({'arg1': 10, 'arg2': 20}, obj.selection.kargs)

        ## print event_selection_str(obj)

##__________________________________________________________________||
