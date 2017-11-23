# Tai Sakuma <tai.sakuma@cern.ch>

##__________________________________________________________________||
class cutflow(object):
    def __repr__(self):
        return '{}()'.format(self.__class__.__name__)

    def begin(self, event):
        self.addr_cutflow = [ ]
        event.cutflow = self.addr_cutflow

        self.cutflow_name_dict = {
            1 : 'Signal', 2 : 'SingleMu', 3 : 'DoubleMu',
            4 : 'SingleEle', 5 : 'DoubleEle', 6 : 'SinglePhoton',
            -1 : 'other'
            }

    def event(self, event):
        event.cutflow = self.addr_cutflow
        self.addr_cutflow[:] = [self.cutflow_name_dict[event.cutflowId[0]]]

##__________________________________________________________________||
