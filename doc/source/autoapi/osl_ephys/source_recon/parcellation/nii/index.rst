:py:mod:`osl_ephys.source_recon.parcellation.nii`
=================================================

.. py:module:: osl_ephys.source_recon.parcellation.nii

.. autoapi-nested-parse::

   Utility functions to work with parcellation niftii files.

   Example code
   ------------

   import os
   import os.path as op
   from osl_ephys.source_recon import parcellation

   workingdir = '/Users/woolrich/osl/osl/source_recon/parcellation/files/'
   parc_name = 'Schaefer2018_100Parcels_7Networks_order_FSLMNI152_2mm'

   os.system('fslmaths /Users/woolrich/Downloads/{} {}'.format(parc_name, workingdir))

   tmpdir = op.join(workingdir, 'tmp')
   os.mkdir(tmpdir)
   parcel3d_fname = op.join(workingdir, parc_name + '.nii.gz')
   parcel4d_fname = op.join(workingdir, parc_name + '_4d.nii.gz')
   parcellation.nii.convert_3dparc_to_4d(parcel3d_fname, parcel4d_fname, tmpdir, 100)

   mni_file = '/Users/woolrich/osl/osl/source_recon/parcellation/files/MNI152_T1_8mm_brain.nii.gz'
   spatial_res = 8 # mm
   parcel4d_ds_fname = op.join(workingdir, parc_name + '_4d_ds' + str(spatial_res) + '.nii.gz')
   parcellation.nii.spatially_downsample(parcel4d_fname, parcel4d_ds_fname, mni_file, spatial_res)

   os.system('fslmaths /usr/local/fsl/data/atlases/HarvardOxford/HarvardOxford-sub-prob-2mm.nii.gz -thr 50 -bin /Users/woolrich/osl/osl/source_recon/parcellation/files/HarvardOxford-sub-prob-bin-2mm.nii.gz')

   file_in = '/Users/woolrich/osl/osl/source_recon/parcellation/files/Schaefer2018_100Parcels_7Networks_order_FSLMNI152_2mm_4d.nii.gz'
   file_out = '/Users/woolrich/osl/osl/source_recon/parcellation/files/HarvOxf-sub-Schaefer100-combined-2mm_4d.nii.gz'
   file_append = '/Users/woolrich/osl/osl/source_recon/parcellation/files/HarvardOxford-sub-prob-bin-2mm.nii.gz'
   parcel_indices = [3,4,5,6,8,9,10,14,15,16,17,18,19,20] # index from 0
   parcellation.nii.append_4d_parcellation(file_in, file_out, file_append, parcel_indices)

   parc_name = '/Users/woolrich/osl/osl/source_recon/parcellation/files/HarvOxf-sub-Schaefer100-combined-2mm_4d'
   parcel4d_fname = op.join(parc_name + '.nii.gz')
   mni_file = '/Users/woolrich/osl/osl/source_recon/parcellation/files/MNI152_T1_8mm_brain.nii.gz'
   spatial_res = 8 # mm
   parcel4d_ds_fname = op.join(parc_name + '_ds' + str(spatial_res) + '.nii.gz')
   parcellation.nii.spatially_downsample(parcel4d_fname, parcel4d_ds_fname, mni_file, spatial_res)


   fslmaths /Users/woolrich/osl/osl/source_recon/parcellation/files/HarvOxf-sub-Schaefer100-combined-2mm_4d.nii.gz -Tmaxn /Users/woolrich/osl/osl/source_recon/parcellation/files/HarvOxf-sub-Schaefer100-combined-2mm.nii.gz



Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   osl_ephys.source_recon.parcellation.nii.convert_4dparc_to_3d
   osl_ephys.source_recon.parcellation.nii.convert_3dparc_to_4d
   osl_ephys.source_recon.parcellation.nii.spatially_downsample
   osl_ephys.source_recon.parcellation.nii.append_4d_parcellation



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


