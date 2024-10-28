:py:mod:`osl_ephys.preprocessing`
=================================

.. py:module:: osl_ephys.preprocessing


Submodules
----------
.. toctree::
   :titlesonly:
   :maxdepth: 1

   batch/index.rst
   ica_label/index.rst
   mne_wrappers/index.rst
   osl_wrappers/index.rst
   plot_ica/index.rst


Package Contents
----------------

Classes
~~~~~~~

.. autoapisummary::

   osl_ephys.preprocessing.osl_MNEBrowseFigure



Functions
~~~~~~~~~

.. autoapisummary::

   osl_ephys.preprocessing.find_run_id
   osl_ephys.preprocessing.validate_outdir
   osl_ephys.preprocessing.process_file_inputs
   osl_ephys.preprocessing.dask_parallel_bag
   osl_ephys.preprocessing.check_version
   osl_ephys.preprocessing.set_random_seed
   osl_ephys.preprocessing.print_custom_func_info
   osl_ephys.preprocessing.import_data
   osl_ephys.preprocessing.find_func
   osl_ephys.preprocessing.load_config
   osl_ephys.preprocessing.check_config_versions
   osl_ephys.preprocessing.get_config_from_fif
   osl_ephys.preprocessing.append_preproc_info
   osl_ephys.preprocessing.write_dataset
   osl_ephys.preprocessing.read_dataset
   osl_ephys.preprocessing.plot_preproc_flowchart
   osl_ephys.preprocessing.run_proc_chain
   osl_ephys.preprocessing.run_proc_batch
   osl_ephys.preprocessing.main
   osl_ephys.preprocessing.plot_ica
   osl_ephys.preprocessing._plot_sources
   osl_ephys.preprocessing._get_browser
   osl_ephys.preprocessing._init_browser
   osl_ephys.preprocessing.flatten_recursive
   osl_ephys.preprocessing._plot_ica_sources_evoked



Attributes
~~~~~~~~~~

.. autoapisummary::

   osl_ephys.preprocessing.logger
   osl_ephys.preprocessing.logger
   osl_ephys.preprocessing.backend
   osl_ephys.preprocessing.__doc__


.. py:function:: find_run_id(infile, preload=True)


.. py:function:: validate_outdir(outdir)

   Checks if an output directory exists and if not creates it.


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


.. py:function:: check_version(test_statement, mode='warn')

   Check whether the version of a package meets a specified condition.

   :param test_statement: Package version comparison string in the standard format expected by python installs.
                          eg 'osl-ephys<1.0.0' or 'osl-ephys==0.6.dev0'
   :type test_statement: str
   :param mode: Flag indicating whether to warn the user or raise an error if the comparison fails
   :type mode: {'warn', 'assert'}


.. py:function:: set_random_seed(seed=None)

   Set all random seeds.

   This includes Python's random module and NumPy.

   :param seed: Random seed.
   :type seed: int


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


.. py:data:: logger

   

