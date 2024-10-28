:py:mod:`osl_ephys.utils.opm`
=============================

.. py:module:: osl_ephys.utils.opm

.. autoapi-nested-parse::

   Utility function for handling OPM data.



Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   osl_ephys.utils.opm.convert_notts
   osl_ephys.utils.opm.correct_mri



Attributes
~~~~~~~~~~

.. autoapisummary::

   osl_ephys.utils.opm.coreg_filenames


.. py:function:: convert_notts(notts_opm_mat_file, smri_file, tsv_file, fif_file, smri_fixed_file)

   Convert Nottingham OPM data from matlab file to fif file.

   :param notts_opm_mat_file: The matlab file containing the OPM data.
   :type notts_opm_mat_file: str
   :param smri_file: The structural MRI file.
   :type smri_file: str
   :param tsv_file: The tsv file containing the sensor locations and orientations.
   :type tsv_file: str
   :param fif_file: The output fif file.
   :type fif_file: str
   :param smri_fixed_file: The output structural MRI file with corrected sform.
   :type smri_fixed_file: str

   .. rubric:: Notes

   The matlab file is assumed to contain a variable called 'data' which is
   a matrix of size nSamples x nChannels.
   The matlab file is assumed to contain a variable called 'fs' which is
   the sampling frequency.
   The tsv file is assumed to contain a header row, and the following columns:
   name, type, bad, x, y, z, qx, qy, qz
   The x,y,z columns are the sensor locations in metres.
   The qx,qy,qz columns are the sensor orientations in metres.


.. py:function:: correct_mri(smri_file, smri_fixed_file)

   Correct the sform in the structural MRI file.

   :param smri_file: The structural MRI file.
   :type smri_file: str
   :param smri_fixed_file: The output structural MRI file with corrected sform.
   :type smri_fixed_file: str

   :returns: **sform_std** -- The new sform.
   :rtype: ndarray

   .. rubric:: Notes

   The sform is corrected so that it is in standard orientation.


.. py:data:: coreg_filenames

   

