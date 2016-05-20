# Tai Sakuma <tai.sakuma@cern.ch>
import numpy as np

##__________________________________________________________________||
class jet40pTOverMhtCosDPhi(object):
    def begin(self, event):
        self.mht = [ ]

        self.pt = [ ]
        self.phi = [ ]
        self.ptOverMht = [ ]

        self.dphi = [ ]
        self.cappedDphi = [ ]

        self.sinDphi = [ ]
        self.cosDphi = [ ]

        self.sinCappedDphi = [ ]
        self.cosCappedDphi = [ ]

        self.sinDphiOverF = [ ]
        self.sinCappedDphiOverF = [ ]

        ## self.sinDphiOverFPlusCosDphi = [ ]
        self.sinCappedDphiOverFPlusCosCappedDphi = [ ]

        self.sinCappedDphiLogOneOverF = [ ]

        self._attach_to_event(event)

    def _attach_to_event(self, event):
        event.mht_jet40 = self.mht

        event.jet40_pt = self.pt
        event.jet40_phi = self.phi
        event.jet40_ptOverMht = self.ptOverMht

        event.jet40_dphi = self.dphi
        event.jet40_cappedDphi = self.cappedDphi

        event.jet40_sinDphi = self.sinDphi
        event.jet40_cosDphi = self.cosDphi

        event.jet40_sinCappedDphi = self.sinCappedDphi
        event.jet40_cosCappedDphi = self.cosCappedDphi

        event.jet40_sinDphiOverF = self.sinDphiOverF
        event.jet40_sinCappedDphiOverF = self.sinCappedDphiOverF

        ## event.jet40_sinDphiOverFPlusCosDphi = self.sinDphiOverFPlusCosDphi
        event.jet40_sinCappedDphiOverFPlusCosCappedDphi = self.sinCappedDphiOverFPlusCosCappedDphi

        event.jet40_sinCappedDphiLogOneOverF = self.sinCappedDphiLogOneOverF

    def event(self, event):
        self._attach_to_event(event)

        idxs = [i for i in range(len(event.jet_pt)) if event.jet_pt[i] > 40]
        if not idxs:
            self.pt[:] = [ ]
            self.phi[:] = [ ]
            self.ptOverMht[:] = [ ]
            self.cosDphi[:] = [ ]
            self.sinDphi[:] = [ ]
            self.dphi[:] = [ ]
            self.cappedDphi[:] = [ ]
            self.sinDphiOverF[:] = [ ]
            self.mht[:] = [ ]
            self.sinCappedDphi[:] = [ ]
            self.sinCappedDphiOverF[:] = [ ]
            self.sinCappedDphiLogOneOverF[:] = [ ]
            self.cosCappedDphi[:] = [ ]
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

        self.mht[:] = [mht.item()]

        # the list of cos(Dphi), for each jet
        cos_dphi = (mhtx*px + mhty*py)/(mht*pt)
        self.cosDphi[:] = [e.item() for e in cos_dphi]

        dphi = np.arccos(cos_dphi)
        self.dphi[:] = [e.item() for e in dphi]

        cappedDphi = np.minimum(dphi, np.pi/2.0)
        self.cappedDphi[:] = [e.item() for e in cappedDphi]

        sin_dphi = np.sin(dphi)
        self.sinDphi[:] = [e.item() for e in sin_dphi]

        sin_cappedDphi = np.sin(cappedDphi)
        self.sinCappedDphi[:] = [e.item() for e in sin_cappedDphi]

        cos_cappedDphi = np.cos(cappedDphi)
        self.cosCappedDphi[:] = [e.item() for e in cos_cappedDphi]

        f = pt/mht
        self.ptOverMht[:] = [e.item() for e in f]

        sin_dphi_over_f = sin_dphi/f
        self.sinDphiOverF[:] = [e.item() for e in sin_dphi_over_f]

        sin_cappedDphi_over_f = sin_cappedDphi/f
        self.sinCappedDphiOverF[:] = [e.item() for e in sin_cappedDphi_over_f]

        sin_cappedDphi_over_f_plus_cos_cappedDphi = sin_cappedDphi/(f + cos_cappedDphi)
        self.sinCappedDphiOverFPlusCosCappedDphi[:] = [e.item() for e in sin_cappedDphi_over_f_plus_cos_cappedDphi]

        logf = np.log(f)
        sin_cappedDphi_minus_log_f = sin_cappedDphi*(-logf)
        self.sinCappedDphiLogOneOverF[:] = [e.item() for e in sin_cappedDphi_minus_log_f]

##__________________________________________________________________||
