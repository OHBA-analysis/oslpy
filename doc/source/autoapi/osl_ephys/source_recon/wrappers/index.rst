:py:mod:`osl_ephys.source_recon.wrappers`
=========================================

.. py:module:: osl_ephys.source_recon.wrappers

.. autoapi-nested-parse::

   Wrappers for source reconstruction.

   This module contains the functions callable using a 'source_recon'
   section of a config.



Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   osl_ephys.source_recon.wrappers.extract_polhemus_from_info
   osl_ephys.source_recon.wrappers.extract_fiducials_from_fif
   osl_ephys.source_recon.wrappers.remove_stray_headshape_points
   osl_ephys.source_recon.wrappers.save_mni_fiducials
   osl_ephys.source_recon.wrappers.extract_polhemus_from_pos
   osl_ephys.source_recon.wrappers.extract_polhemus_from_elc
   osl_ephys.source_recon.wrappers.compute_surfaces
   osl_ephys.source_recon.wrappers.coregister
   osl_ephys.source_recon.wrappers.forward_model
   osl_ephys.source_recon.wrappers.beamform
   osl_ephys.source_recon.wrappers.parcellate
   osl_ephys.source_recon.wrappers.beamform_and_parcellate
   osl_ephys.source_recon.wrappers.find_template_subject
   osl_ephys.source_recon.wrappers.fix_sign_ambiguity
   osl_ephys.source_recon.wrappers.extract_rhino_files



Attributes
~~~~~~~~~~

.. autoapisummary::

   osl_ephys.source_recon.wrappers.logger


.. py:data:: logger

   

.. py:function:: extract_polhemus_from_info(outdir, subject, include_eeg_as_headshape=False, include_hpi_as_headshape=True, preproc_file=None, epoch_file=None)

   Wrapper function to extract fiducials/headshape points.

   :param outdir: Path to where to output the source reconstruction files.
   :type outdir: str
   :param subject: Subject name/id.
   :type subject: str
   :param include_eeg_as_headshape: Should we include EEG locations as headshape points?
   :type include_eeg_as_headshape: bool, optional
   :param include_hpi_as_headshape: Should we include HPI locations as headshape points?
   :type include_hpi_as_headshape: bool, optional
   :param preproc_file: Path to the preprocessed fif file.
   :type preproc_file: str, optional
   :param epoch_file: Path to the preprocessed fif file.
   :type epoch_file: str, optional


.. py:function:: extract_fiducials_from_fif(*args, **kwargs)

   Wrapper for extract_polhemus_from_info.


.. py:function:: remove_stray_headshape_points(outdir, subject, nose=True)

   Remove stray headshape points.

   This function removes headshape points on the nose, neck and far from the head.

   :param outdir: Path to where to output the source reconstruction files.
   :type outdir: str
   :param subject: Subject name/id.
   :type subject: str
   :param noise: Should we remove headshape points near the nose?
                 Useful to remove these if we have defaced structurals or aren't
                 extracting the nose from the structural.
   :type noise: bool, optional


.. py:function:: save_mni_fiducials(outdir, subject, filepath)

   Wrapper to save MNI fiducials.

   :param outdir: Path to where to output the source reconstruction files.
   :type outdir: str
   :param subject: Subject name/id.
   :type subject: str
   :param filepath: Full path to the text file containing the fiducials.

                    Any reference to '{subject}' (or '{0}') is replaced by the subject ID.
                    E.g. 'data/fiducials/{subject}_smri_fids.txt' with subject='sub-001'
                    will become 'data/fiducials/sub-001_smri_fids.txt'.

                    The file must be in MNI space with the following format:

                        nas -0.5 77.5 -32.6
                        lpa -74.4 -20.0 -27.2
                        rpa 75.4 -21.1 -21.9

                    Note, the first column (fiducial naming) is ignored but the rows must
                    be in the above order, i.e. be (nasion, left, right).

                    The order of the coordinates is the same as given in FSLeyes.
   :type filepath: str


.. py:function:: extract_polhemus_from_pos(outdir, subject, filepath)

   Wrapper to save polhemus data from a .pos file.

   :param outdir: Path to where to output the source reconstruction files.
   :type outdir: str
   :param subject: Subject name/id.
   :type subject: str
   :param filepath: Full path to the pos file for this subject.
                    Any reference to '{subject}' (or '{0}') is replaced by the subject ID.
                    E.g. 'data/{subject}/meg/{subject}_headshape.pos' with subject='sub-001'
                    becomes 'data/sub-001/meg/sub-001_headshape.pos'.
   :type filepath: str


