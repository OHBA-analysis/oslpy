# The OHBA Software Library for the analysis of electrophysiological data (osl-ephys)

Tools for MEG/EEG analysis.

Documentation: https://osl-ephys.readthedocs.io/en/latest/.

## Installation

See the [official documentation](https://osl-ephys.readthedocs.io/en/latest/install.html) for recommended installation instructions.

Alternatively, osl-ephys can be installed from source code within a [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html) (or [Anaconda](https://docs.anaconda.com/free/anaconda/install/index.html)) environment using the following.

### Linux

```
git clone https://github.com/OHBA-analysis/osl-ephys.git
cd osl-ephys
conda env create -f envs/linux.yml
conda activate osle
pip install -e .
```

### Mac

```
git clone https://github.com/OHBA-analysis/osl-ephys.git
cd osl-ephys
conda env create -f envs/mac.yml
conda activate osle
pip install -e .
```

### Oxford-specific computers

If you are installing on an OHBA workstation computer (HBAWS) use:
```
git clone https://github.com/OHBA-analysis/osl-ephys.git
cd osl-ephys
conda env create -f envs/hbaws.yml
conda activate osle
pip install -e .
pip install spyder==5.1.5
```

Or on the BMRC cluster:
```
git clone https://github.com/OHBA-analysis/osl-ephys.git
cd osl-ephys
conda env create -f envs/bmrc.yml
conda activate osle
pip install -e .
```

## Removing OSL

Simply removing the conda environment and delete the repository:
```
conda env remove -n osle
rm -rf osl-ephys
```

## For Developers

Run tests:
```
cd osl_ephys
pytest tests
```
or to run a specific test:
```
cd osl_ephys/tests
pytest test_file_handling.py
```

Build documentation (if `build_sphinx` is not recognised, first try `pip install sphinx==5.3.0`):
```
python setup.py build_sphinx
```
Compiled docs can be found in `doc/build/html/index.html`.
