# Tai Sakuma <tai.sakuma@cern.ch>
from .Modules.LambdaStr import LambdaStr

##__________________________________________________________________||
def LambdaStrFactory(lambda_str, name = None, **kargs):
    return LambdaStr(lambda_str = lambda_str, name = name)

##__________________________________________________________________||
