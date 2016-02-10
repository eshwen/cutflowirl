from .Modules.LambdaStr import LambdaStr
from .bintype_monojet import bintype_monojet
from .bintype_asymjet import bintype_asymjet
from .bintype_symjet import bintype_symjet
from .bintype_highht import bintype_highht
from .biasedDPhi import biasedDPhi
from .biasedDPhi20 import biasedDPhi20

##__________________________________________________________________||
def bintype_biasedDPhi(AllClass, AnyClass, **kargs):

    ret = AllClass(name = 'bintype_biasedDPhi')
    bintypes = AnyClass(name = 'bintypes')
    ret.add(bintypes)

    monojet = AllClass(name = 'monojet')
    asymjet = AllClass(name = 'asymjet')
    symjet = AllClass(name = 'symjet')
    highht = AllClass(name = 'highht')

    bintypes.add(monojet)
    bintypes.add(asymjet)
    bintypes.add(symjet)
    bintypes.add(highht)

    ## monojet
    monojet.add(bintype_monojet(AllClass, AnyClass, **kargs))
    monojet.add(biasedDPhi20(AllClass, AnyClass, **kargs))

    ## asymjet
    asymjet.add(bintype_asymjet(AllClass, AnyClass, **kargs))
    asymjet.add(biasedDPhi(AllClass, AnyClass, **kargs))

    ## symjet
    symjet.add(bintype_symjet(AllClass, AnyClass, **kargs))
    symjet.add(biasedDPhi(AllClass, AnyClass, **kargs))

    ## highht
    highht.add(bintype_highht(AllClass, AnyClass, **kargs))
    highht.add(biasedDPhi(AllClass, AnyClass, **kargs))

    return ret

##__________________________________________________________________||
