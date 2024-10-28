:py:mod:`osl_ephys.source_recon.parcellation`
=============================================

.. py:module:: osl_ephys.source_recon.parcellation

.. autoapi-nested-parse::

   Parcellation related functions and files.



Submodules
----------
.. toctree::
   :titlesonly:
   :maxdepth: 1

   nii/index.rst
   parcellation/index.rst


Package Contents
----------------


Functions
~~~~~~~~~

.. autoapisummary::

   osl_ephys.source_recon.parcellation.log_or_print
   osl_ephys.source_recon.parcellation.load_parcellation
   osl_ephys.source_recon.parcellation.find_file
   osl_ephys.source_recon.parcellation.guess_parcellation
   osl_ephys.source_recon.parcellation.parcellate_timeseries
   osl_ephys.source_recon.parcellation._get_parcel_timeseries
   osl_ephys.source_recon.parcellation.resample_parcellation
   osl_ephys.source_recon.parcellation.symmetric_orthogonalise
   osl_ephys.source_recon.parcellation.parcel_centers
   osl_ephys.source_recon.parcellation.plot_parcellation
   osl_ephys.source_recon.parcellation.plot_psd
   osl_ephys.source_recon.parcellation.plot_correlation
   osl_ephys.source_recon.parcellation._parcel_timeseries2nii
   osl_ephys.source_recon.parcellation.convert2niftii
   osl_ephys.source_recon.parcellation.convert2mne_raw
   osl_ephys.source_recon.parcellation.convert2mne_epochs
   osl_ephys.source_recon.parcellation.spatial_dist_adjacency
   osl_ephys.source_recon.parcellation.parcel_vector_to_voxel_grid
   osl_ephys.source_recon.parcellation.convert_4dparc_to_3d
   osl_ephys.source_recon.parcellation.convert_3dparc_to_4d
   osl_ephys.source_recon.parcellation.spatially_downsample
   osl_ephys.source_recon.parcellation.append_4d_parcellation



.. py:function:: log_or_print(msg, warning=False)

   Execute logger.info if an OSL logger has been setup, otherwise print.

   :param msg: Message to log/print.
   :type msg: str
   :param warning: Is the msg a warning? Defaults to False, which will print info.
   :type warning: bool


.. py:function:: load_parcellation(parcellation_file)

   Load a parcellation file.

   :param parcellation_file: Path to parcellation file.
   :type parcellation_file: str

   :returns: **parcellation** -- Parcellation.
   :rtype: nibabel image


.. py:function:: find_file(filename)

   Look for a parcellation file within the package.

   :param filename: Path to parcellation file to look for.
   :type filename: str

   :returns: **filename** -- Path to parcellation file found.
   :rtype: str


.. py:function:: guess_parcellation(data, return_path=False)

   Guess parcellation file from data.

   :param data: Data to guess parcellation from. first dimension is assumed to be parcels.
   :type data: vector or matrix
   :param return_path: If True, return path to parcellation file, otherwise return filename.
   :type return_path: bool

   :returns: **filename** -- Path to parcellation file.
   :rtype: str


.. py:function:: parcellate_timeseries(parcellation_file, voxel_timeseries, voxel_coords, method, working_dir)

   Parcellate a voxel time series.

   :param parcellation_file: Parcellation file (or path to parcellation file).
   :type parcellation_file: str
   :param voxel_timeseries: (nvoxels x ntpts) or (nvoxels x ntpts x ntrials) data to be parcellated.
                            Data is assumed to be in same space as the parcellation (e.g. typically corresponds to the output from beamforming.transform_recon_timeseries).
   :type voxel_timeseries: numpy.ndarray
   :param voxel_coords: (nvoxels x 3) coordinates of voxel_timeseries in mm in same space as parcellation (e.g. typically corresponds to the output from beamforming.transform_recon_timeseries).
   :type voxel_coords: numpy.ndarray
   :param method: ``'pca'`` - take 1st PC in each parcel
                  ``'spatial_basis'`` - The parcel time-course for each spatial map is the 1st PC from all voxels, weighted by the spatial map.
                  If the parcellation is unweighted and non-overlapping, 'spatialBasis' will give the same result as 'PCA' except with a different normalization.
   :type method: str
   :param working_dir: Directory to put temporary file in. If None, attempt to use same directory as passed in parcellation.
   :type working_dir: str

   :returns: * **parcel_timeseries** (*numpy.ndarray*) -- nparcels x ntpts, or nparcels x ntpts x ntrials, parcellated data.
             * **voxel_weightings** (*numpy.ndarray*) -- nvoxels x nparcels, Voxel weightings for each parcel, corresponds to parcel_data = voxel_weightings.T * voxel_data
             * **voxel_assignments** (*bool numpy.ndarray*) -- nvoxels x nparcels, Boolean assignments indicating for each voxel the winner takes all parcel it belongs to.


