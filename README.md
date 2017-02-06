### a quick example


Move to a work dir:
```bash
cd /some/work/dir/
```

The code runs in any envriomment with Python 2.7, ROOT 6, and several other common libraries.

In this example, we will run in `cmsenv`. 

Source `cmsset_default.sh` if it is not done yet.
```bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
```

Check out `cmsenv` if it is not done yet.
```bash
export SCRAM_ARCH=slc6_amd64_gcc530
cmsrel CMSSW_8_0_26
```

Enter the `cmsenv`:
```bash
cd CMSSW_8_0_26/src/
cmsenv
cd ../../
```

Check out this repo:
```bash
git clone git@github.com:TaiSakuma/cutflowirl.git
```

Check out submodules:
```bash
cd cutflowirl
git submodule init
git submodule update
cd ..
```

Run:
```bash
./cutflowirl/twirl_mktbl.py --components SMS_T1tttt_madgraphMLM --max-events-per-process 500000 --logging-level INFO --parallel-mode htcondor
```

A cutflow table is created at `tbl/out/tbl_cutflow.txt`
```bash
cat tbl/out/tbl_cutflow.txt
```

Remove a temporary dir if you don't need:
```bash
rm -rf _ccsp_temp/
```
