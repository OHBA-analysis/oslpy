:py:mod:`osl_ephys.source_recon.rhino.utils`
============================================

.. py:module:: osl_ephys.source_recon.rhino.utils

.. autoapi-nested-parse::

   RHINO utilities.



Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   osl_ephys.source_recon.rhino.utils.get_rhino_files
   osl_ephys.source_recon.rhino.utils.system_call
   osl_ephys.source_recon.rhino.utils.get_gridstep
   osl_ephys.source_recon.rhino.utils.niimask2indexpointcloud
   osl_ephys.source_recon.rhino.utils.niimask2mmpointcloud
   osl_ephys.source_recon.rhino.utils.closest_node
   osl_ephys.source_recon.rhino.utils.get_vol_info_from_nii
   osl_ephys.source_recon.rhino.utils.get_sform
   osl_ephys.source_recon.rhino.utils.get_orient
   osl_ephys.source_recon.rhino.utils.check_nii_for_nan
   osl_ephys.source_recon.rhino.utils.majority
   osl_ephys.source_recon.rhino.utils.binary_majority3d
   osl_ephys.source_recon.rhino.utils.rigid_transform_3D
   osl_ephys.source_recon.rhino.utils.xform_points
   osl_ephys.source_recon.rhino.utils.best_fit_transform
   osl_ephys.source_recon.rhino.utils.nearest_neighbor
   osl_ephys.source_recon.rhino.utils.icp
   osl_ephys.source_recon.rhino.utils.rhino_icp
   osl_ephys.source_recon.rhino.utils.get_vtk_mesh_native
   osl_ephys.source_recon.rhino.utils.get_flirtcoords2native_xform
   osl_ephys.source_recon.rhino.utils.transform_vtk_mesh
   osl_ephys.source_recon.rhino.utils.get_mne_xform_from_flirt_xform
   osl_ephys.source_recon.rhino.utils.get_flirt_xform_between_axes
   osl_ephys.source_recon.rhino.utils.timeseries2nii
   osl_ephys.source_recon.rhino.utils.recon_timeseries2niftii
   osl_ephys.source_recon.rhino.utils.save_or_show_renderer
   osl_ephys.source_recon.rhino.utils.create_freesurfer_meshes_from_bet_surfaces
   osl_ephys.source_recon.rhino.utils.create_freesurfer_mesh_from_bet_surface
   osl_ephys.source_recon.rhino.utils.transform_bet_surfaces
   osl_ephys.source_recon.rhino.utils.extract_rhino_files



.. py:function:: get_rhino_files(subjects_dir, subject)

   Get paths to all RHINO files.

   Files will be in subjects_dir/subject/rhino.

   :param subjects_dir: Directory containing the subject directories.
   :type subjects_dir: string
   :param subject: Subject directory name to put the coregistration files in.
   :type subject: string

   :returns: **files** -- A dict of files generated and used by RHINO. Contains three keys:
             - 'surf': containing surface extraction file paths.
             - 'coreg': containing coregistration file paths.
             - 'fwd_model': containing the forward model file path.
   :rtype: dict


.. py:function:: system_call(cmd, verbose=False)

   Run a system call.

   :param cmd: Command to run.
   :type cmd: string
   :param verbose: Print command before running.
   :type verbose: bool


.. py:function:: get_gridstep(coords)

   Get gridstep (i.e. spatial resolution of dipole grid) in mm.

   :param coords: Coordinates.
   :type coords: numpy.ndarray

   :returns: **gridstep** -- Spatial resolution of dipole grid in mm.
   :rtype: int


.. py:function:: niimask2indexpointcloud(nii_fname, volindex=None)

   Takes in a nii.gz mask file name (which equals zero for background and != zero for the mask) and returns the mask as a 3 x npoints point cloud.

   :param nii_fname: A nii.gz mask file name (with zero for background, and !=0 for the mask).
   :type nii_fname: string
   :param volindex: Volume index, used if nii_mask is a 4D file.
   :type volindex: int

   :returns: **pc** -- 3 x npoints point cloud as voxel indices.
   :rtype: numpy.ndarray


.. py:function:: niimask2mmpointcloud(nii_mask, volindex=None)

   Takes in a nii.gz mask (which equals zero for background and neq zero for the mask) and returns the mask as a 3 x npoints point cloud in native space in mm's.

   :param nii_mask: A nii.gz mask file name or the [x,y,z] volume (with zero for background, and !=0 for the mask).
   :type nii_mask: string
   :param volindex: Volume index, used if nii_mask is a 4D file.
   :type volindex: int

   :returns: * **pc** (*numpy.ndarray*) -- 3 x npoints point cloud as mm in native space (using sform).
             * **values** (*numpy.ndarray*) -- npoints values.


