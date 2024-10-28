:py:mod:`osl_ephys.maxfilter.maxfilter`
=======================================

.. py:module:: osl_ephys.maxfilter.maxfilter

.. autoapi-nested-parse::

   Maxfiltering.



Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   osl_ephys.maxfilter.maxfilter._add_headpos
   osl_ephys.maxfilter.maxfilter._add_movecomp
   osl_ephys.maxfilter.maxfilter._add_movecompinter
   osl_ephys.maxfilter.maxfilter._add_hpie
   osl_ephys.maxfilter.maxfilter._add_hpig
   osl_ephys.maxfilter.maxfilter._add_hpisubt
   osl_ephys.maxfilter.maxfilter._add_autobad
   osl_ephys.maxfilter.maxfilter._add_autobad_dur
   osl_ephys.maxfilter.maxfilter._add_badlimit
   osl_ephys.maxfilter.maxfilter._add_bad
   osl_ephys.maxfilter.maxfilter._add_linefreq
   osl_ephys.maxfilter.maxfilter._add_tsss
   osl_ephys.maxfilter.maxfilter._add_trans
   osl_ephys.maxfilter.maxfilter._add_force
   osl_ephys.maxfilter.maxfilter._add_inorder
   osl_ephys.maxfilter.maxfilter._add_outorder
   osl_ephys.maxfilter.maxfilter._add_ctc
   osl_ephys.maxfilter.maxfilter._add_cal
   osl_ephys.maxfilter.maxfilter._add_origin
   osl_ephys.maxfilter.maxfilter._add_frame
   osl_ephys.maxfilter.maxfilter._add_scanner
   osl_ephys.maxfilter.maxfilter.quick_load_dig
   osl_ephys.maxfilter.maxfilter.fit_cbu_origin
   osl_ephys.maxfilter.maxfilter.run_maxfilter
   osl_ephys.maxfilter.maxfilter.run_multistage_maxfilter
   osl_ephys.maxfilter.maxfilter.run_cbu_3stage_maxfilter
   osl_ephys.maxfilter.maxfilter.run_maxfilter_batch
   osl_ephys.maxfilter.maxfilter.main



Attributes
~~~~~~~~~~

.. autoapisummary::

   osl_ephys.maxfilter.maxfilter.parser


.. py:data:: parser

   

.. py:function:: _add_headpos(cmd, args, outfif)

   Estimates and stores head position parameters but does not transform data


.. py:function:: _add_movecomp(cmd, args)

   Estimates head movements and transforms data.

   Data are transformed to reference head position in continuous raw data


.. py:function:: _add_movecompinter(cmd, args)

   Estimates head movements and transforms data with intermittent HPI

   Data are transformed to reference head position in continuous raw data


.. py:function:: _add_hpie(cmd, args)

   sets the error limit for hpi coil fitting (def 5 mm)


.. py:function:: _add_hpig(cmd, args)

   sets the g-value limit for hpi coil fitting (def 0.98)


.. py:function:: _add_hpisubt(cmd, args)

   subtracts hpi signals: chpi sine amplitudes, amp + linefreq harmonics,
   or switch off (def = amp)


.. py:function:: _add_autobad(cmd, args)

   sets automated bad channel detection on: scan the whole raw data file, off: no autobad


.. py:function:: _add_autobad_dur(cmd, args)

   sets automated bad channel detection on with specified duration.


.. py:function:: _add_badlimit(cmd, args)

   Threshold for bad channel detection (>ave+X*SD)


.. py:function:: _add_bad(cmd, args)

   sets the list of static bad channels (logical chnos, e.g.: 0323 1042 2631)


.. py:function:: _add_linefreq(cmd, args)

   sets the basic line interference frequency (50/60Hz)


.. py:function:: _add_tsss(cmd, args)

   Add all tsss related args


.. py:function:: _add_trans(cmd, args)

   transforms the data into head position in <fiff_file>


.. py:function:: _add_force(cmd, args)

   Ignore program warnings....


.. py:function:: _add_inorder(cmd, args)

   sets the order of the inside expansion


.. py:function:: _add_outorder(cmd, args)

   sets the order of the outside expansion


.. py:function:: _add_ctc(cmd, args)

   uses the cross-talk matrix in <ctcfile>


.. py:function:: _add_cal(cmd, args)

   uses the fine-calibration in <calfile>


.. py:function:: _add_origin(cmd, args)

   set a custom sphere origin.


