import numpy as np

##__________________________________________________________________||
class Count(object):
    def __init__(self):
        self._results = [ ]

    def begin(self, n):
        self._results[:] = [[i] + [0]*2 for i in range(n)]

    def count(self, pass_):
        for r, p in zip(self._results, pass_):
            r[2] += 1 # total
            if p: r[1] += 1 # pass

##__________________________________________________________________||
class EventSelectionAllCount(object):
    """select events that meet all conditions

    """

    def __init__(self, name = None):
        if name is not None: self.name = name
        self.selections = [ ]
        self.count = Count()

    def add(self, selection):
        self.selections.append(selection)

    def begin(self, event):
        for s in self.selections:
            if hasattr(s, 'begin'): s.begin(event)
        self.count.begin(len(self.selections))

    def event(self, event):
        ret = True
        pass_ = [ ]
        for s in self.selections:
            pass_.append(s(event))
            if not pass_[-1]:
                ret = False
                break
        self.count.count(pass_)
        return ret

    def __call__(self, event):
        return self.event(event)

    def end(self):
        for s in self.selections:
            if hasattr(s, 'end'): s.end()

    def results(self):
        return self.count

##__________________________________________________________________||
