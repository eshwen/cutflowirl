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
class TestCount_operator(unittest.TestCase):

    def setUp(self):
        self.obj1 = Count()
        self.obj2 = Count()

        self.obj1._results  = [
            [0, 2, 2],
            [1, 1, 2],
            [2, 0, 1],
            ]

        self.obj2._results  = [
            [0, 3, 5],
            [1, 2, 4],
            [2, 1, 2],
        ]

        self.expected = [
            [0, 5, 7],
            [1, 3, 6],
            [2, 1, 3],
            ]

    def test_add(self):
        obj3 = self.obj1 + self.obj2
        self.assertEqual(self.expected, obj3._results)
        self.assertIsNot(self.obj1._results, obj3._results)
        self.assertIsNot(self.obj2._results, obj3._results)

    def test_radd(self):
        obj3 = sum([self.obj1, self.obj2]) # 0 + obj1 is executed
        self.assertEqual(self.expected, obj3._results)
        self.assertIsNot(self.obj1._results, obj3._results)
        self.assertIsNot(self.obj2._results, obj3._results)

    def test_iadd(self):
        obj1 = self.obj1

        self.obj1 += self.obj2
        self.assertIs(self.obj1, obj1)
        self.assertEqual(self.expected, self.obj1._results)


##__________________________________________________________________||
