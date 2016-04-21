# Tai Sakuma <tai.sakuma@cern.ch>
import numpy as np

##__________________________________________________________________||
class tbDphi(object):
    def begin(self, event):
        self.minTbDphia50b1 = [ ]
        event.minTbDphia50b1 = self.minTbDphia50b1

        self.minTbDphiKink = [ ]
        event.minTbDphiKink = self.minTbDphiKink

        self.minTbDphiKink1p4 = [ ]
        event.minTbDphiKink1p4 = self.minTbDphiKink1p4

        self.minFtbDphiKink = [ ]
        event.minFtbDphiKink = self.minFtbDphiKink

        self.g = G()
        self.g2 = lambda x: np.minimum(x, 1.0)
        self.g3 = lambda x: np.minimum(x, 1.4)

        self.minbDphi = [ ]
        event.minbDphi = self.minbDphi

        self.minDphi = [ ]
        event.minDphi = self.minDphi

        self.maxPtOverMht = [ ]
        event.maxPtOverMht = self.maxPtOverMht

        self.minSinDphi = [ ]
        event.minSinDphi = self.minSinDphi

        self.mhtMinSinDphi = [ ]
        event.mhtMinSinDphi = self.mhtMinSinDphi

        self.minSinDphiOverPtOverMht = [ ]
        event.minSinDphiOverPtOverMht = self.minSinDphiOverPtOverMht

        self.minSinCappedDphi = [ ]
        event.minSinCappedDphi = self.minSinCappedDphi

        self.mhtMinSinCappedDphi = [ ]
        event.mhtMinSinCappedDphi = self.mhtMinSinCappedDphi

        self.minSinCappedDphiOverPtOverMht = [ ]
        event.minSinCappedDphiOverPtOverMht = self.minSinCappedDphiOverPtOverMht

    def event(self, event):
        event.minTbDphia50b1 = self.minTbDphia50b1
        event.minTbDphiKink = self.minTbDphiKink
        event.minTbDphiKink1p4 = self.minTbDphiKink1p4
        event.minFtbDphiKink = self.minFtbDphiKink
        event.minbDphi = self.minbDphi
        event.minDphi = self.minDphi
        event.maxPtOverMht = self.maxPtOverMht
        event.minSinDphi = self.minSinDphi
        event.mhtMinSinDphi = self.mhtMinSinDphi
        event.minSinDphiOverPtOverMht = self.minSinDphiOverPtOverMht
        event.minSinCappedDphi = self.minSinCappedDphi
        event.mhtMinSinCappedDphi = self.mhtMinSinCappedDphi
        event.minSinCappedDphiOverPtOverMht = self.minSinCappedDphiOverPtOverMht

        if len(event.jet40_pt) <= 1:
            self.minTbDphia50b1[:] = [-1]
            self.minTbDphiKink[:] = [-1]
            self.minTbDphiKink1p4[:] = [-1]
            self.minFtbDphiKink[:] = [-1]
            self.minbDphi[:] = [-1]
            self.minDphi[:] = [-1]
            self.maxPtOverMht[:] = [ ]
            self.minSinDphi[:] = [ ]
            self.mhtMinSinDphi[:] = [ ]
            self.minSinDphiOverPtOverMht[:] = [ ]
            self.minSinCappedDphi[:] = [ ]
            self.mhtMinSinCappedDphi[:] = [ ]
            self.minSinCappedDphiOverPtOverMht[:] = [ ]
            return

        dphi = np.array(event.jet40_dphi)
        self.minDphi[:] = [dphi.min().item()]

        f = np.array(event.jet40_ptOverMht)
        self.maxPtOverMht[:] = [f.max().item()]

        sin_dphi = np.array(event.jet40_sinDphi)
        min_sin_dphi = sin_dphi.min()
        self.minSinDphi[:] = [min_sin_dphi.item()]

        mht = event.mht_jet40[0]
        mht_min_sin_dphi = mht*min_sin_dphi
        self.mhtMinSinDphi[:] = [mht_min_sin_dphi.item()]

        sin_dphi_over_f = np.array(event.jet40_sinDphiOverPtOverMht)
        min_sin_dphi_over_f = sin_dphi_over_f.min()
        self.minSinDphiOverPtOverMht[:] = [min_sin_dphi_over_f.item()]

        sin_cappedDphi = np.array(event.jet40_sinCappedDphi)
        min_sin_cappedDphi = sin_cappedDphi.min()
        self.minSinCappedDphi[:] = [min_sin_cappedDphi.item()]

        mht_min_sin_cappedDphi = mht*min_sin_cappedDphi
        self.mhtMinSinCappedDphi[:] = [mht_min_sin_cappedDphi.item()]

        sin_CappedDphi_over_f = np.array(event.jet40_sinCappedDphiOverPtOverMht)
        min_sin_CappedDphi_over_f = sin_CappedDphi_over_f.min()
        self.minSinCappedDphiOverPtOverMht[:] = [min_sin_CappedDphi_over_f.item()]

        cos_dphi = np.array(event.jet40_cosDphi)

        # indices of the jets to be used
        idxs = [i for i in range(len(event.jet_pt)) if event.jet_pt[i] > 40]

        # read pT and phi for the jets for the indices from the event
        pt = np.array([event.jet_pt[i] for i in idxs])
        phi = np.array([event.jet_phi[i] for i in idxs])

        minTbDphia50b1 = calculate_mintbDphi(f, cos_dphi, self.g)
        minTbDphia50b1 = minTbDphia50b1.item() # convert numpy.dtype to python native type
        self.minTbDphia50b1[:] = [minTbDphia50b1]

        self.minTbDphiKink[:] = [calculate_mintbDphi(f, cos_dphi, self.g2).item()]
        self.minTbDphiKink1p4[:] = [calculate_mintbDphi(f, cos_dphi, self.g3).item()]

        self.minbDphi[:] = [calculate_minbDphi_with_f(f, cos_dphi).item()]

        self.minFtbDphiKink[:] = [calculate_minftbDphi(f, cos_dphi, self.g2).item()]



    def end(self):
        self.g2 = None
        self.g3 = None

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
class G(object):
    def __init__(self, a = 50, b = 1):
        self.a = a
        self.b = b

    def __call__(self, f):
        numer = self.a*(f - self.b + 1.0/(self.a*self.b))
        numer = numer - np.sqrt(self.a**2*(f - self.b + 1.0/(self.a*self.b))**2 + 4.0*self.a)
        g = numer/(2.0*self.a) + self.b
        return g

