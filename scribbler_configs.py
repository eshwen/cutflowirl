#!/usr/bin/env python
import ast
import json

import Binning
Binning = Binning.Binning

##__________________________________________________________________||
class ScribblerBase(object):
    def begin(self, event): pass
    def event(self, event): pass
    def end(self): pass
    def copyFrom(self, src): pass

##__________________________________________________________________||
class Alias(ScribblerBase):
    def __init__(self, src, alias):
        self.src = src
        self.alias = alias

    def begin(self, event):
        setattr(event, self.alias, getattr(event, self.src))

    def event(self, event):
        setattr(event, self.alias, getattr(event, self.src))

##__________________________________________________________________||
class PrivatePuWeightFromNVert(ScribblerBase):
    def __init__(self, path):
        file = open(path)

        columns = file.readline().split()
        # e.g. ['nVert', 'corr']

        self.varName = columns[0]
        # e.g. 'nVert'

        self.weightDict = dict([[ast.literal_eval(e) for e in l.split()[0:2]] for l in file])
        # e.g.,  {1: 18.59651, 2: 5.441605, 3: 3.31272, 4: 2.687147, 5: 2.396046, 6: 2.246987}

        self.binning = Binning(boundaries = sorted(self.weightDict.keys()))

    def begin(self, event):
        self.vals = [ ]
        event.PrivatePuWeightFromNVert = self.vals

    def event(self, event):
        event.PrivatePuWeightFromNVert = self.vals
        self.vals[:] = [self.weightDict[self.binning(getattr(event, self.varName)[0])]]

##__________________________________________________________________||
class inCertifiedLumiSections(ScribblerBase):
    def __init__(self, json_path):
        self.certifiedLumiSections = [ ]
        j = json.load(open(json_path))
        for run in sorted(j.keys()):
            for lumi_range in j[run]:
                lumis = range(lumi_range[0], lumi_range[1] + 1)
                self.certifiedLumiSections.extend([(int(run), ls) for ls in lumis])
        # e.g., self.certifiedLumiSections = [(256941, 137), (256941, 138), (256941, 139)]
        self.certifiedLumiSections = set(self.certifiedLumiSections)

    def begin(self, event):
        self.vals = [ ]
        event.inCertifiedLumiSections = self.vals

    def event(self, event):
        event.inCertifiedLumiSections = self.vals
        self.vals[:] = [(event.run[0], event.lumi[0]) in self.certifiedLumiSections]

##__________________________________________________________________||
class cutflow(ScribblerBase):
    def begin(self, event):
        self.addr_cutflow = [ ]
        self.addr_cutflowId = [ ]
        event.cutflow = self.addr_cutflow
        event.cutflowId = self.addr_cutflowId
        # (nMuoV, nEleV, nPhoV, nMuoS, nEleS, nPhoS)
        self.nObjs_cutflowId_dict = {
            (0, 0, 0, 0, 0, 0) : 1, # 'Signal'
            (1, 0, 0, 1, 0, 0) : 2, # 'SingleMu'
            (2, 0, 0, 2, 0, 0) : 3, # 'DoubleMu'
            (0, 1, 0, 0, 1, 0) : 4, # 'SingleEle'
            (0, 2, 0, 0, 2, 0) : 5, # 'DoubleEle'
            (0, 0, 1, 0, 0, 1) : 6, # 'SinglePhoton'
            }

        self.cutflow_name_dict = {
            1 : 'Signal', 2 : 'SingleMu', 3 : 'DoubleMu',
            4 : 'SingleEle', 5 : 'DoubleEle', 6 : 'SinglePhoton',
            -1 : 'other'
            }

    def event(self, event):
        event.cutflow = self.addr_cutflow
        event.cutflowId = self.addr_cutflowId
        key = (event.nMuonsVeto[0],
               event.nElectronsVeto[0],
               event.nPhotonsVeto[0],
               event.nMuonsSelection[0],
               event.nElectronsSelection[0],
               event.nPhotonsSelection[0]
        )
        if key in self.nObjs_cutflowId_dict:
            cutflowId = self.nObjs_cutflowId_dict[key]
        else:
            cutflowId = -1
        self.addr_cutflowId[:] = [cutflowId]
        self.addr_cutflow[:] = [self.cutflow_name_dict[cutflowId]]

