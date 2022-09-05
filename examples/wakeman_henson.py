#!/usr/bin/env python

"""Run RHINO-based source recon on Wakeman-Henson dataset.

See run_wakeman_henson.m for matlab equivalent.
"""

import os
import os.path as op

import mne
from mne.beamformer import make_lcmv, apply_lcmv_epochs
from osl import rhino
import glmtools as glm
import h5py
from anamnesis import obj_from_hdf5file
import matplotlib.pyplot as plt
import numpy as np
import osl

base_dir = "/Users/woolrich/homedir/vols_data/WakeHen/"
fif_file_in = op.join(base_dir, "raw/sub001/MEG/run_02_sss.fif")

outbase = op.join(base_dir, "wakehen_glm")
fif_file_preproc = op.join(outbase, "preproc_data/sub001_run_02_sss_raw.fif")

baseline_correct = True
run_compute_surfaces = True
run_coreg = True
run_forward_model = True
run_sensor_space = False

contrast_of_interest = 15

outname = os.path.join(outbase, fif_file_preproc.split("/")[-1])

use_eeg = False
use_meg = True

chantypes = []
chantypes_reject_thresh = {"eog": 250e-6}
rank = {}

if use_eeg:
    chantypes.append("eeg")
    rank.update({"eeg": 30})
    chantypes_reject_thresh.update({"eeg": 250e-6})

if use_meg:
    chantypes.append("mag"),
    chantypes.append("grad"),
    rank.update({"meg": 60})
    chantypes_reject_thresh.update({"mag": 4e-12, "grad": 4000e-13})

print("Channel types to use: {}".format(chantypes))
print("Channel types and ranks for source recon: {}".format(rank))

# ------------- #
# Preprocessing #
# ------------- #

# Load config file
config = """
    meta:
      event_codes:
        famous/first: 5
        famous/immediate: 6
        famous/last: 7
        unfamiliar/first: 13
        unfamiliar/immediate: 14
        unfamiliar/last: 15
        scrambled/first: 17
        scrambled/immediate: 18
        scrambled/last: 19
    preproc:
      - find_events:       {min_duration: 0.005}
      - set_channel_types: {EEG062: eog, EEG062: eog, EEG063: ecg}
      - filter:            {l_freq: 1.1, h_freq: 175}
      - notch_filter:      {freqs: 50 100 150}
      - resample:          {sfreq: 150}
"""

# Run preproc
dataset = osl.preprocessing.run_proc_chain(
    fif_file_in, config, outdir=outbase, overwrite=True
)

dataset["raw"].filter(
    l_freq=1,
    h_freq=30,
    method="iir",
    iir_params={"order": 5, "btype": "bandpass", "ftype": "butter"},
)

epochs = mne.Epochs(
    dataset["raw"],
    dataset["events"],
    dataset["event_id"],
    tmin=-0.5,
    tmax=1.5,
    baseline=(None, 0),
)

epochs.drop_bad(reject=chantypes_reject_thresh)

if use_eeg:
    epochs.set_eeg_reference(ref_channels="average", projection=True)

# ------------------- #
# Setup design matrix #
# ------------------- #

DC = glm.design.DesignConfig()
DC.add_regressor(name="FamousFirst", rtype="Categorical", codes=5)
DC.add_regressor(name="FamousImmediate", rtype="Categorical", codes=6)
DC.add_regressor(name="FamousLast", rtype="Categorical", codes=7)
DC.add_regressor(name="UnfamiliarFirst", rtype="Categorical", codes=13)
DC.add_regressor(name="UnfamiliarImmediate", rtype="Categorical", codes=14)
DC.add_regressor(name="UnfamiliarLast", rtype="Categorical", codes=15)
DC.add_regressor(name="ScrambledFirst", rtype="Categorical", codes=17)
DC.add_regressor(name="ScrambledImmediate", rtype="Categorical", codes=18)
DC.add_regressor(name="ScrambledLast", rtype="Categorical", codes=19)
DC.add_simple_contrasts()
DC.add_contrast(
    name="Famous", values={"FamousFirst": 1, "FamousImmediate": 1, "FamousLast": 1}
)
DC.add_contrast(
    name="Unfamiliar",
    values={"UnfamiliarFirst": 1, "UnfamiliarImmediate": 1, "UnfamiliarLast": 1},
)
DC.add_contrast(
    name="Scrambled",
    values={"ScrambledFirst": 1, "ScrambledImmediate": 1, "ScrambledLast": 1},
)
DC.add_contrast(
    name="FamScram",
    values={
        "FamousFirst": 1,
        "FamousLast": 1,
        "ScrambledFirst": -1,
        "ScrambledLast": -1,
    },
)
DC.add_contrast(
    name="FirstLast",
    values={
        "FamousFirst": 1,
        "FamousLast": -1,
        "ScrambledFirst": 1,
        "ScrambledLast": 1,
    },
)
DC.add_contrast(
    name="Interaction",
    values={
        "FamousFirst": 1,
        "FamousLast": -1,
        "ScrambledFirst": -1,
        "ScrambledLast": 1,
    },
)
DC.add_contrast(
    name="Visual",
    values={
        "FamousFirst": 1,
        "FamousImmediate": 1,
        "FamousLast": 1,
        "UnfamiliarFirst": 1,
        "UnfamiliarImmediate": 1,
        "UnfamiliarLast": 1,
        "ScrambledFirst": 1,
        "ScrambledImmediate": 1,
        "ScrambledLast": 1,
    },
)

