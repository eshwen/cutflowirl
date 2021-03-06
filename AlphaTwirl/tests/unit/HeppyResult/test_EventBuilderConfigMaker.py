import sys
import unittest

from AlphaTwirl.HeppyResult import EventBuilderConfig

##__________________________________________________________________||
hasROOT = False
try:
    import ROOT
    hasROOT = True
except ImportError:
    pass

if hasROOT:
    from AlphaTwirl.HeppyResult import EventBuilderConfigMaker

##__________________________________________________________________||
class MockAnalyzer(object):
    def __init__(self):
        self.path = '/heppyresult/dir/TTJets/treeProducerSusyAlphaT'

##__________________________________________________________________||
class MockComponent(object):
    def __init__(self):
        self.treeProducerSusyAlphaT = MockAnalyzer()
        self.name = 'TTJets'

##__________________________________________________________________||
class MockTObject(object):
    def __init__(self, name):
        self.name = name

    def GetEntries(self):
        return 2500

##__________________________________________________________________||
class MockTFile(object):
    def Open(self, path):
        self.path = path
        return self
    def Get(self, name):
        return MockTObject(name)

##__________________________________________________________________||
class MockROOT(object):
    def __init__(self): self.TFile = MockTFile()


##__________________________________________________________________||
@unittest.skipUnless(hasROOT, "has no ROOT")
class TestEventBuilderConfigMaker(unittest.TestCase):

    def setUp(self):
        self.moduleEventBuilderConfigMaker = sys.modules['AlphaTwirl.HeppyResult.EventBuilderConfigMaker']
        self.orgROOT = self.moduleEventBuilderConfigMaker.ROOT
        self.moduleEventBuilderConfigMaker.ROOT = MockROOT()

    def tearDown(self):
        self.moduleEventBuilderConfigMaker.ROOT = self.orgROOT

    def test_create_config_for(self):
        obj = EventBuilderConfigMaker(
            analyzerName = 'treeProducerSusyAlphaT',
            fileName = 'tree.root',
            treeName = 'tree'
        )

        component = MockComponent()

        expected = EventBuilderConfig(
            inputPath = '/heppyresult/dir/TTJets/treeProducerSusyAlphaT/tree.root',
            treeName = 'tree',
            maxEvents = 30,
            start = 20,
            component = component,
            name = 'TTJets'
        )

        actual = obj.create_config_for(
            component,
            file_ = '/heppyresult/dir/TTJets/treeProducerSusyAlphaT/tree.root',
            start = 20,
            length = 30
        )

        self.assertEqual(expected, actual)

    def test_file_list_in(self):
        obj = EventBuilderConfigMaker(
            analyzerName = 'treeProducerSusyAlphaT',
            fileName = 'tree.root',
            treeName = 'tree'
        )

        component = MockComponent()

        expected = ['/heppyresult/dir/TTJets/treeProducerSusyAlphaT/tree.root']

        actual = obj.file_list_in(component)

        self.assertEqual(expected, actual)

    def test_file_list_in_maxFiles(self):
        obj = EventBuilderConfigMaker(
            analyzerName = 'treeProducerSusyAlphaT',
            fileName = 'tree.root',
            treeName = 'tree'
        )

        component = MockComponent()

        expected = [ ]

        actual = obj.file_list_in(component, maxFiles = 0)

        self.assertEqual(expected, actual)

    def test_file_nevents_list_for(self):
        obj = EventBuilderConfigMaker(
            analyzerName = 'treeProducerSusyAlphaT',
            fileName = 'tree.root',
            treeName = 'tree'
        )

        component = MockComponent()

        expected = [('/heppyresult/dir/TTJets/treeProducerSusyAlphaT/tree.root', 2500)]

        actual = obj.file_nevents_list_for(component)

        self.assertEqual(expected, actual)

    def test_file_nevents_list_for_maxFiles(self):
        obj = EventBuilderConfigMaker(
            analyzerName = 'treeProducerSusyAlphaT',
            fileName = 'tree.root',
            treeName = 'tree'
        )

        component = MockComponent()

        expected = [('/heppyresult/dir/TTJets/treeProducerSusyAlphaT/tree.root', 2500)]
        actual = obj.file_nevents_list_for(component, maxFiles = 1)
        self.assertEqual(expected, actual)

        expected = [ ]
        actual = obj.file_nevents_list_for(component, maxFiles = 0)
        self.assertEqual(expected, actual)

##__________________________________________________________________||
