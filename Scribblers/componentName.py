# Tai Sakuma <tai.sakuma@cern.ch>
from .ScribblerBase import ScribblerBase

##__________________________________________________________________||
class componentName(ScribblerBase):
    def begin(self, event):
        self.vals = [ ]
        event.componentName = self.vals

        self.vals[:] = [event.component.name]
        # e.g., "HTMHT_Run2015D_PromptReco_25ns"

    def event(self, event):
        event.componentName = self.vals

##__________________________________________________________________||
