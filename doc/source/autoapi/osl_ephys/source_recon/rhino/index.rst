:py:mod:`osl_ephys.source_recon.rhino`
======================================

.. py:module:: osl_ephys.source_recon.rhino

.. autoapi-nested-parse::

   Registration of Headshapes Including Nose in OSL (RHINO).



Submodules
----------
.. toctree::
   :titlesonly:
   :maxdepth: 1

   coreg/index.rst
   forward_model/index.rst
   fsl_utils/index.rst
   polhemus/index.rst
   surfaces/index.rst
   utils/index.rst


Package Contents
----------------


Functions
~~~~~~~~~

.. autoapisummary::

   osl_ephys.source_recon.rhino.get_surfaces_filenames
   osl_ephys.source_recon.rhino.log_or_print
   osl_ephys.source_recon.rhino.get_coreg_filenames
   osl_ephys.source_recon.rhino.coreg
   osl_ephys.source_recon.rhino.coreg_metrics
   osl_ephys.source_recon.rhino.coreg_display
   osl_ephys.source_recon.rhino.bem_display
   osl_ephys.source_recon.rhino.get_coreg_filenames
   osl_ephys.source_recon.rhino.log_or_print
   osl_ephys.source_recon.rhino.extract_polhemus_from_info
   osl_ephys.source_recon.rhino.save_mni_fiducials
   osl_ephys.source_recon.rhino.plot_polhemus_points
   osl_ephys.source_recon.rhino.delete_headshape_points
   osl_ephys.source_recon.rhino.remove_stray_headshape_points
   osl_ephys.source_recon.rhino.extract_polhemus_from_pos
   osl_ephys.source_recon.rhino.extract_polhemus_from_elc
   osl_ephys.source_recon.rhino.log_or_print
   osl_ephys.source_recon.rhino.forward_model
   osl_ephys.source_recon.rhino.make_fwd_solution
   osl_ephys.source_recon.rhino.setup_volume_source_space
   osl_ephys.source_recon.rhino.log_or_print
   osl_ephys.source_recon.rhino.get_surfaces_filenames
   osl_ephys.source_recon.rhino.check_if_already_computed
   osl_ephys.source_recon.rhino.compute_surfaces
   osl_ephys.source_recon.rhino.surfaces_display
   osl_ephys.source_recon.rhino.plot_surfaces
   osl_ephys.source_recon.rhino.setup_fsl
   osl_ephys.source_recon.rhino.check_fsl
   osl_ephys.source_recon.rhino.fsleyes
   osl_ephys.source_recon.rhino.fsleyes_overlay



.. py:function:: get_surfaces_filenames(subjects_dir, subject)

   Generates a dict of files generated and used by rhino.compute_surfaces.

   Files will be in subjects_dir/subject/rhino/surfaces.

   :param subjects_dir: Directory containing the subject directories.
   :type subjects_dir: string
   :param subject: Subject directory name to put the surfaces in.
   :type subject: string

   :returns: **filenames** -- A dict of files generated and used by rhino.compute_surfaces. Note that  due to the unusal naming conventions used by BET:
             - bet_inskull_*_file is actually the brain surface
             - bet_outskull_*_file is actually the inner skull surface
             - bet_outskin_*_file is the outer skin/scalp surface
   :rtype: dict


.. py:function:: log_or_print(msg, warning=False)

   Execute logger.info if an OSL logger has been setup, otherwise print.

   :param msg: Message to log/print.
   :type msg: str
   :param warning: Is the msg a warning? Defaults to False, which will print info.
   :type warning: bool


.. py:function:: get_coreg_filenames(subjects_dir, subject)

   Files used in coregistration by RHINO.

   Files will be in subjects_dir/subject/rhino/coreg.

   :param subjects_dir: Directory containing the subject directories.
   :type subjects_dir: string
   :param subject: Subject directory name to put the coregistration files in.
   :type subject: string

   :returns: **filenames** -- A dict of files generated and used by RHINO.
   :rtype: dict


