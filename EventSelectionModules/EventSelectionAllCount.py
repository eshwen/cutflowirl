import itertools
import copy

from .Count import Count

##__________________________________________________________________||
class EventSelectionAllCount(object):
    """select events that meet all conditions

    """

    def __init__(self, name = None):
        self.name = name if name is not None else 'All'
        self.selections = [ ]
        self.count = Count()

    def __repr__(self):
        return '{}(name = {!r}, selections = {!r}), count = {!r}'.format(
            self.__class__.__name__,
            self.name,
            self.selections,
            self.count
        )

    def copy_from(self, src):
        src = copy.deepcopy(src)
        self.count = src.count

    def add(self, selection):
        self.selections.append(selection)
        self.count.add(selection)

    def begin(self, event):
        for s in self.selections:
            if hasattr(s, 'begin'): s.begin(event)

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

    def results(self, increment = False):

        ret = self.count.copy()

        # reversed enumerate
        for i, s in itertools.izip(reversed(xrange(len(self.selections))), reversed(self.selections)):
            if hasattr(s, 'results'):
                ret.insert(i, s.results(increment = True))

        if increment:
            ret.increment_depth(by = 1)

        return ret

##__________________________________________________________________||
