:py:mod:`osl_ephys.preprocessing.batch`
=======================================

.. py:module:: osl_ephys.preprocessing.batch

.. autoapi-nested-parse::

   Tools for batch preprocessing.



Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   osl_ephys.preprocessing.batch.print_custom_func_info
   osl_ephys.preprocessing.batch.import_data
   osl_ephys.preprocessing.batch.find_func
   osl_ephys.preprocessing.batch.load_config
   osl_ephys.preprocessing.batch.check_config_versions
   osl_ephys.preprocessing.batch.get_config_from_fif
   osl_ephys.preprocessing.batch.append_preproc_info
   osl_ephys.preprocessing.batch.write_dataset
   osl_ephys.preprocessing.batch.read_dataset
   osl_ephys.preprocessing.batch.plot_preproc_flowchart
   osl_ephys.preprocessing.batch.run_proc_chain
   osl_ephys.preprocessing.batch.run_proc_batch
   osl_ephys.preprocessing.batch.main



Attributes
~~~~~~~~~~

.. autoapisummary::

   osl_ephys.preprocessing.batch.logger


.. py:data:: logger

   

.. py:function:: print_custom_func_info(func)

   Prints info for user-specified functions.

   :param func: Function to wrap.
   :type func: function

   :returns: Wrapped function.
   :rtype: function


.. py:function:: import_data(infile, preload=True)

   Imports data from a file.

   :param infile: Path to file to read. File can be bti, fif, ds, meg4 or vhdr.
   :type infile: str
   :param preload: Should we load the data in the file?
   :type preload: bool

   :returns: **raw** -- Data as an MNE Raw object.
   :rtype: :py:class:`mne.io.Raw <mne.io.Raw>`


.. py:function:: find_func(method, target='raw', extra_funcs=None)

   Find a preprocessing function.

   Function priority:

   1. User custom function

   2. MNE/osl-ephys wrapper

   3. MNE method on Raw or Epochs (specified by target)

   :param method: Function name.
   :type method: str
   :param target: Type of MNE object to preprocess. Can be ``'raw'``, ``'epochs'``, ``'evoked'``, ``'power'`` or ``'itc'``.
   :type target: str
   :param extra_funcs: List of user-defined functions.
   :type extra_funcs: list

   :returns: Function to preprocess an MNE object.
   :rtype: function


.. py:function:: load_config(config)

   Load config.

   :param config: Path to yaml file or string to convert to dict or a dict.
   :type config: str or dict

   :returns: Preprocessing config.
   :rtype: dict


.. py:function:: check_config_versions(config)

   Get config from a preprocessed fif file.

   :param config: Preprocessing configuration to check.
   :type config: dictionary or yaml string

   :raises AssertionError: Raised if package version mismatch found in 'version_assert'
   :raises Warning: Raised if package version mismatch found in 'version_warn'


.. py:function:: get_config_from_fif(inst)

   Get config from a preprocessed fif file.

   Reads the ``inst.info['description']`` field of a fif file to get the preprocessing config.

   :param inst: Preprocessed MNE object.
   :type inst: :py:class:`mne.io.Raw <mne.io.Raw>`, :py:class:`mne.Epochs <mne.Epochs>`, :py:class:`mne.Evoked <mne.Evoked>`

   :returns: Preprocessing config.
   :rtype: dict


.. py:function:: append_preproc_info(dataset, config, extra_funcs=None)

   Add to the config of already preprocessed data to ``inst.info['description']``.

   :param dataset: Preprocessed dataset.
   :type dataset: dict
   :param config: Preprocessing config.
   :type config: dict

   :returns: Dataset dict containing the preprocessed data edited in place.
   :rtype: dict


.. py:function:: write_dataset(dataset, outbase, run_id, ftype='preproc-raw', overwrite=False, skip=None)

   Write preprocessed data to a file.

   Will write all keys in the dataset dict to disk with corresponding extensions.

   :param dataset: Preprocessed dataset.
   :type dataset: dict
   :param outbase: Path to directory to write to.
   :type outbase: str
   :param run_id: ID for the output file.
   :type run_id: str
   :param ftype: Extension for the fif file (default ``preproc-raw``)
   :type ftype: str
   :param overwrite: Should we overwrite if the file already exists?
   :type overwrite: bool
   :param skip: List of keys to skip writing to disk. If None, we don't skip any keys.
   :type skip: list or None
   :param Output:
   :param ------:
   :param fif_outname: The saved fif file name
   :type fif_outname: str


.. py:function:: read_dataset(fif, preload=False, ftype=None)

   Reads ``fif``/``npy``/``yml`` files associated with a dataset.

   :param fif: Path to raw fif file (can be preprocessed).
   :type fif: str
   :param preload: Should we load the raw fif data?
   :type preload: bool
   :param ftype: Extension for the fif file (will be replaced for e.g. ``'_events.npy'`` or
                 ``'_ica.fif'``). If ``None``, we assume the fif file is preprocessed with
                 ``osl-ephys`` and has the extension ``'_preproc-raw'``. If this fails, we guess
                 the extension as whatever comes after the last ``'_'``.
   :type ftype: str

   :returns: **dataset** -- Contains keys: ``'raw'``, ``'events'``, ``'event_id'``, ``'epochs'``, ``'ica'``.
   :rtype: dict


