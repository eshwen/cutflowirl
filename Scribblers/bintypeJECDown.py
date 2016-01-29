# Tai Sakuma <tai.sakuma@cern.ch>
from .ScribblerBase import ScribblerBase
from .Determin_bintype import determin_bintype

##__________________________________________________________________||
class bintypeJECDown(ScribblerBase):
    def begin(self, event):
        self.addr_bintype = [ ]
        self.addr_bintypeId = [ ]
        event.bintypeJECDown = self.addr_bintype
        event.bintypeIdJECDown = self.addr_bintypeId

    def event(self, event):
        event.bintypeJECDown = self.addr_bintype
        event.bintypeIdJECDown = self.addr_bintypeId
        bintype, bintypeId = determin_bintype(event.nJet40JECDown[0], event.nJet100JECDown[0], event.ht40JECDown[0])
        self.addr_bintype[:] = [bintype]
        self.addr_bintypeId[:] = [bintypeId]

##__________________________________________________________________||
