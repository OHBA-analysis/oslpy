:py:mod:`osl_ephys.source_recon.beamforming`
============================================

.. py:module:: osl_ephys.source_recon.beamforming

.. autoapi-nested-parse::

   Beamforming.



Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   osl_ephys.source_recon.beamforming.get_beamforming_filenames
   osl_ephys.source_recon.beamforming.make_lcmv
   osl_ephys.source_recon.beamforming.make_plots
   osl_ephys.source_recon.beamforming.load_lcmv
   osl_ephys.source_recon.beamforming.apply_lcmv
   osl_ephys.source_recon.beamforming.apply_lcmv_raw
   osl_ephys.source_recon.beamforming.get_recon_timeseries
   osl_ephys.source_recon.beamforming.transform_recon_timeseries
   osl_ephys.source_recon.beamforming.get_leadfields
   osl_ephys.source_recon.beamforming._make_lcmv
   osl_ephys.source_recon.beamforming._compute_beamformer
   osl_ephys.source_recon.beamforming._prepare_beamformer_input
   osl_ephys.source_recon.beamforming.voxel_timeseries



.. py:function:: get_beamforming_filenames(subjects_dir, subject)

   Get beamforming filenames.

   Files will be in subjects_dir/subject/beamforming

   :param subjects_dir: Directory containing the subject directories.
   :type subjects_dir: string
   :param subject: Subject name.
   :type subject: string

   :returns: **filenames** -- A dict of files.
   :rtype: dict


.. py:function:: make_lcmv(subjects_dir, subject, data, chantypes=None, data_cov=None, noise_cov=None, reg=0, label=None, pick_ori='max-power-pre-weight-norm', rank='info', noise_rank='info', weight_norm='unit-noise-gain-invariant', reduce_rank=True, depth=None, inversion='matrix', verbose=None, save_filters=False)

   Compute LCMV spatial filter.

   Modified version of mne.beamformer.make_lcmv.

   :param subjects_dir: Directory to find subject directories in.
   :type subjects_dir: str
   :param subject: Subject name.
   :type subject: str
   :param data: The measurement data to specify the channels to include. Bad channels in info['bads'] are not used. Will also be used to calculate data_cov.
   :type data: instance of mne.Raw | mne.Epochs
   :param chantypes: List of channel types to use to calculate the noise covariance. E.g. ['eeg'], ['mag', 'grad'], ['eeg', 'mag', 'grad'].
   :type chantypes: list
   :param data_cov: The noise covariance matrix used to whiten. If None will be computed from dat.
   :type data_cov: instance of mne.Covariance | None
   :param noise_cov: The noise covariance matrix used to whiten. If None will be computed from dat as a diagonal matrix with variances set to the average of all sensors of that type.
   :type noise_cov: instance of mne.Covariance | None
   :param reg: The regularization for the whitened data covariance.
   :type reg: float
   :param label: Restricts the LCMV solution to a given label.
   :type label: instance of Label
   :param pick_ori: The source orientation to compute the beamformer in.
   :type pick_ori: None | 'normal' | 'max-power' | max-power-pre-weight-norm
   :param rank: This controls the rank computation that can be read from the measurement info or estimated from the data. When a noise covariance is used for whitening, this should reflect the rank of that covariance, otherwise amplification of noise components can occur in whitening (e.g., often during source localization).

                ``None``
                    The rank will be estimated from the data after proper scaling of different channel types.

                ``'info'``
                    The rank is inferred from info. If data have been processed with Maxwell filtering, the Maxwell filtering header is used. Otherwise, the channel counts themselves are used. In both cases, the number of projectors is subtracted from the (effective) number of channels in the data. For example, if Maxwell filtering reduces the rank to 68, with two projectors the returned value will be 66.

                ``'full'``
                    The rank is assumed to be full, i.e. equal to the number of good channels. If a Covariance is passed, this can make sense if it has been (possibly improperly) regularized without taking into account the true data rank.

                dict
                    Calculate the rank only for a subset of channel types, and explicitly specify the rank for the remaining channel types. This can be extremely useful if you already know the rank of (part of) your data, for instance in case you have calculated it earlier.
                    This parameter must be a dictionary whose keys correspond to channel types in the data (e.g. 'meg', 'mag', 'grad', 'eeg'), and whose values are integers representing the respective ranks. For example, {'mag': 90, 'eeg': 45} will assume a rank of 90 and 45 for magnetometer data and EEG data, respectively.
                    The ranks for all channel types present in the data, but not specified in the dictionary will be estimated empirically. That is, if you passed a dataset containing magnetometer, gradiometer, and EEG data together with the dictionary from the previous example, only the gradiometer rank would be determined, while the specified magnetometer and EEG ranks would be taken for granted.

                The default is ``'info'``.
   :type rank: dict | None | 'full' | 'info'
   :param noise_rank: This controls the rank computation that can be read from the measurement info or estimated from the data. When a noise covariance is used for whitening, this should reflect the rank of that covariance, otherwise amplification of noise components can occur in whitening (e.g., often during source localization).
   :type noise_rank: dict | None | 'full' | 'info'
   :param weight_norm: The weight normalization scheme to use.
   :type weight_norm: None | 'unit-noise-gain' | 'unit-noise-gain-invariant' | 'nai'
   :param reduce_rank: Whether to reduce the rank by one during computation of the filter.
   :type reduce_rank: bool
   :param depth: How to weight (or normalize) the forward using a depth prior (see MNE docs).
   :type depth: None | float | dict
   :param inversion: The inversion scheme to compute the weights.
   :type inversion: 'matrix' | 'single'
   :param save_filters: Should we save the LCMV beamforming filter?
   :type save_filters: bool

   :returns: **filters** -- Dictionary containing filter weights from LCMV beamformer. See MNE docs.
   :rtype: instance of mne.beamformer.Beamformer


