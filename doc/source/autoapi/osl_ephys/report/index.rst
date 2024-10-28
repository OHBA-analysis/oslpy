:py:mod:`osl_ephys.report`
==========================

.. py:module:: osl_ephys.report


Submodules
----------
.. toctree::
   :titlesonly:
   :maxdepth: 1

   preproc_report/index.rst
   src_report/index.rst


Package Contents
----------------


Functions
~~~~~~~~~

.. autoapisummary::

   osl_ephys.report.process_file_inputs
   osl_ephys.report.validate_outdir
   osl_ephys.report.log_or_print
   osl_ephys.report.read_dataset
   osl_ephys.report.load_config
   osl_ephys.report.get_config_from_fif
   osl_ephys.report.plot_preproc_flowchart
   osl_ephys.report.gen_report_from_fif
   osl_ephys.report.get_header_id
   osl_ephys.report.gen_html_data
   osl_ephys.report.gen_html_page
   osl_ephys.report.gen_html_summary
   osl_ephys.report.gen_summary_data
   osl_ephys.report.load_template
   osl_ephys.report.plot_flowchart
   osl_ephys.report.plot_rawdata
   osl_ephys.report.plot_channel_time_series
   osl_ephys.report.plot_sensors
   osl_ephys.report.plot_channel_dists
   osl_ephys.report.plot_spectra
   osl_ephys.report.plot_digitisation_2d
   osl_ephys.report.plot_headmovement
   osl_ephys.report.plot_eog_summary
   osl_ephys.report.plot_ecg_summary
   osl_ephys.report.plot_bad_ica
   osl_ephys.report.plot_summary_bad_segs
   osl_ephys.report.plot_summary_bad_chans
   osl_ephys.report.plot_artefact_scan
   osl_ephys.report.print_scan_summary



Attributes
~~~~~~~~~~

.. autoapisummary::

   osl_ephys.report.osl_logger
   osl_ephys.report.__doc__


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


.. py:function:: validate_outdir(outdir)

   Checks if an output directory exists and if not creates it.


.. py:function:: log_or_print(msg, warning=False)

   Execute logger.info if an OSL logger has been setup, otherwise print.

   :param msg: Message to log/print.
   :type msg: str
   :param warning: Is the msg a warning? Defaults to False, which will print info.
   :type warning: bool


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


.. py:function:: load_config(config)

   Load config.

   :param config: Path to yaml file or string to convert to dict or a dict.
   :type config: str or dict

   :returns: Preprocessing config.
   :rtype: dict


.. py:function:: get_config_from_fif(inst)

   Get config from a preprocessed fif file.

   Reads the ``inst.info['description']`` field of a fif file to get the preprocessing config.

   :param inst: Preprocessed MNE object.
   :type inst: :py:class:`mne.io.Raw <mne.io.Raw>`, :py:class:`mne.Epochs <mne.Epochs>`, :py:class:`mne.Evoked <mne.Evoked>`

   :returns: Preprocessing config.
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


.. py:function:: gen_report_from_fif(infiles, outdir, ftype=None, logsdir=None, run_id=None)

   Generate web-report for a set of MNE data objects.

   :param infiles: List of paths to fif files.
   :type infiles: list of str
   :param outdir: Directory to save HTML report and figures to.
   :type outdir: str
   :param ftype: Type of fif file, e.g., ``'raw'`` or ``'preproc-raw'``.
   :type ftype: str
   :param logsdir: Directory the log files were saved into. If None, log files are assumed
                   to be in outdir.replace('report', 'logs')
   :type logsdir: str
   :param run_id: Run ID.
   :type run_id: str


.. py:function:: get_header_id(raw)

   Extract scan name from MNE data object.

   :param raw: MNE Raw object.
   :type raw: mne.io.:py:class:`mne.io.Raw <mne.io.Raw>`.

   :returns: **id** -- Scan name.
   :rtype: str


.. py:function:: gen_html_data(raw, outdir, ica=None, preproc_fif_filename=None, logsdir=None, run_id=None)

   Generate HTML web-report for an MNE data object.

   :param raw: MNE Raw object.
   :type raw: :py:class:`mne.io.Raw <mne.io.Raw>`
   :param outdir: Directory to write HTML data and plots to.
   :type outdir: string
   :param ica: ICA object.
   :type ica: :py:class:`mne.preprocessing.ICA <mne.preprocessing.ICA>`
   :param preproc_fif_filename: Filename of file output by preprocessing
   :type preproc_fif_filename: str
   :param logsdir: Directory the log files were saved into. If None, log files are assumed
                   to be in reportdir.replace('report', 'logs')
   :type logsdir: str
   :param run_id: Run ID.
   :type run_id: str


.. py:function:: gen_html_page(outdir, logsdir=None)

   Generate an HTML page from a report directory.

   :param outdir: Directory to generate HTML report with.
   :type outdir: str

   :returns: **success** -- Whether the report was successfully generated.
   :rtype: bool


.. py:function:: gen_html_summary(reportdir, logsdir=None)

   Generate an HTML summary from a report directory.

   :param reportdir: Directory to generate HTML summary report with.
   :type reportdir: str
   :param logsdir: Directory the log files were saved into. If None, log files are assumed
                   to be in reportdir.replace('report', 'logs')
   :type logsdir: str


.. py:function:: gen_summary_data(subject_data)