.. py:function:: _get_parcel_timeseries(voxel_timeseries, parcellation_asmatrix, method='spatial_basis')

   Calculate parcel timeseries.

   :param voxel_timeseries: (nvoxels x ntpts) or (nvoxels x ntpts x ntrials) and is assumed to be on the same grid as parcellation (typically output by beamforming.transform_recon_timeseries).
   :type voxel_timeseries: numpy.ndarray
   :param parcellation_asmatrix: (nvoxels x nparcels) and is assumed to be on the same grid as voxel_timeseries.
   :type parcellation_asmatrix: numpy.ndarray
   :param method: ``'pca'`` - take 1st PC of voxels
                  ``'spatial_basis'`` - The parcel time-course for each spatial map is the 1st PC from all voxels, weighted by the spatial map.
                  If the parcellation is unweighted and non-overlapping, 'spatialBasis' will give the same result as 'PCA' except with a different normalization.
   :type method: str

   :returns: * **parcel_timeseries** (*numpy.ndarray*) -- nparcels x ntpts, or nparcels x ntpts x ntrials
             * **voxel_weightings** (*numpy.ndarray*) -- nvoxels x nparcels
               Voxel weightings for each parcel to compute parcel_timeseries from
               voxel_timeseries
             * **voxel_assignments** (*bool numpy.ndarray*) -- nvoxels x nparcels
               Boolean assignments indicating for each voxel the winner takes all
               parcel it belongs to


.. py:function:: resample_parcellation(parcellation_file, voxel_coords, working_dir=None)

   Resample parcellation so that its voxel coords correspond (using nearest neighbour) to passed in voxel_coords.
   Passed in voxel_coords and parcellation must be in the same space, e.g. MNI.

   Used to make sure that the parcellation's voxel coords are the same as the voxel coords for some timeseries data, before calling _get_parcel_timeseries.

   :param parcellation_file: Path to parcellation file. In same space as voxel_coords.
   :type parcellation_file: str
   :param voxel_coords: (nvoxels x 3) coordinates in mm in same space as parcellation.
   :param working_dir: Dir to put temp file in. If None, attempt to use same dir as passed in parcellation.
   :type working_dir: str

   :returns: **parcellation_asmatrix** -- (nvoxels x nparcels) resampled parcellation
   :rtype: numpy.ndarray


.. py:function:: symmetric_orthogonalise(timeseries, maintain_magnitudes=False, compute_weights=False)

   Returns orthonormal matrix L which is closest to A, as measured by the Frobenius norm of (L-A). The orthogonal matrix is constructed from a singular
   value decomposition of A.

   If maintain_magnitudes is True, returns the orthogonal matrix L, whose columns have the same magnitude as the respective columns of A, and which is closest to
   A, as measured by the Frobenius norm of (L-A).

   :param timeseries: (nparcels x ntpts) or (nparcels x ntpts x ntrials) data to orthoganlise. In the latter case, the ntpts and ntrials dimensions are concatenated.
   :type timeseries: numpy.ndarray
   :param maintain_magnitudes:
   :type maintain_magnitudes: bool
   :param compute_weights:
   :type compute_weights: bool

   :returns: * **ortho_timeseries** (*numpy.ndarray*) -- (nparcels x ntpts) or (nparcels x ntpts x ntrials) orthoganalised data
             * **weights** (*numpy.ndarray*) -- (optional output depending on compute_weights flag) weighting matrix such that, ortho_timeseries = timeseries * weights

   .. rubric:: References

   Colclough, G. L., Brookes, M., Smith, S. M. and Woolrich, M. W., "A symmetric multivariate leakage correction for MEG connectomes," NeuroImage 117, pp. 439-448 (2015)


.. py:function:: parcel_centers(parcellation_file)

   Get coordinates of parcel centers.

   :param parcellation_file: Path to parcellation file.
   :type parcellation_file: str

   :returns: **coords** -- Coordinates of each parcel. Shape is (n_parcels, 3).
   :rtype: np.ndarray


