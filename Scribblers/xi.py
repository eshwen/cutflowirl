# Tai Sakuma <tai.sakuma@cern.ch>
import numpy as np

##__________________________________________________________________||
class xi(object):
    def begin(self, event):
        self.xi = [ ]
        self._attach_to_event(event)

    def _attach_to_event(self, event):
        event.xi = self.xi

    def event(self, event):
        self._attach_to_event(event)

        sinMinDphiTilde = np.sin(event.minDphiTilde)
        maxH = np.array(event.maxH)

        if not (sinMinDphiTilde.size == 1 and maxH.size == 1):
            self.xi[:] = [-1]
            return

        self.xi[:] = np.arctan2(sinMinDphiTilde, maxH)

##__________________________________________________________________||
