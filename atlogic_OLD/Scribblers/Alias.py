# Tai Sakuma <tai.sakuma@cern.ch>

##__________________________________________________________________||
class Alias(object):
    def __init__(self, src, alias):
        self.src = src
        self.alias = alias

    def __repr__(self):
        name_value_pairs = (
            ('src', self.src),
            ('alias', self.alias),
        )
        return '{}({})'.format(
            self.__class__.__name__,
            ', '.join(['{} = {!r}'.format(n, v) for n, v in name_value_pairs]),
        )

    def begin(self, event):
        setattr(event, self.alias, getattr(event, self.src))

    def event(self, event):
        setattr(event, self.alias, getattr(event, self.src))

##__________________________________________________________________||
