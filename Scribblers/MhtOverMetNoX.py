# Tai Sakuma <tai.sakuma@cern.ch>
from .ScribblerBase import ScribblerBase

##__________________________________________________________________||
class MhtOverMetNoX(ScribblerBase):
    def begin(self, event):
        self.vals = [ ]
        event.MhtOverMetNoX = self.vals

    def event(self, event):
        event.MhtOverMetNoX = self.vals
        if event.metNoX_pt[0] <= 0.00:
            self.vals[:] = [float("inf")]
            return
        self.vals[:] = [event.mht40_pt[0]/event.metNoX_pt[0]]

##__________________________________________________________________||