.. py:function:: _add_frame(cmd, args)

   set origin frame.


.. py:function:: _add_scanner(cmd, args)


.. py:function:: quick_load_dig(fname)


.. py:function:: fit_cbu_origin(infif, outbase=None, remove_nose=True)


.. py:function:: run_maxfilter(infif, outfif, args, logfile_tag='')

   Wrapper for Elekta Maxfilter.

   :param infif: Path to input fif file (raw data).
   :type infif: str
   :param outfif: Path to output fif file (maxfiltered).
   :type outfif: str
   :param args: Dictionary of arguments to pass to maxfilter.  See ``help(osl_ephys.maxfilter)`` for all options, and
                Notes for recommendations.
   :type args: dict
   :param logfile_tag: Tag to append to logfile name. The default is ''. This is used to
                       differentiate between different stages of maxfiltering (e.g., ``'_trans'``, ``'_tsss'``).
   :type logfile_tag: str, optional

   :returns: * **outfif** (*str*) -- Path to output fif file (maxfiltered).
             * **stdlog** (*str*) -- Path to logfile.

   .. rubric:: Notes

   The recommended use for maxfilter at OHBA is to run multistage maxfiltering, with the following options:
   ``args = {'maxpath': '/neuro/bin/util/maxfilter', 'scanner': 'Neo', 'mode': 'multistage', 'tsss': {}, 'headpos': {}, 'movecomp': {}}``


.. py:function:: run_multistage_maxfilter(infif, outbase, args)

   Wrapper for running :py:func:`run_maxfilter <osl_ephys.maxfilter.run_maxfilter>` in three sequential steps:

   1. Find Bad Channels

   2. Signal Space Separation

   3. Translate to reference file

   :param infif: Path to input fif file (raw data).
   :type infif: str
   :param outbase: output directory.
   :type outbase: str
   :param args: Dictionary of arguments to pass to maxfilter. See ``help(osl_ephys.maxfilter)`` for all options.
   :type args: dict

   .. rubric:: Notes

   All files are written to disk and the output of each stage is used as the input to the next.

   General advice (from CBU):

   * don't use ``'trans'`` with ``'movecomp'``

   * don't use ``'autobad'`` with ``'headpos'`` or ``'movecomp'``

   * don't use ``'autobad'`` with ``'st'``

   .. rubric:: References

   https://imaging.mrc-cbu.cam.ac.uk/meg/Maxfilter
   https://imaging.mrc-cbu.cam.ac.uk/meg/maxbugs


.. py:function:: run_cbu_3stage_maxfilter(infif, outbase, args)

   Wrapper for running :py:func:`run_maxfilter <osl_ephys.maxfilter.run_maxfilter>` in three
   sequential steps used by MRC Cognition and Brain Sciences Unit (CBU) in Cambridge:

   0. Fit Origin without nose

   1. Find Bad Channels

   2. Signal Space Separation

   3. Translate to default

   :param infif: Path to input fif file (raw data).
   :type infif: str
   :param outbase: output directory.
   :type outbase: str
   :param args: Dictionary of arguments to pass to maxfilter.  See ``help(osl_ephys.maxfilter)`` for all options.
   :type args: dict

   .. rubric:: Notes

   All files are written to disk and the output of each stage is used as the input to the next.

   .. rubric:: References

   https://imaging.mrc-cbu.cam.ac.uk/meg/Maxfilter
   https://imaging.mrc-cbu.cam.ac.uk/meg/maxbugs


.. py:function:: run_maxfilter_batch(files, outdir, args=None)

   Batch Maxfiltering.

   :param files: Path(s) to raw fif files to maxfilter.
   :type files: str or list of str
   :param outdir: Path to directory to save output to.
   :type outdir: str
   :param args: List of additional optional arguments to pass to osl_maxfilter.  See ``help(osl_ephys.maxfilter)`` for all options.
                If a string is passed it it split input a list (delimited by spaces).
                E.g. ``args="--maxpath /neuro/bin/util/maxfilter"``
                is equivalent to ``args=["--maxpath", "/neuro/bin/util/maxfilter"]``.
   :type args: str

   .. rubric:: Notes

   Example use:

   >>> run_maxfilter_batch(files="/path/to/fif", outdir="/path/to/outdir",
       args="--maxpath /neuro/bin/util/maxfilter --scanner Neo --tsss --mode
       multistage --headpos --movecomp")



.. py:function:: main(argv=None)


