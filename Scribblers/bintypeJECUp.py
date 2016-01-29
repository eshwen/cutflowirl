# Tai Sakuma <tai.sakuma@cern.ch>
from .ScribblerBase import ScribblerBase
from .Determin_bintype import determin_bintype

##__________________________________________________________________||
class bintypeJECUp(ScribblerBase):
    def begin(self, event):
        self.addr_bintype = [ ]
        self.addr_bintypeId = [ ]
        event.bintypeJECUp = self.addr_bintype
        event.bintypeIdJECUp = self.addr_bintypeId

    def event(self, event):
        event.bintypeJECUp = self.addr_bintype
        event.bintypeIdJECUp = self.addr_bintypeId
        bintype, bintypeId = determin_bintype(event.nJet40JECUp[0], event.nJet100JECUp[0], event.ht40JECUp[0])
        self.addr_bintype[:] = [bintype]
        self.addr_bintypeId[:] = [bintypeId]

##__________________________________________________________________||