.. py:function:: make_plots(subjects_dir, subject, filters, data)

   Plot LCMV beamforming filters.

   :param subjects_dir: Directory containing the subject directories.
   :type subjects_dir: string
   :param subject: Subject name.
   :type subject: string
   :param filters: Filters to plot.
   :type filters: mne.beamformer.Beamformer
   :param data: Data used to create the filters.
   :type data: mne.Raw or mne.Epochs

   :returns: * **filters_cov_plot** (*str*) -- Path to covariance plot.
             * **filters_svd_plot** (*str*) -- Path to eigenspectrum plot.


.. py:function:: load_lcmv(subjects_dir, subject)

   Load LCMV beamforming filters.

   :param subjects_dir: Directory containing the subject directories.
   :type subjects_dir: string
   :param subject: Subject name.
   :type subject: string

   :returns: **filters** -- Dictionary containing filter weights from LCMV beamformer. See MNE docs.
   :rtype: instance of mne.beamformer.Beamformer


.. py:function:: apply_lcmv(data, filters, reject_by_annotation='omit')

   Apply a LCMV filter to an MNE Raw or Epochs object.

   :param data: The data to apply the LCMV filter to.
   :type data: instance of :py:class:`mne.io.Raw` or :py:class:`mne.Epochs`
   :param filters: The LCMV filter to apply.
   :type filters: instance of :py:class:`mne.beamformer.Beamformer`
   :param reject_by_annotation: If string, the annotation description to use to reject epochs.
                                If list of str, the annotation descriptions to use to reject epochs.
                                If None, do not reject epochs.
   :type reject_by_annotation: str | list of str | None

   :rtype: :py:class:`mne.SourceEstimate`


