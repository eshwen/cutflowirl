# Tai Sakuma <tai.sakuma@cern.ch>
from ...EventSelectionModules.EventSelectionAllCount import EventSelectionAllCount
import unittest

##__________________________________________________________________||
class MockEvent(object): pass

##__________________________________________________________________||
class MockEventSelection(object):
    def __init__(self):
        self.isBeginCalled = False
        self.isEndCalled = False
        self.ret = True

    def begin(self, event):
        self.isBeginCalled = True

    def __call__(self, event):
        return self.ret

    def end(self):
        self.isEndCalled = True

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

        self.assertFalse(selection1.isBeginCalled)
        self.assertFalse(selection2.isBeginCalled)

        self.assertFalse(selection1.isEndCalled)
        self.assertFalse(selection2.isEndCalled)

        event = MockEvent()
        obj.begin(event)
        self.assertTrue(selection1.isBeginCalled)
        self.assertTrue(selection2.isBeginCalled)

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
        self.assertTrue(selection1.isEndCalled)
        self.assertTrue(selection2.isEndCalled)

        count = obj.results()
        self.assertEqual(
            [
                [0, 2, 4],
                [1, 1, 2],
            ],
            count._results
        )

##__________________________________________________________________||
