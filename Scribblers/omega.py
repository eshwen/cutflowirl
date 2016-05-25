# Tai Sakuma <tai.sakuma@cern.ch>
import numpy as np

##__________________________________________________________________||
class omega(object):
    def begin(self, event):
        self.minTanOmega = [ ]
        self.minFTanOmega = [ ]
        self.mhtMinFTanOmega = [ ]

        self.minTanChi = [ ]

        self.minTanKappa = [ ]
        self.logMinTanKappa = [ ]

        self.minTanXi = [ ]
        self.tanZeta = [ ]

        self._attach_to_event(event)

    def _attach_to_event(self, event):
        event.minTanOmega = self.minTanOmega
        event.minFTanOmega = self.minFTanOmega
        event.mhtMinFTanOmega = self.mhtMinFTanOmega

        event.minTanChi = self.minTanChi

        event.minTanKappa = self.minTanKappa
        event.logMinTanKappa = self.logMinTanKappa

        event.minTanXi = self.minTanXi
        event.tanZeta = self.tanZeta

        pass

    def event(self, event):
        self._attach_to_event(event)
        if len(event.jet40_pt) <= 1:
            self.minTanOmega[:] = [-1]
            self.minTanChi[:] = [-1]
            self.minTanKappa[:] = [-1]
            self.minFTanOmega[:] = [-1]
            self.mhtMinFTanOmega[:] = [-1]
            self.logMinTanKappa[:] = [-1]
            self.minTanXi[:] = [-1]
            self.tanZeta[:] = [-1]
            return

        mht = event.mht_jet40[0]
        f = np.array(event.jet40_ptOverMht)
        sin_dphi = np.array(event.jet40_sinDphi)
        cos_dphi = np.array(event.jet40_cosDphi)

        sin_cappedDphi = np.array(event.jet40_sinCappedDphi)

        g = np.minimum(f, -cos_dphi)
        fTanOmega = np.sqrt(1 + g**2 + 2*g*cos_dphi)

        tanOmega = fTanOmega/f
        minTanOmega = tanOmega.min()
        self.minTanOmega[:] = [minTanOmega.item()]

        ff = np.minimum(f, f - g)
        tanChi = fTanOmega/ff
        minTanChi = tanChi.min()
        minTanChi = np.where(minTanChi < 10, minTanChi, 10) # set the maximum 10
        self.minTanChi[:] = [minTanChi.item()]

        minFTanOmega = fTanOmega.min()
        self.minFTanOmega[:] = [minFTanOmega.item()]

        mhtMinFTanOmega = mht*minFTanOmega
        self.mhtMinFTanOmega[:] = [mhtMinFTanOmega.item()]

        denom = np.where(f - g > 0, f - g, 0.0001) # avoid divide by zero
        tanKappa = fTanOmega/denom
        minTanKappa = tanKappa.min()
        self.minTanKappa[:] = [minTanKappa.item()]
        self.logMinTanKappa[:] = [np.log(minTanKappa).item()]

        f_modified = np.where(fTanOmega == minFTanOmega, f - g, f)
        denom = f_modified.max()
        denom = np.where(denom > 0, denom, 0.0001) # avoid divide by zero
        minTanXi = minFTanOmega/denom
        self.minTanXi[:] = [minTanXi.item()]

        tanZeta = np.where(all(cos_dphi <= 0), 1/f.max(), minTanXi)
        self.tanZeta[:] = [tanZeta.item()]

        ## if not all(cos_dphi <= 0): return
        ## print cos_dphi
        ## print event.minTanXi, event.tanZeta

        ## if all(np.abs(s - sin_dphi) < 0.00001): return
        # if  np.abs(s.min() - sin_cappedDphi.min()) < 0.00001: return
        # print s.min(), sin_cappedDphi.min()
        # print sin_dphi
        # print f
        # print sin_cappedDphi
        # print s
        # print self.minTanOmega[0]
        # print tanOmega
        # print tanKappa

##__________________________________________________________________||