.. py:function:: apply_lcmv_raw(raw, filters, reject_by_annotation='omit')

   Modified version of mne.beamformer.apply_lcmv_raw.

   :param raw: The raw data to apply the LCMV filter to.
   :type raw: instance of :py:class:`mne.io.Raw`
   :param filters: The LCMV filter to apply.
   :type filters: instance of :py:class:`mne.beamformer.Beamformer`
   :param reject_by_annotation: If string, the annotation description to use to reject epochs.
                                If list of str, the annotation descriptions to use to reject epochs.
                                If None, do not reject epochs.
   :type reject_by_annotation: str | list of str | None

   :rtype: :py:class:`mne.SourceEstimate`


.. py:function:: get_recon_timeseries(subjects_dir, subject, coord_mni, recon_timeseries_head)

   Gets the reconstructed time series nearest to the passed coordinates in MNI space.

   :param subjects_dir: Directory to find subject directories in.
   :type subjects_dir: string
   :param subject: Subject name.
   :type subject: string
   :param coord_mni: 3D coordinate in MNI space to get timeseries for
   :type coord_mni: (3,) numpy.ndarray
   :param recon_timeseries_head: Reconstructed time courses in head (polhemus) space. Assumes that the dipoles are the same (and in the same order) as those in the forward model, rhino_files['fwd_model'].
   :type recon_timeseries_head: (ndipoles, ntpts) np.array

   :returns: **recon_timeseries** -- The timecourse in recon_timeseries_head nearest to coord_mni.
   :rtype: numpy.ndarray


.. py:function:: transform_recon_timeseries(subjects_dir, subject, recon_timeseries, spatial_resolution=None, reference_brain='mni')

   Spatially resamples a (ndipoles x ntpts) array of reconstructed time courses (in head/polhemus space) to dipoles on the brain grid of the specified reference brain.

   :param subjects_dir: Directory to find subject directories in.
   :type subjects_dir: string
   :param subject: Subject name.
   :type subject: string
   :param recon_timeseries: (ndipoles, ntpts) or (ndipoles, ntpts, ntrials) of reconstructed time courses (in head (polhemus) space). Assumes that the dipoles are the same (and in the
                            same order) as those in the forward model, rhino_files['fwd_model']. Typically derive from the VolSourceEstimate's output by MNE source recon methods,
                            e.g. mne.beamformer.apply_lcmv, obtained using a forward model generated by RHINO.
   :type recon_timeseries: numpy.ndarray
   :param spatial_resolution: Resolution to use for the reference brain in mm (must be an integer, or will be cast to nearest int). If None, then the gridstep used in rhino_files['fwd_model'] is used.
   :type spatial_resolution: int
   :param reference_brain: 'mni' indicates that the reference_brain is the stdbrain in MNI space.
                           'mri' indicates that the reference_brain is the subject's sMRI in the scaled native/mri space.
                           'unscaled_mri' indicates that the reference_brain is the subject's sMRI in unscaled native/mri space.
                           Note that scaled/unscaled relates to the allow_smri_scaling option in coreg. If allow_scaling was False, then the unscaled MRI will be the same as the scaled MRI.
   :type reference_brain: string

   :returns: * **recon_timeseries_out** (*(ndipoles, ntpts) numpy.ndarray*) -- Array of reconstructed time courses resampled on the reference brain grid.
             * **reference_brain_fname** (*string*) -- File name of the requested reference brain at the requested spatial resolution, int(spatial_resolution) (with zero for background, and !=0 for brain).
             * **coords_out** (*(3, ndipoles) numpy.ndarray*) -- Array of coordinates (in mm) of dipoles in recon_timeseries_out in "reference_brain" space.