.. py:function:: plot_parcellation(parcellation_file, **kwargs)

   Plots a parcellation.

   :param parcellation_file: Path to parcellation file.
   :type parcellation_file: str
   :param kwargs: Keyword arguments to pass to nilearn.plotting.plot_markers.
   :type kwargs: keyword arguments


.. py:function:: plot_psd(parc_ts, fs, parcellation_file, filename, freq_range=None)

   Plot PSD of each parcel time course.

   :param parc_ts: (parcels, time) or (parcels, time, epochs) time series.
   :type parc_ts: np.ndarray
   :param fs: Sampling frequency in Hz.
   :type fs: float
   :param parcellation_file: Path to parcellation file.
   :type parcellation_file: str
   :param filename: Output filename.
   :type filename: str
   :param freq_range: Low and high frequency in Hz.
   :type freq_range: list of len 2


.. py:function:: plot_correlation(parc_ts, filename)

   Plot correlation between parcel time courses.

   :param parc_ts: (parcels, time) or (parcels, time, epochs) time series.
   :type parc_ts: np.ndarray
   :param filename: Output filename.
   :type filename: str


.. py:function:: _parcel_timeseries2nii(parcellation_file, parcel_timeseries_data, voxel_weightings, voxel_assignments, voxel_coords, out_nii_fname=None, working_dir=None, times=None, method='assignments')

   Outputs parcel_timeseries_data as a niftii file using passed in parcellation.

   The parcellation and parcel_timeseries_data need to have the same number of parcels.

   :param parcellation_file: Path to parcellation file.
   :type parcellation_file: str
   :param parcel_timeseries_data: Needs to be nparcels x ntpts
   :type parcel_timeseries_data: numpy.ndarray
   :param voxel_weightings: (nvoxels x nparcels) voxel weightings for each parcel to compute parcel_timeseries from voxel_timeseries.
   :type voxel_weightings: numpy.ndarray
   :param voxel_assignments: (nvoxels x nparcels) boolean assignments indicating for each voxel the winner takes all parcel it belongs to.
   :type voxel_assignments: bool numpy.ndarray
   :param voxel_coords: (nvoxels x 3) coordinates of voxel_timeseries in mm in same space as parcellation (e.g. typically corresponds to the output from beamforming.transform_recon_timeseries).
   :type voxel_coords: numpy.ndarray
   :param working_dir: Directory name to put files in.
   :type working_dir: str
   :param out_nii_fname: Output name to put files in.
   :type out_nii_fname: str
   :param times: (ntpts,) times points in seconds. Will assume that time points are regularly spaced. Used to set nii file up correctly.
   :type times: array
   :param method: "weights" or "assignments"
   :type method: str

   :returns: **out_nii_fname** -- Output nii filename, will be output at spatial resolution of parcel_timeseries['voxel_coords'].
   :rtype: str


.. py:function:: convert2niftii(parc_data, parcellation_file, mask_file, tres=1, tmin=0)

   Convert parcellation to NIfTI.

   Takes (nparcels) or (nvolumes x nparcels) parc_data and returns (xvoxels x yvoxels x zvoxels x nvolumes) niftii file containing parc_data on a volumetric grid.

   :param parc_data: (nparcels) or (nvolumes x nparcels) parcel data.
   :type parc_data: np.ndarray
   :param parcellation_file: Path to niftii parcellation file.
   :type parcellation_file: str
   :param mask_file: Path to niftii parcellation mask file.
   :type mask_file: str
   :param tres: Resolution of 4th dimension in secs
   :type tres: float
   :param tmin: Value of first time point in secs
   :type tmin: float

   :returns: **nii** -- (xvoxels x yvoxels x zvoxels x nvolumes) nib.Nifti1Image containing parc_data on a volumetric grid.
   :rtype: nib.Nifti1Image


