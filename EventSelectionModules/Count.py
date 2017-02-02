import copy

##__________________________________________________________________||
N_KEYS = 2
IDX_PASS = 2
IDX_TOTAL = 3

##__________________________________________________________________||
class Count(object):
    def __init__(self):
        self._results = [ ]

    def __repr__(self):
        return '{}({!r})'.format(self.__class__.__name__, self._results)

    def copy(self):
        return copy.deepcopy(self)

    def add(self, selection):
        class_name = selection.__class__.__name__
        selection_name = selection.name if hasattr(selection, 'name') and selection.name is not None else ''
        pass_ = 0
        total = 0
        self._results.append([class_name, selection_name, pass_, total])

    def count(self, pass_):
        for r, p in zip(self._results, pass_):
            r[IDX_TOTAL] += 1 # total
            if p: r[IDX_PASS] += 1 # pass

    def insert(self, i, other):
        self._results[(i + 1):(i + 1)] = other._results

    def results(self):
        return self._results

    def __add__(self, other):
        ret = self.copy()

        if other == 0: # other is 0 when e.g. sum([obj1, obj2])
            return ret

        self._add_results_inplace(ret._results, other._results)
        return ret

    def __iadd__(self, other):
        self._add_results_inplace(self._results, other._results)
        return self

    def __radd__(self, other):
        return self.__add__(other)

    def _add_results_inplace(self, res1, res2):
        if not len(res1) == len(res2):
            import logging
            logging.warning('cannot add because res1 and res2 don\'t have the same length: res1 = {}, res2 = {}'.format(res1, res2))
            return

        if not all([(r1[:N_KEYS] == r2[:N_KEYS]) for r1, r2 in zip(res1, res2)]):
            import logging
            logging.warning('cannot add because res1 and res2 don\'t have the same key columns: res1 = {}, res2 = {}'.format(res1, res2))
            return

        for r1, r2 in zip(res1, res2):
            r1[IDX_PASS] += r2[IDX_PASS]
            r1[IDX_TOTAL] += r2[IDX_TOTAL]

##__________________________________________________________________||
