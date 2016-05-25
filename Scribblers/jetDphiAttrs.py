# Tai Sakuma <tai.sakuma@cern.ch>
import numpy as np

##__________________________________________________________________||
class jetDphiAttrs(object):
    def __init__(self, inJetPrefix, outJetPrefix, minJetPt = None):
        self.inJetPrefix = inJetPrefix
        self.outJetPrefix = outJetPrefix
        self.minJetPt = minJetPt

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

        self.sinCappedDphiOverFPlusCosCappedDphi = [ ]

        self.sinCappedDphiLogOneOverF = [ ]

        self._attach_to_event(event)

    def _attach_to_event(self, event):
        setattr(event, 'mht_{}'.format(self.outJetPrefix), self.mht)

        setattr(event, '{}_pt'.format(self.outJetPrefix), self.pt)

        setattr(event, '{}_phi'.format(self.outJetPrefix), self.phi)
        setattr(event, '{}_ptOverMht'.format(self.outJetPrefix), self.ptOverMht)

        setattr(event, '{}_dphi'.format(self.outJetPrefix), self.dphi) 
        setattr(event, '{}_cappedDphi'.format(self.outJetPrefix), self.cappedDphi) 

        setattr(event, '{}_sinDphi'.format(self.outJetPrefix), self.sinDphi) 
        setattr(event, '{}_cosDphi'.format(self.outJetPrefix), self.cosDphi) 

        setattr(event, '{}_sinCappedDphi'.format(self.outJetPrefix), self.sinCappedDphi) 
        setattr(event, '{}_cosCappedDphi'.format(self.outJetPrefix), self.cosCappedDphi) 

        setattr(event, '{}_sinDphiOverF'.format(self.outJetPrefix), self.sinDphiOverF)
        setattr(event, '{}_sinCappedDphiOverF'.format(self.outJetPrefix), self.sinCappedDphiOverF) 

        setattr(event, '{}_sinCappedDphiOverFPlusCosCappedDphi'.format(self.outJetPrefix), self.sinCappedDphiOverFPlusCosCappedDphi) 

        setattr(event, '{}_sinCappedDphiLogOneOverF'.format(self.outJetPrefix), self.sinCappedDphiLogOneOverF) 

    def event(self, event):
        self._attach_to_event(event)

        event_jet_pt = getattr(event, '{}_pt'.format(self.inJetPrefix))

        idxs = range(len(event_jet_pt))
        if self.minJetPt is not None:
            idxs = [i for i in idxs if event_jet_pt[i] >= self.minJetPt]

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

        self.pt[:] = [event_jet_pt[i] for i in idxs]

        event_jet_phi = getattr(event, '{}_phi'.format(self.inJetPrefix))
        self.phi[:] = [event.jet_phi[i] for i in idxs]

        pt = np.array(self.pt)
        phi = np.array(self.phi)

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