.. py:function:: get_leadfields(subjects_dir, subject, spatial_resolution=None, reference_brain='mni', orientation='max-dim', verbose=None)

   Spatially resamples a (nsensors x ndipoles) array of leadfields (in head/polhemus space) to dipoles on the brain grid of the specified reference brain.

   :param subjects_dir: Directory to find subject directories in.
   :type subjects_dir: str
   :param subject: Subject name.
   :type subject: str
   :param leadfield: (nsensors, ndipoles) containing the lead field of each dipole (in head (polhemus) space). Assumes that the dipoles are the same (and in the same order)
                     as those in the forward model, rhino_files['fwd_model']. Typically derive from the VolSourceEstimate's output by MNE source recon methods,
                     e.g. mne.beamformer.apply_lcmv, obtained using a forward model generated by RHINO.
   :type leadfield: numpy.ndarray
   :param spatial_resolution: Resolution to use for the reference brain in mm (must be an integer, or will be cast to nearest int). If None, then the gridstep used in rhino_files['fwd_model'] is used.
   :type spatial_resolution: int
   :param reference_brain: 'mni' indicates that the reference_brain is the stdbrain in MNI space.
                           'mri' indicates that the reference_brain is the subject's sMRI in the scaled native/mri space.
                           'unscaled_mri' indicates that the reference_brain is the subject's sMRI in unscaled native/mri space.
                           Note that Scaled/unscaled relates to the allow_smri_scaling option in coreg. If allow_scaling was False, then the unscaled MRI will be the same as the scaled MRI.
   :type reference_brain: str
   :param orientation: How should we reduce the 3 leadfield dimensions into a scaler? Options:
                       'l2-norm' takes the L2 norm across the xyz dimensions.
                       'max-dim' takes the leadfield with the highest value across the xyz dimensions.
                       'max-power' projects the leadfield onto the eigenvector with the smallest eigenvalue, this is equivalent to the maximum power orientation.
   :type orientation: str
   :param verbose: If True, print out more information.
   :type verbose: bool

   :returns: * **leadfield_out** (*numpy.ndarray*) -- (nsensors, ndipoles) np.array of lead fields resampled on the reference brain grid.
             * **coords_out** (*(3, ndipoles) numpy.ndarray*) -- Array of coordinates (in mm) of dipoles in leadfield_out in "reference_brain" space.


.. py:function:: _make_lcmv(info, forward, data_cov, reg=0.05, noise_cov=None, label=None, pick_ori=None, rank='info', noise_rank='info', weight_norm='unit-noise-gain-invariant', reduce_rank=False, depth=None, inversion='matrix', verbose=None)

   Compute LCMV spatial filter.

   Modified version of mne.beamformer._make_lcmv.

   :param info: The measurement info to specify the channels to include.
   :type info: instance of :py:class:`mne.Info`
   :param forward: The forward solution.
   :type forward: instance of :py:class:`mne.Forward`
   :param data_cov: The data covariance object.
   :type data_cov: instance of :py:class:`mne.Covariance`
   :param reg: The regularization for the whitened data covariance.
   :type reg: float
   :param noise_cov: The noise covariance object.
   :type noise_cov: instance of :py:class:`mne.Covariance`
   :param label: Restricts the LCMV solution to a given label.
   :type label: instance of :py:class:`mne.Label`
   :param pick_ori: The source orientation to compute the beamformer in.
   :type pick_ori: None | 'normal' | 'max-power' | max-power-pre-weight-norm
   :param rank: This controls the rank computation that can be read from the measurement info or estimated from the data. When a noise covariance is used for whitening, this should reflect the rank of that covariance, otherwise amplification of noise components can occur in whitening (e.g., often during source localization).

                ``None``
                    The rank will be estimated from the data after proper scaling of different channel types.

                ``'info'``
                    The rank is inferred from info. If data have been processed with Maxwell filtering, the Maxwell filtering header is used. Otherwise, the channel counts themselves are used. In both cases, the number of projectors is subtracted from the (effective) number of channels in the data. For example, if Maxwell filtering reduces the rank to 68, with two projectors the returned value will be 66.

                ``'full'``
                    The rank is assumed to be full, i.e. equal to the number of good channels. If a Covariance is passed, this can make sense if it has been (possibly improperly) regularized without taking into account the true data rank.

                dict
                    Calculate the rank only for a subset of channel types, and explicitly specify the rank for the remaining channel types. This can be extremely useful if you already know the rank of (part of) your data, for instance in case you have calculated it earlier.
                    This parameter must be a dictionary whose keys correspond to channel types in the data (e.g. 'meg', 'mag', 'grad', 'eeg'), and whose values are integers representing the respective ranks. For example, {'mag': 90, 'eeg': 45} will assume a rank of 90 and 45 for magnetometer data and EEG data, respectively.
                    The ranks for all channel types present in the data, but not specified in the dictionary will be estimated empirically. That is, if you passed a dataset containing magnetometer, gradiometer, and EEG data together with the dictionary from the previous example, only the gradiometer rank would be determined, while the specified magnetometer and EEG ranks would be taken for granted.

                The default is ``'info'``.
   :type rank: dict | None | 'full' | 'info'
   :param noise_rank: This controls the rank computation that can be read from the measurement info or estimated from the data. When a noise covariance is used for whitening, this should reflect the rank of that covariance, otherwise amplification of noise components can occur in whitening (e.g., often during source localization).
   :type noise_rank: dict | None | 'full' | 'info'
   :param weight_norm: The weight normalization scheme to use.
   :type weight_norm: None | 'unit-noise-gain' | 'nai'
   :param reduce_rank: Whether to reduce the rank by one during computation of the filter.
   :type reduce_rank: bool
   :param depth: How to weight (or normalize) the forward using a depth prior (see Notes).
   :type depth: None | float | dict
   :param inversion: The inversion scheme to compute the weights.
   :type inversion: 'matrix' | 'single'
   :param verbose: If not None, override default verbose level (see mne.verbose).
   :type verbose: bool, str, int, or None

   :returns: **filters** -- Dictionary containing filter weights from LCMV beamformer. See MNE docs.
   :rtype: instance of :py:class:`mne.beamformer.Beamformer`


