
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

    def __add__(self, other):
        ret = Count()
        results = list(self._results) # copy
        if not other == 0: # other is 0 when e.g. sum([obj1, obj2])
            self._add_results_inplace(results, other._results)
        ret._results[:] = results
        return ret

    def __iadd__(self, other):
        self._add_results_inplace(self._results, other._results)
        return self

    def __radd__(self, other):
        return self.__add__(other)

    def _add_results_inplace(self, res1, res2):
        for r1, r2 in zip (res1, res2):
            r1[1] += r2[1]
            r1[2] += r2[2]

##__________________________________________________________________||