.. py:function:: coreg(fif_file, subjects_dir, subject, use_headshape=True, use_nose=True, use_dev_ctf_t=True, already_coregistered=False, allow_smri_scaling=False, n_init=1)

   Coregistration.

   Calculates a linear, affine transform from native sMRI space to
   polhemus (head) space, using headshape points that include the
   nose (if useheadshape = True). Requires ``rhino.compute_surfaces``
   to have been run. This is based on the OSL Matlab version of
   RHINO.
   Call ``get_coreg_filenames(subjects_dir, subject)`` to get a file
   list of generated files. RHINO firsts registers the polhemus-
   derived fiducials (nasion, rpa, lpa) in polhemus space to the
   sMRI-derived fiducials in native sMRI space.

   RHINO then refines this by making use of polhemus-derived headshape
   points that trace out the surface of the head (scalp), and ideally
   include the nose.

   Finally, these polhemus-derived headshape points in polhemus space
   are registered to the sMRI-derived scalp surface in native sMRI space.

   In more detail:

   1)  Map location of fiducials in MNI standard space brain to native sMRI space. These are then used as the location of the sMRI-derived fiducials in native sMRI space.

   2a) We have polhemus-derived fids in polhemus space and sMRI-derived fids in native sMRI space. Use these to estimate the affine xform from native sMRI space to polhemus
       (head) space.

   2b) We can also optionally learn the best scaling to add to this affine xform, such that the sMRI-derived fids are scaled in size to better match the polhemus-derived fids.
       This assumes that we trust the size (e.g. in mm) of the polhemus-derived fids, but not the size of sMRI-derived fids. E.g. this might be the case if we do not trust
       the size (e.g. in mm) of the sMRI, or if we are using a template sMRI that would has not come from this subject.

   3)  If a scaling is learnt in step 2, we apply it to sMRI, and to anything derived from sMRI.

   4)  Transform sMRI-derived headshape points into polhemus space.

   5)  We have the polhemus-derived headshape points in polhemus space and the sMRI-derived headshape (scalp surface) in native sMRI space.  Use these to estimate the affine
       xform from native sMRI space using the ICP algorithm initilaised using the xform estimate in step 2.

   :param fif_file: Full path to MNE-derived fif file.
   :type fif_file: string
   :param subjects_dir: Directory to put RHINO subject dirs in. Files will be in subjects_dir/subject/coreg.
   :type subjects_dir: string
   :param subject: Subject name dir to put RHINO files in. Files will be in subjects_dir/subject/coreg.
   :type subject: string
   :param use_headshape: Determines whether polhemus derived headshape points are used.
   :type use_headshape: bool
   :param use_nose: Determines whether nose is used to aid coreg, only relevant if use_headshape=True.
   :type use_nose: bool
   :param use_dev_ctf_t: Determines whether to set dev_head_t equal to dev_ctf_t in fif_file's info. This option is only potentially needed for fif files originating from CTF scanners.
                         Will be ignored if dev_ctf_t does not exist in info (e.g. if the data is from a MEGIN scanner)
   :type use_dev_ctf_t: bool
   :param already_coregistered: Indicates that the data is already coregistered. Causes a simplified coreg to be run that assumes that device space, head space and mri space are all the same space,
                                and that the sensor locations and polhemus points (if there are any) are already in that space. This means that dev_head_t is identity and that dev_mri_t is identity.
                                This simplified coreg is needed to ensure that all the necessary coreg output files are created.
   :type already_coregistered: bool
   :param allow_smri_scaling: Indicates if we are to allow scaling of the sMRI, such that the sMRI-derived fids are scaled in size to better match the polhemus-derived fids. This assumes that we
                              trust the size (e.g. in mm) of the polhemus-derived fids, but not the size of the sMRI-derived fids. E.g. this might be the case if we do not trust the size (e.g. in mm)
                              of the sMRI, or if we are using a template sMRI that has not come from this subject.
   :type allow_smri_scaling: bool
   :param n_init: Number of initialisations for the ICP algorithm that performs coregistration.
   :type n_init: int


