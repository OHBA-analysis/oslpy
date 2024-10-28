:py:mod:`osl_ephys.preprocessing.osl_wrappers`
==============================================

.. py:module:: osl_ephys.preprocessing.osl_wrappers

.. autoapi-nested-parse::

   Wrappers for MNE functions to perform preprocessing.



Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   osl_ephys.preprocessing.osl_wrappers.gesd
   osl_ephys.preprocessing.osl_wrappers._find_outliers_in_dims
   osl_ephys.preprocessing.osl_wrappers._find_outliers_in_segments
   osl_ephys.preprocessing.osl_wrappers.detect_artefacts
   osl_ephys.preprocessing.osl_wrappers.detect_maxfilt_zeros
   osl_ephys.preprocessing.osl_wrappers.detect_badsegments
   osl_ephys.preprocessing.osl_wrappers.detect_badchannels
   osl_ephys.preprocessing.osl_wrappers.drop_bad_epochs
   osl_ephys.preprocessing.osl_wrappers.run_osl_read_dataset
   osl_ephys.preprocessing.osl_wrappers.run_osl_bad_segments
   osl_ephys.preprocessing.osl_wrappers.run_osl_bad_channels
   osl_ephys.preprocessing.osl_wrappers.run_osl_drop_bad_epochs
   osl_ephys.preprocessing.osl_wrappers.run_osl_ica_manualreject



Attributes
~~~~~~~~~~

.. autoapisummary::

   osl_ephys.preprocessing.osl_wrappers.logger


.. py:data:: logger

   

.. py:function:: gesd(x, alpha=0.05, p_out=0.1, outlier_side=0)

   Detect outliers using Generalized ESD test

    Parameters
    ----------
    x : vector
       Data set containing outliers
    alpha : scalar
       Significance level to detect at (default = 0.05)
    p_out : int
       Maximum number of outliers to detect (default = 10% of data set)
    outlier_side : {-1,0,1}
       Specify sidedness of the test
          - outlier_side = -1 -> outliers are all smaller
          - outlier_side = 0  -> outliers could be small/negative or large/positive (default)
          - outlier_side = 1  -> outliers are all larger

   :returns: * **idx** (*boolean vector*) -- Boolean array with TRUE wherever a sample is an outlier
             * **x2** (*vector*) -- Input array with outliers removed

   .. rubric:: References

   B. Rosner (1983). Percentage Points for a Generalized ESD Many-Outlier Procedure. Technometrics 25(2), pp. 165-172.
   http://www.jstor.org/stable/1268549?seq=1


.. py:function:: _find_outliers_in_dims(X, axis=-1, metric_func=np.std, gesd_args=None)

   Find outliers across specified dimensions of an array


.. py:function:: _find_outliers_in_segments(X, axis=-1, segment_len=100, metric_func=np.std, gesd_args=None, channel_wise=False, channel_axis=0, threshold=0.05)

   Identify outlier segments within an array.
   Parameters:
   - X: np.ndarray
       Input data array with dimensions (channel, time).
   - axis: int
       The axis along which to segment the data (default is -1, the last axis).
   - channel_axis: int
       The axis along which channels are stored (default is 0, the first axis).
   - segment_len: iant
       Length of each segment along the specified axis.
   - metric_func: callable
       Function to compute the metric for each segment (default is np.std).
   - gesd_args: dict
       Additional arguments to pass to the GESD.
   - channel_wise: bool
       If True, the function will treat each channel seperately when detecting bad segments.
   - channel_axis: int
       The axis to treat as the channel axis. Only used when ``channel_wise=True``.
   - threshold: str or float
       Threshold for outlier detection. Only used when ``channel_wise=True``.
       If 'any', a segment is marked as an outlier if
       any of its channels is an outlier.
       If a float, a segment is marked as an outlier if the fraction of outlier
       channels exceeds the threshold.

   Returns:
   - bads: np.ndarray
       Boolean array indicating outlier segments.


