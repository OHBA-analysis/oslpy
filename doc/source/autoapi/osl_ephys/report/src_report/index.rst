:py:mod:`osl_ephys.report.src_report`
=====================================

.. py:module:: osl_ephys.report.src_report

.. autoapi-nested-parse::

   Reporting tool for source reconstruction.



Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   osl_ephys.report.src_report.gen_html_data
   osl_ephys.report.src_report.gen_html_page
   osl_ephys.report.src_report.gen_html_summary
   osl_ephys.report.src_report.plot_config
   osl_ephys.report.src_report.plot_parcellation
   osl_ephys.report.src_report.plot_sign_flipping_results
   osl_ephys.report.src_report.add_to_data
   osl_ephys.report.src_report.update_config



.. py:function:: gen_html_data(config, outdir, subject, reportdir, logger=None, extra_funcs=None, logsdir=None)

   Generate data for HTML report.

   :param config: Source reconstruction config.
   :type config: dict
   :param outdir: Source reconstruction directory.
   :type outdir: str
   :param subject: Subject name.
   :type subject: str
   :param reportdir: Report directory.
   :type reportdir: str
   :param logger: Logger.
   :type logger: logging.getLogger
   :param extra_funcs: List of extra functions to run
   :type extra_funcs: list
   :param logsdir: Directory the log files were saved into. If None, log files are assumed
                   to be in reportdir.replace('report', 'logs')
   :type logsdir: str


.. py:function:: gen_html_page(reportdir)

   Generate an HTML page from a report directory.

   :param reportdir: Directory to generate HTML report with.
   :type reportdir: str

   :returns: Whether the report was generated successfully.
   :rtype: bool


.. py:function:: gen_html_summary(reportdir, logsdir=None)

   Generate an HTML summary from a report directory.

   :param reportdir: Directory to generate HTML summary report with.
                     logsdir: str
   :type reportdir: str
   :param Directory the log files were saved into. If None: to be in reportdir.replace('report', 'logs')
   :param log files are assumed: to be in reportdir.replace('report', 'logs')

   :returns: Whether the report was generated successfully.
   :rtype: bool


.. py:function:: plot_config(config, reportdir)

   Plots a config flowchart.

   :param config: Config to plot.
   :type config: dict
   :param reportdir: Path to report directory. We will save the plot in this directory.
   :type reportdir: str

   :returns: **path** -- Path to plot.
   :rtype: str


.. py:function:: plot_parcellation(parcellation_file, reportdir)

   Plot parcellation.

   :param parcellation_file: Path to parcellation file.
   :type parcellation_file: str
   :param reportdir: Path to report directory. We will save the plot in this directory.
   :type reportdir: str

   :returns: **path** -- Path to plot.
   :rtype: str


.. py:function:: plot_sign_flipping_results(metrics, reportdir)

   Plot sign flipping results.

   :param metrics: Sign flipping metrics. Shape is (n_subjects, n_iter + 1).
   :type metrics: np.ndarray
   :param reportdir: Path to report directory. We will save the plot in this directory.
   :type reportdir: str

   :returns: **path** -- Path to plot.
   :rtype: str


.. py:function:: add_to_data(data_file, info)

   Adds info to a dictionary containing info for the source recon report.

   :param data_file: Path to pickle file containing the data dictionary.
   :type data_file: str
   :param info: Info to add.
   :type info: dict


.. py:function:: update_config(old_config, new_config)

   Merge/update a config.

   :param old_config: Old config.
   :type old_config: dict
   :param new_config: New config.
   :type new_config: dict

   :returns: **config** -- Merge/updated config.
   :rtype: dict


