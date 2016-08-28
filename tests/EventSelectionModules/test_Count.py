# Tai Sakuma <tai.sakuma@cern.ch>
from ...EventSelectionModules.EventSelectionAllCount import Count
import unittest

##__________________________________________________________________||
class Test_Count(unittest.TestCase):

    def test_empty(self):
        obj = Count()
        obj.begin(n = 0)
        obj.count(pass_ = [ ])

    def test_one(self):
        obj = Count()
        obj.begin(n = 1)

        self.assertEqual(
            [
                [0, 0, 0],
            ],
            obj._results
        )

        obj.count(pass_ = [True])
        self.assertEqual(
            [
                [0, 1, 1],
            ],
            obj._results
        )

        obj.count(pass_ = [False])
        self.assertEqual(
            [
                [0, 1, 2],
            ],
            obj._results
        )

    def test_three(self):
        obj = Count()
        obj.begin(n = 3)

        self.assertEqual(
            [
                [0, 0, 0],
                [1, 0, 0],
                [2, 0, 0],
            ],
            obj._results
        )

        obj.count(pass_ = [True, False])
        self.assertEqual(
            [
                [0, 1, 1],
                [1, 0, 1],
                [2, 0, 0],
            ],
            obj._results
        )

        obj.count(pass_ = [True, True, False])
        self.assertEqual(
            [
                [0, 2, 2],
                [1, 1, 2],
                [2, 0, 1],
            ],
            obj._results
        )
##__________________________________________________________________||
