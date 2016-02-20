# Tai Sakuma <tai.sakuma@cern.ch>
from .ScribblerBase import ScribblerBase
from .determin_bintype import determin_bintype

##__________________________________________________________________||
class bintype(ScribblerBase):
    def begin(self, event):
        self.addr_bintype = [ ]
        self.addr_bintypeId = [ ]
        event.bintype = self.addr_bintype
        event.bintypeId = self.addr_bintypeId

    def event(self, event):
        event.bintype = self.addr_bintype
        event.bintypeId = self.addr_bintypeId
        bintype, bintypeId = determin_bintype(event.nJet40[0], event.nJet100[0], event.ht40[0])
        self.addr_bintype[:] = [bintype]
        self.addr_bintypeId[:] = [bintypeId]

##__________________________________________________________________||