.. py:function:: extract_polhemus_from_elc(outdir, subject, filepath, remove_headshape_near_nose=False)

   Wrapper to save polhemus data from an .elc file.

   :param outdir: Path to where to output the source reconstruction files.
   :type outdir: str
   :param subject: Subject name/id.
   :type subject: str
   :param filepath: Full path to the elc file for this subject.
                    Any reference to '{subject}' (or '{0}') is replaced by the subject ID.
                    E.g. 'data/{subject}/meg/{subject}_headshape.elc' with subject='sub-001'
                    becomes 'data/sub-001/meg/sub-001_headshape.elc'.
   :type filepath: str
   :param remove_headshape_near_nose: Should we remove any headshape points near the nose?
   :type remove_headshape_near_nose: bool, optional


.. py:function:: compute_surfaces(outdir, subject, smri_file, include_nose=True, recompute_surfaces=False, do_mri2mniaxes_xform=True, use_qform=False, reportdir=None)

   Wrapper for computing surfaces.

   :param outdir: Path to where to output the source reconstruction files.
   :type outdir: str
   :param subject: Subject name/id.
   :type subject: str
   :param smri_file: Path to the T1 weighted structural MRI file to use in source
                     reconstruction.
   :type smri_file: str
   :param include_nose: Should we include the nose when we're extracting the surfaces?
   :type include_nose: bool, optional
   :param recompute_surfaces: Specifies whether or not to run compute_surfaces, if the passed
                              in options have already been run.
   :type recompute_surfaces: bool, optional
   :param do_mri2mniaxes_xform: Specifies whether to do step 1) of compute_surfaces, i.e. transform
                                sMRI to be aligned with the MNI axes. Sometimes needed when the sMRI
                                goes out of the MNI FOV after step 1).
   :type do_mri2mniaxes_xform: bool, optional
   :param use_qform: Should we replace the sform with the qform? Useful if the sform code
                     is incompatible with OSL, but the qform is compatible.
   :type use_qform: bool, optional
   :param reportdir: Path to report directory.
   :type reportdir: str, optional


.. py:function:: coregister(outdir, subject, smri_file, preproc_file=None, epoch_file=None, use_nose=True, use_headshape=True, already_coregistered=False, allow_smri_scaling=False, n_init=1, reportdir=None)

   Wrapper for coregistration.

   :param outdir: Path to where to output the source reconstruction files.
   :type outdir: str
   :param subject: Subject name/id.
   :type subject: str
   :param smri_file: Path to the T1 weighted structural MRI file to use in source
                     reconstruction.
   :type smri_file: str
   :param preproc_file: Path to the preprocessed fif file.
   :type preproc_file: str, optional
   :param epoch_file: Path to the preprocessed epochs fif file.
   :type epoch_file: str, optional
   :param use_nose: Should we use the nose in the coregistration?
   :type use_nose: bool, optional
   :param use_headshape: Should we use the headshape points in the coregistration?
   :type use_headshape: bool, optional
   :param already_coregistered: Indicates that the data is already coregistered.
   :type already_coregistered: bool, optional
   :param allow_smri_scaling: Indicates if we are to allow scaling of the sMRI, such that
                              the sMRI-derived fids are scaled in size to better match the
                              polhemus-derived fids. This assumes that we trust the size
                              (e.g. in mm) of the polhemus-derived fids, but not the size
                              of the sMRI-derived fids. E.g. this might be the case if we
                              do not trust the size (e.g. in mm) of the sMRI, or if we are
                              using a template sMRI that has not come from this subject.
   :type allow_smri_scaling: bool, optional
   :param n_init: Number of initialisations for coregistration.
   :type n_init: int, optional
   :param reportdir: Path to report directory.
   :type reportdir: str, optional


