# Tai Sakuma <tai.sakuma@cern.ch>
from .ScribblerBase import ScribblerBase

##__________________________________________________________________||
class MhtOverMetNoHF(ScribblerBase):
    def begin(self, event):
        self.vals = [ ]
        event.MhtOverMetNoHF = self.vals

    def event(self, event):
        event.MhtOverMetNoHF = self.vals
        if event.metNoHF_pt[0] <= 0.00:
            self.vals[:] = [float("inf")]
            return
        self.vals[:] = [event.mht40_pt[0]/event.metNoHF_pt[0]]

##__________________________________________________________________||