.. py:function:: coreg_metrics(subjects_dir, subject)

   Calculate metrics that summarise the coregistration.

   :param subjects_dir: Directory containing RHINO subject directories.
   :type subjects_dir: string
   :param subject: Subject name directory containing RHINO files.
   :type subject: string

   :returns: **fiducial_distances** -- Distance in cm between the polhemus and sMRI fiducials. Order is nasion, lpa, rpa.
   :rtype: np.ndarray


.. py:function:: coreg_display(subjects_dir, subject, plot_type='surf', display_outskin=True, display_outskin_with_nose=True, display_sensors=True, display_sensor_oris=True, display_fiducials=True, display_headshape_pnts=True, filename=None)

   Display coregistration.

   Displays the coregistered RHINO scalp surface and polhemus/sensor locations.

   Display is done in MEG (device) space (in mm).

   Purple dots are the polhemus derived fiducials (these only get used to initialse the coreg, if headshape points are being used).

   Yellow diamonds are the MNI standard space derived fiducials (these are the ones that matter).

   :param subjects_dir: Directory to put RHINO subject dirs in. Files will be in subjects_dir/subject/rhino/coreg.
   :type subjects_dir: string
   :param subject: Subject name dir to put RHINO files in. Files will be in subjects_dir/subject/rhino/coreg.
   :type subject: string
   :param plot_type:
                     Either:
                         'surf' to do a 3D surface plot using surface meshes.
                         'scatter' to do a scatter plot using just point clouds.
   :type plot_type: string
   :param display_outskin_with_nose: Whether to show nose with scalp surface in the display.
   :type display_outskin_with_nose: bool
   :param display_outskin: Whether to show scalp surface in the display.
   :type display_outskin: bool
   :param display_sensors: Whether to include sensors in the display.
   :type display_sensors: bool
   :param display_sensor_oris - bool: Whether to include sensor orientations in the display.
   :param display_fiducials - bool: Whether to include fiducials in the display.
   :param display_headshape_pnts - bool: Whether to include headshape points in the display.
   :param filename: Filename to save display to (as an interactive html).
                    Must have extension .html.
   :type filename: str


.. py:function:: bem_display(subjects_dir, subject, plot_type='surf', display_outskin_with_nose=True, display_sensors=False, filename=None)

   Displays the coregistered RHINO scalp surface and inner skull surface.

   Display is done in MEG (device) space (in mm).

   :param subjects_dir: Directory to find RHINO subject dirs in.
   :type subjects_dir: string
   :param subject: Subject name dir to find RHINO files in.
   :type subject: string
   :param plot_type:
                     Either:
                         'surf' to do a 3D surface plot using surface meshes.
                         'scatter' to do a scatter plot using just point clouds.
   :type plot_type: string
   :param display_outskin_with_nose: Whether to include nose with scalp surface in the display.
   :type display_outskin_with_nose: bool
   :param display_sensors: Whether to include sensor locations in the display.
   :type display_sensors: bool
   :param filename: Filename to save display to (as an interactive html). Must have extension .html.
   :type filename: str


.. py:function:: get_coreg_filenames(subjects_dir, subject)

   Files used in coregistration by RHINO.

   Files will be in subjects_dir/subject/rhino/coreg.

   :param subjects_dir: Directory containing the subject directories.
   :type subjects_dir: string
   :param subject: Subject directory name to put the coregistration files in.
   :type subject: string

   :returns: **filenames** -- A dict of files generated and used by RHINO.
   :rtype: dict


.. py:function:: log_or_print(msg, warning=False)

   Execute logger.info if an OSL logger has been setup, otherwise print.

   :param msg: Message to log/print.
   :type msg: str
   :param warning: Is the msg a warning? Defaults to False, which will print info.
   :type warning: bool


