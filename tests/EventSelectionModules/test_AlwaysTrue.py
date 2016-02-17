# Tai Sakuma <tai.sakuma@cern.ch>
from ...EventSelectionModules.AlwaysTrue import AlwaysTrue
import unittest

##__________________________________________________________________||
class MockEvent(object):
    pass

##__________________________________________________________________||
class Test_AlwaysTrue(unittest.TestCase):

    def test_one(self):
        obj = AlwaysTrue()
        event = MockEvent()
        self.assertTrue(obj(event))

##__________________________________________________________________||