##__________________________________________________________________||
def calculate_mintbDphi(f, cos_dphi, g):
    """
    Args:
    f (numpy.array): a list of the ratios, jet_pt/MHT
    cos_dphi (numpy.array): a list of cosine of Ddphi(jet, MHT)
    g (function): a function of f (= pt/mht)
    
    Returns:
      the minimum tunable biased Dphi (tbDphi)
    """

    f = g(f)

    cos_tbdphi = (f + cos_dphi)/np.sqrt(1 + f**2 + 2*f*cos_dphi)
    
    # the list of tbdphi, for each jet
    tbdphi = np.arccos(cos_tbdphi)

    # the minimum biased Dphi, tbDphi_min
    tbdphi_min = tbdphi.min()

    return tbdphi_min

##__________________________________________________________________||
def calculate_minftbDphi(f, cos_dphi, G):
    """
    Args:
    f (numpy.array): a list of the ratios, jet_pt/MHT
    cos_dphi (numpy.array): a list of cosine of Ddphi(jet, MHT)
    G (function): a function of f (= pt/mht)
    
    Returns:
      the minimum flipped tunable biased Dphi (tbDphi)
    """

    g = G(f)

    cos_dphi_f = np.where(f > 1, np.absolute(cos_dphi), cos_dphi)

    cos_tbdphi = (g + cos_dphi_f)/np.sqrt(1 + g**2 + 2*g*cos_dphi_f)
    
    # the list of tbdphi, for each jet
    tbdphi = np.arccos(cos_tbdphi)

    # the minimum biased Dphi, tbDphi_min
    tbdphi_min = tbdphi.min()

    return tbdphi_min

##__________________________________________________________________||
