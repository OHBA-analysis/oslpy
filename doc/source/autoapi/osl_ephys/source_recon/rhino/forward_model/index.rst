:py:mod:`osl_ephys.source_recon.rhino.forward_model`
====================================================

.. py:module:: osl_ephys.source_recon.rhino.forward_model

.. autoapi-nested-parse::

   Forward modelling in RHINO.



Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   osl_ephys.source_recon.rhino.forward_model.forward_model
   osl_ephys.source_recon.rhino.forward_model.make_fwd_solution
   osl_ephys.source_recon.rhino.forward_model.setup_volume_source_space



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


