:py:mod:`osl_ephys.utils.study`
===============================

.. py:module:: osl_ephys.utils.study


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   osl_ephys.utils.study.Study




.. py:class:: Study(studydir)


   Class for simple file finding and looping.

   :param studydir: The study directory with wildcards.
   :type studydir: str

   .. attribute:: studydir

      The study directory with wildcards.

      :type: str

   .. attribute:: fieldnames

      The wildcards in the study directory, i.e., the field names in between {braces}.

      :type: list

   .. attribute:: globdir

      The study directory with wildcards replaced with *.

      :type: str

   .. attribute:: match_files

      The files that match the globdir.

      :type: list

   .. attribute:: match_values

      The values of the field names (i.e., wildcards) for each file.

      :type: list

   .. attribute:: fields

      The field names and values for each file.

      :type: dict

   .. rubric:: Notes

   This class is a simple wrapper around glob and parse. It works something like this:

   >>> studydir = '/path/to/study/{subject}/{session}/{subject}_{task}.fif'
   >>> study = Study(studydir)

   Get all files in the study directory:

   >>> study.get()

   Get all files for a particular subject:

   >>> study.get(subject='sub-01')

   Get all files for a particular subject and session:

   >>> study.get(subject='sub-01', session='ses-01')

   The fieldnames that are not specified in ``get`` are replaced with wildcards (``*``).

   .. py:method:: refresh()

      Refresh the study directory.


   .. py:method:: get(check_exist=True, **kwargs)

      Get files from the study directory that match the fieldnames.

      :param check_exist: Whether to check if the files exist.
      :type check_exist: bool
      :param \*\*kwargs: The field names and values to match.
      :type \*\*kwargs: dict

      :returns: **out** -- The files that match the field names and values.
      :rtype: list

      .. rubric:: Notes

      Example using ``Study`` and ``Study.get()``:

      >>> studydir = '/path/to/study/{subject}/{session}/{subject}_{task}.fif'
      >>> study = Study(studydir)

      Get all files in the study directory:

      >>> study.get()

      Get all files for a particular subject:

      >>> study.get(subject='sub-01')

      Get all files for a particular subject and session:

      >>> study.get(subject='sub-01', session='ses-01')

      The fieldnames that are not specified in ``get`` are replaced with wildcards (``*``).



