:py:mod:`osl_ephys.source_recon.rhino.polhemus`
===============================================

.. py:module:: osl_ephys.source_recon.rhino.polhemus

.. autoapi-nested-parse::

   Functions related to polhemus fiducials.



Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   osl_ephys.source_recon.rhino.polhemus.extract_polhemus_from_info
   osl_ephys.source_recon.rhino.polhemus.save_mni_fiducials
   osl_ephys.source_recon.rhino.polhemus.plot_polhemus_points
   osl_ephys.source_recon.rhino.polhemus.delete_headshape_points
   osl_ephys.source_recon.rhino.polhemus.remove_stray_headshape_points
   osl_ephys.source_recon.rhino.polhemus.extract_polhemus_from_pos
   osl_ephys.source_recon.rhino.polhemus.extract_polhemus_from_elc



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