##__________________________________________________________________||
class componentName(ScribblerBase):
    def begin(self, event):
        self.vals = [ ]
        event.componentName = self.vals

        self.vals[:] = [event.component.name]
        # e.g., "HTMHT_Run2015D_PromptReco_25ns"

    def event(self, event):
        event.componentName = self.vals

##__________________________________________________________________||
class PrimaryDataset(ScribblerBase):
    def begin(self, event):
        self.vals = [ ]
        event.PrimaryDataset = self.vals

        # assume the first string before '_' is the primary dataset name
        # e.g., 'HTMHT' if "HTMHT_Run2015D_PromptReco_25ns"
        pd = event.componentName[0].split('_')[0]
        self.vals[:] = [pd]

    def event(self, event):
        event.PrimaryDataset = self.vals

##__________________________________________________________________||
class GenProcess(ScribblerBase):
    def begin(self, event):
        self.vals = [ ]
        event.GenProcess = self.vals

        # assume the first string before '_' is the name of the generated process
        # e.g., 'QCD' if "QCD_HT1500to2000_25ns"
        pd = event.componentName[0].split('_')[0]
        self.vals[:] = [pd]

    def event(self, event):
        event.GenProcess = self.vals

##__________________________________________________________________||
class njetnbjetbin(ScribblerBase):
    def __init__(self):
        self.nbjet40binning = Binning(boundaries = (0, 1, 2, 3))
        self.njet40binning = Binning(boundaries = (1, 2, 3, 4, 5))
        self.njet100binning = Binning(boundaries = (1, 2))

    def begin(self, event):
        self.vals = [ ]
        event.njetnbjetbin = self.vals

        # (nBJet40, nJet40, nJet100)
        self.bindict = {
            # monojet bins
            (0, 1, 1) : 'eq0b_eq1j', (1, 1, 1) : 'eq1b_eq1j',

            # asymetric bins
            (0, 2, 1) : 'eq0b_eq2a', (1, 2, 1) : 'eq1b_eq2a', (2, 2, 1) : 'eq2b_eq2a',
            (0, 3, 1) : 'eq0b_eq3a', (1, 3, 1) : 'eq1b_eq3a', (2, 3, 1) : 'eq2b_eq3a', (3, 3, 1) : 'ge3b_eq3a',
            (0, 4, 1) : 'eq0b_eq4a', (1, 4, 1) : 'eq1b_eq4a', (2, 4, 1) : 'eq2b_eq4a', (3, 4, 1) : 'ge3b_eq4a',
            (0, 5, 1) : 'eq0b_ge5a', (1, 5, 1) : 'eq1b_ge5a', (2, 5, 1) : 'eq2b_ge5a', (3, 5, 1) : 'ge3b_ge5a',

            # symetric bins
            (0, 2, 2) : 'eq0b_eq2j', (1, 2, 2) : 'eq1b_eq2j', (2, 2, 2) : 'eq2b_eq2j',
            (0, 3, 2) : 'eq0b_eq3j', (1, 3, 2) : 'eq1b_eq3j', (2, 3, 2) : 'eq2b_eq3j', (3, 3, 2) : 'ge3b_eq3j',
            (0, 4, 2) : 'eq0b_eq4j', (1, 4, 2) : 'eq1b_eq4j', (2, 4, 2) : 'eq2b_eq4j', (3, 4, 2) : 'ge3b_eq4j',
            (0, 5, 2) : 'eq0b_ge5j', (1, 5, 2) : 'eq1b_ge5j', (2, 5, 2) : 'eq2b_ge5j', (3, 5, 2) : 'ge3b_ge5j',
            }

    def event(self, event):
        event.njetnbjetbin = self.vals
        key = (
            self.nbjet40binning(event.nBJet40[0]),
            self.njet40binning(event.nJet40[0]),
            self.njet100binning(event.nJet100[0])
        )
        if key not in self.bindict:
            self.vals[:] = ['other']
            return
        self.vals[:] = [self.bindict[key]]

