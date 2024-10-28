:py:mod:`osl_ephys.preprocessing.plot_ica`
==========================================

.. py:module:: osl_ephys.preprocessing.plot_ica

.. autoapi-nested-parse::

   Plotting functions for ICA.



Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   osl_ephys.preprocessing.plot_ica.osl_MNEBrowseFigure



Functions
~~~~~~~~~

.. autoapisummary::

   osl_ephys.preprocessing.plot_ica.plot_ica
   osl_ephys.preprocessing.plot_ica._plot_sources
   osl_ephys.preprocessing.plot_ica._get_browser
   osl_ephys.preprocessing.plot_ica._init_browser
   osl_ephys.preprocessing.plot_ica.flatten_recursive
   osl_ephys.preprocessing.plot_ica._plot_ica_sources_evoked



Attributes
~~~~~~~~~~

.. autoapisummary::

   osl_ephys.preprocessing.plot_ica.logger
   osl_ephys.preprocessing.plot_ica.backend


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


