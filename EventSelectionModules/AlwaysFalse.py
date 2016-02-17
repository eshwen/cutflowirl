
##__________________________________________________________________||
class AlwaysFalse(object):
    """never select events

    """
    def __init__(self, name = None):
        if name is not None: self.name = name

    def __call__(self, event): return False

##__________________________________________________________________||
