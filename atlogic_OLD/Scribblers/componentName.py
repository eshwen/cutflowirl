# Tai Sakuma <tai.sakuma@cern.ch>

##__________________________________________________________________||
class componentName(object):

    def __repr__(self):
        return '{}()'.format(
            self.__class__.__name__,
        )

    def begin(self, event):
        self.vals = [ ]
        event.componentName = self.vals

        self.vals[:] = [event.component.name]
        # e.g., "HTMHT_Run2015D_PromptReco_25ns"

    def event(self, event):
        event.componentName = self.vals

##__________________________________________________________________||