.. py:function:: detect_artefacts(X, axis=None, reject_mode='dim', metric_func=np.std, segment_len=100, gesd_args=None, ret_mode='bad_inds', channel_wise=False, channel_axis=0, channel_threshold=0.05)

   Detect bad observations or segments in a dataset

   :param X: Array to find artefacts in.
   :type X: ndarray
   :param axis: Index of the axis to detect artefacts in
   :type axis: int
   :param reject_mode: Flag indicating whether to detect outliers across a dimension (dim;
                       default) or whether to split a dim into segments and detect outliers in
                       the them (segments)
   :type reject_mode: {'dim' | 'segments'}
   :param metric_func: Function defining metric to detect outliers on. Defaults to np.std but
                       can be any function taking an array and returning a single number.
   :type metric_func: function
   :param segement_len: Integer window length of dummy epochs for bad_segment detection
   :type segement_len: int > 0
   :param gesd_args: Dictionary of arguments to pass to gesd
   :type gesd_args: dict
   :param ret_mode: Flag indicating whether to return the indices for good observations,
                    indices for bad observations (default), the input data with outliers
                    removed (zero_bads) or the input data with outliers replaced with nans
                    (nan_bads)
   :type ret_mode: {'good_inds','bad_inds','zero_bads','nan_bads'}
   :param channel_wise: If True, the function will treat each channel seperately when detecting bad segments,
                        only used when ``reject_mode='segments'``.
   :type channel_wise: bool
   :param channel_axis: The axis to treat as the channel axis. Only used when ``channel_wise=True``.
   :type channel_axis: int
   :param channel_threshold: The treshold to use for channel-wise detection. Only used when ``channel_wise=True``.
   :type channel_threshold: str or float

   :returns: If ret_mode is ``'bad_inds'`` or ``'good_inds'``, this returns a boolean vector
             of length ``X.shape[axis]`` indicating good or bad samples. If ``ret_mode`` is
             ``'zero_bads'`` or ``'nan_bads'`` this returns an array copy of the input data
             ``X`` with bad samples set to zero or ``np.nan`` respectively.
   :rtype: ndarray


.. py:function:: detect_maxfilt_zeros(raw)

   This function tries to load the maxfilter log files in order
       to annotate zeroed out data in the :py:class:`mne.io.Raw <mne.io.Raw>` object. It
       assumes that the log file is in the same directory as the
       raw file and has the same name, but with the extension ``.log``.

   :param raw: MNE raw object.
   :type raw: :py:class:`mne.io.Raw <mne.io.Raw>`

   :returns: **bad_inds** -- Boolean array indicating which time points are zeroed out.
   :rtype: np.array of bool (n_times,) or None


.. py:function:: detect_badsegments(raw, picks, segment_len=1000, significance_level=0.05, metric='std', ref_meg='auto', mode=None, detect_zeros=True, channel_wise=False, channel_axis=0, channel_threshold=0.05)

   Set bad segments in an MNE :py:class:`Raw <mne.io.Raw>` object as defined by the Generalized ESD test in :py:func:`osl_ephys.preprocessing.osl_wrappers.gesd <osl_ephys.preprocessing.osl_wrappers.gesd>`.


   :param raw: MNE raw object.
   :type raw: :py:class:`mne.io.Raw <mne.io.Raw>`
   :param picks: Channel types to pick. See Notes for recommendations.
   :type picks: str
   :param segment_len: Window length to divide the data into (non-overlapping).
   :type segment_len: int
   :param significance_level: Significance level for detecting outliers. Must be between 0-1.
   :type significance_level: float
   :param metric: Metric to use. Could be ``'std'``, ``'var'`` or ``'kurtosis'``.
   :type metric: str
   :param ref_meg: ref_meg argument to pass with :py:func:`mne.pick_types <mne.pick_types>`.
   :type ref_meg: str
   :param mode: Should be ``None`` ``'diff'`` or ``'maxfilter'``.
                When ``mode='diff'`` we calculate a difference time series before
                detecting bad segments. When ``mode='maxfilter'`` we only mark the
                segments with zeros from MaxFiltering as bad.
   :type mode: str
   :param detect_zeros: Should we detect segments of zeros based on the maxfilter files?
   :type detect_zeros: bool
   :param channel_wise: If True, the function will treat each channel seperately.
   :type channel_wise: bool
   :param channel_axis: The axis to treat as the channel axis. Only used when ``channel_wise=True``.
   :type channel_axis: int
   :param channel_threshold: The treshold to use for channel-wise detection. Only used when ``channel_wise=True``.
   :type channel_threshold: str or float

   :returns: **raw** -- MNE raw object with bad segments annotated.
   :rtype: :py:class:`mne.io.Raw <mne.io.Raw>`

   .. rubric:: Notes

   Note that for Elekta/MEGIN data, we recommend using ``picks: 'mag'`` or ``picks: 'grad'`` separately (in no particular order).

   Note that with CTF data, mne.pick_types will return:
       ~274 axial grads (as magnetometers) if ``{picks: 'mag', ref_meg: False}``
       ~28 reference axial grads if ``{picks: 'grad'}``.
       Thus, it is recommended to use ``picks:'mag'`` in combination with ``ref_mag: False``, and ``picks:'grad'`` separately (in no particular order).


