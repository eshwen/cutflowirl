from ...EventSelectionModules.AlternativeSequences import AlternativeSequences
from ...EventSelectionModules.EventSelectionAll import EventSelectionAll
from ...EventSelectionModules.EventSelectionAny import EventSelectionAny
from ...EventSelectionModules.LambdaStr import LambdaStr
from ...event_selection_str import event_selection_str
import unittest

##__________________________________________________________________||
class Test_AlternativeSequences(unittest.TestCase):

    def setUp(self):

        kargs = dict(
            name = 'cutflows',
            datamc = 'mc',
            metnohf = False,
            arg1 = 10,
            sequences = (
                dict(name = 'test_cutflow1',
                     kargs = dict(arg1 = 31, arg2 = 52, arg3 = 102),
                     levels = (
                         ('test_cutflow1_level1', dict(arg1 = 1, arg2 = 2)),
                         'test_cutflow1_level2'
                     )),
                dict(name = 'test_cutflow2',
                     levels = ('test_cutflow2_level1', 'test_cutflow2_level2', 'test_cutflow2_level3')),
                dict(levels = ('test_cutflow3_level1', )),
            ))

        self.obj = AlternativeSequences(EventSelectionAll, EventSelectionAny, **kargs)

    def test_obj_basics(self):

        self.assertIsInstance(self.obj, EventSelectionAny)
        self.assertEqual('cutflows', self.obj.name)

        self.assertEqual(3, len(self.obj.selections))


    def test_cutflow1_general(self):

        cutflow1 = self.obj.selections[0]

        self.assertIsInstance(cutflow1, EventSelectionAll)

        self.assertEqual('test_cutflow1', cutflow1.name)
        self.assertEqual(2, len(cutflow1.selections))

        cutflow1_level1, cutflow1_level2 = cutflow1.selections
        self.assertEqual('test_cutflow1_level1', cutflow1_level1.name)
        self.assertEqual(
            {'datamc': 'mc', 'metnohf': False, 'arg1': 1, 'arg2': 2, 'arg3': 102},
            cutflow1_level1.kargs
        )

        self.assertEqual('test_cutflow1_level2', cutflow1_level2.name)
        self.assertEqual(
            {'datamc': 'mc', 'metnohf': False, 'arg1': 31, 'arg2': 52, 'arg3': 102},
            cutflow1_level2.kargs
        )

    def test_cutflow2_no_args(self):

        cutflow2 = self.obj.selections[1]

        self.assertIsInstance(cutflow2, EventSelectionAll)

        self.assertEqual('test_cutflow2', cutflow2.name)
        self.assertEqual(3, len(cutflow2.selections))

        cutflow2_level1, cutflow2_level2, cutflow2_level3 = cutflow2.selections
        self.assertEqual('test_cutflow2_level1', cutflow2_level1.name)
        self.assertEqual(
            {'datamc': 'mc', 'metnohf': False, 'arg1': 10},
            cutflow2_level1.kargs
        )

        self.assertEqual('test_cutflow2_level2', cutflow2_level2.name)
        self.assertEqual(
            {'datamc': 'mc', 'metnohf': False, 'arg1': 10},
            cutflow2_level2.kargs
        )

        self.assertEqual('test_cutflow2_level3', cutflow2_level3.name)
        self.assertEqual(
            {'datamc': 'mc', 'metnohf': False, 'arg1': 10},
            cutflow2_level3.kargs
        )

    def test_cutflow3_no_name(self):

        cutflow3 = self.obj.selections[2]

        self.assertIsInstance(cutflow3, EventSelectionAll)

        self.assertFalse(hasattr(cutflow3, 'name'))
        self.assertEqual(1, len(cutflow3.selections))

        cutflow3_level1 = cutflow3.selections[0]
        self.assertEqual('test_cutflow3_level1', cutflow3_level1.name)
        self.assertEqual(
            {'datamc': 'mc', 'metnohf': False, 'arg1': 10},
            cutflow3_level1.kargs
        )

        # print event_selection_str(es)

##__________________________________________________________________||
