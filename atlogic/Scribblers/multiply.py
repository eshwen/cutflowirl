# Tai Sakuma <tai.sakuma@cern.ch>
import numpy as np

##__________________________________________________________________||
class multiply(object):
    def __init__(self, srcName1, srcName2, outName):
        self.srcName1 = srcName1
        self.srcName2 = srcName2
        self.outName = outName

    def __repr__(self):
        name_value_pairs = (
            ('srcName1', self.srcName1),
            ('srcName2', self.srcName2),
            ('outName', self.outName),
        )
        return '{}({})'.format(
            self.__class__.__name__,
            ', '.join(['{} = {!r}'.format(n, v) for n, v in name_value_pairs]),
        )

    def begin(self, event):
        self.out = [ ]
        self._attach_to_event(event)

    def _attach_to_event(self, event):
        setattr(event, self.outName, self.out)

    def event(self, event):
        self._attach_to_event(event)

        src1 = np.array(getattr(event, self.srcName1))
        src2 = np.array(getattr(event, self.srcName2))
        out = src1*src2
        self.out[:] = out


##__________________________________________________________________||