.. py:function:: _compute_beamformer(G, Cm, reg, n_orient, weight_norm, pick_ori, reduce_rank, rank, inversion, nn, orient_std, whitener)

   Compute a spatial beamformer filter (LCMV or DICS).

   For more detailed information on the parameters, see the docstrings of `make_lcmv` and `make_dics`.

   Modified version of mne.beamformer._compute_beamformer.

   :param G: The leadfield.
   :type G: (n_dipoles, n_channels) numpy.ndarray
   :param Cm: The data covariance matrix.
   :type Cm: (n_channels, n_channels) numpy.ndarray
   :param reg: Regularization parameter.
   :type reg: float
   :param n_orient: Number of dipole orientations defined at each source point
   :type n_orient: int
   :param weight_norm: The weight normalization scheme to use.
   :type weight_norm: None | 'unit-noise-gain' | 'nai'
   :param pick_ori: The source orientation to compute the beamformer in.
   :type pick_ori: None | 'normal' | 'max-power' | max-power-pre-weight-norm
   :param reduce_rank: Whether to reduce the rank by one during computation of the filter.
   :type reduce_rank: bool
   :param rank: See compute_rank.
   :type rank: dict | None | 'full' | 'info'
   :param inversion: The inversion scheme to compute the weights.
   :type inversion: 'matrix' | 'single'
   :param nn: The source normals.
   :type nn: (n_dipoles, 3) numpy.ndarray
   :param orient_std: The std of the orientation prior used in weighting the lead fields.
   :type orient_std: (n_dipoles,) numpy.ndarray
   :param whitener: The whitener.
   :type whitener: (n_channels, n_channels) numpy.ndarray

   :returns: **W** -- The beamformer filter weights.
   :rtype: (n_dipoles, n_channels) numpy.ndarray


