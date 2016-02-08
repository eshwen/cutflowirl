#!/usr/bin/env python
from .ScribblerBase import ScribblerBase

##__________________________________________________________________||
class metNoXNoHF(ScribblerBase):
    def begin(self, event):
        self.val_pt = [ ]
        self.val_phi = [ ]
        event.metNoXNoHF_pt = self.val_pt
        event.metNoXNoHF_phi = self.val_phi
        self.itsdict = {
            'Signal': ('metNoHF_pt', 'metNoHF_phi'),
            'SingleMu': ('metNoMuNoHF_pt', 'metNoMuNoHF_phi'),
            'DoubleMu': ('metNoMuNoHF_pt', 'metNoMuNoHF_phi'),
            'SingleEle': ('metNoEleNoHF_pt', 'metNoEleNoHF_phi'),
            'DoubleEle': ('metNoEleNoHF_pt', 'metNoEleNoHF_phi'),
            'SinglePhoton': ('metNoPhotonNoHF_pt', 'metNoPhotonNoHF_phi'),
        }

    def event(self, event):
        event.metNoXNoHF_pt = self.val_pt
        event.metNoXNoHF_phi = self.val_phi
        cutflow = event.cutflow[0]
        if not cutflow in self.itsdict: cutflow = 'Signal'
        self.val_pt[:] = [getattr(event, self.itsdict[cutflow][0])[0]]
        self.val_phi[:] = [getattr(event, self.itsdict[cutflow][1])[0]]

##__________________________________________________________________||