.. py:function:: detect_badchannels(raw, picks, ref_meg='auto', significance_level=0.05)

   Set bad channels in an MNE :py:class:`Raw <mne.io.Raw>` object as defined by the Generalized ESD test in :py:func:`osl_ephys.preprocessing.osl_wrappers.gesd <osl_ephys.preprocessing.osl_wrappers.gesd>`.

   :param raw: MNE raw object.
   :type raw: :py:class:`mne.io.Raw <mne.io.Raw>`
   :param picks: Channel types to pick. See Notes for recommendations.
   :type picks: str
   :param ref_meg: ref_meg argument to pass with :py:func:`mne.pick_types <mne.pick_types>`.
   :type ref_meg: str
   :param significance_level: Significance level for detecting outliers. Must be between 0-1.
   :type significance_level: float

   :returns: **raw** -- MNE Raw object with bad channels marked.
   :rtype: :py:class:`mne.io.Raw <mne.io.Raw>`

   .. rubric:: Notes

   Note that for Elekta/MEGIN data, we recommend using ``picks:'mag'`` or ``picks:'grad'`` separately (in no particular order).

   Note that with CTF data, mne.pick_types will return:
       ~274 axial grads (as magnetometers) if ``{picks: 'mag', ref_meg: False}``
       ~28 reference axial grads if ``{picks: 'grad'}``.
       Thus, it is recommended to use ``picks:'mag'`` in combination with ``ref_mag: False``,  and ``picks:'grad'`` separately (in no particular order).


.. py:function:: drop_bad_epochs(epochs, picks, significance_level=0.05, max_percentage=0.1, outlier_side=0, metric='std', ref_meg='auto', mode=None)

   Drop bad epochs in an MNE :py:class:`Epochs <mne.Epochs>` object as defined by the Generalized ESD test in :py:func:`osl_ephys.preprocessing.osl_wrappers.gesd <osl_ephys.preprocessing.osl_wrappers.gesd>`.

   :param epochs: MNE Epochs object.
   :type epochs: :py:class:`mne.Epochs <mne.Epochs>`
   :param picks: Channel types to pick.
   :type picks: str
   :param significance_level: Significance level for detecting outliers. Must be between 0-1.
   :type significance_level: float
   :param max_percentage: Maximum fraction of the epochs to drop. Should be between 0-1.
   :type max_percentage: float
   :param outlier_side: Specify sidedness of the test:

                        * outlier_side = -1 -> outliers are all smaller

                        * outlier_side = 0  -> outliers could be small/negative or large/positive (default)

                        * outlier_side = 1  -> outliers are all larger
   :type outlier_side: int
   :param metric: Metric to use. Could be ``'std'``, ``'var'`` or ``'kurtosis'``.
   :type metric: str
   :param ref_meg: ref_meg argument to pass with :py:func:`mne.pick_types <mne.pick_types>`.
   :type ref_meg: str
   :param mode: Should be ``'diff'`` or ``None``. When ``mode='diff'`` we calculate a difference time
                series before detecting bad segments.
   :type mode: str

   :returns: **epochs** -- MNE Epochs object with bad epoches marked.
   :rtype: :py:meth:`mne.Epochs <mne.Epochs>`

   .. rubric:: Notes

   Note that with CTF data, mne.pick_types will return:
       ~274 axial grads (as magnetometers) if ``{picks: 'mag', ref_meg: False}``
       ~28 reference axial grads if ``{picks: 'grad'}``.


