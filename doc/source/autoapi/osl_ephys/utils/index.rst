:py:mod:`osl_ephys.utils`
=========================

.. py:module:: osl_ephys.utils


Subpackages
-----------
.. toctree::
   :titlesonly:
   :maxdepth: 3

   simulation_config/index.rst
   spmio/index.rst


Submodules
----------
.. toctree::
   :titlesonly:
   :maxdepth: 1

   create_neuromag306_info/index.rst
   file_handling/index.rst
   logger/index.rst
   misc/index.rst
   opm/index.rst
   package/index.rst
   parallel/index.rst
   run_func/index.rst
   simulate/index.rst
   study/index.rst
   version_utils/index.rst


Package Contents
----------------

Classes
~~~~~~~

.. autoapisummary::

   osl_ephys.utils.Study
   osl_ephys.utils.SPMMEEG



Functions
~~~~~~~~~

.. autoapisummary::

   osl_ephys.utils.process_file_inputs
   osl_ephys.utils.sanitise_filepath
   osl_ephys.utils._load_unicode_inputs
   osl_ephys.utils.find_run_id
   osl_ephys.utils.validate_outdir
   osl_ephys.utils.get_rawdir
   osl_ephys.utils.add_subdir
   osl_ephys.utils.osl_print
   osl_ephys.utils.dask_parallel_bag
   osl_ephys.utils.simulate_data
   osl_ephys.utils.simulate_raw_from_template
   osl_ephys.utils.simulate_rest_mvar
   osl_ephys.utils.convert_notts
   osl_ephys.utils.correct_mri
   osl_ephys.utils.soft_import
   osl_ephys.utils.run_package_tests
   osl_ephys.utils.check_version



Attributes
~~~~~~~~~~

.. autoapisummary::

   osl_ephys.utils.osl_logger
   osl_ephys.utils.fname
   osl_ephys.utils.coreg_filenames
   osl_ephys.utils.__doc__


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



.. py:data:: osl_logger

   

.. py:function:: process_file_inputs(inputs)

   Process inputs for several cases

   The argument, inputs, can be...
   1) string path to unicode file
   2) string path to dir (e.g. if CTF .ds dir)
   3) string path to file or regular-expression matching files
   4) list of string paths to files
   5) list of string paths to dirs (e.g. if CTF .ds dirs)
   6) list of tuples with path to file and output name pairs
   7) list of MNE objects


.. py:function:: sanitise_filepath(fname)

   Remove leading/trailing whitespace, tab, newline and carriage return
   characters.


.. py:function:: _load_unicode_inputs(fname)


.. py:function:: find_run_id(infile, preload=True)


.. py:function:: validate_outdir(outdir)

   Checks if an output directory exists and if not creates it.


.. py:function:: get_rawdir(files)

   Gets the raw data directory from filename(s).


.. py:function:: add_subdir(file, outdir, run_id=None)

   Add sub-directory.


.. py:function:: osl_print(s, logfile=None)


.. py:class:: SPMMEEG(filename)


   .. py:property:: size


   .. py:property:: chantype


   .. py:property:: n_good_samples


   .. py:method:: get_data(montage=None)

      Return memorymapped data and optionally apply a montage.


   .. py:method:: epoch_data(data)


   .. py:method:: define_trial(event_type, pre_stim, post_stim)


   .. py:method:: mark_artefacts_as_bad()


   .. py:method:: _channel_property(property_)


   .. py:method:: full_index(channel_type)


   .. py:method:: reindex_good_samples()


   .. py:method:: reindex_event_samples()


   .. py:method:: print_info()


   .. py:method:: _find_dat_file()


   .. py:method:: indchantype(channel_type)


   .. py:method:: indsample(t)


   .. py:method:: indtrial(cond)



