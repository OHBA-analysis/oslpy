:py:mod:`osl_ephys.source_recon.batch`
======================================

.. py:module:: osl_ephys.source_recon.batch

.. autoapi-nested-parse::

   Batch processing for source reconstruction.



Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   osl_ephys.source_recon.batch.load_config
   osl_ephys.source_recon.batch.find_func
   osl_ephys.source_recon.batch.run_src_chain
   osl_ephys.source_recon.batch.run_src_batch



Attributes
~~~~~~~~~~

.. autoapisummary::

   osl_ephys.source_recon.batch.logger


.. py:data:: logger

   

.. py:function:: load_config(config)

   Load config.

   :param config: Path to yaml file or str to convert to dict or a dict.
   :type config: str or dict

   :returns: **config** -- Source reconstruction config.
   :rtype: dict


.. py:function:: find_func(method, extra_funcs)

   Find a source reconstruction function.

   :param method: Function name.
   :type method: str
   :param extra_funcs: Custom functions.
   :type extra_funcs: list of functions

   :returns: **func** -- Function to use.
   :rtype: function


.. py:function:: run_src_chain(config, outdir, subject, preproc_file=None, smri_file=None, epoch_file=None, logsdir=None, reportdir=None, gen_report=True, verbose='INFO', mneverbose='WARNING', extra_funcs=None, random_seed='auto')

   Source reconstruction.

   :param config: Source reconstruction config.
   :type config: str or dict
   :param outdir: Source reconstruction directory.
   :type outdir: str
   :param subject: Subject name.
   :type subject: str
   :param preproc_file: Preprocessed fif file.
   :type preproc_file: str
   :param smri_file: Structural MRI file.
   :type smri_file: str
   :param epoch_file: Epoched fif file.
   :type epoch_file: str
   :param logsdir: Directory to save log files to.
   :type logsdir: str
   :param reportdir: Directory to save report files to.
   :type reportdir: str
   :param gen_report: Should we generate a report?
   :type gen_report: bool
   :param verbose: Level of verbose.
   :type verbose: str
   :param mneverbose: Level of MNE verbose.
   :type mneverbose: str
   :param extra_funcs: Custom functions.
   :type extra_funcs: list of functions
   :param random_seed: Random seed to set. If 'auto', a random seed will be generated. Random seeds are set for both Python and NumPy.
                       If None, no random seed is set.
   :type random_seed: 'auto' (default), int or None

   :returns: **flag** -- Flag indicating whether source reconstruction was successful.
   :rtype: bool


.. py:function:: run_src_batch(config, outdir, subjects, preproc_files=None, smri_files=None, epoch_files=None, logsdir=None, reportdir=None, gen_report=True, verbose='INFO', mneverbose='WARNING', extra_funcs=None, dask_client=False, random_seed='auto')

   Batch source reconstruction.

   :param config: Source reconstruction config.
   :type config: str or dict
   :param outdir: Source reconstruction directory.
   :type outdir: str
   :param subjects: Subject names.
   :type subjects: list of str
   :param preproc_files: Preprocessed fif files.
   :type preproc_files: list of str
   :param smri_files: Structural MRI files. Can be 'standard' to use MNI152_T1_2mm.nii
                      for the structural.
   :type smri_files: list of str or str
   :param epoch_files: Epoched fif file.
   :type epoch_files: list of str
   :param logsdir: Directory to save log files to.
   :type logsdir: str
   :param reportdir: Directory to save report files to.
   :type reportdir: str
   :param gen_report: Should we generate a report?
   :type gen_report: bool
   :param verbose: Level of verbose.
   :type verbose: str
   :param mneverbose: Level of MNE verbose.
   :type mneverbose: str
   :param extra_funcs: Custom functions.
   :type extra_funcs: list of functions
   :param dask_client: Are we using a dask client?
   :type dask_client: bool
   :param random_seed: Random seed to set. If 'auto', a random seed will be generated. Random seeds are set for both Python and NumPy.
                       If None, no random seed is set.
   :type random_seed: 'auto' (default), int or None

   :returns: **flags** -- Flags indicating whether coregistration was successful.
   :rtype: list of bool