.. py:function:: _prepare_beamformer_input(info, forward, label=None, pick_ori=None, noise_cov=None, rank=None, pca=False, loose=None, combine_xyz='fro', exp=None, limit=None, allow_fixed_depth=True, limit_depth_chs=False)

   Input preparation common for LCMV, DICS, and RAP-MUSIC.

   Modified version of mne.beamformer._prepare_beamformer_input.

   :param info: Measurement info
   :type info: instance of :py:class:`mne.Info`
   :param forward: The forward solution.
   :type forward: instance of :py:class:`mne.Forward`
   :param label: Restricts the forward solution to a given label.
   :type label: instance of :py:class:`mne.Label` | None
   :param pick_ori: The source orientation to compute the beamformer in.
   :type pick_ori: None | 'normal' | 'max-power' | 'vector' | 'max-power-pre-weight-norm'
   :param noise_cov: The noise covariance.
   :type noise_cov: instance of :py:class:`mne.Covariance` | None
   :param rank: See :py:func:`mne.compute_rank`.
   :type rank: dict | None | 'full' | 'info'
   :param pca: If True, the rank of the forward is reduced to match the rank of the noise covariance matrix.
   :type pca: bool
   :param loose: Value that weights the source variances of the dipole components defining the tangent space of the cortical surfaces. If ``None``, no loose orientation constraint is applied.
   :type loose: float | None
   :param combine_xyz: How to combine the dipoles in the same locations of the forward model when picking normals. See :py:func:`mne.forward._pick_ori`.
   :type combine_xyz: str
   :param exp: Exponent for the depth weighting. If None, no depth weighting is performed.
   :type exp: float | None
   :param limit: Limit on depth weighting factors. If None, no upper limit is applied.
   :type limit: float | None
   :param allow_fixed_depth: If True, fixed depth weighting is allowed.
   :type allow_fixed_depth: bool
   :param limit_depth_chs: If True, use only grad channels for depth weighting.
   :type limit_depth_chs: bool

   :returns: * **is_free_ori** (*bool*) -- Whether the forward operator is free orientation.
             * **info** (instance of :py:class:`mne.Info`) -- Measurement info restricted to selected channels.
             * **proj** (*array*) -- The SSP/PCA projector.
             * **vertno** (*array*) -- The indices of the vertices corresponding to the source space.
             * **G** (*array*) -- The forward operator restricted to selected channels.
             * **whitener** (*array*) -- The whitener for the selected channels.
             * **nn** (*array*) -- The normals of the source space.
             * **orient_std** (*array*) -- The standard deviation of the orientation prior.


.. py:function:: voxel_timeseries(subjects_dir, subject, preproc_file, chantypes, freq_range=None, spatial_resolution=None, reference_brain='mni', reject_by_annotation=None)

   Get the voxel time series of beamformed data.

   :param subjects_dir: Directory to find subject directories in.
   :type subjects_dir: str
   :param subject: Subject name.
   :type subject: str
   :param preproc_file: Path to the preprocessed fif file.
   :type preproc_file: str
   :param chantypes: Channel types to use in beamforming.
   :type chantypes: list of str
   :param freq_range: Lower and upper band to bandpass filter before beamforming. If None, no filtering is done.
   :type freq_range: list
   :param spatial_resolution: Resolution for beamforming to use for the reference brain in mm (must be an integer, or will be cast to nearest int).
                              If None, then the gridstep used in rhino_files['fwd_model'] is used.
   :type spatial_resolution: int
   :param reference_brain: 'mni' indicates that the reference_brain is the stdbrain in MNI space.
                           'mri' indicates that the reference_brain is the subject's sMRI in the scaled native/mri space.
                           'unscaled_mri' indicates that the reference_brain is the subject's sMRI in unscaled native/mri space.
                           Note that Scaled/unscaled relates to the allow_smri_scaling option in coreg. If allow_scaling was False, then the unscaled MRI will be the same as the scaled MRI.
   :type reference_brain: str
   :param reject_by_annotation: Argument passed to .get_data() if the preproc file contains an MNE Raw object.
   :type reject_by_annotation: str

   :returns: * **voxel_data** (*np.ndarray*) -- Voxel time series in (voxels, time) format.
             * **voxel_coords** (*np.ndarray*) -- Voxel coordinates in MNI space.


