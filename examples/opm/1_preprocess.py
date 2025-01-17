"""Preprocess OPM data.

"""

# Authors: Chetan Gohil <chetan.gohil@psych.ox.ac.uk>

from osl_ephys import preprocessing

# Preprocessing steps to apply
config = """
    preproc:
    - resample: {sfreq: 150}
    - filter: {l_freq: 4, h_freq: 40, method: iir, iir_params: {order: 5, ftype: butter}}
    - bad_segments: {segment_len: 300, picks: mag, significance_level: 0.25}
    - bad_channels: {picks: meg, significance_level: 0.4}        
"""

# List of fif files to preprocess
inputs = ["raw/13703-braille_test-meg.fif"]

# Subject IDs
subjects = ["13703"]

# Directory to save output to
outdir = "data"

# Do preprocessing
dataset = preprocessing.run_proc_batch(
    config,
    inputs,
    subjects=subjects,
    outdir=outdir,
    overwrite=True,
)