.. py:function:: load_template(tname)

   Load an HTML template from the templates directory.

   :param tname: Name of the template to load.
   :type tname: str

   :returns: **template** -- The loaded template.
   :rtype: jinja2.Template


.. py:function:: plot_flowchart(raw, savebase=None)

   Plots preprocessing flowchart(s)

   :param raw: MNE Raw object.
   :type raw: :py:class:`mne.io.Raw <mne.io.Raw>`
   :param savebase: Base string for saving figures.
   :type savebase: str

   :returns: **fpath** -- Path to saved figure.
   :rtype: str


.. py:function:: plot_rawdata(raw, savebase)

   Plots raw data.

   :param raw: MNE Raw object.
   :type raw: :py:class:`mne.io.Raw <mne.io.Raw>`
   :param savebase: Base string for saving figures.
   :type savebase: str

   :returns: **fpath** -- Path to saved figure.
   :rtype: str


.. py:function:: plot_channel_time_series(raw, savebase=None, exclude_bads=False)

   Plots sum-square time courses.

   :param raw: MNE Raw object.
   :type raw: :py:class:`mne.io.Raw <mne.io.Raw>`
   :param savebase: Base string for saving figures.
   :type savebase: str
   :param exclude_bads: Whether to exclude bad channels and bad segments.
   :type exclude_bads: bool

   :returns: **fpath** -- Path to saved figure.
   :rtype: str


.. py:function:: plot_sensors(raw, savebase=None)

   Plots sensors with bad channels highlighted.

   :param raw: MNE Raw object.
   :type raw: :py:class:`mne.io.Raw <mne.io.Raw>`
   :param savebase: Base string for saving figures.
   :type savebase: str

   :returns: **fpath** -- Path to saved figure.
   :rtype: str


.. py:function:: plot_channel_dists(raw, savebase=None, exclude_bads=True)

   Plot distributions of temporal standard deviation.

   :param raw: MNE Raw object.
   :type raw: :py:class:`mne.io.Raw <mne.io.Raw>`
   :param savebase: Base string for saving figures.
   :type savebase: str
   :param exclude_bads: Whether to exclude bad channels and bad segments.
   :type exclude_bads: bool

   :returns: **fpath** -- Path to saved figure.
   :rtype: str


.. py:function:: plot_spectra(raw, savebase=None)

   Plot power spectra for each sensor modality.

   :param raw: MNE Raw object.
   :type raw: :py:class:`mne.io.Raw <mne.io.Raw>`
   :param savebase: Base string for saving figures.
   :type savebase: str

   :returns: * **fpath1** (*str*) -- Path to saved figure (full spectra).
             * **fpath2** (*str*) -- Path to saved figure (zoomed in spectra).


.. py:function:: plot_digitisation_2d(raw, savebase=None)

   Plots the digitisation and headshape.

   :param raw: MNE Raw object.
   :type raw: :py:class:`mne.io.Raw <mne.io.Raw>`
   :param savebase: Base string for saving figures.
   :type savebase: str

   :returns: **fpath** -- Path to saved figure.
   :rtype: str


.. py:function:: plot_headmovement(raw, savebase=None)

   Plot headmovement - WORK IN PROGRESS... seems v-slow atm


.. py:function:: plot_eog_summary(raw, savebase=None)

   Plot raw EOG time series.


.. py:function:: plot_ecg_summary(raw, savebase=None)

   Plot ECG summary.

   :param raw: MNE Raw object.
   :type raw: :py:class:`mne.io.Raw <mne.io.Raw>`
   :param savebase: Base string for saving figures.
   :type savebase: str

   :returns: **fpath** -- Path to saved figure.
   :rtype: str


.. py:function:: plot_bad_ica(raw, ica, savebase)

   Plot ICA characteristics for rejected components.

   :param raw: MNE Raw object.
   :type raw: :py:class:`mne.io.Raw <mne.io.Raw>`
   :param ica: MNE ICA object.
   :type ica: :py:class:`mne.preprocessing.ICA <mne.preprocessing.ICA>`
   :param savebase: Base string for saving figures.
   :type savebase: str

   :returns: **fpath** -- Path to saved figure.
   :rtype: str


.. py:function:: plot_summary_bad_segs(subject_data, reportdir)

   Plot summary of bad channels over subjects.

   :param subject_data: list of data for each subject, typically generated by gen_html_data
   :type subject_data: list
   :param reportdir: Path to report directory. We will save the plot in this directory.
   :type reportdir: str

   :returns: **path** -- Path to plot.
   :rtype: str


.. py:function:: plot_summary_bad_chans(subject_data, reportdir)

   Plot summary of bad channels over subjects.

   :param subject_data: list of data for each subject, typically generated by gen_html_data
   :type subject_data: list
   :param reportdir: Path to report directory. We will save the plot in this directory.
   :type reportdir: str

   :returns: **path** -- Path to plot.
   :rtype: str


.. py:function:: plot_artefact_scan(raw, savebase=None)

   Plot artefact scan.

   :param raw: MNE Raw object.
   :type raw: :py:class:`mne.io.Raw <mne.io.Raw>`
   :param savebase: Base string for saving figures.
   :type savebase: str

   :returns: **fpath** -- Path to saved figure.
   :rtype: str


.. py:function:: print_scan_summary(raw)

   Print a text summary of an MNE file.

   :param raw: MNE Raw object.
   :type raw: :py:class:`mne.io.Raw <mne.io.Raw>`


.. py:data:: osl_logger

   

.. py:data:: __doc__

   

