:py:mod:`osl_ephys.utils.file_handling`
=======================================

.. py:module:: osl_ephys.utils.file_handling

.. autoapi-nested-parse::

   File handling utility functions.



Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   osl_ephys.utils.file_handling.process_file_inputs
   osl_ephys.utils.file_handling.sanitise_filepath
   osl_ephys.utils.file_handling._load_unicode_inputs
   osl_ephys.utils.file_handling.find_run_id
   osl_ephys.utils.file_handling.validate_outdir
   osl_ephys.utils.file_handling.get_rawdir
   osl_ephys.utils.file_handling.add_subdir
   osl_ephys.utils.file_handling.osl_print



Attributes
~~~~~~~~~~

.. autoapisummary::

   osl_ephys.utils.file_handling.osl_logger


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


