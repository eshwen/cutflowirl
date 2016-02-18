#!/usr/bin/env python
from Scribblers.ScribblerBase import ScribblerBase
from Scribblers.Alias import Alias
from Scribblers.PrimaryDataset import PrimaryDataset
from Scribblers.inCertifiedLumiSections import inCertifiedLumiSections
from Scribblers.cutflow import cutflow
from Scribblers.metNoX import metNoX
from Scribblers.WeightFromTbl import WeightFromTbl
from Scribblers.componentName import componentName
from Scribblers.GenProcess import GenProcess
from Scribblers.njetnbjetbin import njetnbjetbin
from Scribblers.htbin import htbin
from Scribblers.bintype import bintype
from Scribblers.bintypeJECUp import bintypeJECUp
from Scribblers.bintypeJECDown import bintypeJECDown
from Scribblers.metNoXNoHF import metNoXNoHF
from Scribblers.MhtOverMet import MhtOverMet
from Scribblers.MhtOverMetNoHF import MhtOverMetNoHF
from Scribblers.MhtOverMetNoX import MhtOverMetNoX
from Scribblers.MhtOverMetNoXNoHF import MhtOverMetNoXNoHF
from Scribblers.nMuonsIsolated import nMuonsIsolated
from Scribblers.nElectronsIsolated import nElectronsIsolated
from Scribblers.nElectronsBarrel import nElectronsBarrel
from Scribblers.nPhotons200 import nPhotons200
from Scribblers.inEventList import inEventList

##__________________________________________________________________||
def scribbler_configs(datamc, pd, gen_process, json = None, metnohf = False):
    """
    Args:

    datamc: "data" or "mc"

    pd: True or False

    gen_process: True or False

    json: path to json file for certified data

    metnohf: True or False

    """

    ret = [ ]
    if datamc == 'data' and pd:
        ret.append(PrimaryDataset())

    if datamc == 'mc' and gen_process:
        ret.append(GenProcess())

    if datamc == 'data' and json is not None:
        ret.append(inCertifiedLumiSections(json))

    ret.append(cutflow())
    ret.append(metNoX())

    ret.append(njetnbjetbin())
    ret.append(htbin())
    ret.append(bintype())
    ret.append(bintypeJECUp())
    ret.append(bintypeJECDown())
    ret.append(MhtOverMet())
    ret.append(MhtOverMetNoX())

    ret.append(nMuonsIsolated())
    ret.append(nElectronsIsolated())
    ret.append(nElectronsBarrel())
    ret.append(nPhotons200())

    if metnohf:
        ret.append(metNoXNoHF())
        ret.append(MhtOverMetNoHF())
        ret.append(MhtOverMetNoXNoHF())

    return ret

##__________________________________________________________________||
