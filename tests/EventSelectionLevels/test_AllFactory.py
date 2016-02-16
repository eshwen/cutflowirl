from ...EventSelectionLevels.AllFactory import AllFactory
from ...EventSelectionLevels.Modules.EventSelectionAll import EventSelectionAll
from ...EventSelectionLevels.Modules.EventSelectionAny import EventSelectionAny
from ...EventSelectionLevels.Modules.LambdaStr import LambdaStr
import unittest

##__________________________________________________________________||
class Test_AllFactory(unittest.TestCase):

    def test_obj(self):
        path_cfg_list = ("ev : ev.nJet[0] >= 2", "ev : ev.nMET[0] >= 200")
        kargs = dict(arg1 = 10, arg2 = 20, AllClass = EventSelectionAll, LambdaStrClass = LambdaStr)
        obj = AllFactory(path_cfg_list, name = 'test_all', **kargs)

##__________________________________________________________________||
