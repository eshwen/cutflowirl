# Tai Sakuma <tai.sakuma@cern.ch>
from ...EventSelectionModules.EventSelectionAllCount import EventSelectionAllCount
import unittest

##__________________________________________________________________||
class MockEvent(object): pass

##__________________________________________________________________||
class MockEventSelection(object):
    def __init__(self):
        self.is_begin_called = False
        self.is_end_called = False
        self.ret = True

    def begin(self, event):
        self.is_begin_called = True

    def __call__(self, event):
        return self.ret

    def end(self):
        self.is_end_called = True

##__________________________________________________________________||
class Test_EventSelectionAllCount(unittest.TestCase):

    def test_empty(self):
        obj = EventSelectionAllCount()

        event = MockEvent()
        obj.begin(event)

        event = MockEvent()
        self.assertTrue(obj(event))

        count = obj.results()
        self.assertEqual([ ], count._results)

    def test_standard(self):
        obj = EventSelectionAllCount()
        selection1 = MockEventSelection()
        selection2 = MockEventSelection()

        obj.add(selection1)
        obj.add(selection2)

        self.assertFalse(selection1.is_begin_called)
        self.assertFalse(selection2.is_begin_called)

        self.assertFalse(selection1.is_end_called)
        self.assertFalse(selection2.is_end_called)

        event = MockEvent()
        obj.begin(event)
        self.assertTrue(selection1.is_begin_called)
        self.assertTrue(selection2.is_begin_called)

        event = MockEvent()
        selection1.ret = True   # 1/1
        selection2.ret = True   # 1/1
        self.assertTrue(obj(event))

        event = MockEvent()
        selection1.ret = True   # 2/2
        selection2.ret = False  # 1/2
        self.assertFalse(obj(event))

        event = MockEvent()
        selection1.ret = False  # 2/3
        selection2.ret = True   # 1/2
        self.assertFalse(obj.event(event))

        event = MockEvent()
        selection1.ret = False  # 2/4
        selection2.ret = False  # 1/2
        self.assertFalse(obj.event(event))

        obj.end()
        self.assertTrue(selection1.is_end_called)
        self.assertTrue(selection2.is_end_called)

        count = obj.results()
        self.assertEqual(
            [
                [0, 2, 4],
                [1, 1, 2],
            ],
            count._results
        )

    def test_nested(self):
        #
        # all (obj) --- all (obj1) --- sel (sel11)
        #            |              +- sel (sel12)
        #            +- all (obj2) --- sel (sel21)
        #            |              +- sel (sel22)
        #            +- sel (sel3)
        #

        obj = EventSelectionAllCount()
        obj1 = EventSelectionAllCount()
        obj2 = EventSelectionAllCount()
        sel3 = MockEventSelection()
        sel11 = MockEventSelection()
        sel12 = MockEventSelection()
        sel21 = MockEventSelection()
        sel22 = MockEventSelection()
        obj.add(obj1)
        obj.add(obj2)
        obj.add(sel3)
        obj1.add(sel11)
        obj1.add(sel12)
        obj2.add(sel21)
        obj2.add(sel22)

        self.assertFalse(sel11.is_begin_called)
        self.assertFalse(sel12.is_begin_called)
        self.assertFalse(sel21.is_begin_called)
        self.assertFalse(sel22.is_begin_called)
        self.assertFalse(sel3.is_begin_called)

        self.assertFalse(sel11.is_end_called)
        self.assertFalse(sel12.is_end_called)
        self.assertFalse(sel21.is_end_called)
        self.assertFalse(sel22.is_end_called)
        self.assertFalse(sel3.is_end_called)

        event = MockEvent()
        obj.begin(event)
        self.assertTrue(sel11.is_begin_called)
        self.assertTrue(sel12.is_begin_called)
        self.assertTrue(sel21.is_begin_called)
        self.assertTrue(sel22.is_begin_called)
        self.assertTrue(sel3.is_begin_called)

        event = MockEvent()
        sel11.ret = True   # 1/1
        sel12.ret = True   # 1/1
        sel21.ret = True   # 1/1
        sel22.ret = True   # 1/1
        sel3.ret = True   # 1/1
        self.assertTrue(obj(event))

        obj.end()
        self.assertTrue(sel11.is_end_called)
        self.assertTrue(sel12.is_end_called)
        self.assertTrue(sel21.is_end_called)
        self.assertTrue(sel22.is_end_called)
        self.assertTrue(sel3.is_end_called)

        count = obj.results()
        self.assertEqual(
            [
                [0, 1, 1],
                [0, 1, 1],
                [1, 1, 1],
                [1, 1, 1],
                [0, 1, 1],
                [1, 1, 1],
                [2, 1, 1],
            ],
            count._results
        )

##__________________________________________________________________||
