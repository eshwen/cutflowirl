from ...EventSelectionModules.cutflows import cutflows
from ...EventSelectionModules.EventSelectionAll import EventSelectionAll
from ...EventSelectionModules.EventSelectionAny import EventSelectionAny
from ...EventSelectionModules.LambdaStr import LambdaStr
import unittest

##__________________________________________________________________||
class Test_cutflows(unittest.TestCase):

    def test_call(self):
        kargs = dict(
            datamc = 'mc',
            metnohf = False,
            arg1 = 10,
            cutflows = (
                ('test_cutflow1', dict(
                    kargs = dict(arg1 = 31, arg2 = 52, arg3 = 102),
                    levels = (
                        ('level1', dict(arg1 = 1, arg2 = 2)),
                        'level2')
                )),
                ('test_cutflow2', dict(levels = ('level1', 'level2'))),
                'test_cutflow3',
                ('test_cutflow4', dict(kargs = dict(arg1 = 11, arg2 = 22))),
            ))

        es = cutflows(EventSelectionAll, EventSelectionAny, **kargs)
        ## print test_event_selection_str(es)

##__________________________________________________________________||
def test_event_selection_str(eventSelection):
    out = test_event_selection_io(eventSelection)
    return out.getvalue()

##__________________________________________________________________||
def test_event_selection_io(eventSelection, out = None, prep = ''):

    if out is None:
        import StringIO
        out = StringIO.StringIO()

    import inspect

    def print_name(es):
        ret = '<'
        if hasattr(es, 'name'):
            ret += str(es.name)
        ret += (':')
        if inspect.isfunction(es):
            ret += es.__name__
        else:
            ret += es.__class__.__name__
        ret += '>'
        return ret

    out.write(prep)

    if isinstance(eventSelection, LambdaStr):
        out.write(print_name(eventSelection))
        out.write(' ')
        out.write(eventSelection.lambda_str)
        out.write('\n')
        return out

    if isinstance(eventSelection, EventSelectionAll):
        out.write(print_name(eventSelection))
        out.write('\n')
        for e in eventSelection.selections:
            test_event_selection_io(e, out, prep + '  ')
        return out

    if isinstance(eventSelection, EventSelectionAny):
        out.write(print_name(eventSelection))
        out.write('\n')
        for e in eventSelection.selections:
            test_event_selection_io(e, out, prep + '  ')
        return out

    out.write(print_name(eventSelection))
    out.write('\n')
    return out

##__________________________________________________________________||
