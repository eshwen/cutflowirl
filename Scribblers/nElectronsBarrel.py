# Tai Sakuma <tai.sakuma@cern.ch>
from .ScribblerBase import ScribblerBase

##__________________________________________________________________||
class nElectronsBarrel(ScribblerBase):
    def begin(self, event):
        self.vals = [ ]
        event.nElectronsBarrel = self.vals

    def event(self, event):
        event.nElectronsBarrel = self.vals
        self.vals[:] = [len([eta for eta in event.ele_eta if -1.479 < eta < 1.479])]

##__________________________________________________________________||