.. py:function:: run_osl_read_dataset(dataset, userargs)

   Reads ``fif``/``npy``/``yml`` files associated with a dataset.

   :param fif: Path to raw fif file (can be preprocessed).
   :type fif: str
   :param preload: Should we load the raw fif data?
   :type preload: bool
   :param ftype: Extension for the fif file (will be replaced for e.g. ``'_events.npy'`` or
                 ``'_ica.fif'``). If ``None``, we assume the fif file is preprocessed with
                 osl-ephys and has the extension ``'_preproc-raw'``. If this fails, we guess
                 the extension as whatever comes after the last ``'_'``.
   :type ftype: str
   :param extra_keys: Space separated list of extra keys to read in from the same directory as the fif file.
                      If no suffix is provided, it's assumed to be .pkl. e.g., 'glm' will read in '..._glm.pkl'
                      'events.npy' will read in '..._events.npy'.
   :type extra_keys: str

   :returns: **dataset** -- Contains keys: ``'raw'``, ``'events'``, ``'event_id'``, ``'epochs'``, ``'ica'``.
   :rtype: dict


.. py:function:: run_osl_bad_segments(dataset, userargs)

   osl-ephys Batch wrapper for :py:meth:`detect_badsegments <osl_ephys.preprocessing.osl_wrappers.detect_badsegments>`.

   :param dataset: Dictionary containing at least an MNE object with the key ``raw``.
   :type dataset: dict
   :param userargs: Dictionary of additional arguments to be passed to :py:meth:`detect_badsegments <osl_ephys.preprocessing.osl_wrappers.detect_badsegments>`.
   :type userargs: dict

   :returns: **dataset** -- Input dictionary containing MNE objects that have been modified in place.
   :rtype: dict


.. py:function:: run_osl_bad_channels(dataset, userargs)

   osl-ephys Batch wrapper for :py:func:`detect_badchannels <osl_ephys.preprocessing.osl_wrappers.detect_badchannels>`.

   :param dataset: Dictionary containing at least an MNE object with the key ``raw``.
   :type dataset: dict
   :param userargs: Dictionary of additional arguments to be passed to :py:meth:`detect_badchannels <osl_ephys.preprocessing.osl_wrappers.detect_badchannels>`.
   :type userargs: dict

   :returns: **dataset** -- Input dictionary containing MNE objects that have been modified in place.
   :rtype: dict

   .. rubric:: Notes

   Note that using 'picks' with CTF data, mne.pick_types will return:
       ~274 axial grads (as magnetometers) if ``{picks: 'mag', ref_meg: False}``
       ~28 reference axial grads if ``{picks: 'grad'}``.


.. py:function:: run_osl_drop_bad_epochs(dataset, userargs)

   osl-ephys Batch wrapper for :py:meth:`drop_bad_epochs <osl_ephys.preprocessing.osl_wrappers.drop_bad_epochs>`.

   :param dataset: Dictionary containing at least an MNE object with the key ``raw``.
   :type dataset: dict
   :param userargs: Dictionary of additional arguments to be passed to :py:meth:`drop_bad_epochs <osl_ephys.preprocessing.osl_wrappers.drop_bad_epochs>`.
   :type userargs: dict

   :returns: **dataset** -- Input dictionary containing MNE objects that have been modified in place.
   :rtype: dict


.. py:function:: run_osl_ica_manualreject(dataset, userargs)

   osl-ephys Batch wrapper for :py:func:`osl_ephys.preprocessing.plot_ica <osl_ephys.preprocessing.plot_ica.plot_ica>`, and optionally :py:meth:`ICA.apply <mne.preprocessing.ICA.apply>`.

   This function opens an interactive window to allow the user to manually reject ICA components. Note that this function will modify the input MNE object in place.
   The interactive plotting function might not work on all systems depending on the backend in use. It will most likely work when using an IDE (e.g. Spyder,
   Pycharm, VS Cose) but not in a Jupyter Notebook.

   :param dataset: Dictionary containing at least an MNE object with the keys ``raw`` and ``ica``.
   :type dataset: dict
   :param userargs: Dictionary of additional arguments to be passed to :py:func:`plot_ica <osl_ephys.preprocessing.plot_ica>`.
   :type userargs: dict

   :returns: **dataset** -- Input dictionary containing MNE objects that have been modified in place.
   :rtype: dict


