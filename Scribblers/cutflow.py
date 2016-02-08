# Tai Sakuma <tai.sakuma@cern.ch>
from .ScribblerBase import ScribblerBase

##__________________________________________________________________||
class cutflow(ScribblerBase):
    def begin(self, event):
        self.addr_cutflow = [ ]
        self.addr_cutflowId = [ ]
        event.cutflow = self.addr_cutflow
        event.cutflowId = self.addr_cutflowId
        # (nMuoV, nEleV, nPhoV, nMuoS, nEleS, nPhoS)
        self.nObjs_cutflowId_dict = {
            (0, 0, 0, 0, 0, 0) : 1, # 'Signal'
            (1, 0, 0, 1, 0, 0) : 2, # 'SingleMu'
            (2, 0, 0, 2, 0, 0) : 3, # 'DoubleMu'
            (0, 1, 0, 0, 1, 0) : 4, # 'SingleEle'
            (0, 2, 0, 0, 2, 0) : 5, # 'DoubleEle'
            (0, 0, 1, 0, 0, 1) : 6, # 'SinglePhoton'
            }

        self.cutflow_name_dict = {
            1 : 'Signal', 2 : 'SingleMu', 3 : 'DoubleMu',
            4 : 'SingleEle', 5 : 'DoubleEle', 6 : 'SinglePhoton',
            -1 : 'other'
            }

    def event(self, event):
        event.cutflow = self.addr_cutflow
        event.cutflowId = self.addr_cutflowId
        key = (event.nMuonsVeto[0],
               event.nElectronsVeto[0],
               event.nPhotonsVeto[0],
               event.nMuonsSelection[0],
               event.nElectronsSelection[0],
               event.nPhotonsSelection[0]
        )
        if key in self.nObjs_cutflowId_dict:
            cutflowId = self.nObjs_cutflowId_dict[key]
        else:
            cutflowId = -1
        self.addr_cutflowId[:] = [cutflowId]
        self.addr_cutflow[:] = [self.cutflow_name_dict[cutflowId]]

##__________________________________________________________________||
