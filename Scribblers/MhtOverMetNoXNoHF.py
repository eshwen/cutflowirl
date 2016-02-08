# Tai Sakuma <tai.sakuma@cern.ch>
from .ScribblerBase import ScribblerBase

##__________________________________________________________________||
class MhtOverMetNoXNoHF(ScribblerBase):
    def begin(self, event):
        self.vals = [ ]
        event.MhtOverMetNoXNoHF = self.vals

    def event(self, event):
        event.MhtOverMetNoXNoHF = self.vals
        if event.metNoXNoHF_pt[0] <= 0.00:
            self.vals[:] = [float("inf")]
            return
        self.vals[:] = [event.mht40_pt[0]/event.metNoXNoHF_pt[0]]

##__________________________________________________________________||
