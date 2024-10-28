:py:mod:`osl_ephys.source_recon.rhino.surfaces`
===============================================

.. py:module:: osl_ephys.source_recon.rhino.surfaces

.. autoapi-nested-parse::

   Calculation of surfaces in RHINO.



Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   osl_ephys.source_recon.rhino.surfaces.get_surfaces_filenames
   osl_ephys.source_recon.rhino.surfaces.check_if_already_computed
   osl_ephys.source_recon.rhino.surfaces.compute_surfaces
   osl_ephys.source_recon.rhino.surfaces.surfaces_display
   osl_ephys.source_recon.rhino.surfaces.plot_surfaces



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


