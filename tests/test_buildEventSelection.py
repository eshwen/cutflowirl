from ..buildEventSelection import buildEventSelection
import unittest

##__________________________________________________________________||
class Test_buildEventSelection(unittest.TestCase):

    def test_call(self):

        kargs = dict(
            arg1 = 10,
            arg2 = 20,
            levels = (
                ('test_level1', dict(arg2 = 2, arg3 = 3)),
                'test_level2',
            ))

        obj = buildEventSelection(**kargs)

##__________________________________________________________________||
