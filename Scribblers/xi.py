# Tai Sakuma <tai.sakuma@cern.ch>
import numpy as np

##__________________________________________________________________||
class xi(object):
    def begin(self, event):
        self.tanXi = [ ]
        self.xi = [ ]
        self._attach_to_event(event)

    def _attach_to_event(self, event):
        event.tanXi = self.tanXi
        event.xi = self.xi

    def event(self, event):
        self._attach_to_event(event)
        if len(event.jet40_pt) <= 1:
            self.tanXi[:] = [-1]
            self.xi[:] = [-1]
            return

        self.tanXi[:] = [event.minSinDphiTilde[0]/event.maxH[0]]
        self.xi[:] = [np.arctan2(event.minSinDphiTilde[0], event.maxH[0])]

##__________________________________________________________________||
