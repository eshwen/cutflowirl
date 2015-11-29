
##__________________________________________________________________||
class EventSelectionAll(object):
    """select events that meet all conditions

    """

    def __init__(self, name = None):
        if name is not None: self.name = name
        self.selections = [ ]

    def add(self, selection):
        self.selections.append(selection)

    def begin(self, event):
        for s in self.selections:
            if hasattr(s, 'begin'): s.begin(event)

    def __call__(self, event):
        for s in self.selections:
            if not s(event): return False
        return True

    def end(self):
        for s in self.selections:
            if hasattr(s, 'end'): s.end()

##__________________________________________________________________||
