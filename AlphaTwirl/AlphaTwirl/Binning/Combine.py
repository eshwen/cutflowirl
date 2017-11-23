# Tai Sakuma <tai.sakuma@cern.ch>

##__________________________________________________________________||
def returnTrue(x): return True

##__________________________________________________________________||
def plusOne(x): return x + 1

##__________________________________________________________________||
class Combine(object):
    """A combine two binnings.

    This class uses *low* for the values below *at* and otherwise uses
    *high*.

    This class requires bin labels of both binnings to be values in
    the bins.

    """
    def __init__(self, low, high, at):
        self._low = low
        self._high = high
        self._at = at

    def __call__(self, val):
        if val < self._at:
            return self._low(val)
        else:
            return self._high(val)

    def next(self, bin):
        if bin < self._at:
            bin = self._low.next(bin)
            if bin < self._at:
                return bin
            else:
                return self._high(bin)
        return self._high.next(bin)

##__________________________________________________________________||