.. py:function:: dask_parallel_bag(func, iter_args, func_args=None, func_kwargs=None)

   A maybe more consistent alternative to ``dask_parallel``.

   :param func: The function to run in parallel.
   :type func: function
   :param iter_args: A list of iterables to pass to func.
   :type iter_args: list
   :param func_args: A list of positional arguments to pass to func.
   :type func_args: list, optional
   :param func_kwargs: A dictionary of keyword arguments to pass to func.
   :type func_kwargs: dict, optional

   :returns: **flags** -- A list of return values from func.
   :rtype: list

   .. rubric:: References

   https://docs.dask.org/en/stable/bag.html


.. py:function:: simulate_data(model, num_samples=1000, num_realisations=1, use_cov=True, noise=None)

   Simulate data from a linear model.

   :param model: A linear model object.
   :type model: sails.AbstractLinearModel
   :param num_samples: The number of samples to simulate.
   :type num_samples: int
   :param num_realisations: The number of realisations to simulate.
   :type num_realisations: int
   :param use_cov: Whether to use the residual covariance matrix.
   :type use_cov: bool

   :returns: **Y** -- The simulated data.
   :rtype: ndarray, shape (num_sources, num_samples, num_realisations)


.. py:function:: simulate_raw_from_template(sim_samples, bad_segments=None, bad_channels=None, flat_channels=None, noise=None)

   Simulate raw MEG data from a 306-channel MEGIN template.

   :param sim_samples: The number of samples to simulate.
   :type sim_samples: int
   :param bad_segments: The bad segments to simulate.
   :type bad_segments: list of tuples
   :param bad_channels: The bad channels to simulate.
   :type bad_channels: list of ints
   :param flat_channels: The flat channels to simulate.
   :type flat_channels: list of ints

   :returns: **sim** -- The simulated data.
   :rtype: :py:class:`mne.io.Raw <mne.io.Raw>`


.. py:function:: simulate_rest_mvar(raw, sim_samples, mvar_pca=32, mvar_order=12, picks=None, modalities=None, drop_dig=False)

   Simulate resting state data from a raw object using a reduced MVAR model.

   :param raw: The raw object to simulate from.
   :type raw: :py:class:`mne.io.Raw <mne.io.Raw>`
   :param sim_samples: The number of samples to simulate.
   :type sim_samples: int
   :param mvar_pca: The number of PCA components to use.
   :type mvar_pca: int
   :param mvar_order: The MVAR model order.
   :type mvar_order: int
   :param picks: The picks to use. See :py:func:`mne.pick_types <mne.pick_types>`.
   :type picks: dict
   :param modalities: The modalities to use. See :py:func:`mne.pick_types <mne.pick_types>`.
   :type modalities: list of str
   :param drop_dig: Whether to drop the digitisation points.
   :type drop_dig: bool

   :returns: **sim** -- The simulated data.
   :rtype: :py:class:`mne.io.Raw <mne.io.Raw>`

   .. rubric:: Notes

   Best used on low sample rate data <200Hz. fiff only for now.


.. py:data:: fname
   :value: '/Users/andrew/Projects/ntad/raw_data/meeg_pilots/NTAD_Neo_Pilot2_RSO.fif'

   

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

   

.. py:function:: soft_import(package)

   Try to import a package raising friendly error if not present.


.. py:function:: run_package_tests()

   Run OSL tests from within python

   https://docs.pytest.org/en/7.1.x/how-to/usage.html

   .. rubric:: Notes

   Calling pytest.main() will result in importing your tests and any modules
   that they import. Due to the caching mechanism of python’s import system,
   making subsequent calls to pytest.main() from the same process will not
   reflect changes to those files between the calls. For this reason, making
   multiple calls to pytest.main() from the same process
   (in order to re-run tests, for example) is not recommended.


.. py:function:: check_version(test_statement, mode='warn')

   Check whether the version of a package meets a specified condition.

   :param test_statement: Package version comparison string in the standard format expected by python installs.
                          eg 'osl-ephys<1.0.0' or 'osl-ephys==0.6.dev0'
   :type test_statement: str
   :param mode: Flag indicating whether to warn the user or raise an error if the comparison fails
   :type mode: {'warn', 'assert'}


.. py:data:: __doc__

   