.. py:function:: closest_node(node, nodes)

   Find nearest node in nodes to the passed in node.

   :returns: * **index** (*int*) -- Index to the nearest node in nodes.
             * **distance** (*float*) -- Distance.


.. py:function:: get_vol_info_from_nii(mri)

   Read volume info from an MRI file.

   :param mri: Path to MRI file.
   :type mri: str

   :returns: **out** -- Dictionary with keys 'mri_width', 'mri_height', 'mri_depth' and 'mri_volume_name'.
   :rtype: dict


.. py:function:: get_sform(nii_file)

   sform allows mapping from simple voxel index cordinates (e.g. from 0 to 256) in scanner space to continuous coordinates (in mm)

   sformcode = os.popen('fslorient -getsformcode {}'.format(nii_file)).read().strip()


.. py:function:: get_orient(nii_file)


.. py:function:: check_nii_for_nan(filename)


.. py:function:: majority(values_ptr, len_values, result, data)

   def _majority(buffer, required_majority):
      return buffer.sum() >= required_majority

   See: https://ilovesymposia.com/2017/03/12/scipys-new-lowlevelcallable-is-a-game-changer/

   Numba cfunc that takes in:
   a double pointer pointing to the values within the footprint,
   a pointer-sized integer that specifies the number of values in the footprint,
   a double pointer for the result, and
   a void pointer, which could point to additional parameters


.. py:function:: binary_majority3d(img)

   Set a pixel to 1 if a required majority (default=14) or more pixels in its 3x3x3 neighborhood are 1, otherwise, set the pixel to 0. img is a 3D binary image