print(DC.to_yaml())

data = glm.io.load_mne_epochs(epochs)

# Create Design Matrix
des = DC.design_from_datainfo(data.info)
des.plot_summary(show=True, savepath=outname.replace(".fif", "_design.png"))

# --------------------- #
# Sensor Space Analysis #
# --------------------- #

if run_sensor_space:

    # Create GLM data

    epochs.load_data()
    epochs.pick(chantypes)

    data = glm.io.load_mne_epochs(epochs)

    # ------------------------------------------------------

    # Fit Model
    model_sensor = glm.fit.OLSModel(des, data)

    # Save GLM
    glmname = outname.replace(".fif", "_glm.hdf5")
    out = h5py.File(outname.replace(".fif", "_glm.hdf5"), "w")
    des.to_hdf5(out.create_group("design"))
    data.to_hdf5(out.create_group("data"))
    model_sensor.to_hdf5(out.create_group("model_sensor"))
    out.close()

    # ------------------------------------------------------

    # Load Subj GLM
    model_sensor = obj_from_hdf5file(glmname, "model_sensor")

    # Make MNE object with contrast
    ev = mne.EvokedArray(
        np.abs(model_sensor.copes[contrast_of_interest, :, :]), epochs.info, tmin=-0.5
    )

    if baseline_correct:
        ev.apply_baseline()

    # Plot result
    times = [0.115 + 0.034, 0.17 + 0.034]
    ev.plot_joint(times=times)

# --------------------------------------------------------- #
# Compute info for source recon (coreg, forward model, BEM) #
# --------------------------------------------------------- #

subjects_dir = outbase
subject = "subject1_run2"

# input files
smri_file = op.join(
    "/Users/woolrich/homedir/vols_data/WakeHen", "structurals", "highres001.nii.gz"
)
gridstep = 8  # mm

# Setup polhemus files for coreg
outdir = op.join(subjects_dir, subject)
(
    polhemus_headshape_file,
    polhemus_nasion_file,
    polhemus_rpa_file,
    polhemus_lpa_file,
) = rhino.extract_polhemus_from_info(fif_file_preproc, outdir)

if run_compute_surfaces:
    rhino.compute_surfaces(
        smri_file, subjects_dir, subject, include_nose=False, cleanup_files=True
    )

    rhino.surfaces_display(subjects_dir, subject)

if run_coreg:
    # call rhino
    rhino.coreg(
        fif_file_preproc,
        subjects_dir,
        subject,
        polhemus_headshape_file,
        polhemus_nasion_file,
        polhemus_rpa_file,
        polhemus_lpa_file,
        use_headshape=True,
        use_nose=False,
    )

    # Purple dots are the polhemus derived fiducials
    # Yellow diamonds are the sMRI derived fiducials
    # Position of sMRI derived fiducials are the ones that are refined if
    # useheadshape=True was used for rhino.coreg
    rhino.coreg_display(
        subjects_dir,
        subject,
        plot_type="surf",
        display_outskin_with_nose=False,
        display_sensors=True,
    )

if run_forward_model:
    if use_eeg:
        model = "Triple Layer"
    else:
        model = "Single Layer"

    rhino.forward_model(
        subjects_dir,
        subject,
        model=model,
        eeg=use_eeg,
        meg=use_meg,
        gridstep=gridstep,
        mindist=4.0,
    )

    rhino.bem_display(
        subjects_dir,
        subject,
        plot_type="surf",
        display_outskin_with_nose=False,
        display_sensors=True,
    )

# -------------------------------- #
# Apply source recon to epoch data #
# -------------------------------- #

epochs = mne.Epochs(
    dataset["raw"],
    dataset["events"],
    dataset["event_id"],
    tmin=-0.5,
    tmax=1.5,
    baseline=(None, 0),
)

epochs.drop_bad(reject=chantypes_reject_thresh, verbose=True)

epochs.load_data()

if use_eeg:
    epochs.set_eeg_reference(ref_channels="average", projection=True)

epochs.pick(chantypes)

# make LCMV filter
filters = rhino.make_lcmv(
    subjects_dir,
    subject,
    epochs,
    chantypes,
    reg=0,
    pick_ori="max-power-pre-weight-norm",
    weight_norm="nai",
    rank=rank,
    reduce_rank=True,
    verbose=True,
)

