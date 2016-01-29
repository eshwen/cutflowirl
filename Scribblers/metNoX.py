# Tai Sakuma <tai.sakuma@cern.ch>
from .ScribblerBase import ScribblerBase

##__________________________________________________________________||
class metNoX(ScribblerBase):
    def begin(self, event):
        self.val_pt = [ ]
        self.val_phi = [ ]
        event.metNoX_pt = self.val_pt
        event.metNoX_phi = self.val_phi
        self.itsdict = {
            'Signal': ('met_pt', 'met_phi'),
            'SingleMu': ('metNoMu_pt', 'metNoMu_phi'),
            'DoubleMu': ('metNoMu_pt', 'metNoMu_phi'),
            'SingleEle': ('metNoEle_pt', 'metNoEle_phi'),
            'DoubleEle': ('metNoEle_pt', 'metNoEle_phi'),
            'SinglePhoton': ('metNoPhoton_pt', 'metNoPhoton_phi'),
        }

    def event(self, event):
        event.metNoX_pt = self.val_pt
        event.metNoX_phi = self.val_phi
        cutflow = event.cutflow[0]
        if not cutflow in self.itsdict: cutflow = 'Signal'
        self.val_pt[:] = [getattr(event, self.itsdict[cutflow][0])[0]]
        self.val_phi[:] = [getattr(event, self.itsdict[cutflow][1])[0]]

##__________________________________________________________________||
