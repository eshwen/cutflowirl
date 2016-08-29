# Tai Sakuma <tai.sakuma@cern.ch>
import unittest
import copy

from ...EventSelectionModules.EventSelectionAllCount import Count

##__________________________________________________________________||
class Test_Count(unittest.TestCase):

    def test_copy(self):
        obj = Count()
        obj._results[:] = [[0, 2, 3]]
        obj1 = obj.copy()
        self.assertIsNot(obj, obj1)
        self.assertIsNot(obj._results, obj1._results)
        self.assertEqual([[0, 2, 3]], obj1._results)

    def test_insert(self):
        obj = Count()
        obj._results[:] = [
            [0, 6, 8],
            [1, 3, 6],
            [2, 1, 3],
        ]

        obj1 = Count()
        obj1._results[:] = [
            [0, 4, 6],
            [1, 3, 4],
        ]

        obj.insert(1, obj1)

        self.assertEqual(
            [
                [0, 6, 8],
                [1, 3, 6],
                [0, 4, 6],
                [1, 3, 4],
                [2, 1, 3],
            ],
            obj._results
        )

    def test_insert_at_end(self):
        obj = Count()
        obj._results[:] = [
            [0, 6, 8],
            [1, 3, 6],
            [2, 1, 3],
        ]

        obj1 = Count()
        obj1._results[:] = [
            [0, 2, 3],
            [1, 1, 2],
        ]

        obj.insert(2, obj1)

        self.assertEqual(
            [
                [0, 6, 8],
                [1, 3, 6],
                [2, 1, 3],
                [0, 2, 3],
                [1, 1, 2],
            ],
            obj._results
        )

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

        self.obj1_results_org = [
            [0, 2, 2],
            [1, 1, 2],
            [2, 0, 1],
            ]
        self.obj1 = Count()
        self.obj1._results = copy.deepcopy(self.obj1_results_org)

        self.obj2_results_org = [
            [0, 3, 5],
            [1, 2, 4],
            [2, 1, 2],
        ]
        self.obj2 = Count()
        self.obj2._results = copy.deepcopy(self.obj2_results_org)

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

        self.assertIsNot(self.obj1_results_org, self.obj1._results)
        self.assertEqual(self.obj1_results_org, self.obj1._results)

        self.assertIsNot(self.obj2_results_org, self.obj2._results)
        self.assertEqual(self.obj2_results_org, self.obj2._results)

    def test_radd(self):
        obj3 = sum([self.obj1, self.obj2]) # 0 + obj1 is executed
        self.assertEqual(self.expected, obj3._results)
        self.assertIsNot(self.obj1._results, obj3._results)
        self.assertIsNot(self.obj2._results, obj3._results)

        self.assertIsNot(self.obj1_results_org, self.obj1._results)
        self.assertEqual(self.obj1_results_org, self.obj1._results)

        self.assertIsNot(self.obj2_results_org, self.obj2._results)
        self.assertEqual(self.obj2_results_org, self.obj2._results)

    def test_iadd(self):
        obj1 = self.obj1

        self.obj1 += self.obj2
        self.assertIs(self.obj1, obj1)
        self.assertEqual(self.expected, self.obj1._results)

        self.assertIsNot(self.obj1_results_org, self.obj1._results)

        self.assertIsNot(self.obj2_results_org, self.obj2._results)
        self.assertEqual(self.obj2_results_org, self.obj2._results)

    @unittest.skip("skip because of logging. assertLogs can be used here for Python 3.4")
    def test_add_incompatible_different_length(self):
        obj2 = Count()
        obj2._results  = [
            [0, 3, 5],
            [1, 2, 4],
        ]
        obj3 = self.obj1 + obj2
        self.assertEqual(self.obj1._results, obj3._results)

    @unittest.skip("skip because of logging. assertLogs can be used here for Python 3.4")
    def test_add_incompatible_different_first_values(self):
        obj2 = Count()
        obj2._results  = [
            [0, 3, 5],
            [1, 2, 4],
            [3, 1, 2],
        ]
        obj3 = self.obj1 + obj2
        self.assertEqual(self.obj1._results, obj3._results)

##__________________________________________________________________||
