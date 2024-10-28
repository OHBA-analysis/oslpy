:py:mod:`osl_ephys.source_recon.rhino.coreg`
============================================

.. py:module:: osl_ephys.source_recon.rhino.coreg

.. autoapi-nested-parse::

   Registration of Headshapes Including Nose in osl-ephys (RHINO).



Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   osl_ephys.source_recon.rhino.coreg.get_coreg_filenames
   osl_ephys.source_recon.rhino.coreg.coreg
   osl_ephys.source_recon.rhino.coreg.coreg_metrics
   osl_ephys.source_recon.rhino.coreg.coreg_display
   osl_ephys.source_recon.rhino.coreg.bem_display



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