.. py:function:: forward_model(outdir, subject, gridstep=8, model='Single Layer', eeg=False, reportdir=None)

   Wrapper for computing the forward model.

   :param outdir: Path to where to output the source reconstruction files.
   :type outdir: str
   :param subject: Subject name/id.
   :type subject: str
   :param gridstep: A grid will be constructed with the spacing given by ``gridstep``
                    in mm, generating a volume source space.
   :type gridstep: int, optional
   :param model: Type of forward model to use. Can be 'Single Layer' or 'Triple Layer',
                 where:
                 'Single Layer' use a single layer (brain/cortex)
                 'Triple Layer' uses three layers (scalp, inner skull, brain/cortex)
   :type model: str, optional
   :param eeg: Are we using EEG channels in the source reconstruction?
   :type eeg: bool, optional
   :param reportdir: Path to report directory.
   :type reportdir: str, optional


.. py:function:: beamform(outdir, subject, preproc_file, epoch_file, chantypes, rank, freq_range=None, weight_norm='nai', pick_ori='max-power-pre-weight-norm', reg=0, reportdir=None)

   Wrapper function for beamforming.

   :param outdir: Path to where to output the source reconstruction files.
   :type outdir: str
   :param subject: Subject name/id.
   :type subject: str
   :param preproc_file: Path to the preprocessed fif file.
   :type preproc_file: str
   :param epoch_file: Path to epoched preprocessed fif file.
   :type epoch_file: str
   :param chantypes: Channel types to use in beamforming.
   :type chantypes: str or list of str
   :param rank: Keys should be the channel types and the value should be the rank
                to use.
   :type rank: dict
   :param freq_range: Lower and upper band to bandpass filter before beamforming.
                      If None, no filtering is done.
   :type freq_range: list, optional
   :param weight_norm: Beamformer weight normalisation.
   :type weight_norm: str, optional
   :param pick_ori: Orientation of the dipoles.
   :type pick_ori: str, optional
   :param reg: The regularization for the whitened data covariance.
   :type reg: float, optional
   :param reportdir: Path to report directory
   :type reportdir: str, optional


.. py:function:: parcellate(outdir, subject, preproc_file, epoch_file, parcellation_file, method, orthogonalisation, spatial_resolution=None, reference_brain='mni', extra_chans='stim', reportdir=None)

   Wrapper function for parcellation.

   :param outdir: Path to where to output the source reconstruction files.
   :type outdir: str
   :param subject: Subject name/id.
   :type subject: str
   :param preproc_file: Path to the preprocessed fif file.
   :type preproc_file: str
   :param epoch_file: Path to epoched preprocessed fif file.
   :type epoch_file: str
   :param parcellation_file: Path to the parcellation file to use.
   :type parcellation_file: str
   :param method: Method to use in the parcellation.
   :type method: str
   :param orthogonalisation: Should we do orthogonalisation?
   :type orthogonalisation: bool
   :param spatial_resolution: Resolution for beamforming to use for the reference brain in mm
                              (must be an integer, or will be cast to nearest int). If None, then
                              the gridstep used in coreg_filenames['forward_model_file'] is used.
   :type spatial_resolution: int, optional
   :param reference_brain: 'mni' indicates that the reference_brain is the stdbrain in MNI space.
                           'mri' indicates that the reference_brain is the subject's sMRI in the
                           scaled native/mri space.
                           'unscaled_mri' indicates that the reference_brain is the subject's
                           sMRI in unscaled native/mri space.
                           Note that Scaled/unscaled relates to the allow_smri_scaling option
                           in coreg. If allow_scaling was False, then the unscaled MRI will be
                           the same as the scaled MRI.
   :type reference_brain: str, optional
   :param extra_chans: Extra channels to include in the parc-raw.fif file.
                       Defaults to 'stim'. Stim channels are always added to parc-raw.fif
                       in addition to extra_chans.
   :type extra_chans: str or list of str, optional
   :param reportdir: Path to report directory.
   :type reportdir: str, optional


