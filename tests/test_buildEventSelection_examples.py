from ..buildEventSelection import buildEventSelection
from ..EventSelectionLevels.Modules.EventSelectionAll import EventSelectionAll
from ..EventSelectionLevels.Modules.EventSelectionAny import EventSelectionAny
from ..EventSelectionLevels.Modules.LambdaStr import LambdaStr

import unittest

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

    if hasattr(eventSelection, 'lambda_str'):
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
class Test_buildEventSelection_examples(unittest.TestCase):

    def test_call_001(self):

        es = buildEventSelection(
            datamc = 'data',
            levels = (
                'PD_HLT',
                'baseline_kinematics',
                'met_filters',
                'unique_promptPhoton_phaseSpace_in_QCD_and_GJets',
            )
        )

    def test_call_002(self):

        es = buildEventSelection(
            datamc = 'data',
            levels = (
                'PD_HLT',
                'baseline_kinematics',
                ('cutflows', dict(
                    cutflows = (
                        ('Signal', dict(levels = ('Id', 'PD', 'loose'))),
                        ('SingleMu', dict(levels = ('Id', 'PD'))),
                        ('DoubleMu', dict(levels = ('Id', 'PD'))),
                        ('SingleEle', dict(levels = ('Id', 'PD'))),
                        ('DoubleEle', dict(levels = ('Id', 'PD'))),
                        ('SinglePhoton', dict(levels = ('Id', 'PD', 'loose'))),
                    ))),
                )
        )

    def test_call_003(self):

        es = buildEventSelection(
            datamc = 'mc',
            levels = (
                'PD_HLT',
                'baseline_kinematics_loose_JECvariation',
                ('cutflows', dict(
                    cutflows = (
                        ('Signal', dict(levels = ('Id', 'PD', 'loose_JECvariation'))),
                        ('SingleMu', dict(levels = ('Id', 'PD'))),
                        ('DoubleMu', dict(levels = ('Id', 'PD'))),
                        ('SingleEle', dict(levels = ('Id', 'PD'))),
                        ('DoubleEle', dict(levels = ('Id', 'PD'))),
                        ('SinglePhoton', dict(levels = ('Id', 'PD', 'loose_JECvariation'))),
                        ('BaselineMu', dict(levels = ('Id', 'PD'))),
                    ))),
                )
        )
        # print test_event_selection_str(es)

##__________________________________________________________________||
