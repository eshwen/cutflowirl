# Tai Sakuma <tai.sakuma@cern.ch>

##__________________________________________________________________||
class inEventList(object):
    def __init__(self, event_list_paths, branch_name):
        self.branch_name = branch_name
        self.event_list_paths = event_list_paths

        self.eventList = set()
        for path in self.event_list_paths:
            self.eventList.update({l.strip() for l in open(path)})
            # self.eventList.update({tuple([int(w) for w in l.strip().split(':')]) for l in open(path)})

    def begin(self, event):
        self.vals = [ ]
        setattr(event, self.branch_name, self.vals)

#         self.eventList = set()
#         for path in self.event_list_paths:
#             self.eventList.update({tuple([int(w) for w in l.strip().split(':')]) for l in open(path)})
#             # set of tuples of (run, lumi, evt)
#             # e.g., set([(260627, 1708, 3096828758), (260627, 1708, 3097158216)])


    def event(self, event):
        setattr(event, self.branch_name, self.vals)
        # self.vals[:] = [(event.run[0], event.lumi[0], event.evt[0]) in self.eventList]
        self.vals[:] = ["{}:{}:{}".format(event.run[0], event.lumi[0], event.evt[0]) in self.eventList]
#        if self.vals[0]:
#            print (event.run[0], event.lumi[0], event.evt[0]), self.vals[0]

    def end(self):
        self.eventList = None

##__________________________________________________________________||
