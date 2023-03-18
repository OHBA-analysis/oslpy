"""Save continuous parcellated data.

"""

import os
import mne
import numpy as np
from glob import glob

# Directories
src_dir = "/ohba/pi/knobre/cgohil/pd_gripper/src"
out_dir = f"{src_dir}/npy"

os.makedirs(out_dir, exist_ok=True)

# Save epoched data as a numpy file
files = sorted(glob(src_dir + "/*/rhino/parc-raw.fif"))
for i, file in enumerate(files):
    print(f"Saving data: {file} -> {out_dir}/subject{i}.npy")
    epochs = mne.io.read_raw_fif(file, verbose=False)
    data = epochs.get_data(reject_by_annotation="omit").T  # (time, channels)
    np.save(f"{out_dir}/subject{i}.npy", data)