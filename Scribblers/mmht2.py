# Tai Sakuma <tai.sakuma@cern.ch>
import numpy as np

##__________________________________________________________________||
class mmht2(object):
    def begin(self, event):
        self.maxCf = [ ]
        self._attach_to_event(event)

    def _attach_to_event(self, event):
        event.maxCf = self.maxCf

    def event(self, event):
        self._attach_to_event(event)
        if len(event.jet40_pt) <= 1:
            self.maxCf[:] = [-1]
            return

        f = np.array(event.jet40_ptOverMht)

        sin_cappedDphi = np.array(event.jet40_sinCappedDphi)
        min_sin_cappedDphi = sin_cappedDphi.min()

        cos_cappedDphi = np.array(event.jet40_cosCappedDphi)

        correctedF = np.where(sin_cappedDphi == min_sin_cappedDphi, f + cos_cappedDphi, f)
        correctedF = correctedF/min_sin_cappedDphi
        self.maxCf[:] = [correctedF.max().item()]

##__________________________________________________________________||