.. py:function:: plot_ica(ica, inst, picks=None, start=None, stop=None, title=None, show=True, block=False, show_first_samp=False, show_scrollbars=True, time_format='float', n_channels=10, bad_labels_list=['eog', 'ecg', 'emg', 'hardware', 'other'])

   osl-ephys' adaptation of MNE's :py:meth:`mne.preprocessing.ICA.plot_sources <mne.preprocessing.ICA.plot_sources>` function to
   plot estimated latent sources given the unmixing matrix.

   Typical usecases:

   1. plot evolution of latent sources over time based on (Raw input)
   2. plot latent source around event related time windows (Epochs input)
   3. plot time-locking in ICA space (Evoked input)

   :param ica: The ICA solution.
   :type ica: :py:class:`mne.preprocessing.ICA <mne.preprocessing.ICA>`.
   :param inst: The object to plot the sources from.
   :type inst: :py:class:`mne.io.Raw <mne.io.Raw>`, :py:class:`mne.Epochs <mne.Epochs>`, or :py:class:`mne.Evoked <mne.Evoked>`.
   :param picks: Channel types to pick.
   :type picks: str
   :param start: If ``inst`` is a :py:class:`mne.io.Raw <mne.io.Raw>` or an  :py:class:`mne.Evoked <mne.Evoked>` object, the first and
                 last time point (in seconds) of the data to plot. If ``inst`` is a
                 :py:class:`mne.io.Raw <mne.io.Raw>` object, ``start=None`` and ``stop=None`` will be
                 translated into ``start=0.`` and ``stop=3.``, respectively. For
                 :py:class:`mne.Evoked <mne.Evoked>`, ``None`` refers to the beginning and end of the evoked
                 signal. If ``inst`` is an  :py:class:`mne.Epochs <mne.Epochs>` object, specifies the index of
                 the first and last epoch to show.
   :type start: float | int | None
   :param stop: If ``inst`` is a :py:class:`mne.io.Raw <mne.io.Raw>` or an  :py:class:`mne.Evoked <mne.Evoked>` object, the first and
                last time point (in seconds) of the data to plot. If ``inst`` is a
                :py:class:`mne.io.Raw <mne.io.Raw>` object, ``start=None`` and ``stop=None`` will be
                translated into ``start=0.`` and ``stop=3.``, respectively. For
                :py:class:`mne.Evoked <mne.Evoked>`, ``None`` refers to the beginning and end of the evoked
                signal. If ``inst`` is an  :py:class:`mne.Epochs <mne.Epochs>` object, specifies the index of
                the first and last epoch to show.
   :type stop: float | int | None
   :param title: The window title. If None a default is provided.
   :type title: str | None
   :param show: Show figure if True.
   :type show: bool
   :param block: Whether to halt program execution until the figure is closed.
                 Useful for interactive selection of components in raw and epoch
                 plotter. For evoked, this parameter has no effect. Defaults to False.
   :type block: bool
   :param show_first_samp: If True, show time axis relative to the ``raw.first_samp``.
   :type show_first_samp: bool
   :param n_channels: Number of channels to show at the same time (default: 10)
   :type n_channels: int
   :param bad_labels_list: list of bad labels to show in the bad labels list that can be used to mark the type of
                           bad component. Defaults to ``["eog", "ecg", "emg", "hardware", "other"]``.
   :type bad_labels_list: list of str

   :returns: **fig** -- The figure.
   :rtype: instance of Figure

   .. rubric:: Notes

   For raw and epoch instances, it is possible to select components for
   exclusion by clicking on the line. The selected components are added to
   ``ica.exclude`` on close.

   .. versionadded:: 0.10.0


.. py:function:: _plot_sources(ica, inst, picks, exclude, start, stop, show, title, block, show_scrollbars, show_first_samp, time_format, n_channels, bad_labels_list)

   Adaptation of MNE's `mne.preprocessing.ica._plot_sources` function to allow for OSL additions.



.. py:data:: backend

   

.. py:function:: _get_browser(**kwargs)

   OSL Adaptation of MNE's `mne.viz._figure._get_browser` function
   that instantiate a new MNE browse-style figure.



.. py:function:: _init_browser(backend, **kwargs)


.. py:class:: osl_MNEBrowseFigure(inst, figsize, ica=None, xlabel='Time (s)', **kwargs)


   Bases: :py:obj:`mne.viz._mpl_figure.MNEBrowseFigure`

   OSL's adaptatation of MNE's `mne.viz._mpl_figure.MNEBrowseFigure` that
   creates an interactive figure with scrollbars, for data browsing.

   .. py:method:: _update_picks()

      Compute which channel indices to show.


   .. py:method:: _draw_traces()

      Draw (or redraw) the channel data.


   .. py:method:: plot_topos(ica, ax_topo, picks)


   .. py:method:: _keypress(event)

      Handle keypress events.


   .. py:method:: _update_vscroll()

      Update the vertical scrollbar (channel) selection indicator.


   .. py:method:: _close(event)

      Handle close events (via keypress or window [x]).



.. py:function:: flatten_recursive(lst)

   Flatten a list using recursion.


.. py:function:: _plot_ica_sources_evoked(evoked, picks, exclude, title, show, ica, labels=None, n_channels=10, bad_labels_list=None)

   Plot average over epochs in ICA space.

   :param evoked: The Evoked to be used.
   :type evoked: instance of mne.Evoked
   :param %(picks_base)s all sources in the order as fitted.:
   :param exclude: The components marked for exclusion. If None (default), ICA.exclude
                   will be used.
   :type exclude: array-like of int
   :param title: The figure title.
   :type title: str
   :param show: Show figure if True.
   :type show: bool
   :param labels: The ICA labels attribute.
   :type labels: None | dict


.. py:data:: __doc__

   

