# Tai Sakuma <tai.sakuma@cern.ch>
import numpy as np

##__________________________________________________________________||
class mmht(object):
    def begin(self, event):

        self.minbDphi = [ ]
        self.minDphi = [ ]
        self.maxDphi = [ ]
        self.maxPtOverMht = [ ]
        self.minSinDphi = [ ]
        self.mhtMinSinDphi = [ ]
        self.minSinDphiOverPtOverMht = [ ]
        self.minSinCappedDphi = [ ]
        self.mhtMinSinCappedDphi = [ ]
        self.minSinCappedDphiOverPtOverMht = [ ]
        self.minSinCappedPulledDphi = [ ]
        self.mhtMinSinCappedPulledDphi = [ ]
        self.minSinCappedPulledDphiOverPtOverMht = [ ]

        self._attach_to_event(event)

    def _attach_to_event(self, event):
        event.minbDphi = self.minbDphi
        event.minDphi = self.minDphi
        event.maxDphi = self.maxDphi
        event.maxPtOverMht = self.maxPtOverMht
        event.minSinDphi = self.minSinDphi
        event.mhtMinSinDphi = self.mhtMinSinDphi
        event.minSinDphiOverPtOverMht = self.minSinDphiOverPtOverMht
        event.minSinCappedDphi = self.minSinCappedDphi
        event.mhtMinSinCappedDphi = self.mhtMinSinCappedDphi
        event.minSinCappedDphiOverPtOverMht = self.minSinCappedDphiOverPtOverMht
        event.minSinCappedPulledDphi = self.minSinCappedPulledDphi
        event.mhtMinSinCappedPulledDphi = self.mhtMinSinCappedPulledDphi
        event.minSinCappedPulledDphiOverPtOverMht = self.minSinCappedPulledDphiOverPtOverMht

    def event(self, event):
        self._attach_to_event(event)
        if len(event.jet40_pt) <= 1:
            self.minbDphi[:] = [-1]
            self.minDphi[:] = [-1]
            self.maxDphi[:] = [-1]
            self.maxPtOverMht[:] = [ ]
            self.minSinDphi[:] = [ ]
            self.mhtMinSinDphi[:] = [ ]
            self.minSinDphiOverPtOverMht[:] = [ ]
            self.minSinCappedDphi[:] = [ ]
            self.mhtMinSinCappedDphi[:] = [ ]
            self.minSinCappedDphiOverPtOverMht[:] = [ ]
            self.minSinCappedPulledDphi[:] = [ ]
            self.mhtMinSinCappedPulledDphi[:] = [ ]
            self.minSinCappedPulledDphiOverPtOverMht[:] = [ ]
            return

        dphi = np.array(event.jet40_dphi)
        self.minDphi[:] = [dphi.min().item()]

        self.maxDphi[:] = [dphi.max().item()]

        f = np.array(event.jet40_ptOverMht)
        self.maxPtOverMht[:] = [f.max().item()]

        cos_dphi = np.array(event.jet40_cosDphi)
        self.minbDphi[:] = [calculate_minbDphi_with_f(f, cos_dphi).item()]

        sin_cappedDphi = np.array(event.jet40_sinCappedDphi)
        min_sin_cappedDphi = sin_cappedDphi.min()
        self.minSinCappedDphi[:] = [min_sin_cappedDphi.item()]

        mht = event.mht_jet40[0]

        mht_min_sin_cappedDphi = mht*min_sin_cappedDphi
        self.mhtMinSinCappedDphi[:] = [mht_min_sin_cappedDphi.item()]

        sin_CappedDphi_over_f = np.array(event.jet40_sinCappedDphiOverPtOverMht)
        min_sin_CappedDphi_over_f = sin_CappedDphi_over_f.min()
        self.minSinCappedDphiOverPtOverMht[:] = [min_sin_CappedDphi_over_f.item()]

        sin_cappedPulledDphi = np.array(event.jet40_sinCappedPulledDphi)
        min_sin_cappedPulledDphi = sin_cappedPulledDphi.min()
        self.minSinCappedPulledDphi[:] = [min_sin_cappedPulledDphi.item()]

        mht_min_sin_cappedPulledDphi = mht*min_sin_cappedPulledDphi
        self.mhtMinSinCappedPulledDphi[:] = [mht_min_sin_cappedPulledDphi.item()]

        sin_CappedPulledDphi_over_f = np.array(event.jet40_sinCappedPulledDphiOverPtOverMht)
        min_sin_CappedPulledDphi_over_f = sin_CappedPulledDphi_over_f.min()
        self.minSinCappedPulledDphiOverPtOverMht[:] = [min_sin_CappedPulledDphi_over_f.item()]

        # sin_dphi = np.array(event.jet40_sinDphi)
        # min_sin_dphi = sin_dphi.min()
        # self.minSinDphi[:] = [min_sin_dphi.item()]
        # 
        # mht_min_sin_dphi = mht*min_sin_dphi
        # self.mhtMinSinDphi[:] = [mht_min_sin_dphi.item()]
        # 
        # sin_dphi_over_f = np.array(event.jet40_sinDphiOverPtOverMht)
        # min_sin_dphi_over_f = sin_dphi_over_f.min()
        # self.minSinDphiOverPtOverMht[:] = [min_sin_dphi_over_f.item()]

##__________________________________________________________________||
def calculate_minbDphi_in_original_way(pt, phi):
    """
    Args:
    pt (numpy.array): a list of jet pT
    phi (numpy.array): a list of jet phi

    Returns:
      the minimum biased Dphi
    """

    # px and py of the jets
    px = pt*np.cos(phi)
    py = pt*np.sin(phi)

    # MHT
    mhtx = -np.sum(px)
    mhty = -np.sum(py)
    mht = np.sqrt(mhtx**2 + mhty**2)

    # the list of cos(Dphi), for each jet
    cos_dphi = (mhtx*px + mhty*py)/(mht*pt)

    # the list of biased MHT
    bmhtx = mhtx + px
    bmhty = mhty + py
    bmht = np.sqrt(bmhtx**2 + bmhty**2)

    # the list of cos(bDphi), for each jet
    cos_bdphi = (bmhtx*px + bmhty*py)/(bmht*pt)

    # the list of bDphi, for each jet
    bdphi = np.arccos(cos_bdphi)

    # the minimum biased Dphi, bDphi_min
    bdphi_min = bdphi.min()
    return bdphi_min

##__________________________________________________________________||
def calculate_minbDphi_with_f(f, cos_dphi):
    """
    Args:
    f (numpy.array): a list of the ratios, jet_pt/MHT
    cos_dphi (numpy.array): a list of cosine of Ddphi(jet, MHT)

    Returns:
      the minimum biased Dphi
    """

    cos_bdphi = (f + cos_dphi)/np.sqrt(1 + f**2 + 2*f*cos_dphi)

    # the list of bDphi, for each jet
    bdphi = np.arccos(cos_bdphi)

    # the minimum biased Dphi, bDphi_min
    bdphi_min = bdphi.min()

    return bdphi_min

##__________________________________________________________________||
