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
        self.f = [ ]

        self.dphi = [ ]
        self.dphiHat = [ ]

        self.sinDphi = [ ]
        self.cosDphi = [ ]

        self.sinDphiHat = [ ]
        self.cosDphiHat = [ ]

        self.tanOmega = [ ]
        self.omega = [ ]

        self.tanOmegaHat = [ ]
        self.omegaHat = [ ]

        self.tanbDphiHat = [ ]

        self.bDphi = [ ]
        self.sinbDphi = [ ]
        self.cosbDphi = [ ]

        self.g = [ ]
        self.sinDphiTilde = [ ]

        self.tanOmegaTilde = [ ]
        self.omegaTilde = [ ]

        self.k = [ ]

        self.tanChi = [ ]
        self.chi = [ ]

        self.h = [ ]

        self._attach_to_event(event)

    def _attach_to_event(self, event):
        setattr(event, 'mht_{}'.format(self.outJetPrefix), self.mht)

        setattr(event, '{}_pt'.format(self.outJetPrefix), self.pt)

        setattr(event, '{}_phi'.format(self.outJetPrefix), self.phi)
        setattr(event, '{}_f'.format(self.outJetPrefix), self.f)

        setattr(event, '{}_dphi'.format(self.outJetPrefix), self.dphi)
        setattr(event, '{}_dphiHat'.format(self.outJetPrefix), self.dphiHat)

        setattr(event, '{}_sinDphi'.format(self.outJetPrefix), self.sinDphi)
        setattr(event, '{}_cosDphi'.format(self.outJetPrefix), self.cosDphi)

        setattr(event, '{}_sinDphiHat'.format(self.outJetPrefix), self.sinDphiHat)
        setattr(event, '{}_cosDphiHat'.format(self.outJetPrefix), self.cosDphiHat)

        setattr(event, '{}_tanOmega'.format(self.outJetPrefix), self.tanOmega)
        setattr(event, '{}_omega'.format(self.outJetPrefix), self.omega)

        setattr(event, '{}_tanOmegaHat'.format(self.outJetPrefix), self.tanOmegaHat)
        setattr(event, '{}_omegaHat'.format(self.outJetPrefix), self.omegaHat)

        setattr(event, '{}_tanbDphiHat'.format(self.outJetPrefix), self.tanbDphiHat)

        setattr(event, '{}_bDphi'.format(self.outJetPrefix), self.bDphi)
        setattr(event, '{}_sinbDphi'.format(self.outJetPrefix), self.sinbDphi)
        setattr(event, '{}_cosbDphi'.format(self.outJetPrefix), self.cosbDphi)

        setattr(event, '{}_g'.format(self.outJetPrefix), self.g)

        setattr(event, '{}_sinDphiTilde'.format(self.outJetPrefix), self.sinDphiTilde)

        setattr(event, '{}_tanOmegaTilde'.format(self.outJetPrefix), self.tanOmegaTilde)
        setattr(event, '{}_omegaTilde'.format(self.outJetPrefix), self.omegaTilde)

        setattr(event, '{}_k'.format(self.outJetPrefix), self.k)

        setattr(event, '{}_tanChi'.format(self.outJetPrefix), self.tanChi)
        setattr(event, '{}_chi'.format(self.outJetPrefix), self.chi)

        setattr(event, '{}_h'.format(self.outJetPrefix), self.h)

    def event(self, event):
        self._attach_to_event(event)

        event_jet_pt = getattr(event, '{}_pt'.format(self.inJetPrefix))

        idxs = range(len(event_jet_pt))
        if self.minJetPt is not None:
            idxs = [i for i in idxs if event_jet_pt[i] >= self.minJetPt]

        if not idxs:
            self.mht[:] = [ ]
            self.pt[:] = [ ]
            self.phi[:] = [ ]
            self.f[:] = [ ]
            self.dphi[:] = [ ]
            self.dphiHat[:] = [ ]
            self.sinDphi[:] = [ ]
            self.cosDphi[:] = [ ]
            self.sinDphiHat[:] = [ ]
            self.cosDphiHat[:] = [ ]
            self.tanOmega[:] = [ ]
            self.omega[:] = [ ]
            self.tanOmegaHat[:] = [ ]
            self.omegaHat[:] = [ ]
            self.tanbDphiHat[:] = [ ]
            self.bDphi[:] = [ ]
            self.sinbDphi[:] = [ ]
            self.cosbDphi[:] = [ ]
            self.g[:] = [ ]
            self.sinDphiTilde[:] = [ ]
            self.tanOmegaTilde[:] = [ ]
            self.omegaTilde[:] = [ ]
            self.k[:] = [ ]
            self.tanChi[:] = [ ]
            self.chi[:] = [ ]
            self.h[:] = [ ]
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
        cosDphi = (mhtx*px + mhty*py)/(mht*pt)
        cosDphi = np.minimum(cosDphi, 1.0)
        cosDphi = np.maximum(cosDphi, -1.0)
        self.cosDphi[:] = cosDphi

        dphi = np.arccos(cosDphi)
        self.dphi[:] = dphi

        dphiHat = np.minimum(dphi, np.pi/2.0)
        self.dphiHat[:] = dphiHat

        sinDphi = np.sin(dphi)
        self.sinDphi[:] = sinDphi

        sinDphiHat = np.sin(dphiHat)
        self.sinDphiHat[:] = sinDphiHat

        cosDphiHat = np.cos(dphiHat)
        self.cosDphiHat[:] = cosDphiHat

        f = pt/mht
        self.f[:] = f

        tanOmega = sinDphi/f
        self.tanOmega[:] = tanOmega

        omega = np.arctan2(sinDphi, f)
        self.omega[:] = omega

        tanOmegaHat = sinDphiHat/f
        self.tanOmegaHat[:] = tanOmegaHat

        omegaHat = np.arctan2(sinDphiHat, f)
        self.omegaHat[:] = omegaHat

        tanbDphiHat = sinDphiHat/(f + cosDphiHat)
        self.tanbDphiHat[:] = tanbDphiHat

        cosbDphi = (f + cosDphi)/np.sqrt(1 + f**2 + 2*f*cosDphi)
        cosbDphi = np.minimum(cosbDphi, 1.0)
        cosbDphi = np.maximum(cosbDphi, -1.0)
        self.cosbDphi[:] = cosbDphi

        bDphi = np.arccos(cosbDphi)
        self.bDphi[:] = bDphi

        sinbDphi = np.sin(bDphi)
        self.sinbDphi[:] = sinbDphi

        g = np.maximum(cosDphi, -f)
        self.g[:] = g

        sinDphiTilde = np.sqrt(1 + g**2 - 2*g*cosDphi)
        # should be the same as np.where(f + cosDphi >= 0, sinDphi, sinDphi/sinbDphi)
        self.sinDphiTilde[:] = sinDphiTilde

        tanOmegaTilde = sinDphiTilde/f
        self.tanOmegaTilde[:] = tanOmegaTilde

        omegaTilde = np.arctan2(sinDphiTilde, f)
        self.omegaTilde[:] = omegaTilde

        k = np.minimum(f, f + g)
        self.k[:] = k

        tanChi = sinDphiTilde/k
        tanChi = np.minimum(tanChi, 30) # set the maximum 30
        self.tanChi[:] = tanChi

        chi = np.arctan2(sinDphiTilde, k)
        self.chi[:] = chi

        h = np.where(sinDphiTilde == sinDphiTilde.min(), f + g, f)
        self.h[:] = h

##__________________________________________________________________||
