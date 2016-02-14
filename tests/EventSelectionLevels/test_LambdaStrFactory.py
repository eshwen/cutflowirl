from ...EventSelectionLevels.LambdaStrFactory import LambdaStrFactory
from ...EventSelectionLevels.Modules.LambdaStr import LambdaStr
import unittest

##__________________________________________________________________||
class Test_LambdaStrFactory(unittest.TestCase):

    def setUp(self):
        self.obj = LambdaStrFactory(lambda_str = 'ev : ev.inCertifiedLumiSections[0]', name = 'JSON', LambdaStrClass = LambdaStr)

    def test_obj(self):
        self.assertIsInstance(self.obj, LambdaStr)
        self.assertEqual('ev : ev.inCertifiedLumiSections[0]', self.obj.lambda_str)
        self.assertEqual('JSON', self.obj.name)

##__________________________________________________________________||
