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

    def event(self, event):
        event.minTbDphia50b1 = self.minTbDphia50b1
        event.minTbDphiKink = self.minTbDphiKink
        event.minTbDphiKink1p4 = self.minTbDphiKink1p4
        event.minFtbDphiKink = self.minFtbDphiKink

        if len(event.jet40_pt) <= 1:
            self.minTbDphia50b1[:] = [-1]
            self.minTbDphiKink[:] = [-1]
            self.minTbDphiKink1p4[:] = [-1]
            self.minFtbDphiKink[:] = [-1]
            return

        f = np.array(event.jet40_ptOverMht)

        cos_dphi = np.array(event.jet40_cosDphi)

        minTbDphia50b1 = calculate_mintbDphi(f, cos_dphi, self.g)
        minTbDphia50b1 = minTbDphia50b1.item() # convert numpy.dtype to python native type
        self.minTbDphia50b1[:] = [minTbDphia50b1]

        self.minTbDphiKink[:] = [calculate_mintbDphi(f, cos_dphi, self.g2).item()]
        self.minTbDphiKink1p4[:] = [calculate_mintbDphi(f, cos_dphi, self.g3).item()]

        self.minFtbDphiKink[:] = [calculate_minftbDphi(f, cos_dphi, self.g2).item()]

    def end(self):
        self.g2 = None
        self.g3 = None

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