# plot data covariance matrix
filters["data_cov"].plot(epochs.info)

# stc is list of source space trial time series (in head/polhemus space)
stc = apply_lcmv_epochs(epochs, filters)

# ---------------------------- #
# Fit GLM to source recon data #
# ---------------------------- #

# turns this into a ntrials x nsources x ntpts array
sourcespace_epoched_data = []
for trial in stc:
    sourcespace_epoched_data.append(trial.data)
sourcespace_epoched_data = np.stack(sourcespace_epoched_data)

# Create GLM data
data = glm.data.TrialGLMData(data=sourcespace_epoched_data)

# Show Design Matrix
des.plot_summary(show=True, savepath=outname.replace(".fif", "_design.png"))

# ------------------------------------------------------

# Fit Model
model_source = glm.fit.OLSModel(des, data)

# Save GLM
glmname = outname.replace(".fif", "_source_glm.hdf5")
out = h5py.File(outname.replace(".fif", "_source_glm.hdf5"), "w")
des.to_hdf5(out.create_group("design"))
data.to_hdf5(out.create_group("data"))
model_source.to_hdf5(out.create_group("model_source_epochs"))
out.close()

# -------------------------------------- #
# Compute stats of interest from GLM fit #
# -------------------------------------- #

acopes = []

# take abs(cope) due to 180 degree ambiguity in dipole orientation
acope = np.abs(model_source.copes[contrast_of_interest])

# globally normalise by the mean
acope = acope / np.mean(acope)

if baseline_correct:
    baseline_mean = np.mean(
        abs(model_source.copes[contrast_of_interest][:, epochs.times < 0]), 1
    )
    # acope = acope - np.reshape(baseline_mean.T,[acope.shape[0],1])
    acope = acope - np.reshape(baseline_mean, [-1, 1])

acopes.append(acope)

# ----------------------------------------------- #
# Output stats as 3D nii files at tpt of interest #
# ----------------------------------------------- #

stats_dir = op.join(subjects_dir, subject, "rhino", "stats")
if not os.path.isdir(stats_dir):
    os.mkdir(stats_dir)

# output nii nearest to this time point in msecs:
tpt = 0.110 + 0.034
volume_num = epochs.time_as_index(tpt)[0]

out_nii_fname = op.join(
    stats_dir,
    "acope{}_vol{}_mni_{}mm.nii.gz".format(contrast_of_interest, volume_num, gridstep),
)
out_nii_fname, stdbrain_mask_fname = rhino.recon_timeseries2niftii(
    subjects_dir,
    subject,
    recon_timeseries=acopes[0][:, volume_num],
    out_nii_fname=out_nii_fname,
)

rhino.fsleyes_overlay(stdbrain_mask_fname, out_nii_fname)

# ------------------------------------------------------ #
# Plot time course of cope at a specified MNI coordinate #
# ------------------------------------------------------ #

coord_mni = np.array([18, -80, -7])

recon_timeseries = rhino.get_recon_timeseries(
    subjects_dir, subject, coord_mni, acopes[0]
)

plt.figure()
plt.plot(epochs.times, recon_timeseries)
plt.title(
    "abs(cope) for contrast {}, at MNI coord={}mm".format(
        contrast_of_interest, coord_mni
    )
)
plt.xlabel("time (s)")
plt.ylabel("abs(cope)")

# -------------------------------------------------------------------------- #
# Convert cope to standard brain grid in MNI space, for doing group stats    #
# (sourcespace_epoched_data and therefore acopes are in head/polhemus space) #
# -------------------------------------------------------------------------- #

(
    acope_timeseries_mni,
    reference_brain_fname,
    mni_coords_out,
    _,
) = rhino.transform_recon_timeseries(
    subjects_dir, subject, recon_timeseries=acopes[0], reference_brain="mni"
)

# ------------------------------------------------------------------ #
# Write cope as 4D niftii file on a standard brain grid in MNI space #
# 4th dimension is timepoint within a trial                          #
# ------------------------------------------------------------------ #

out_nii_fname = op.join(
    stats_dir, "acope{}_mni_{}mm.nii.gz".format(contrast_of_interest, gridstep)
)
out_nii_fname, stdbrain_mask_fname = rhino.recon_timeseries2niftii(
    subjects_dir,
    subject,
    recon_timeseries=acopes[0],
    out_nii_fname=out_nii_fname,
    reference_brain="mni",
    times=epochs.times,
)

rhino.fsleyes_overlay(stdbrain_mask_fname, out_nii_fname)

# From fsleyes drop down menus Select "View/Time series"
# To see time labelling in secs:
#   - In the Time series panel, select Settings (the spanner icon)
#   - In the Time series settings popup, select "Use Pix Dims"