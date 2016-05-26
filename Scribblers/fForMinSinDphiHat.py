# Tai Sakuma <tai.sakuma@cern.ch>
import numpy as np

##__________________________________________________________________||
class fForMinSinDphiHat(object):
    def begin(self, event):
        self.fForMinSinDphiHat = [ ]
        self._attach_to_event(event)

    def _attach_to_event(self, event):
        event.fForMinSinDphiHat = self.fForMinSinDphiHat

    def event(self, event):
        self._attach_to_event(event)

        sinDphiHat = np.array(event.jet40_sinDphiHat)
        if sinDphiHat.size == 0:
            self.fForMinSinDphiHat[:] = [ ]
            return

        minSinDphiHat = sinDphiHat.min()

        f = np.array(event.jet40_f)

        fForMinSinDphiHat = f[sinDphiHat == minSinDphiHat][0]
        self.fForMinSinDphiHat[:] = [fForMinSinDphiHat.item()]


##__________________________________________________________________||