.. py:function:: extract_polhemus_from_info(fif_file, headshape_outfile, nasion_outfile, rpa_outfile, lpa_outfile, include_eeg_as_headshape=False, include_hpi_as_headshape=True)

   Extract polhemus from FIF info.

   Extract polhemus fids and headshape points from MNE raw.info and write them out in the required file format for rhino (in head/polhemus space in mm).

   Should only be used with MNE-derived .fif files that have the expected digitised points held in info['dig'] of fif_file.

   :param fif_file: Full path to MNE-derived fif file.
   :type fif_file: string
   :param headshape_outfile: Filename to save headshape points to.
   :type headshape_outfile: string
   :param nasion_outfile: Filename to save nasion to.
   :type nasion_outfile: string
   :param rpa_outfile: Filename to save rpa to.
   :type rpa_outfile: string
   :param lpa_outfile: Filename to save lpa to.
   :type lpa_outfile: string
   :param include_eeg_as_headshape: Should we include EEG locations as headshape points?
   :type include_eeg_as_headshape: bool, optional
   :param include_hpi_as_headshape: Should we include HPI locations as headshape points?
   :type include_hpi_as_headshape: bool, optional


.. py:function:: save_mni_fiducials(fiducials_file, nasion_outfile, rpa_outfile, lpa_outfile)

   Save MNI fiducials used to calculate sMRI fiducials.

   The file must be in MNI space with the following format:

       nas -0.5 77.5 -32.6
       lpa -74.4 -20.0 -27.2
       rpa 75.4 -21.1 -21.9

   Note, the first column (fiducial naming) is ignored but the rows must be in the above order, i.e. be (nasion, left, right).

   The order of the coordinates is the same as given in FSLeyes.

   :param fiducials_file: Full path to text file containing the sMRI fiducials.
   :type fiducials_file: str
   :param headshape_outfile: Filename to save nasion to.
   :type headshape_outfile: str
   :param nasion_outfile: Filename to save naison to.
   :type nasion_outfile: str
   :param rpa_outfile: Filename to save rpa to.
   :type rpa_outfile: str
   :param lpa_outfile: Filename to save lpa to.
   :type lpa_outfile: str


.. py:function:: plot_polhemus_points(txt_fnames, colors=None, scales=None, markers=None, alphas=None)

   Plot polhemus points.

   :param txt_fnames: List of filenames containing polhemus points.
   :type txt_fnames: list of strings
   :param colors: List of colors for each set of points.
   :type colors: list of tuples
   :param scales: List of scales for each set of points.
   :type scales: list of floats
   :param markers: List of markers for each set of points.
   :type markers: list of strings
   :param alphas: List of alphas for each set of points.
   :type alphas: list of floats


.. py:function:: delete_headshape_points(recon_dir=None, subject=None, polhemus_headshape_file=None)

   Interactively delete headshape points.

   Shows an interactive figure of the polhemus derived headshape points in polhemus space. Points can be clicked on to delete them.

   The figure should be closed upon completion, at which point there is the option to save the deletions.

   :param subjects_dir: Directory containing the subject directories, in the directory structure used by RHINO:
   :type subjects_dir: string
   :param subject: Subject directory name, in the directory structure used by RHINO.
   :type subject: string
   :param polhemus_headshape_file: Full file path to get the polhemus_headshape_file from, and to save any changes to. Note that this is an npy file containing the
                                   (3 x num_headshapepoints) numpy array of headshape points.
   :type polhemus_headshape_file: string

   .. rubric:: Notes

   We can call this in two different ways, either:

   1) Specify the subjects_dir AND the subject directory in the
      directory structure used by RHINO:

           delete_headshape_points(recon_dir=recon_dir, subject=subject)

   or:

   2) Specify the full path to the .npy file containing the (3 x num_headshapepoints) numpy array of headshape points:

           delete_headshape_points(polhemus_headshape_file=polhemus_headshape_file)


.. py:function:: remove_stray_headshape_points(outdir, subject, nose=True)

   Remove stray headshape points.

   Removes headshape points near the nose, on the neck or far away from the head.

   :param outdir: Path to subjects directory.
   :type outdir: str
   :param subject: Subject directory name.
   :type subject: str
   :param noise: Should we remove headshape points near the nose?
                 Useful to remove these if we have defaced structurals or aren't
                 extracting the nose from the structural.
   :type noise: bool, optional


