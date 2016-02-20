# Tai Sakuma <tai.sakuma@cern.ch>
from .ScribblerBase import ScribblerBase
from .determin_bintypeId import bintype_name_dict

##__________________________________________________________________||
class bintypeJECDown(ScribblerBase):
    def begin(self, event):
        self.addr_bintype = [ ]
        event.bintypeJECDown = self.addr_bintype

    def event(self, event):
        event.bintypeJECDown = self.addr_bintype
        self.addr_bintype[:] = [bintype_name_dict[event.bintypeIdJECDown[0]]]

##__________________________________________________________________||