##__________________________________________________________________||
class htbin(ScribblerBase):
    def __init__(self):
        self.htbinning = Binning(boundaries = (200, 250, 300, 350, 400, 600, 800))

    def begin(self, event):
        self.vals = [ ]
        event.htbin = self.vals

    def event(self, event):
        event.htbin = self.vals
        self.vals[:] = [self.htbinning(event.ht40[0])]

##__________________________________________________________________||
class Determin_bintype(object):
    def __init__(self):
        self.njet40binning = Binning(boundaries = (1, 2))
        self.njet100binning = Binning(boundaries = (1, 2))
        self.htbinning = Binning(boundaries = (200, 800))

        # (nJet40, nJet100, ht40)
        self.tuple_bintypeId_dict = {
            (1, 1, 200) : 1, # 'monojet',
            (2, 1, 200) : 2, # 'asymjet',
            (2, 2, 200) : 3, # 'symjet',
            (1, 1, 800) : 1, # 'monojet',
            (2, 1, 800) : 4, # 'highht',
            (2, 2, 800) : 4, # 'highht',
        }

        self.bintype_name_dict = {
            1 : 'monojet', 2 : 'asymjet', 3 : 'symjet', 4 : 'highht',
            -1 : 'other'
            }

    def __call__(self, nJet40, nJet100, ht40):
        key = (self.njet40binning(nJet40), self.njet100binning(nJet100), self.htbinning(ht40))
        if key in self.tuple_bintypeId_dict:
            bintypeId = self.tuple_bintypeId_dict[key]
        else:
            bintypeId = -1
        bintype = self.bintype_name_dict[bintypeId]
        return bintype, bintypeId

determin_bintype = Determin_bintype()

##__________________________________________________________________||
class bintype(ScribblerBase):
    def begin(self, event):
        self.addr_bintype = [ ]
        self.addr_bintypeId = [ ]
        event.bintype = self.addr_bintype
        event.bintypeId = self.addr_bintypeId

    def event(self, event):
        event.bintype = self.addr_bintype
        event.bintypeId = self.addr_bintypeId
        bintype, bintypeId = determin_bintype(event.nJet40[0], event.nJet100[0], event.ht40[0])
        self.addr_bintype[:] = [bintype]
        self.addr_bintypeId[:] = [bintypeId]

##__________________________________________________________________||
class bintypeJECUp(ScribblerBase):
    def begin(self, event):
        self.addr_bintype = [ ]
        self.addr_bintypeId = [ ]
        event.bintypeJECUp = self.addr_bintype
        event.bintypeIdJECUp = self.addr_bintypeId

    def event(self, event):
        event.bintypeJECUp = self.addr_bintype
        event.bintypeIdJECUp = self.addr_bintypeId
        bintype, bintypeId = determin_bintype(event.nJet40JECUp[0], event.nJet100JECUp[0], event.ht40JECUp[0])
        self.addr_bintype[:] = [bintype]
        self.addr_bintypeId[:] = [bintypeId]

##__________________________________________________________________||
class bintypeJECDown(ScribblerBase):
    def begin(self, event):
        self.addr_bintype = [ ]
        self.addr_bintypeId = [ ]
        event.bintypeJECDown = self.addr_bintype
        event.bintypeIdJECDown = self.addr_bintypeId

    def event(self, event):
        event.bintypeJECDown = self.addr_bintype
        event.bintypeIdJECDown = self.addr_bintypeId
        bintype, bintypeId = determin_bintype(event.nJet40JECDown[0], event.nJet100JECDown[0], event.ht40JECDown[0])
        self.addr_bintype[:] = [bintype]
        self.addr_bintypeId[:] = [bintypeId]

