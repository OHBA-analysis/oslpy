:py:mod:`osl_ephys.source_recon`
================================

.. py:module:: osl_ephys.source_recon


Subpackages
-----------
.. toctree::
   :titlesonly:
   :maxdepth: 3

   parcellation/index.rst
   rhino/index.rst


Submodules
----------
.. toctree::
   :titlesonly:
   :maxdepth: 1

   batch/index.rst
   beamforming/index.rst
   sign_flipping/index.rst
   wrappers/index.rst


Package Contents
----------------


Functions
~~~~~~~~~

.. autoapisummary::

   osl_ephys.source_recon.validate_outdir
   osl_ephys.source_recon.find_run_id
   osl_ephys.source_recon.set_random_seed
   osl_ephys.source_recon.load_config
   osl_ephys.source_recon.find_func
   osl_ephys.source_recon.run_src_chain
   osl_ephys.source_recon.run_src_batch
   osl_ephys.source_recon.setup_fsl
   osl_ephys.source_recon.find_template_subject



Attributes
~~~~~~~~~~

.. autoapisummary::

   osl_ephys.source_recon.logger
   osl_ephys.source_recon.__doc__


.. py:function:: validate_outdir(outdir)

   Checks if an output directory exists and if not creates it.


.. py:function:: find_run_id(infile, preload=True)


.. py:function:: set_random_seed(seed=None)

   Set all random seeds.

   This includes Python's random module and NumPy.

   :param seed: Random seed.
   :type seed: int


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


.. py:function:: setup_fsl(directory)

   Setup FSL.

   :param directory: Path to FSL installation.
   :type directory: str


.. py:function:: find_template_subject(outdir, subjects, n_embeddings=1, standardize=True, epoched=False)

   Function to find a good subject to align other subjects to in the sign flipping.

   Note, this function expects parcellated data to exist in the following
   location: outdir/*/parc/parc-*.fif, the * here represents subject
   directories or 'raw' vs 'epo'.

   :param outdir: Path to where to output the source reconstruction files.
   :type outdir: str
   :param subjects: Subjects to include.
   :type subjects: str
   :param n_embeddings: Number of time-delay embeddings that we will use (if we are doing any).
   :type n_embeddings: int, optional
   :param standardize: Should we standardize (z-transform) the data before sign flipping?
   :type standardize: bool, optional
   :param epoched: Are we performing sign flipping on parc-raw.fif (epoched=False) or
                   parc-epo.fif files (epoched=True)?
   :type epoched: bool, optional

   :returns: **template** -- Template subject.
   :rtype: str


.. py:data:: __doc__

   