.. py:function:: plot_preproc_flowchart(config, outname=None, show=True, stagecol='wheat', startcol='red', fig=None, ax=None, title=None)

   Make a summary flowchart of a preprocessing chain.

   :param config: Preprocessing config to plot.
   :type config: dict
   :param outname: Output filename.
   :type outname: str
   :param show: Should we show the plot?
   :type show: bool
   :param stagecol: Stage colour.
   :type stagecol: str
   :param startcol: Start colour.
   :type startcol: str
   :param fig: Matplotlib figure to plot on.
   :type fig: matplotlib.figure
   :param ax: Matplotlib axes to plot on.
   :type ax: :py:class:`matplotlib.axes <matplotlib.axes>`
   :param title: Title for the plot.
   :type title: str

   :returns: * **fig** (:py:class:`matplotlib.figure <matplotlib.figure>`)
             * **ax** (:py:class:`matplotlib.axes <matplotlib.axes>`)


.. py:function:: run_proc_chain(config, infile, subject=None, ftype='preproc-raw', outdir=None, logsdir=None, reportdir=None, ret_dataset=True, gen_report=None, overwrite=False, skip_save=None, extra_funcs=None, random_seed='auto', verbose='INFO', mneverbose='WARNING')

   Run preprocessing for a single file.

   :param config: Preprocessing config.
   :type config: str or dict
   :param infile: Path to input file.
   :type infile: str
   :param subject: Subject ID. This will be the sub-directory in outdir.
   :type subject: str
   :param ftype: Extension for the fif file (default ``preproc-raw``)
   :type ftype: str
   :param outdir: Output directory.
   :type outdir: str
   :param logsdir: Directory to save log files to.
   :type logsdir: str
   :param reportdir: Directory to save report files to.
   :type reportdir: str
   :param ret_dataset: Should we return a dataset dict?
   :type ret_dataset: bool
   :param gen_report: Should we generate a report?
   :type gen_report: bool
   :param overwrite: Should we overwrite the output file if it already exists?
   :type overwrite: bool
   :param skip_save: List of keys to skip writing to disk. If None, we don't skip any keys.
   :type skip_save: list or None (default)
   :param extra_funcs: User-defined functions.
   :type extra_funcs: list
   :param random_seed: Random seed to set. If 'auto', a random seed will be generated. Random seeds are set for both Python and NumPy.
                       If None, no random seed is set.
   :type random_seed: 'auto' (default), int or None
   :param verbose: Level of info to print.
                   Can be: ``'CRITICAL'``, ``'ERROR'``, ``'WARNING'``, ``'INFO'``, ``'DEBUG'`` or ``'NOTSET'``.
   :type verbose: str
   :param mneverbose: Level of info from MNE to print.
                      Can be: ``'CRITICAL'``, ``'ERROR'``, ``'WARNING'``, ``'INFO'``, ``'DEBUG'`` or ``'NOTSET'``.
   :type mneverbose: str

   :returns: If ``ret_dataset=True``, a dict containing the preprocessed dataset with the following keys: ``raw``, ``ica``, ``epochs``, ``events``, ``event_id``.
             An empty dict is returned if preprocessing fails. If ``ret_dataset=False``, we return a flag indicating whether preprocessing was successful.
   :rtype: dict or bool


.. py:function:: run_proc_batch(config, files, subjects=None, ftype='preproc-raw', outdir=None, logsdir=None, reportdir=None, gen_report=True, overwrite=False, skip_save=None, extra_funcs=None, random_seed='auto', verbose='INFO', mneverbose='WARNING', strictrun=False, dask_client=False)

   Run batched preprocessing.

   This function will write output to disk (i.e. will not return the preprocessed
   data).

   :param config: Preprocessing config.
   :type config: str or dict
   :param files: Can be a list of Raw objects or a list of filenames (or ``.ds`` dir names if CTF data)
                 or a path to a textfile list of filenames (or ``.ds`` dir names if CTF data).
   :type files: str or list or mne.Raw
   :param subjects: Subject directory names. These are sub-directories in outdir.
   :type subjects: list of str
   :param ftype: Extension of the preprocessed fif files. Default option is `_preproc-raw`.
   :type ftype: None or str
   :param outdir: Output directory.
   :type outdir: str
   :param logsdir: Directory to save log files to.
   :type logsdir: str
   :param reportdir: Directory to save report files to.
   :type reportdir: str
   :param gen_report: Should we generate a report?
   :type gen_report: bool
   :param overwrite: Should we overwrite the output file if it exists?
   :type overwrite: bool
   :param skip_save: List of keys to skip writing to disk. If None, we don't skip any keys.
   :type skip_save: list or None (default)
   :param extra_funcs: User-defined functions.
   :type extra_funcs: list
   :param random_seed: Random seed to set. If 'auto', a random seed will be generated. Random seeds are set for both Python and NumPy.
                       If None, no random seed is set.
   :type random_seed: 'auto' (default), int or None
   :param verbose: Level of info to print.
                   Can be: ``'CRITICAL'``, ``'ERROR'``, ``'WARNING'``, ``'INFO'``, ``'DEBUG'`` or ``'NOTSET'``.
   :type verbose: str
   :param mneverbose: Level of info from MNE to print.
                      Can be: ``'CRITICAL'``, ``'ERROR'``, ``'WARNING'``, ``'INFO'``, ``'DEBUG'`` or ``'NOTSET'``.
   :type mneverbose: str
   :param strictrun: Should we ask for confirmation of user inputs before starting?
   :type strictrun: bool
   :param dask_client: Indicate whether to use a previously initialised :py:class:`dask.distributed.Client <distributed.Client>` instance.
   :type dask_client: bool

   :returns: Flags indicating whether preprocessing was successful for each input file.
   :rtype: list of bool

   .. rubric:: Notes

   If you are using a :py:class:`dask.distributed.Client <distributed.Client>` instance, you must initialise it
   before calling this function. For example:

   >>> from dask.distributed import Client
   >>> client = Client(threads_per_worker=1, n_workers=4)


.. py:function:: main(argv=None)

   Main function for command line interface.

   :param argv: Command line arguments.
   :type argv: list


