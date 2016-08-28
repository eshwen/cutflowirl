
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