.. py:function:: beamform_and_parcellate(outdir, subject, preproc_file, epoch_file, chantypes, rank, parcellation_file, method, orthogonalisation, freq_range=None, weight_norm='nai', pick_ori='max-power-pre-weight-norm', reg=0, spatial_resolution=None, reference_brain='mni', extra_chans='stim', reportdir=None)

   Wrapper function for beamforming and parcellation.

   :param outdir: Path to where to output the source reconstruction files.
   :type outdir: str
   :param subject: Subject name/id.
   :type subject: str
   :param preproc_file: Path to the preprocessed fif file.
   :type preproc_file: str
   :param epoch_file: Path to epoched preprocessed fif file.
   :type epoch_file: str
   :param chantypes: Channel types to use in beamforming.
   :type chantypes: str or list of str
   :param rank: Keys should be the channel types and the value should be the rank
                to use.
   :type rank: dict
   :param parcellation_file: Path to the parcellation file to use.
   :type parcellation_file: str
   :param method: Method to use in the parcellation.
   :type method: str
   :param orthogonalisation: Should we do orthogonalisation?
   :type orthogonalisation: bool
   :param freq_range: Lower and upper band to bandpass filter before beamforming.
                      If None, no filtering is done.
   :type freq_range: list, optional
   :param weight_norm: Beamformer weight normalisation.
   :type weight_norm: str, optional
   :param pick_ori: Orientation of the dipoles.
   :type pick_ori: str, optional
   :param reg: The regularization for the whitened data covariance.
   :type reg: float, optional
   :param spatial_resolution: Resolution for beamforming to use for the reference brain in mm
                              (must be an integer, or will be cast to nearest int). If None,
                              then the gridstep used in coreg_filenames['forward_model_file']
                              is used.
   :type spatial_resolution: int, optional
   :param reference_brain: 'mni' indicates that the reference_brain is the stdbrain in MNI space.
                           'mri' indicates that the reference_brain is the subject's sMRI in the
                           scaled native/mri space.
                           'unscaled_mri' indicates that the reference_brain is the subject's
                           sMRI in unscaled native/mri space.
                           Note that Scaled/unscaled relates to the allow_smri_scaling option
                           in coreg. If allow_scaling was False, then the unscaled MRI will be
                           the same as the scaled MRI.
   :type reference_brain: str, optional
   :param extra_chans: Extra channels to include in the parc-raw.fif file.
                       Defaults to 'stim'. Stim channels are always added to parc-raw.fif
                       in addition to extra_chans.
   :type extra_chans: str or list of str, optional
   :param reportdir: Path to report directory.
   :type reportdir: str, optional


.. py:function:: find_template_subject(outdir, subjects, n_embeddings=1, standardize=True, epoched=False)

   Function to find a good subject to align other subjects to in the sign flipping.

   Note, this function expects parcellated data to exist in the following
   location: outdir/*/parc/parc-*.fif, the * here represents subject
   directories or 'raw' vs 'epo'.

   :param outdir: Path to where to output the source reconstruction files.
   :type outdir: str
   :param subjects: Subjects to include.
   :type subjects: str
   :param n_embeddings: Number of time-delay embeddings that we will use (if we are doing any).
   :type n_embeddings: int, optional
   :param standardize: Should we standardize (z-transform) the data before sign flipping?
   :type standardize: bool, optional
   :param epoched: Are we performing sign flipping on parc-raw.fif (epoched=False) or
                   parc-epo.fif files (epoched=True)?
   :type epoched: bool, optional

   :returns: **template** -- Template subject.
   :rtype: str


.. py:function:: fix_sign_ambiguity(outdir, subject, preproc_file, template, n_embeddings, standardize, n_init, n_iter, max_flips, epoched=False, reportdir=None)

   Wrapper function for fixing the dipole sign ambiguity.

   :param outdir: Path to where to output the source reconstruction files.
   :type outdir: str
   :param subject: Subject name/id.
   :type subject: str
   :param preproc_file: Path to the preprocessed fif file.
   :type preproc_file: str
   :param template: Template subject.
   :type template: str
   :param n_embeddings: Number of time-delay embeddings that we will use (if we are doing any).
   :type n_embeddings: int
   :param standardize: Should we standardize (z-transform) the data before sign flipping?
   :type standardize: bool
   :param n_init: Number of initializations.
   :type n_init: int
   :param n_iter: Number of sign flipping iterations per subject to perform.
   :type n_iter: int
   :param max_flips: Maximum number of channels to flip in an iteration.
   :type max_flips: int
   :param epoched: Are we performing sign flipping on parc-raw.fif (epoched=False) or
                   parc-epo.fif files (epoched=True)?
   :type epoched: bool, optional
   :param reportdir: Path to report directory.
   :type reportdir: str, optional


.. py:function:: extract_rhino_files(outdir, subject, old_outdir)

   Wrapper function for extracting RHINO files from a previous run.

   :param outdir: Path to the NEW source reconstruction directory.
   :type outdir: str
   :param subject: Subject name/id.
   :type subject: str
   :param old_outdir: OLD source reconstruction directory to copy RHINO files to.
   :type old_outdir: str


