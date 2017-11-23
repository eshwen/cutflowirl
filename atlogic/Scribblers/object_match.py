# Tai Sakuma <tai.sakuma@cern.ch>
import numpy as np
import itertools

##__________________________________________________________________||
class ObjectMatch(object):
    def __init__(self,
                 obj1_eta, obj1_phi,
                 obj2_eta, obj2_phi,
                 deltaR = 0.4,
                 obj1_vars = [ ],
                 obj2_vars = [ ],
                 obj1_matched_vars = [ ],
                 obj2_matched_sorted_vars = [ ],
                 obj1_unmatched_vars = None,
                 obj2_unmatched_vars = None
    ):
        self.obj1_eta_name = obj1_eta
        self.obj1_phi_name = obj1_phi
        self.obj2_eta_name = obj2_eta
        self.obj2_phi_name = obj2_phi
        self.deltaR = deltaR
        self.obj1_var_names = obj1_vars
        self.obj2_var_names = obj2_vars
        self.obj1_matched_var_names = obj1_matched_vars
        self.obj2_matched_sorted_var_names = obj2_matched_sorted_vars
        self.obj1_unmatched_var_names = obj1_unmatched_vars
        self.obj2_unmatched_var_names = obj2_unmatched_vars

    def __repr__(self):
        return '{}(obj1_eta = {!r}, obj1_phi = {!r}, obj2_eta = {!r}, obj2_phi = {!r}, deltaR = {!r}, obj1_vars = {!r}, obj2_vars = {!r}, obj1_matched_vars = {!r}, obj2_matched_sorted_vars = {!r}, obj1_unmatched_vars = {!r}, obj2_unmatched_vars = {!r})'.format(
            self.__class__.__name__,
            self.obj1_eta_name,
            self.obj1_phi_name,
            self.obj2_eta_name,
            self.obj2_phi_name,
            self.deltaR,
            self.obj1_var_names,
            self.obj2_var_names,
            self.obj1_matched_var_names,
            self.obj2_matched_sorted_var_names,
            self.obj1_unmatched_var_names,
            self.obj2_unmatched_var_names
        )

    def begin(self, event):
        for n in self.obj1_matched_var_names:
            setattr(self, n, [ ])

        if self.obj2_matched_sorted_var_names is not None:
            for n in self.obj2_matched_sorted_var_names:
                setattr(self, n, [ ])

        if self.obj1_unmatched_var_names is not None:
            for n in self.obj1_unmatched_var_names:
                setattr(self, n, [ ])

        if self.obj2_unmatched_var_names is not None:
            for n in self.obj2_unmatched_var_names:
                setattr(self, n, [ ])

        self._attach_to_event(event)

    def _attach_to_event(self, event):

        for n in self.obj1_matched_var_names:
            setattr(event, n, getattr(self, n))

        if self.obj2_matched_sorted_var_names is not None:
            for n in self.obj2_matched_sorted_var_names:
                setattr(event, n, getattr(self, n))

        if self.obj1_unmatched_var_names is not None:
            for n in self.obj1_unmatched_var_names:
                setattr(event, n, getattr(self, n))

        if self.obj2_unmatched_var_names is not None:
            for n in self.obj2_unmatched_var_names:
                setattr(event, n, getattr(self, n))

    def event(self, event):
        self._attach_to_event(event)
        self._obj1_eta = event.genJet_eta
        self._obj1_phi = event.genJet_phi
        self._obj2_eta = event.jet_eta
        self._obj2_phi = event.jet_phi
        idx1 = range(len(self._obj1_eta))
        idx2 = range(len(self._obj2_eta))
        idx_pairs = itertools.product(idx1, idx2)
        idx_pairs = [(i1, i2) for i1, i2 in idx_pairs if self._match(i1, i2)]
        if idx_pairs:
            idx1_matched, idx2_matched = zip(*idx_pairs)
        else:
            idx1_matched, idx2_matched = [ ], [ ]

        idx1_unmatched = [i for i in idx1 if i not in idx1_matched]
        idx2_unmatched = [i for i in idx2 if i not in idx2_matched]

        for nin, nout in zip(self.obj1_var_names, self.obj1_matched_var_names):
            getattr(self, nout)[:] = [getattr(event, nin)[i] for i in idx1_matched]

        if self.obj2_matched_sorted_var_names is not None:
            for nin, nout in zip(self.obj2_var_names, self.obj2_matched_sorted_var_names):
                getattr(self, nout)[:] = [getattr(event, nin)[i] for i in idx2_matched]

        if self.obj1_unmatched_var_names is not None:
            for nin, nout in zip(self.obj1_var_names, self.obj1_unmatched_var_names):
                getattr(self, nout)[:] = [getattr(event, nin)[i] for i in idx1_unmatched]

        if self.obj2_unmatched_var_names is not None:
            for nin, nout in zip(self.obj2_var_names, self.obj2_unmatched_var_names):
                getattr(self, nout)[:] = [getattr(event, nin)[i] for i in idx2_unmatched]

    def _match(self, i1, i2):
        return self._deltaR(
            self._obj1_eta[i1], self._obj1_phi[i1],
            self._obj2_eta[i2], self._obj2_phi[i2]
        ) <= self.deltaR

    def _deltaR(self, eta1, phi1, eta2, phi2):
        deta = eta1 - eta2
        dphi = self._deltaPhi(phi1, phi2)
        return np.sqrt(deta*deta + dphi*dphi)

    def _deltaPhi(self, phi1, phi2):
        ret = phi1 - phi2
        while ret > 2*np.pi:
            ret -= 2*np.pi
        while ret < -2*np.pi:
            ret += 2*np.pi
        return ret

    def end(self):
        pass

##__________________________________________________________________||