.. py:function:: extract_polhemus_from_pos(outdir, subject, filepath)

   Saves fiducials/headshape from a pos file.

   :param outdir: Subjects directory.
   :type outdir: str
   :param subject: Subject subdirectory/ID.
   :type subject: str
   :param filepath: Full path to the .pos file for this subject.
                    Any reference to '{subject}' (or '{0}') is replaced by the subject ID.
                    E.g. 'data/{subject}/meg/{subject}_headshape.pos' with subject='sub-001'
                    becomes 'data/sub-001/meg/sub-001_headshape.pos'.
   :type filepath: str


.. py:function:: extract_polhemus_from_elc(outdir, subject, filepath, remove_headshape_near_nose=False)

   Saves fiducials/headshape from an elc file.

   :param outdir: Subjects directory.
   :type outdir: str
   :param subject: Subject subdirectory/ID.
   :type subject: str
   :param filepath: Full path to the .elc file for this subject.
                    Any reference to '{subject}' (or '{0}') is replaced by the subject ID.
                    E.g. 'data/{subject}/meg/{subject}_headshape.elc' with subject='sub-001'
                    becomes 'data/sub-001/meg/sub-001_headshape.elc'.
   :type filepath: str
   :param remove_headshape_near_nose: Should we remove any headshape points near the nose?
   :type remove_headshape_near_nose: bool, optional


.. py:function:: log_or_print(msg, warning=False)

   Execute logger.info if an OSL logger has been setup, otherwise print.

   :param msg: Message to log/print.
   :type msg: str
   :param warning: Is the msg a warning? Defaults to False, which will print info.
   :type warning: bool


.. py:function:: forward_model(subjects_dir, subject, model='Single Layer', gridstep=8, mindist=4.0, exclude=0.0, eeg=False, meg=True, verbose=False)

   Compute forward model.

   :param subjects_dir: Directory to find RHINO subject dirs in.
   :type subjects_dir: string
   :param subject: Subject name dir to find RHINO files in.
   :type subject: string
   :param model: 'Single Layer' or 'Triple Layer'
                 'Single Layer' to use single layer (brain/cortex)
                 'Triple Layer' to three layers (scalp, inner skull, brain/cortex)
   :type model: string
   :param gridstep: A grid will be constructed with the spacing given by ``gridstep`` in mm generating a volume source space.
   :type gridstep: int
   :param mindist: Exclude points closer than this distance (mm) to the bounding surface.
   :type mindist: float
   :param exclude: Exclude points closer than this distance (mm) from the center of mass of the bounding surface.
   :type exclude: float
   :param eeg: Whether to compute forward model for eeg sensors
   :type eeg: bool
   :param meg: Whether to compute forward model for meg sensors
   :type meg: bool


.. py:function:: make_fwd_solution(subjects_dir, subject, src, bem, meg=True, eeg=True, mindist=0.0, ignore_ref=False, n_jobs=1, verbose=None)

   Calculate a forward solution for a subject. This is a RHINO wrapper for mne.make_forward_solution.

   See mne.make_forward_solution for the full set of parameters, with the exception of:

   :param subjects_dir: Directory to find RHINO subject dirs in.
   :type subjects_dir: string
   :param subject: Subject name dir to find RHINO files in.
   :type subject: string

   :returns: **fwd** -- The forward solution.
   :rtype: instance of Forward

   .. rubric:: Notes

   Forward modelling is done in head space.

   The coords of points to reconstruct to can be found in the output here:

   >>> fwd['src'][0]['rr'][fwd['src'][0]['vertno']]

   where they are in head space in metres.

   The same coords of points to reconstruct to can be found in the input here:

   >>> src[0]['rr'][src[0]['vertno']]

   where they are in native MRI space in metres.


