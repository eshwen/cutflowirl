# Tai Sakuma <tai.sakuma@cern.ch>
import numpy as np

##__________________________________________________________________||
class jet40pTOverMhtCosDPhi(object):
    def begin(self, event):
        self.pt = [ ]
        self.phi = [ ]
        self.ptOverMht = [ ]
        self.cosDphi = [ ]
        self.dphi = [ ]

        event.jet40_pt = self.pt
        event.jet40_phi = self.phi
        event.jet40_ptOverMht = self.ptOverMht
        event.jet40_cosDphi = self.cosDphi
        event.jet40_dphi = self.dphi

    def event(self, event):
        event.jet40_ptOverMht = self.ptOverMht
        event.jet40_pt = self.pt
        event.jet40_phi = self.phi
        event.jet40_ptOverMht = self.ptOverMht
        event.jet40_cosDphi = self.cosDphi
        event.jet40_dphi = self.dphi

        idxs = [i for i in range(len(event.jet_pt)) if event.jet_pt[i] > 40]

        if not idxs:
            self.pt[:] = [ ]
            self.phi[:] = [ ]
            self.ptOverMht[:] = [ ]
            self.cosDphi[:] = [ ]
            self.dphi = [ ]
            return

        self.pt[:] = [event.jet_pt[i] for i in idxs]
        self.phi[:] = [event.jet_phi[i] for i in idxs]

        pt = np.array(self.pt)
        phi = np.array(self.phi[:])

        px = pt*np.cos(phi)
        py = pt*np.sin(phi)

        # MHT
        mhtx = -np.sum(px)
        mhty = -np.sum(py)
        mht = np.sqrt(mhtx**2 + mhty**2)

        # the list of cos(Dphi), for each jet
        cos_dphi = (mhtx*px + mhty*py)/(mht*pt)
        self.cosDphi[:] = [e.item() for e in cos_dphi]

        dphi = np.arccos(cos_dphi)
        self.dphi[:] = [e.item() for e in dphi]

        f = pt/mht
        self.ptOverMht[:] = [e.item() for e in f]

##__________________________________________________________________||
