:py:mod:`osl_ephys.preprocessing.ica_label`
===========================================

.. py:module:: osl_ephys.preprocessing.ica_label

.. autoapi-nested-parse::

   OSL ICA LABEL
   Tool for interactive ICA component labeling and rejection.
   Works with command line arguments or as a function call.



Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   osl_ephys.preprocessing.ica_label.ica_label
   osl_ephys.preprocessing.ica_label.main
   osl_ephys.preprocessing.ica_label.apply



Attributes
~~~~~~~~~~

.. autoapisummary::

   osl_ephys.preprocessing.ica_label.logger


.. py:data:: logger

   

.. py:function:: ica_label(data_dir, subject, reject=None, interactive=True)

   Data bookkeeping and wrapping plot_ica.

   :param data_dir: Path to processed (M/EEG) data.
   :type data_dir: str
   :param subject: Subject/session specific data directory name
   :type subject: str
   :param reject: If 'all', reject all components (previously labeled and newly
                  labeled). If 'manual', reject only manually labeled components. If
                  None (default), only save the ICA data; don't reject any
                  components from the M/EEG data.
   :type reject: bool or str


.. py:function:: main(argv=None)

   Command-line interface for ica_label.

   :param argv: List of strings to be parsed as command-line arguments. If None,
                sys.argv will be used.
   :type argv: list

   .. rubric:: Example

   From the command line (in the osl-ephys environment), use as follows:

   osl_ica_label reject_argument /path/to/processed_data subject_name

   The `reject_argument` specifies whether to reject 'all' selected components from the data, only
   the 'manual' rejected, or None (and only save the ICA object, without rejecting components).
   The `subject_name` should be the name of the subject directory in the processed data directory.
   The /path/to/processed_data can be omitted when the command is run from the processed data directory.
   If both the subject_name and directory are omitted, the script will attempt to process all subjects in the
   processed data directory.
   For example:

   osl_ica_label manual /path/to/proc_dir sub-001_run01

   or:

   osl_ica_label all sub-001_run01

   Then use the GUI to label components (click on the time course to mark, use
   number keys to label marked components as specific artefacts, and use
   the arrow keys to navigate. Close the plot.
   all/manual/None components will be removed from the M/EEG data and saved. The
   ICA data will be saved with the new labels. If the report directory is specified
   or in the assumed osl-ephys directory structure, the subject report and log file is updated.


.. py:function:: apply(argv=None)

   Command-line function for removing all labeled components from the data.

   :param argv: List of strings to be parsed as command-line arguments. If None,
                sys.argv will be used.
   :type argv: list

   .. rubric:: Example

   From the command line (in the osl-ephys environment), use as follows:

   osl_ica_apply /path/to/processed_data subject_name

   The `subject_name` should be the name of the subject directory in the processed data directory. If omitted,
   the script will attempt to process all subjects in the processed data directory. The /path/to/processed_data
   can also be omitted when the command is run from the processed data directory (only when processing all subjects).

   For example:

   osl_ica_apply /path/to/proc_dir sub-001_run01

   or:

   osl_ica_apply

   Then use the GUI to label components (click on the time course to mark, use
   number keys to label marked components as specific artefacts, and use
   the arrow keys to navigate. Close the plot.
   all/manual/None components will be removed from the M/EEG data and saved. The
   ICA data will be saved with the new labels. If the report/logs directories are
   in the assumed osl-ephys directory structure, the subject report and log file are updated.