##__________________________________________________________________||
class metNoX(ScribblerBase):
    def begin(self, event):
        self.val_pt = [ ]
        self.val_phi = [ ]
        event.metNoX_pt = self.val_pt
        event.metNoX_phi = self.val_phi
        self.itsdict = {
            'Signal': ('met_pt', 'met_phi'),
            'SingleMu': ('metNoMu_pt', 'metNoMu_phi'),
            'DoubleMu': ('metNoMu_pt', 'metNoMu_phi'),
            'SingleEle': ('metNoEle_pt', 'metNoEle_phi'),
            'DoubleEle': ('metNoEle_pt', 'metNoEle_phi'),
            'SinglePhoton': ('metNoPhoton_pt', 'metNoPhoton_phi'),
        }

    def event(self, event):
        event.metNoX_pt = self.val_pt
        event.metNoX_phi = self.val_phi
        cutflow = event.cutflow[0]
        if not cutflow in self.itsdict: cutflow = 'Signal'
        self.val_pt[:] = [getattr(event, self.itsdict[cutflow][0])[0]]
        self.val_phi[:] = [getattr(event, self.itsdict[cutflow][1])[0]]

##__________________________________________________________________||
class metNoXNoHF(ScribblerBase):
    def begin(self, event):
        self.val_pt = [ ]
        self.val_phi = [ ]
        event.metNoXNoHF_pt = self.val_pt
        event.metNoXNoHF_phi = self.val_phi
        self.itsdict = {
            'Signal': ('metNoHF_pt', 'metNoHF_phi'),
            'SingleMu': ('metNoMuNoHF_pt', 'metNoMuNoHF_phi'),
            'DoubleMu': ('metNoMuNoHF_pt', 'metNoMuNoHF_phi'),
            'SingleEle': ('metNoEleNoHF_pt', 'metNoEleNoHF_phi'),
            'DoubleEle': ('metNoEleNoHF_pt', 'metNoEleNoHF_phi'),
            'SinglePhoton': ('metNoPhotonNoHF_pt', 'metNoPhotonNoHF_phi'),
        }

    def event(self, event):
        event.metNoXNoHF_pt = self.val_pt
        event.metNoXNoHF_phi = self.val_phi
        cutflow = event.cutflow[0]
        if not cutflow in self.itsdict: cutflow = 'Signal'
        self.val_pt[:] = [getattr(event, self.itsdict[cutflow][0])[0]]
        self.val_phi[:] = [getattr(event, self.itsdict[cutflow][1])[0]]

##__________________________________________________________________||
class MhtOverMet(ScribblerBase):
    def begin(self, event):
        self.vals = [ ]
        event.MhtOverMet = self.vals

    def event(self, event):
        event.MhtOverMet = self.vals
        if event.met_pt[0] <= 0.00:
            self.vals[:] = [float("inf")]
            return
        self.vals[:] = [event.mht40_pt[0]/event.met_pt[0]]

##__________________________________________________________________||
class MhtOverMetNoHF(ScribblerBase):
    def begin(self, event):
        self.vals = [ ]
        event.MhtOverMetNoHF = self.vals

    def event(self, event):
        event.MhtOverMetNoHF = self.vals
        if event.metNoHF_pt[0] <= 0.00:
            self.vals[:] = [float("inf")]
            return
        self.vals[:] = [event.mht40_pt[0]/event.metNoHF_pt[0]]

##__________________________________________________________________||
class MhtOverMetNoX(ScribblerBase):
    def begin(self, event):
        self.vals = [ ]
        event.MhtOverMetNoX = self.vals

    def event(self, event):
        event.MhtOverMetNoX = self.vals
        if event.metNoX_pt[0] <= 0.00:
            self.vals[:] = [float("inf")]
            return
        self.vals[:] = [event.mht40_pt[0]/event.metNoX_pt[0]]

##__________________________________________________________________||
class MhtOverMetNoXNoHF(ScribblerBase):
    def begin(self, event):
        self.vals = [ ]
        event.MhtOverMetNoXNoHF = self.vals

    def event(self, event):
        event.MhtOverMetNoXNoHF = self.vals
        if event.metNoXNoHF_pt[0] <= 0.00:
            self.vals[:] = [float("inf")]
            return
        self.vals[:] = [event.mht40_pt[0]/event.metNoXNoHF_pt[0]]

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