.. py:function:: setup_volume_source_space(subjects_dir, subject, gridstep=5, mindist=5.0, exclude=0.0)

   Set up a volume source space grid inside the inner skull surface.

   This is a RHINO specific version of mne.setup_volume_source_space.

   :param subjects_dir: Directory to find RHINO subject dirs in.
   :type subjects_dir: string
   :param subject: Subject name dir to find RHINO files in.
   :type subject: string
   :param gridstep: A grid will be constructed with the spacing given by ``gridstep`` in mm generating a volume source space.
   :type gridstep: int
   :param mindist: Exclude points closer than this distance (mm) to the bounding surface.
   :type mindist: float
   :param exclude: Exclude points closer than this distance (mm) from the center of mass of the bounding surface.
   :type exclude: float

   :returns: **src** -- A single source space object.
   :rtype: :py:class:`mne.SourceSpaces`

   .. seealso:: :py:func:`mne.setup_volume_source_space`

   .. rubric:: Notes

   This is a RHINO specific version of mne.setup_volume_source_space, which can handle smri's that are niftii files.
   This specifically uses the inner skull surface in:

   >>> get_coreg_filenames(subjects_dir, subject)['bet_inskull_surf_file']

   to define the source space grid.

   This will also copy the:

   >>> get_coreg_filenames(subjects_dir, subject)['bet_inskull_surf_file']

   file to:

       ``subjects_dir/subject/bem/inner_skull.surf`

   since this is where mne expects to find it when mne.make_bem_model is called.

   The coords of points to reconstruct to can be found in the output here:

   >>> src[0]['rr'][src[0]['vertno']]

   where they are in native MRI space in metres.


.. py:function:: log_or_print(msg, warning=False)

   Execute logger.info if an OSL logger has been setup, otherwise print.

   :param msg: Message to log/print.
   :type msg: str
   :param warning: Is the msg a warning? Defaults to False, which will print info.
   :type warning: bool


.. py:function:: get_surfaces_filenames(subjects_dir, subject)

   Generates a dict of files generated and used by rhino.compute_surfaces.

   Files will be in subjects_dir/subject/rhino/surfaces.

   :param subjects_dir: Directory containing the subject directories.
   :type subjects_dir: string
   :param subject: Subject directory name to put the surfaces in.
   :type subject: string

   :returns: **filenames** -- A dict of files generated and used by rhino.compute_surfaces. Note that  due to the unusal naming conventions used by BET:
             - bet_inskull_*_file is actually the brain surface
             - bet_outskull_*_file is actually the inner skull surface
             - bet_outskin_*_file is the outer skin/scalp surface
   :rtype: dict


.. py:function:: check_if_already_computed(subjects_dir, subject, include_nose)

   Checks if surfaces have already been computed.

   :param subjects_dir: Directory to put RHINO subject directories in. Files will be in subjects_dir/subject/surfaces.
   :type subjects_dir: string
   :param subject: Subject name directory to put RHINO files in. Files will be in subjects_dir/subject/surfaces.
   :type subject: string
   :param include_nose: Specifies whether to add the nose to the outer skin (scalp) surface.
   :type include_nose: bool

   :returns: **already_computed** -- Flag indicating if surfaces have been computed.
   :rtype: bool


.. py:function:: compute_surfaces(smri_file, subjects_dir, subject, include_nose=True, cleanup_files=True, recompute_surfaces=False, do_mri2mniaxes_xform=True, use_qform=False)

   Compute surfaces.

   Extracts inner skull, outer skin (scalp) and brain surfaces from passed in smri_file, which is assumed to be a T1, using FSL. Assumes that the sMRI file has a valid sform.

   Call get_surfaces_filenames(subjects_dir, subject) to get a file list of generated files.

   In more detail:
   1) Transform sMRI to be aligned with the MNI axes so that BET works well
   2) Use bet to skull strip sMRI so that flirt works well
   3) Use flirt to register skull stripped sMRI to MNI space
   4) Use BET/BETSURF to get:
   a) The scalp surface (excluding nose), this gives the sMRI-derived headshape points in native sMRI space, which can be used in the headshape points registration later.
   b) The scalp surface (outer skin), inner skull and brain surface, these can be used for forward modelling later. Note that  due to the unusal naming conventions used by BET:
      - bet_inskull_mesh_file is actually the brain surface
      - bet_outskull_mesh_file is actually the inner skull surface
      - bet_outskin_mesh_file is the outer skin/scalp surface
   5) Refine scalp outline, adding nose to scalp surface (optional)
   6) Output the transform from sMRI space to MNI
   7) Output surfaces in sMRI space

   :param smri_file: Full path to structural MRI in niftii format (with .nii.gz extension). This is assumed to have a valid sform, i.e. the sform code needs to be 4 or 1, and the sform
                     should transform from voxel indices to voxel coords in mm. The axis sform used to do this will be the native/sMRI axis used throughout rhino. The qform will be ignored.
   :type smri_file: str
   :param subjects_dir: Directory to put RHINO subject directories in. Files will be in subjects_dir/subject/surfaces.
   :type subjects_dir: str
   :param subject: Subject name directory to put RHINO files in. Files will be in subjects_dir/subject/surfaces.
   :type subject: str
   :param include_nose: Specifies whether to add the nose to the outer skin (scalp) surface. This can help rhino's coreg to work better, assuming that there are headshape points that also
                        include the nose. Requires the smri_file to have a FOV that includes the nose!
   :type include_nose: bool, optional
   :param cleanup_files: Specifies whether to cleanup intermediate files in the coreg directory.
   :type cleanup_files: bool, optional
   :param recompute_surfaces: Specifies whether or not to run compute_surfaces if the passed in options have already been run.
   :type recompute_surfaces: bool, optional
   :param do_mri2mniaxes_xform: Specifies whether to do step 1) above, i.e. transform sMRI to be aligned with the MNI axes. Sometimes needed when the sMRI goes out of the MNI FOV after step 1).
   :type do_mri2mniaxes_xform: bool, optional
   :param use_qform: Should we replace the sform with the qform? Useful if the sform code is incompatible with osl-ephys, but the qform is compatible.
   :type use_qform: bool, optional

   :returns: **already_computed** -- Flag indicating if we're using previously computed surfaces.
   :rtype: bool


.. py:function:: surfaces_display(subjects_dir, subject)

   Display surfaces.

   Displays the surfaces extracted from the sMRI using rhino.compute_surfaces.

   Display is shown in sMRI (native) space.

   :param subjects_dir: Directory to put RHINO subject directories in. Files will be in subjects_dir/subject/surfaces.
   :type subjects_dir: string
   :param subject: Subject name directory to put RHINO files in. Files will be in subjects_dir/subject/surfaces.
   :type subject: string

   .. rubric:: Notes

   bet_inskull_mesh_file is actually the brain surface and bet_outskull_mesh_file is the inner skull surface, due to the naming conventions used by BET.


.. py:function:: plot_surfaces(subjects_dir, subject, include_nose, already_computed=False)

   Plot a structural MRI and extracted surfaces.

   :param subjects_dir: Directory to put RHINO subject directories in. Files will be in subjects_dir/subject/surfaces.
   :type subjects_dir: str
   :param subject: Subject name directory to put RHINO files in. Files will be in subjects_dir/subject/surfaces.
   :type subject: str
   :param include_nose: Specifies whether to add the nose to the outer skin (scalp) surface.
   :type include_nose: bool
   :param already_computed: Have the surfaces (and plots) already been computed?
   :type already_computed: bool, optional

   :returns: **output_files** -- Paths to image files saved by this function.
   :rtype: list of str


.. py:function:: setup_fsl(directory)

   Setup FSL.

   :param directory: Path to FSL installation.
   :type directory: str


.. py:function:: check_fsl()

   Check FSL is installed.


.. py:function:: fsleyes(image_list)

   Displays list of niftii's using external command line call to fsleyes.

   :param image_list: Niftii filenames or tuple of niftii filenames
   :type image_list: string | tuple of strings

   .. rubric:: Examples

   fsleyes(image)
   fsleyes((image1, image2))


.. py:function:: fsleyes_overlay(background_img, overlay_img)

   Displays overlay_img and background_img using external command line call to fsleyes.

   :param background_img: Background niftii filename
   :type background_img: string
   :param overlay_img: Overlay niftii filename
   :type overlay_img: string