.. py:function:: rigid_transform_3D(B, A, compute_scaling=False)

   Calculate affine transform from points in A to point in B.

   :param A: 3 x num_points. Set of points to register from.
   :type A: numpy.ndarray
   :param B: 3 x num_points. Set of points to register to.
   :type B: numpy.ndarray
   :param compute_scaling: Do we compute a scaling on top of rotation and translation?
   :type compute_scaling: bool

   :returns: * **xform** (*numpy.ndarray*) -- Calculated affine transform, does not include scaling.
             * **scaling_xform** (*numpy.ndarray*) -- Calculated scaling transform (a diagonal 4x4 matrix), does not include rotation or translation.
             * **see http** (*//nghiaho.com/?page_id=671*)


.. py:function:: xform_points(xform, pnts)

   Applies homogenous linear transformation to an array of 3D coordinates.

   :param xform: 4x4 matrix containing the affine transform.
   :type xform: numpy.ndarray
   :param pnts: points to transform, should be 3 x num_points.
   :type pnts: numpy.ndarray

   :returns: **newpnts** -- pnts following the xform, will be 3 x num_points.
   :rtype: numpy.ndarray


.. py:function:: best_fit_transform(A, B)

   Calculates the least-squares best-fit transform that maps corresponding points A to B in m spatial dimensions.

   :param A: Nxm numpy array of corresponding points.
   :type A: numpy.ndarray
   :param B: Nxm numpy array of corresponding points.
   :type B: numpy.ndarray
   :param Outputs:
   :param -------:
   :param T: (m+1)x(m+1) homogeneous transformation matrix that maps A on to B.
   :type T: numpy.ndarray


.. py:function:: nearest_neighbor(src, dst)

   Find the nearest (Euclidean) neighbor in dst for each point in src.

   :param src: Nxm array of points.
   :type src: numpy.ndarray
   :param dst: Nxm array of points.
   :type dst: numpy.ndarray

   :returns: * **distances** (*numpy.ndarray*) -- Euclidean distances of the nearest neighbor.
             * **indices** (*numpy.ndarray*) -- dst indices of the nearest neighbor.


.. py:function:: icp(A, B, init_pose=None, max_iterations=50, tolerance=0.0001)

   The Iterative Closest Point method: finds best-fit transform that maps points A on to points B.

   :param A: Nxm numpy array of source mD points.
   :type A: numpy.ndarray
   :param B: Nxm numpy array of destination mD point.
   :type B: numpy.ndarray
   :param init_pose: (m+1)x(m+1) homogeneous transformation.
   :type init_pose: numpy.ndarray
   :param max_iterations: Exit algorithm after max_iterations.
   :type max_iterations: int
   :param tolerance: Convergence criteria.
   :type tolerance: float

   :returns: * **T** (*numpy.ndarray*) -- (4 x 4) Final homogeneous transformation that maps A on to B.
             * **distances** (*numpy.ndarray*) -- Euclidean distances (errors) of the nearest neighbor.
             * **i** (*float*) -- Number of iterations to converge.

   .. rubric:: Notes

   From: https://github.com/ClayFlannigan/icp/blob/master/icp.py


.. py:function:: rhino_icp(smri_headshape_polhemus, polhemus_headshape_polhemus, n_init=10)

   Runs Iterative Closest Point (ICP) with multiple initialisations.

   :param smri_headshape_polhemus: [3 x N] locations of the Headshape points in polehumus space (i.e. MRI scalp surface).
   :type smri_headshape_polhemus: numpy.ndarray
   :param polhemus_headshape_polhemus: [3 x N] locations of the Polhemus headshape points in polhemus space.
   :type polhemus_headshape_polhemus: numpy.ndarray
   :param n_init: Number of random initialisations to perform.
   :type n_init: int

   :returns: **xform** -- [4 x 4] rigid transformation matrix mapping data2 to data.
   :rtype: numpy.ndarray

   .. rubric:: Notes

   Based on Matlab version from Adam Baker 2014.


.. py:function:: get_vtk_mesh_native(vtk_mesh_file, nii_mesh_file)

   Returns mesh rrs in native space in mm and the mesh tris for the passed in vtk_mesh_file

   nii_mesh_file needs to be the corresponding niftii file from bet that corresponds to the same mesh as in vtk_mesh_file


.. py:function:: get_flirtcoords2native_xform(nii_mesh_file)

   Returns xform_flirtcoords2native transform that transforms from flirtcoords space in mm into native space in mm, where the passed in nii_mesh_file specifies the native space

   Note that for some reason flirt outputs transforms of the form: flirt_mni2mri = mri2flirtcoords x mni2mri x flirtcoords2mni

   and bet_surf outputs the .vtk file vertex values in the same flirtcoords mm coordinate system.

   See the bet_surf manual: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/BET/UserGuide#betsurf

   If the image has radiological ordering (see fslorient) then the mm co-ordinates are the voxel co-ordinates scaled by the mm voxel sizes.

   i.e. (x_mm = x_dim * x) where x_mm are the flirtcoords coords in mm, x is the voxel co-ordinate and x_dim is the voxel size in mm.


.. py:function:: transform_vtk_mesh(vtk_mesh_file_in, nii_mesh_file_in, out_vtk_file, nii_mesh_file_out, xform_file)

   Outputs mesh to out_vtk_file, which is the result of applying the transform xform to vtk_mesh_file_in

   nii_mesh_file_in needs to be the corresponding niftii file from bet that corresponds to the same mesh as in vtk_mesh_file_in

   nii_mesh_file_out needs to be the corresponding niftii file from bet that corresponds to the same mesh as in out_vtk_file


.. py:function:: get_mne_xform_from_flirt_xform(flirt_xform, nii_mesh_file_in, nii_mesh_file_out)

   Returns a mm coordinates to mm coordinates MNE xform that corresponds to the passed in flirt xform.

   Note that we need to do this as flirt xforms include an extra xform based on the voxel dimensions (see get_flirtcoords2native_xform).


.. py:function:: get_flirt_xform_between_axes(from_nii, target_nii)

   Computes flirt xform that moves from_nii to have voxel indices on the same axis as  the voxel indices for target_nii.

   Note that this is NOT the same as registration, i.e. the images are not aligned. In fact the actual coordinates (in mm) are unchanged.
   It is instead about putting from_nii onto the same axes so that the voxel INDICES are comparable. This is achieved by using a transform
   that sets the sform of from_nii to be the same as target_nii without changing the actual coordinates (in mm). Transform needed to do this is:

     from2targetaxes = inv(targetvox2target) * fromvox2from

   In more detail:
   We need the sform for the transformed from_nii to be the same as the sform for the target_nii, without changing the actual coordinates (in mm).
   In other words, we need:

       fromvox2from * from_nii_vox = targetvox2target * from_nii_target_vox

   where
     fromvox2from is sform for from_nii (i.e. converts from voxel indices to
         voxel coords in mm)
     and targetvox2target is sform for target_nii
     and from_nii_vox are the voxel indices for from_nii
     and from_nii_target_vox are the voxel indices for from_nii when transformed onto the target axis.

   => from_nii_target_vox = from2targetaxes * from_nii_vox

   where

     from2targetaxes = inv(targetvox2target) * fromvox2from


.. py:function:: timeseries2nii(timeseries, timeseries_coords, reference_mask_fname, out_nii_fname, times=None)

   Maps the (ndipoles,tpts) array of timeseries to the grid defined by reference_mask_fname and outputs them as a niftii file.

   Assumes the timeseries' dipoles correspond to those in reference_mask_fname. Both timeseries and reference_mask_fname are often output from rhino.transform_recon_timeseries.

   :param timeseries: Time courses. Assumes the timeseries' dipoles correspond to those in reference_mask_fname. Typically derives from rhino.transform_recon_timeseries
   :type timeseries: (ndipoles, ntpts) numpy.ndarray
   :param timeseries_coords: Coords in mm for dipoles corresponding to passed in timeseries
   :type timeseries_coords: (ndipoles, 3) numpy.ndarray
   :param reference_mask_fname: A nii.gz mask file name (with zero for background, and !=0 for the mask). Assumes the mask was used to set dipoles for timeseries, typically derived from
                                rhino.transform_recon_timeseries
   :type reference_mask_fname: string
   :param out_nii_fname: output name of niftii file
   :type out_nii_fname: string
   :param times: Times points in seconds. Assume that times are regularly spaced. Used to set nii file up correctly.
   :type times: (ntpts, ) numpy.ndarray

   :returns: **out_nii_fname** -- Name of output niftii file
   :rtype: string


.. py:function:: recon_timeseries2niftii(subjects_dir, subject, recon_timeseries, out_nii_fname, spatial_resolution=None, reference_brain='mni', times=None)

   Converts a (ndipoles,tpts) array of reconstructed timeseries (in head/polhemus space) to the corresponding dipoles in a standard brain grid in MNI space
   and outputs them as a niftii file.

   :param subjects_dir: Directory to find RHINO subject directories in.
   :type subjects_dir: string
   :param subject: Subject name directory to find RHINO files in.
   :type subject: string
   :param recon_timeseries: Reconstructed time courses (in head (polhemus) space). Assumes that the dipoles are the same (and in the same order) as those in the forward model,
                            rhino_files['fwd_model']. Typically derive from the VolSourceEstimate's output by MNE source recon methods, e.g. mne.beamformer.apply_lcmv,
                            obtained using a forward model generated by RHINO.
   :type recon_timeseries: (ndipoles, ntpts) np.ndarray
   :param spatial_resolution: Resolution to use for the reference brain in mm (must be an integer, or will be cast to nearest int). If None, then the gridstep used in rhino_files['fwd_model'] is used.
   :type spatial_resolution: int
   :param reference_brain: 'mni' indicates that the reference_brain is the stdbrain in MNI space.
                           'mri' indicates that the reference_brain is the sMRI in native/mri space.
   :type reference_brain: string, 'mni' or 'mri'
   :param times: Times points in seconds. Will assume that these are regularly spaced.
   :type times: (ntpts, ) np.ndarray

   :returns: * **out_nii_fname** (*string*) -- Name of output niftii file.
             * **reference_brain_fname** (*string*) -- Niftii file name of standard brain mask in MNI space at requested resolution, int(stdbrain_resolution) (with zero for background, and !=0 for the mask).


.. py:function:: save_or_show_renderer(renderer, filename)

   Save or show a renderer.

   :param renderer: MNE renderer object.
   :type renderer: mne.viz.backends._notebook._Renderer Object
   :param filename: Filename to save display to (as an interactive html). Must have extension .html. If None we display the renderer.
   :type filename: str


.. py:function:: create_freesurfer_meshes_from_bet_surfaces(filenames, xform_mri_voxel2mri)


.. py:function:: create_freesurfer_mesh_from_bet_surface(infile, surf_outfile, xform_mri_voxel2mri, nii_mesh_file=None)

   Creates surface mesh in .surf format and in native mri space in mm from infile.

   :param infile:
                  Either:
                      1) .nii.gz file containing zero's for background and one's for surface
                      2) .vtk file generated by bet_surf (in which case the path to the
                      structural MRI, smri_file, must be included as an input)
   :type infile: string
   :param surf_outfile: Path to the .surf file generated, containing the surface mesh in mm
   :type surf_outfile: string
   :param xform_mri_voxel2mri: 4x4 array. Transform from voxel indices to native/mri mm.
   :type xform_mri_voxel2mri: numpy.ndarray
   :param nii_mesh_file: Path to the niftii mesh file that is the niftii equivalent of vtk file passed in as infile (only needed if infile is a vtk file).
   :type nii_mesh_file: string


.. py:function:: transform_bet_surfaces(flirt_xform_file, mne_xform_file, filenames, smri_file)

   Transforms bet surfaces into mne space.

   :param flirt_xform_file: Path to flirt xform file.
   :type flirt_xform_file: string
   :param mne_xform_file: Path to mne xform file.
   :type mne_xform_file: string
   :param filenames: Dictionary containing filenames.
   :type filenames: dict
   :param smri_file: Path to structural MRI file.
   :type smri_file: string


.. py:function:: extract_rhino_files(old_subjects_dir, new_subjects_dir, subjects='all', exclude=None, gen_report=True)

   Extract RHINO files.

   This function extracts surfaces and coregistration files calculated in a previous run.

   :param old_subjects_dir: Subjects directory created with an older version of osl-ephys.
   :type old_subjects_dir: str
   :param new_subjects_dir: New directory to create.
   :type new_subjects_dir: str
   :param subjects: Subjects to include. Defaults to 'all'.
   :type subjects: str or list
   :param exclude: Subjects to exclude.
   :type exclude: str or list
   :param gen_report bool: Should we generate a report?


