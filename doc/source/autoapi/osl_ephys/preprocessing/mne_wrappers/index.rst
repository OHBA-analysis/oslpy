:py:mod:`osl_ephys.preprocessing.mne_wrappers`
==============================================

.. py:module:: osl_ephys.preprocessing.mne_wrappers

.. autoapi-nested-parse::

   Wrappers for MNE functions to perform preprocessing.

   We have run_mne_anonymous which tries to run a method directly on a target
   object (typically an mne Raw or Epochs object).

   In addition, there are a set of wrapper functions for MNE methods which need
   a bit more option processing than the default - for example, converting input
   strings into arrays of frequencies

   Wrapper functions have priority and will be run rather than the direct method
   call if a wrapper is present. If no wrapper is present then we fall back to
   the direct method call.

   Most wrapper functions run on the `` object in `dataset` by default
   and the function docstrings assume this - but is most cases `mne.io.Raw` can
   be replaced with `mne.Epochs` (or `dataset['raw']` by `dataset['epochs']` and
   the function will still work, e.g. :py:meth:`mne.Epochs.pick <mne.Epochs.pick>`.
   In order to apply the method to an object different from `mne.Raw`, the `target`
   argument can be specified in `userargs`. For example, `target: 'epochs'` can be
   specified in the userargs to apply the method to `dataset['epochs']` instead of
   `dataset['raw']`.



Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   osl_ephys.preprocessing.mne_wrappers.run_mne_anonymous
   osl_ephys.preprocessing.mne_wrappers.run_mne_notch_filter
   osl_ephys.preprocessing.mne_wrappers.run_mne_pick
   osl_ephys.preprocessing.mne_wrappers.run_mne_pick_channels
   osl_ephys.preprocessing.mne_wrappers.run_mne_pick_types
   osl_ephys.preprocessing.mne_wrappers.run_mne_resample
   osl_ephys.preprocessing.mne_wrappers.run_mne_set_channel_types
   osl_ephys.preprocessing.mne_wrappers.run_mne_drop_bad
   osl_ephys.preprocessing.mne_wrappers.run_mne_apply_baseline
   osl_ephys.preprocessing.mne_wrappers.run_mne_find_events
   osl_ephys.preprocessing.mne_wrappers.run_mne_epochs
   osl_ephys.preprocessing.mne_wrappers.run_mne_annotate_amplitude
   osl_ephys.preprocessing.mne_wrappers.run_mne_annotate_muscle_zscore
   osl_ephys.preprocessing.mne_wrappers.run_mne_find_bad_channels_maxwell
   osl_ephys.preprocessing.mne_wrappers.run_mne_maxwell_filter
   osl_ephys.preprocessing.mne_wrappers.run_mne_compute_current_source_density
   osl_ephys.preprocessing.mne_wrappers.run_mne_tfr_multitaper
   osl_ephys.preprocessing.mne_wrappers.run_mne_tfr_morlet
   osl_ephys.preprocessing.mne_wrappers.run_mne_tfr_stockwell
   osl_ephys.preprocessing.mne_wrappers.run_mne_ica_raw
   osl_ephys.preprocessing.mne_wrappers.run_mne_ica_autoreject
   osl_ephys.preprocessing.mne_wrappers.run_mne_apply_ica



Attributes
~~~~~~~~~~

.. autoapisummary::

   osl_ephys.preprocessing.mne_wrappers.logger


.. py:data:: logger

   

.. py:function:: run_mne_anonymous(dataset, userargs, method)

   OSL-Batch function which runs a method directly on a target MNE object in ``dataset``,
   typically an :py:class:`mne.io.Raw <mne.io.Raw>` or :py:class:`mne.Epochs <mne.Epochs>` object.

   OSL Batch will first look for OSL/MNE wrapper functions for the method, and
   otherwise will try to run the method directly on the target object.

   :param dataset: Dictionary containing at least an MNE object with the key ``raw``.
   :type dataset: dict
   :param userargs: Contains user arguments for the function.
   :type userargs: dict
   :param method: See :py:class:`mne.io.Raw <mne.io.Raw>` and :py:class:`mne.Epochs <mne.Epochs>` for the available methods.
   :type method: str

   :returns: **dataset** -- Input dictionary containing MNE objects that have been modified in place.
   :rtype: dict


.. py:function:: run_mne_notch_filter(dataset, userargs)

   OSL-Batch wrapper for :py:meth:`mne.io.Raw.notch_filter <mne.io.Raw.notch_filter>`.

   This function calls :py:meth:`notch_filter <mne.io.Raw.notch_filter>` on
   an MNE object in ``dataset``. Additional arguments on the MNE function can be
   specified as a dictionary.

   :param dataset: Dictionary containing at least an MNE object with the key ``raw``.
   :type dataset: dict
   :param userargs: Dictionary of additional arguments to be passed to :py:meth:`mne.io.Raw.notch_filter <mne.io.Raw.notch_filter>`.
   :type userargs: dict

   :returns: **dataset** -- Input dictionary containing MNE objects that have been modified in place.
   :rtype: dict


.. py:function:: run_mne_pick(dataset, userargs)

   OSL-Batch wrapper for :py:meth:`mne.io.Raw.pick <mne.io.Raw.pick>`.

   This function calls :py:meth:`pick <mne.io.Raw.pick>` on an MNE object in
   ``dataset``. Additional arguments on the MNE function can be
   specified as a dictonary.

   :param dataset: Dictionary containing at least an MNE object with the key ``raw``.
   :type dataset: dict
   :param userargs: Dictionary of additional arguments to be passed to :py:meth:`mne.io.Raw.pick <mne.io.Raw.pick>`.
   :type userargs: dict

   :returns: **dataset** -- Input dictionary containing MNE objects that have been modified in place.
   :rtype: dict

   .. rubric:: Notes

   In MNE-Batch, an example call would look like

   >>> preproc:
   >>>  - pick: {picks: 'meg'}

   By default, the :py:meth:`mne.io.Raw.pick <mne.io.Raw.pick>` will be
   called on ``dataset['raw']``, you can specify another options by specifying
   ``target`` in ``userargs``. For example:

   >>> preproc:
   >>>  - pick: {picks: 'meg', target: 'epochs'}

   Then the function or method will be called on ``dataset['epochs']`` instead.


.. py:function:: run_mne_pick_channels(dataset, userargs)

   OSL-Batch wrapper for :py:meth:`mne.io.Raw.pick_channels <mne.io.Raw.pick_channels>`.

   This function calls :py:meth:`pick_channels <mne.io.Raw.pick_channels>` on
   an MNE object in ``dataset``. Additional arguments on the MNE function can be
   specified as a dictonary.

   :param dataset: Dictionary containing at least an MNE object with the key ``raw``.
   :type dataset: dict
   :param userargs: Dictionary of additional arguments to be passed to :py:meth:`mne.io.Raw.pick_channels <mne.io.Raw.pick_channels>`.
   :type userargs: dict

   :returns: **dataset** -- Input dictionary containing MNE objects that have been modified in place.
   :rtype: dict


.. py:function:: run_mne_pick_types(dataset, userargs)

   OSL-Batch wrapper for :py:meth:`raw.pick_types <mne.io.Raw.pick_types>`.

   This function calls :py:meth:`pick_types <mne.io.Raw.pick_types>` on an MNE object in
   ``dataset``. Additional arguments on the MNE function can be specified as a dictonary.

   :param dataset: Dictionary containing at least an MNE object with the key ``raw``.
   :type dataset: dict
   :param userargs: Dictionary of additional arguments to be passed to :py:meth:`mne.io.Raw.pick_types <mne.io.Raw.pick_types>`.
   :type userargs: dict

   :returns: **dataset** -- Input dictionary containing MNE objects that have been modified in place.
   :rtype: dict


.. py:function:: run_mne_resample(dataset, userargs)

   OSL-Batch wrapper for :py:meth:`mne.io.Raw.resample <mne.io.Raw.resample>`.

   This function calls :py:meth:`resample <mne.io.Raw.resample>` on
   an MNE object in ``dataset``. Additional arguments on the MNE function can be
   specified as a dictonary.

   :param dataset: Dictionary containing at least an MNE object with the key ``raw``.
   :type dataset: dict
   :param userargs: Dictionary of additional arguments to be passed to :py:meth:`mne.io.Raw.resample <mne.io.Raw.resample>`.
   :type userargs: dict

   :returns: **dataset** -- Input dictionary containing MNE objects that have been modified in place.
   :rtype: dict


.. py:function:: run_mne_set_channel_types(dataset, userargs)

   OSL-Batch wrapper for :py:meth:`mne.io.Raw.set_channel_types <mne.io.Raw.set_channel_types>`.

   This function calls :py:meth:`set_channel_types <mne.io.Raw.set_channel_types>` on
   an MNE object in ``dataset``. Additional arguments on the MNE function can be
   specified as a dictonary.

   :param dataset: Dictionary containing at least an MNE object with the key ``raw``.
   :type dataset: dict
   :param userargs: Dictionary of additional arguments to be passed to :py:meth:`mne.io.Raw.set_channel_types <mne.io.Raw.set_channel_types>`.
   :type userargs: dict

   :returns: **dataset** -- Input dictionary containing MNE objects that have been modified in place.
   :rtype: dict


.. py:function:: run_mne_drop_bad(dataset, userargs)

   OSL-Batch wrapper for :py:meth:`mne.Epochs.drop_bad <mne.Epochs.drop_bad>`.

   This function calls :py:meth:`drop_bad <mne.Epochs.drop_bad>` on
   an MNE :py:class:`Epochs <mne.Epochs>` object in ``dataset``. Additional arguments on the MNE function can be
   specified as a dictonary.

   :param dataset: Dictionary containing at least an MNE object with the key ``raw`` and ``epochs``.
   :type dataset: dict
   :param userargs: Dictionary of additional arguments to be passed to :py:meth:`mne.Epochs.drop_bad <mne.Epochs.drop_bad>`.
   :type userargs: dict

   :returns: **dataset** -- Input dictionary containing MNE objects that have been modified in place.
   :rtype: dict


.. py:function:: run_mne_apply_baseline(dataset, userargs)

   OSL-Batch wrapper for :py:meth:`epochs.apply_baseline <mne.Epochs.apply_baseline>`.

   This function calls :py:meth:`mne.Epochs.apply_baseline <mne.Epochs.apply_baseline>` on
   an MNE :py:class:`Epochs <mne.Epochs>` object in ``dataset``. Additional arguments on the MNE function can be
   specified as a dictonary.

   :param dataset: Dictionary containing at least an MNE object with the keys ``raw`` and ``epochs``.
   :type dataset: dict
   :param userargs: Dictionary of additional arguments to be passed to :py:meth:`mne.Epochs.apply_baseline <mne.Epochs.apply_baseline>`.
   :type userargs: dict

   :returns: **dataset** -- Input dictionary containing MNE objects that have been modified in place.
   :rtype: dict


.. py:function:: run_mne_find_events(dataset, userargs)

   OSL-Batch wrapper for :py:func:`mne.find_events <mne.find_events>`.

   This function calls :py:func:`find_events <mne.find_events>` on
   an MNE :py:class:`Raw <mne.io.Raw>` object in ``dataset``. Additional arguments on the MNE function can be
   specified as a dictonary.

   :param dataset: Dictionary containing at least an MNE object with the key ``raw``.
   :type dataset: dict
   :param userargs: Dictionary of additional arguments to be passed to :py:func:`mne.find_events <mne.find_events>`.
   :type userargs: dict

   :returns: **dataset** -- Input dictionary containing MNE objects that have been modified in place.
   :rtype: dict


.. py:function:: run_mne_epochs(dataset, userargs)

   OSL-Batch wrapper for :py:class:`mne.Epochs <mne.Epochs>`.

   This function calls :py:class:`mne.Epochs <mne.Epochs>` on the ``raw``, ``events``, and ``event-id``
   keys in ``dataset``. Additional arguments on the MNE function can be specified as a dictonary.

   :param dataset: Dictionary containing at least an MNE object with the keys ``raw``, ``events``, and ``event-id``.
   :type dataset: dict
   :param userargs: Dictionary of additional arguments to be passed to :py:class:`mne.Epochs <mne.Epochs>`.
   :type userargs: dict

   :returns: **dataset** -- Input dictionary containing MNE objects that have been modified in place.
   :rtype: dict


.. py:function:: run_mne_annotate_amplitude(dataset, userargs)

   OSL-Batch wrapper for :py:func:`mne.preprocessing.annotate_amplitude <mne.preprocessing.annotate_amplitude>`.

   This function calls :py:func:`annotate_amplitude <mne.preprocessing.annotate_amplitude>` on
   an MNE object in ``dataset``. Additional arguments on the MNE function can be
   specified as a dictonary.

   :param dataset: Dictionary containing at least an MNE object with the key ``raw``.
   :type dataset: dict
   :param userargs: Dictionary of additional arguments to be passed to :py:func:`mne.preprocessing.annotate_amplitude <mne.preprocessing.annotate_amplitude>`.
   :type userargs: dict

   :returns: **dataset** -- Input dictionary containing MNE objects that have been modified in place.
   :rtype: dict


.. py:function:: run_mne_annotate_muscle_zscore(dataset, userargs)

   OSL-Batch wrapper for :py:func:`mne.preprocessing.annotate_muscle_zscore <mne.preprocessing.annotate_muscle_zscore>`.

   This function calls :py:func:`annotate_muscle_zscore <mne.preprocessing.annotate_muscle_zscore>` on
   an MNE object in ``dataset``. Additional arguments on the MNE function can be
   specified as a dictonary.

   :param dataset: Dictionary containing at least an MNE object with the key ``raw``.
   :type dataset: dict
   :param userargs: Dictionary of additional arguments to be passed to :py:func:`mne.preprocessing.annotate_muscle_zscore <mne.preprocessing.annotate_muscle_zscore>`.
   :type userargs: dict

   :returns: **dataset** -- Input dictionary containing MNE objects that have been modified in place.
   :rtype: dict


.. py:function:: run_mne_find_bad_channels_maxwell(dataset, userargs)

   OSL-Batch wrapper for :py:func:`mne.preprocessing.find_bad_channels_maxwell <mne.preprocessing.find_bad_channels_maxwell>`.

   This function calls :py:func:`find_bad_channels_maxwell <mne.preprocessing.find_bad_channels_maxwell>` on
   an MNE :py:class:`Raw <mne.io.Raw>` object in ``dataset``. Additional arguments on the MNE function can be
   specified as a dictonary.

   :param dataset: Dictionary containing at least an MNE object with the key ``raw``.
   :type dataset: dict
   :param userargs: Dictionary of additional arguments to be passed to :py:func:`mne.preprocessing.find_bad_channels_maxwell <mne.preprocessing.find_bad_channels_maxwell>`.
   :type userargs: dict

   :returns: **dataset** -- Input dictionary containing MNE objects that have been modified in place.
   :rtype: dict


.. py:function:: run_mne_maxwell_filter(dataset, userargs)

   OSL-Batch wrapper for :py:func:`mne.preprocessing.maxwell_filter <mne.preprocessing.maxwell_filter>`.

   This function calls :py:func:`maxwell_filter <mne.preprocessing.maxwell_filter>` on
   an MNE :py:class:`Raw <mne.io.Raw>` object in ``dataset``. Additional arguments on the MNE function can be
   specified as a dictonary.

   :param dataset: Dictionary containing at least an MNE object with the key ``raw``.
   :type dataset: dict
   :param userargs: Dictionary of additional arguments to be passed to :py:func:`mne.preprocessing.maxwell_filter <mne.preprocessing.maxwell_filter>`.
   :type userargs: dict

   :returns: **dataset** -- Input dictionary containing MNE objects that have been modified in place.
   :rtype: dict


.. py:function:: run_mne_compute_current_source_density(dataset, userargs)

   OSL-Batch wrapper for :py:func:`mne.preprocessing.compute_current_source_density <mne.preprocessing.compute_current_source_density>`.

   This function calls :py:func:`compute_current_source_density <mne.preprocessing.compute_current_source_density>` on
   an MNE object in ``dataset``. Additional arguments on the MNE function can be
   specified as a dictonary.

   :param dataset: Dictionary containing at least an MNE object with the key ``raw``.
   :type dataset: dict
   :param userargs: Dictionary of additional arguments to be passed to :py:func:`mne.preprocessing.compute_current_source_density <mne.preprocessing.compute_current_source_density>`.
   :type userargs: dict

   :returns: **dataset** -- Input dictionary containing MNE objects that have been modified in place.
   :rtype: dict


.. py:function:: run_mne_tfr_multitaper(dataset, userargs)

   OSL-Batch wrapper for :py:func:`mne.time_frequency.tfr_multitaper <mne.time_frequency.tfr_multitaper>`.

   This function calls :py:func:`tfr_multitaper <mne.time_frequency.tfr_multitaper>` on
   an MNE :py:class:`Epochs <mne.Epochs>` or :py:class:`Evoked <mne.Evoked>` object in ``dataset``. Additional arguments on the MNE function can be
   specified as a dictonary.

   :param dataset: Dictionary containing at least an MNE object with the keys ``raw``, and ``evoked`` or ``epochs``.
   :type dataset: dict
   :param userargs: Dictionary of additional arguments to be passed to :py:func:`mne.time_frequency.tfr_multitaper <mne.time_frequency.tfr_multitaper>`.
   :type userargs: dict

   :returns: **dataset** -- Input dictionary containing MNE objects that have been modified in place.
   :rtype: dict


.. py:function:: run_mne_tfr_morlet(dataset, userargs)

   OSL-Batch wrapper for :py:func:`mne.time_frequency.tfr_morlet <mne.time_frequency.tfr_morlet>`.

   This function calls :py:func:`tfr_morlet <mne.time_frequency.tfr_morlet>` on
   an MNE :py:class:`Epochs <mne.Epochs>` or :py:class:`Evoked <mne.Evoked>` object in ``dataset``. Additional arguments on the MNE function can be
   specified as a dictonary.

   :param dataset: Dictionary containing at least an MNE object with the keys ``raw``, and ``evoked`` or ``epochs``.
   :type dataset: dict
   :param userargs: Dictionary of additional arguments to be passed to :py:func:`mne.time_frequency.tfr_morlet <mne.time_frequency.tfr_morlet>`.
   :type userargs: dict

   :returns: **dataset** -- Input dictionary containing MNE objects that have been modified in place.
   :rtype: dict


.. py:function:: run_mne_tfr_stockwell(dataset, userargs)

   OSL-Batch wrapper for :py:func:`mne.time_frequency.tfr_stockwell <mne.time_frequency.tfr_stockwell>`.

   This function calls :py:func:`tfr_stockwell <mne.time_frequency.tfr_stockwell>` on
   an MNE :py:class:`Epochs <mne.Epochs>` or :py:class:`Evoked <mne.Evoked>` object in ``dataset``. Additional arguments on the MNE function can be
   specified as a dictonary.

   :param dataset: Dictionary containing at least an MNE object with the keys ``raw``, and ``evoked`` or ``epochs``.
   :type dataset: dict
   :param userargs: Dictionary of additional arguments to be passed to :py:func:`mne.time_frequency.tfr_stockwell <mne.time_frequency.tfr_stockwell>`.
   :type userargs: dict

   :returns: **dataset** -- Input dictionary containing MNE objects that have been modified in place.
   :rtype: dict


.. py:function:: run_mne_ica_raw(dataset, userargs)

   OSL-Batch wrapper for :py:class:`mne.preprocessing.ICA <mne.preprocessing.ICA>`.

   This function creates class :py:class:`ICA <mne.preprocessing.ICA>`
   and fits it to an MNE object in ``dataset``. Additional arguments on the MNE function can be
   specified as a dictonary. The ``raw`` object in ``dataset`` is filtered (1 Hz high pass) before
   fitting the ICA.

   :param dataset: Dictionary containing at least an MNE object with the key ``raw``.
   :type dataset: dict
   :param userargs: Dictionary of additional arguments to be passed to :py:class:`mne.preprocessing.ICA <mne.preprocessing.ICA>` ,
                    :py:meth:`mne.preprocessing.ICA.fit <mne.preprocessing.ICA.fit>`, and :py:meth:`mne.io.Raw.filter <mne.io.Raw.filter>` .
   :type userargs: dict

   :returns: **dataset** -- Input dictionary containing MNE objects that have been modified in place.
   :rtype: dict


.. py:function:: run_mne_ica_autoreject(dataset, userargs)

   OSL-Batch wrapper for :py:meth:`mne.preprocessing.ICA.find_bads_ecg <mne.preprocessing.ICA.find_bads_ecg>` and :py:meth:`mne.preprocessing.ICA.find_bads_eog <mne.preprocessing.ICA.find_bads_eog>`.

   This function identifies IC's that are deemed to correspond to ECG or EOG artifacts, as found by
   :py:meth:`find_bads_ecg <mne.preprocessing.ICA.find_bads_ecg>` and
   :py:meth:`find_bads_eog <mne.preprocessing.ICA.find_bads_eog>` on
   the ``raw`` and ``ica`` objects in ``dataset``. Additional arguments on the MNE functions can be
   specified as a dictonary.

   :param dataset: Dictionary containing at least an MNE object with the key ``raw``.
   :type dataset: dict
   :param userargs: Dictionary of additional arguments to be passed to :py:meth:`mne.preprocessing.ICA.find_bads_ecg <mne.preprocessing.ICA.find_bads_ecg>`
                    and :py:meth:`mne.preprocessing.ICA.find_bads_eog <mne.preprocessing.ICA.find_bads_eog>`.
   :type userargs: dict

   :returns: **dataset** -- Input dictionary containing MNE objects that have been modified in place.
   :rtype: dict


.. py:function:: run_mne_apply_ica(dataset, userargs)

   OSL-Batch wrapper for :py:meth:`mne.preprocessing.ICA.apply <mne.preprocessing.ICA.apply>`.

   This function creates class :py:meth:`mne.preprocessing.ICA.apply <mne.preprocessing.ICA.apply>`
   and fits it to an MNE object in ``dataset``. Additional arguments on the MNE function can be
   specified as a dictonary.

   :param dataset: Dictionary containing at least an MNE object with the key ``raw``.
   :type dataset: dict
   :param userargs: Dictionary of additional arguments to be passed to :py:meth:`mne.preprocessing.ICA.apply <mne.preprocessing.ICA.apply>`.
   :type userargs: dict

   :returns: **dataset** -- Input dictionary containing MNE objects that have been modified in place.
   :rtype: dict


