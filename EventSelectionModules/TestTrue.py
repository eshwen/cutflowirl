
##__________________________________________________________________||
class TestTrue(object):
    """always select events

    """
    def __init__(self, name = None, **kargs):
        if name is not None: self.name = name
        self.kargs = kargs

    def __call__(self, event): return True

##__________________________________________________________________||
