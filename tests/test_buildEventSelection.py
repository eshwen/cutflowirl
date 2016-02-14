from ..buildEventSelection import buildEventSelection
import unittest

##__________________________________________________________________||
class Test_buildEventSelection(unittest.TestCase):

    def test_call(self):

        kargs = dict(
            arg1 = 10,
            arg2 = 20,
            level = dict(factory = 'test_level1', arg2 = 2, arg3 = 3)
        )

        obj = buildEventSelection(**kargs)

##__________________________________________________________________||
