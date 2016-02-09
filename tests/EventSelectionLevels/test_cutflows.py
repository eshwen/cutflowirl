from ...EventSelectionLevels.cutflows import cutflows
from ...EventSelectionLevels.Modules.EventSelectionAll import EventSelectionAll
from ...EventSelectionLevels.Modules.EventSelectionAny import EventSelectionAny
from ...EventSelectionLevels.Modules.LambdaStr import LambdaStr
from ...event_selection_str import event_selection_str
import unittest

##__________________________________________________________________||
class Test_cutflows(unittest.TestCase):

    def test_call(self):
        kargs = dict(
            datamc = 'mc',
            metnohf = False,
            arg1 = 10,
            cutflows = (
                ('test_cutflow1', dict(
                    kargs = dict(arg1 = 31, arg2 = 52, arg3 = 102),
                    levels = (
                        ('level1', dict(arg1 = 1, arg2 = 2)),
                        'level2')
                )),
                ('test_cutflow2', dict(levels = ('level1', 'level2'))),
                'test_cutflow3',
                ('test_cutflow4', dict(kargs = dict(arg1 = 11, arg2 = 22))),
            ))

        es = cutflows(EventSelectionAll, EventSelectionAny, **kargs)
        ## print event_selection_str(es)

##__________________________________________________________________||
