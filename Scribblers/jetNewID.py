# Eshwen Bhal <eshwen.bhal@cern.ch>

##__________________________________________________________________||                                                                                                    
class jetNewID(object):
    """
    This module runs over the entries in jet_newId for each event. If
    it comes across a failed ID (where its value is zero or negative)
    in the array, the whole event fails the cut. Else, it returns the
    value of 1 to the first element of the list "jetNewID".
    """
    def begin(self, event):
        self.vals = [ ]
        event.jetNewID = self.vals

    def event(self, event):
        event.jetNewID = self.vals
        for jet in range(0, len(event.jet_newId)):
            if event.jet_newId[jet] <= 0 and event.jet_pt[jet] > 40:
                self.vals[:] = [0]
                return
        self.vals[:] = [1]

##__________________________________________________________________||                                                                                                    

