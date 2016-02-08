#!/usr/bin/env python
from Scribblers.ScribblerBase import ScribblerBase
from Scribblers.Alias import Alias
from Scribblers.PrimaryDataset import PrimaryDataset
from Scribblers.inCertifiedLumiSections import inCertifiedLumiSections
from Scribblers.cutflow import cutflow
from Scribblers.metNoX import metNoX
from Scribblers.WeightFromTbl import WeightFromTbl
from Scribblers.componentName import componentName
from Scribblers.GenProcess import GenProcess
from Scribblers.njetnbjetbin import njetnbjetbin
from Scribblers.htbin import htbin
from Scribblers.bintype import bintype
from Scribblers.bintypeJECUp import bintypeJECUp
from Scribblers.bintypeJECDown import bintypeJECDown
from Scribblers.metNoXNoHF import metNoXNoHF
from Scribblers.MhtOverMet import MhtOverMet
from Scribblers.MhtOverMetNoHF import MhtOverMetNoHF
from Scribblers.MhtOverMetNoX import MhtOverMetNoX
from Scribblers.MhtOverMetNoXNoHF import MhtOverMetNoXNoHF
from Scribblers.nMuonsIsolated import nMuonsIsolated
from Scribblers.nElectronsIsolated import nElectronsIsolated

##__________________________________________________________________||
def scribbler_configs(datamc, pd, gen_process, json = None, metnohf = False):
    """
    Args:

    datamc: "data" or "mc"

    pd: True or False

    gen_process: True or False

    json: path to json file for certified data

    metnohf: True or False

    """

    ret = [ ]
    if datamc == 'data' and pd:
        ret.append(PrimaryDataset())

    if datamc == 'mc' and gen_process:
        ret.append(GenProcess())

    if datamc == 'data' and json is not None:
        ret.append(inCertifiedLumiSections(json))

    ret.append(cutflow())
    ret.append(metNoX())

    ret.append(njetnbjetbin())
    ret.append(htbin())
    ret.append(bintype())
    ret.append(bintypeJECUp())
    ret.append(bintypeJECDown())
    ret.append(MhtOverMet())
    ret.append(MhtOverMetNoX())

    ret.append(nMuonsIsolated())
    ret.append(nElectronsIsolated())

    if metnohf:
        ret.append(metNoXNoHF())
        ret.append(MhtOverMetNoHF())
        ret.append(MhtOverMetNoXNoHF())

    return ret

##__________________________________________________________________||
class ScribblerVal(ScribblerBase):
    def begin(self, event):
        self.vals = [ ]
        self.val = 0
        event.val = self.vals

    def event(self, event):
        event.val = self.vals
        self.val += 1
        self.vals[:] = [self.val]

##__________________________________________________________________||
if __name__ == '__main__':
    import unittest

    class MockEvent(object):
        pass

    class TestStringMethods(unittest.TestCase):

        def test_read_branch_address_with_same_event_object(self):
            obj = ScribblerVal()
            event = MockEvent()

            obj.begin(event)
            val = event.val

            obj.event(event)
            self.assertEqual(1, val[0])

            obj.event(event)
            self.assertEqual(2, val[0])

        def test_read_event_attribute_with_same_event_object(self):
            obj = ScribblerVal()
            event = MockEvent()

            obj.begin(event)

            obj.event(event)
            self.assertEqual(1, event.val[0])

            obj.event(event)
            self.assertEqual(2, event.val[0])

        def test_read_branch_address_with_different_event_objects(self):
            obj = ScribblerVal()
            event = MockEvent()

            obj.begin(event)
            val = event.val

            event1 = MockEvent()
            obj.event(event1)
            self.assertEqual(1, val[0])

            event2 = MockEvent()
            obj.event(event2)
            self.assertEqual(2, val[0])

        def test_read_event_attribute_with_different_event_objects(self):
            obj = ScribblerVal()
            event = MockEvent()

            obj.begin(event)

            event1 = MockEvent()
            obj.event(event1)
            self.assertEqual(1, event1.val[0])

            event2 = MockEvent()
            obj.event(event2)
            self.assertEqual(2, event2.val[0])


    unittest.main()

##__________________________________________________________________||
