from ..buildEventSelection import buildEventSelection
import unittest

##__________________________________________________________________||
class Test_buildEventSelection(unittest.TestCase):

    def test_call(self):

        buildEventSelection(
            datamc = 'data',
            levels = (
                ('test_level1', dict(arg1 = 1, arg2 = 2)),
                'test_level2',
            )
        )

##__________________________________________________________________||