.. py:function:: convert2mne_raw(parc_data, raw, parcel_names=None, extra_chans='stim')

   Create and returns an MNE raw object that contains parcellated data.

   :param parc_data: (nparcels x ntpts) parcel data.
   :type parc_data: np.ndarray
   :param raw: mne.io.raw object that produced parc_data via source recon and parcellation. Info such as timings and bad segments will be copied from this to parc_raw.
   :type raw: mne.Raw
   :param parcel_names: List of strings indicating names of parcels. If None then names are set to be parcel_0,...,parcel_{n_parcels-1}.
   :type parcel_names: list of str
   :param extra_chans: Extra channels, e.g. 'stim' or 'emg', to include in the parc_raw object. Defaults to 'stim'. stim channels are always added to parc_raw if they are present in raw.
   :type extra_chans: str or list of str

   :returns: **parc_raw** -- Generated parcellation in mne.Raw format.
   :rtype: mne.Raw


.. py:function:: convert2mne_epochs(parc_data, epochs, parcel_names=None)

   Create and returns an MNE Epochs object that contains parcellated data.

   :param parc_data: (nparcels x ntpts x epochs) parcel data.
   :type parc_data: np.ndarray
   :param epochs: mne.io.raw object that produced parc_data via source recon and parcellation. Info such as timings and bad segments will be copied from this to parc_raw.
   :type epochs: mne.Epochs
   :param parcel_names: List of strings indicating names of parcels. If None then names are set to be parcel_0,...,parcel_{n_parcels-1}.
   :type parcel_names: list of str

   :returns: **parc_epo** -- Generated parcellation in :py:class: mne.Epochs` format.
   :rtype: mne.Epochs


.. py:function:: spatial_dist_adjacency(parcellation_file, dist, verbose=False)

   Compute adjacency from distances between parcels.

   :param parcellation_file: Path to parcellation file.
   :type parcellation_file: str
   :param dist: Maximum (geodesic) distance in mm for two parcels to within to be considered as neighbours.
   :type dist: float
   :param verbose: Should we print the distance between parcels that are considered neighbours?
   :type verbose: bool

   :returns: **adj_mat** -- (n_parcels, n_parcels) matrix of zeros (indicating not neighbours) and ones (indicating parcels are neighbours).
   :rtype: np.ndarray


.. py:function:: parcel_vector_to_voxel_grid(mask_file, parcellation_file, vector)

   Takes a vector of parcel values and return a 3D voxel grid.

   :param mask_file: Mask file for the voxel grid. Must be a NIFTI file.
   :type mask_file: str
   :param parcellation_file: Parcellation file. Must be a NIFTI file.
   :type parcellation_file: str
   :param vector: Value at each parcel. Shape must be (n_parcels,).
   :type vector: np.ndarray

   :returns: **voxel_grid** -- Value at each voxel. Shape is (x, y, z), where :code:`x`,
             :code:`y` and :code:`z` correspond to 3D voxel locations.
   :rtype: np.ndarray


.. py:function:: convert_4dparc_to_3d(parcel4d_fname, parcel3d_fname)

   Convert 4D parcellation to 3D.

   :param parcel4d_fname: 4D nifii file, where each volume is a parcel
   :type parcel4d_fname: str
   :param parcel3d_fname: 3D nifii output fule with each voxel with a value of 0 if not in a parcel,
                          or 1...p...n_parcels if in parcel p
   :type parcel3d_fname: str


.. py:function:: convert_3dparc_to_4d(parcel3d_fname, parcel4d_fname, tmpdir, n_parcels)

   Convert 3D parcellation to 4D.

   :param parcel3d_fname: 3D nifii volume with each voxel with a value of 0 if not in a parcel,
                          or 1...p...n_parcels if in parcel p
   :type parcel3d_fname: str
   :param parcel4d_fname: 4D nifii output file, where each volume is a parcel
   :type parcel4d_fname: str
   :param tmpdir: temp dir to write to. Must exist.
   :type tmpdir: str
   :param n_parcels: Number of parcels


.. py:function:: spatially_downsample(file_in, file_out, file_ref, spatial_res)

   Downsample niftii file file_in spatially and writes it to file_out

   :param file_in:
   :type file_in: str
   :param file_out:
   :type file_out: str
   :param file_ref: reference niftii volume at resolution spatial_res
   :type file_ref: str
   :param spatial_res: new spatial res in mm


.. py:function:: append_4d_parcellation(file_in, file_out, file_append, parcel_indices=None)

   Appends volumes in file_append to file_in.

   :param file_in:
   :type file_in: str
   :param file_out:
   :type file_out: str
   :param file_append:
   :type file_append: str
   :param parcel_indices: (n_indices) numpy array containing volume indices (starting from 0) of volumes from file_append to append to file_in
   :type parcel_indices: np.ndarray


