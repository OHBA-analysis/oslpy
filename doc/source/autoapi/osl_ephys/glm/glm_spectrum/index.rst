:py:mod:`osl_ephys.glm.glm_spectrum`
====================================

.. py:module:: osl_ephys.glm.glm_spectrum


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   osl_ephys.glm.glm_spectrum.SensorGLMSpectrum
   osl_ephys.glm.glm_spectrum.GroupSensorGLMSpectrum
   osl_ephys.glm.glm_spectrum.MaxStatPermuteGLMSpectrum
   osl_ephys.glm.glm_spectrum.ClusterPermuteGLMSpectrum



Functions
~~~~~~~~~

.. autoapisummary::

   osl_ephys.glm.glm_spectrum.group_glm_spectrum
   osl_ephys.glm.glm_spectrum.glm_spectrum
   osl_ephys.glm.glm_spectrum.glm_irasa
   osl_ephys.glm.glm_spectrum.read_glm_spectrum
   osl_ephys.glm.glm_spectrum.plot_joint_spectrum_clusters
   osl_ephys.glm.glm_spectrum.plot_source_topo
   osl_ephys.glm.glm_spectrum.plot_joint_spectrum
   osl_ephys.glm.glm_spectrum.plot_sensor_spectrum
   osl_ephys.glm.glm_spectrum.plot_sensor_proj
   osl_ephys.glm.glm_spectrum.plot_sensor_data
   osl_ephys.glm.glm_spectrum.prep_scaled_freq
   osl_ephys.glm.glm_spectrum.get_source_colors
   osl_ephys.glm.glm_spectrum.get_mne_sensor_cols
   osl_ephys.glm.glm_spectrum.plot_channel_layout
   osl_ephys.glm.glm_spectrum.plot_with_cols
   osl_ephys.glm.glm_spectrum.decorate_spectrum



.. py:class:: SensorGLMSpectrum(glmsp, info)


   Bases: :py:obj:`osl_ephys.glm.glm_base.GLMBaseResult`

   A class for GLM-Spectra fitted from MNE-Python Raw objects.

   .. py:method:: plot_joint_spectrum(contrast=0, metric='copes', **kwargs)

      Plot a GLM-Spectrum contrast with spatial line colouring and topograpies.

      :param contrast: Contrast to plot (Default value = 0)
      :type contrast: int
      :param freqs: Which frequencies to plot topos for (Default value = 'auto')
      :type freqs: {list, tuple or 'auto'}
      :param base: The x-axis scaling, set to 0.5 for sqrt freq axis (Default value = 1)
      :type base: float
      :param ax: Axis to plot into (Default value = None)
      :type ax: {None or axis handle}
      :param topo_scale: Whether to fix topomap colour scales across all topos ('joint') or
                         leave them individual (Default value = 'joint')
      :type topo_scale: {'joint' or None}
      :param lw: Line width(Default value = 0.5)
      :type lw: flot
      :param ylabel: Y-axis label(Default value = 'Power')
      :type ylabel: str
      :param title: Plot title(Default value = None)
      :type title: str
      :param ylim: min and max values for y-axis (Default value = None)
      :type ylim: {tuple or list}
      :param xtick_skip: Number of xaxis ticks to skip, useful for tight plots (Default value = 1)
      :type xtick_skip: int
      :param topo_prop: Proportion of plot dedicted to topomaps(Default value = 1/3)
      :type topo_prop: float
      :param metric: Which metric to plot? (Default value = 'copes')
      :type metric: {'copes' or 'tstats}


   .. py:method:: plot_sensor_spectrum(contrast=0, metric='copes', **kwargs)

      Plot a GLM-Spectrum contrast with spatial line colouring.

      :param contrast: Contrast to plot
      :type contrast: int
      :param sensor_proj: Whether to plot an inset topo showing spatial colours (Default
                          value = False)
      :type sensor_proj: bool
      :param xticks: xtick positions (Default value = None)
      :type xticks: array_like of float
      :param xticklabels: labels for xticks (Default value = None)
      :type xticklabels: array_like of str
      :param ax: Axis to plot into (Default value = None)
      :type ax: {None or axis handle}
      :param lw: Line width(Default value = 0.5)
      :type lw: flot
      :param ylabel: Y-axis label(Default value = 'Power')
      :type ylabel: str
      :param title: Plot title(Default value = None)
      :type title: str
      :param ylim: min and max values for y-axis (Default value = None)
      :type ylim: {tuple or list}
      :param xtick_skip: Number of xaxis ticks to skip, useful for tight plots (Default value = 1)
      :type xtick_skip: int
      :param topo_prop: Proportion of plot dedicted to topomaps(Default value = 1/3)
      :type topo_prop: float
      :param metric: Which metric to plot(Default value = 'copes')
      :type metric: {'copes' or 'tstats}



.. py:class:: GroupSensorGLMSpectrum(model, design, config, info, fl_contrast_names=None, data=None)


   Bases: :py:obj:`osl_ephys.glm.glm_base.GroupGLMBaseResult`

   A class for group level GLM-Spectra fitted across mmultiple first-level
   GLM-Spectra computed from MNE-Python Raw objects

   .. py:method:: __str__()

      Return str(self).


   .. py:method:: save_pkl(outname, overwrite=True, save_data=False)

      Save GLM-Spectrum result to a pickle file.

      :param outname: Filename or full file path to write pickle to
      :type outname: str
      :param overwrite: Overwrite previous file if one exists? (Default value = True)
      :type overwrite: bool
      :param save_data: Save STFT data in pickle? This is omitted by default to save disk
                        space (Default value = False)
      :type save_data: bool


   .. py:method:: plot_joint_spectrum(gcontrast=0, fcontrast=0, metric='copes', **kwargs)

      Plot a GLM-Spectrum contrast with spatial line colouring and topograpies.

      :param gcontrast: Group level contrast to plot (Default value = 0)
      :type gcontrast: int
      :param fcontrast: First level contrast to plot (Default value = 0)
      :type fcontrast: int
      :param freqs: Which frequencies to plot topos for (Default value = 'auto')
      :type freqs: {list, tuple or 'auto'}
      :param base: The x-axis scaling, set to 0.5 for sqrt freq axis (Default value = 1)
      :type base: float
      :param ax: Axis to plot into (Default value = None)
      :type ax: {None or axis handle}
      :param topo_scale: Whether to fix topomap colour scales across all topos ('joint') or
                         leave them individual (Default value = 'joint')
      :type topo_scale: {'joint' or None}
      :param lw: Line width(Default value = 0.5)
      :type lw: flot
      :param ylabel: Y-axis label(Default value = 'Power')
      :type ylabel: str
      :param title: Plot title(Default value = None)
      :type title: str
      :param ylim: min and max values for y-axis (Default value = None)
      :type ylim: {tuple or list}
      :param xtick_skip: Number of xaxis ticks to skip, useful for tight plots (Default value = 1)
      :type xtick_skip: int
      :param topo_prop: Proportion of plot dedicted to topomaps(Default value = 1/3)
      :type topo_prop: float
      :param metric: Which metric to plot(Default value = 'copes')
      :type metric: {'copes' or 'tstats}


   .. py:method:: get_fl_contrast(fl_con)

      Get the data from a single first level contrast.

      :param fl_con: First level contrast data index to return
      :type fl_con: int

      :returns: **ret_con** -- GroupSensorGLMSpectrum instance containing a single first level contrast.
      :rtype: :py:class:`GroupSensorGLMSpectrum <osl_ephys.glm.glm_spectrum.GroupSensorGLMSpectrum>`



.. py:class:: MaxStatPermuteGLMSpectrum(glmsp, gl_con, fl_con=0, nperms=1000, tstat_args=None, metric='tstats', nprocesses=1, pooled_dims=(1, 2), tmin=None, tmax=None, fmin=None, fmax=None, picks=None)


   Bases: :py:obj:`osl_ephys.glm.glm_base.SensorMaxStatPerm`

   A class holding the result for sensor x frequency cluster stats computed
   from a group level GLM-Spectrum

   .. py:method:: plot_sig_clusters(thresh, ax=None, base=1, min_extent=1)

      Plot the significant clusters at a given threshold.

      :param thresh: The threshold to consider a cluster significant eg 95 or 99
      :type thresh: float
      :param ax: Matplotlib axes to plot on. (Default value = None)
      :type ax: :py:class:`matplotlib.axes <matplotlib.axes>`
      :param base: The x-axis scaling, set to 0.5 for sqrt freq axis (Default value = 1)
      :type base: float



.. py:class:: ClusterPermuteGLMSpectrum(glmsp, gl_con, fl_con=0, nperms=1000, cluster_forming_threshold=3, tstat_args=None, metric='tstats', tmin=None, tmax=None, fmin=None, fmax=None, picks=None, nprocesses=1)


   Bases: :py:obj:`osl_ephys.glm.glm_base.SensorClusterPerm`

   A class holding the result for sensor x frequency cluster stats computed
   from a group level GLM-Spectrum

   .. py:method:: plot_sig_clusters(thresh, ax=None, base=1, min_extent=1)

      Plot the significant clusters at a given threshold.

      :param thresh: The threshold to consider a cluster significant eg 95 or 99
      :type thresh: float
      :param ax: Matplotlib axes to plot on. (Default value = None)
      :type ax: :py:class:`matplotlib.axes <matplotlib.axes>`
      :param base: The x-axis scaling, set to 0.5 for sqrt freq axis (Default value = 1). (Default value = 1)
      :type base: float



.. py:function:: group_glm_spectrum(inspectra, design_config=None, datainfo=None, metric='copes')

   Compute a group GLM-Spectrum from a set of first-level GLM-Spectra.

   :param inspectra: A list containing either the filepaths of a set of saved GLM-Spectra
                     objects, or the GLM-Spectra objects themselves.
   :type inspectra: list, tuple
   :param design_config: The design specification for the group level model (Default value = None)
   :type design_config: :py:class:`glmtools.design.DesignConfig <glmtools.design.DesignConfig>`
   :param datainfo: Dictionary of data values to use as covariates. The length of each
                    covariate must match the number of input GLM-Spectra (Default value =
                    None)
   :type datainfo: dict
   :param metric: Which metric to plot (Default value = 'copes')
   :type metric: {'copes', or 'tsats'}

   :returns: GroupSensorGLMSpectrum instance containing the group level GLM-Spectrum.
   :rtype: :py:class:`GroupSensorGLMSpectrum <osl_ephys.glm.GroupSensorGLMSpectrum>`

   .. rubric:: References

   .. [1] Quinn, A. J., Atkinson, L., Gohil, C., Kohl, O., Pitt, J., Zich, C., Nobre,
      A. C., & Woolrich, M. W. (2022). The GLM-Spectrum: A multilevel framework
      for spectrum analysis with covariate and confound modelling. Cold Spring
      Harbor Laboratory. https://doi.org/10.1101/2022.11.14.516449


.. py:function:: glm_spectrum(XX, reg_categorical=None, reg_ztrans=None, reg_unitmax=None, contrasts=None, fit_intercept=True, standardise_data=False, window_type='hann', nperseg=None, noverlap=None, nfft=None, detrend='constant', return_onesided=True, scaling='density', mode='psd', fmin=None, fmax=None, axis=-1, fs=1, verbose='WARNING')

   Compute a GLM-Spectrum from a MNE-Python Raw data object.

   :param XX: Data to compute GLM-Spectrum from
   :type XX: {MNE Raw object, or data array}
   :param standardise_data: Flag indicating whether to z-transform input data (Default value = False)
   :type standardise_data: bool
   :param reg_categorical: Dictionary of covariate time series to be added as binary regessors. (Default value = None)
   :type reg_categorical: dict or None
   :param reg_ztrans: Dictionary of covariate time series to be added as z-standardised regessors. (Default value = None)
   :type reg_ztrans: dict or None
   :param reg_unitmax: Dictionary of confound time series to be added as positive-valued unitmax regessors. (Default value = None)
   :type reg_unitmax: dict or None
   :param contrasts: Dictionary of contrasts to be computed in the model.
                     (Default value = None, will add a simple contrast for each regressor)
   :type contrasts: dict or None
   :param fit_intercept: Specifies whether a constant valued 'intercept' regressor is included in the model. (Default value = True)'
   :type fit_intercept: bool
   :param nperseg: Length of each segment. Defaults to None, but if window is str or
                   tuple, is set to 256, and if window is array_like, is set to the
                   length of the window.
   :type nperseg: int
   :param noverlap: Number of samples that successive sliding windows should overlap.
   :type noverlap: int
   :param window_type: Desired window to use. If `window` is a string or tuple, it is
                       passed to `scipy.signal.windows.get_window` to generate the
                       window values, which are DFT-even by default. See `scipy.signal.windows`
                       for a list of windows and required parameters.
                       If `window` is array_like it will be used directly as the window and its
                       length must be nperseg. Defaults to a Hann window.
   :type window_type: str or tuple or array_like, optional
   :param detrend: Specifies how to detrend each segment. If `detrend` is a
                   string, it is passed as the `type` argument to the `detrend`
                   function. If it is a function, it takes a segment and returns a
                   detrended segment. If `detrend` is `False`, no detrending is
                   done. Defaults to 'constant'.'
   :type detrend: str or function or `False`, optional
   :param nfft: Length of the FFT to use (Default value = 256)
   :type nfft: int
   :param axis: Axis of input array along which the computation is performed. (Default value = -1)
   :type axis: int
   :param return_onesided: If `True`, return a one-sided spectrum for real data. If
                           `False` return a two-sided spectrum. Defaults to `True`, but for
                           complex data, a two-sided spectrum is always returned.
   :type return_onesided: bool, optional
   :param mode: Which type of spectrum to return (Default value = 'psd')
   :type mode: {'psd', 'magnitude', 'angle', 'phase', 'complex'}
   :param scaling: Selects between computing the power spectral density ('density')
                   where `Pxx` has units of V**2/Hz and computing the power
                   spectrum ('spectrum') where `Pxx` has units of V**2, if `x`
                   is measured in V and `fs` is measured in Hz. Defaults to
                   'density'
   :type scaling: { 'density', 'spectrum' }
   :param fs: Sampling rate of the data
   :type fs: float
   :param fmin: Smallest frequency in desired range (left hand boundary)
   :type fmin: {float, None}
   :param fmax: Largest frequency in desired range (right hand boundary)'
   :type fmax: {float, None}
   :param verbose: String indicating the level of detail to be printed to the screen during computation.'
   :type verbose: {None, 'DEBUG', 'INFO', 'WARNING', 'CRITICAL'}

   :returns: SensorGLMSpectrum instance containing the fitted GLM-Spectrum.
   :rtype: :py:class:`SensorGLMSpectrum <osl_ephys.glm.glm_spectrum.SensorGLMSpectrum>`

   .. rubric:: References

   .. [1] Quinn, A. J., Atkinson, L., Gohil, C., Kohl, O., Pitt, J., Zich, C., Nobre,
      A. C., & Woolrich, M. W. (2022). The GLM-Spectrum: A multilevel framework
      for spectrum analysis with covariate and confound modelling. Cold Spring
      Harbor Laboratory. https://doi.org/10.1101/2022.11.14.516449


.. py:function:: glm_irasa(XX, method='modified', resample_factors=None, aperiodic_average='median', reg_categorical=None, reg_ztrans=None, reg_unitmax=None, contrasts=None, fit_intercept=True, standardise_data=False, window_type='hann', nperseg=None, noverlap=None, nfft=None, detrend='constant', return_onesided=True, scaling='density', mode='psd', fmin=None, fmax=None, axis=-1, fs=1, verbose='WARNING')

   Compute a GLM-IRASA from a MNE-Python Raw data object.

   :param XX: Data to compute GLM-Spectrum from
   :type XX: {MNE Raw object, or data array}
   :param standardise_data: Flag indicating whether to z-transform input data (Default value = False)
   :type standardise_data: bool
   :param reg_categorical: Dictionary of covariate time series to be added as binary regessors. (Default value = None)
   :type reg_categorical: dict or None
   :param reg_ztrans: Dictionary of covariate time series to be added as z-standardised regessors. (Default value = None)
   :type reg_ztrans: dict or None
   :param reg_unitmax: Dictionary of confound time series to be added as positive-valued unitmax regessors. (Default value = None)
   :type reg_unitmax: dict or None
   :param contrasts: Dictionary of contrasts to be computed in the model.
                     (Default value = None, will add a simple contrast for each regressor)
   :type contrasts: dict or None
   :param fit_intercept: Specifies whether a constant valued 'intercept' regressor is included in the model. (Default value = True)'
   :type fit_intercept: bool
   :param method: whether to compute the original implementation of IRASA or the modified update
                  (default is 'modified')
   :type method: {'original', 'modified'}
   :param resample_factors: array of resampling factors to average across or None, in which a set
                            of factors are automatically computed (default is None).
   :type resample_factors: {None, array_like}
   :param aperiodic_average: method for averaging across irregularly resampled spectra to estimate
                             the aperiodic component (default is 'median').'
   :type aperiodic_average: {'mean', 'median', 'median_bias', 'min'}
   :param nperseg: Length of each segment. Defaults to None, but if window is str or
                   tuple, is set to 256, and if window is array_like, is set to the
                   length of the window.
   :type nperseg: int
   :param noverlap: Number of samples that successive sliding windows should overlap.
   :type noverlap: int
   :param window_type: Desired window to use. If `window` is a string or tuple, it is
                       passed to `scipy.signal.windows.get_window` to generate the
                       window values, which are DFT-even by default. See `scipy.signal.windows`
                       for a list of windows and required parameters.
                       If `window` is array_like it will be used directly as the window and its
                       length must be nperseg. Defaults to a Hann window.
   :type window_type: str or tuple or array_like, optional
   :param detrend: Specifies how to detrend each segment. If `detrend` is a
                   string, it is passed as the `type` argument to the `detrend`
                   function. If it is a function, it takes a segment and returns a
                   detrended segment. If `detrend` is `False`, no detrending is
                   done. Defaults to 'constant'.'
   :type detrend: str or function or `False`, optional
   :param nfft: Length of the FFT to use (Default value = 256)
   :type nfft: int
   :param axis: Axis of input array along which the computation is performed. (Default value = -1)
   :type axis: int
   :param return_onesided: If `True`, return a one-sided spectrum for real data. If
                           `False` return a two-sided spectrum. Defaults to `True`, but for
                           complex data, a two-sided spectrum is always returned.
   :type return_onesided: bool, optional
   :param mode: Which type of spectrum to return (Default value = 'psd')
   :type mode: {'psd', 'magnitude', 'angle', 'phase', 'complex'}
   :param scaling: Selects between computing the power spectral density ('density')
                   where `Pxx` has units of V**2/Hz and computing the power
                   spectrum ('spectrum') where `Pxx` has units of V**2, if `x`
                   is measured in V and `fs` is measured in Hz. Defaults to
                   'density'
   :type scaling: { 'density', 'spectrum' }
   :param fs: Sampling rate of the data
   :type fs: float
   :param fmin: Smallest frequency in desired range (left hand boundary)
   :type fmin: {float, None}
   :param fmax: Largest frequency in desired range (right hand boundary)'
   :type fmax: {float, None}
   :param verbose: String indicating the level of detail to be printed to the screen during computation.'
   :type verbose: {None, 'DEBUG', 'INFO', 'WARNING', 'CRITICAL'}

   :returns: SensorGLMSpectrum instance containing the fitted GLM-Spectrum.
   :rtype: :py:class:`SensorGLMSpectrum <osl_ephys.glm.glm_spectrum.SensorGLMSpectrum>`

   .. rubric:: References

   .. [1] Quinn, A. J., Atkinson, L., Gohil, C., Kohl, O., Pitt, J., Zich, C., Nobre,
      A. C., & Woolrich, M. W. (2022). The GLM-Spectrum: A multilevel framework
      for spectrum analysis with covariate and confound modelling. Cold Spring
      Harbor Laboratory. https://doi.org/10.1101/2022.11.14.516449


.. py:function:: read_glm_spectrum(infile)

   Read in a GLMSpectrum object that has been saved as as a pickle.

   :param infile: Filepath of saved object
   :type infile: str

   :returns: **glmsp** -- SensorGLMSpectrum instance containing the fitted GLM-Spectrum.
   :rtype: :py:class:`SensorGLMSpectrum <osl_ephys.glm.glm_spectrum.SensorGLMSpectrum>`


.. py:function:: plot_joint_spectrum_clusters(xvect, psd, clusters, info, ax=None, freqs='auto', base=1, topo_scale='joint', lw=0.5, ylabel='Power', title='', ylim=None, xtick_skip=1, topo_prop=1 / 5, topo_cmap=None, topomap_args=None)

   Plot a GLM-Spectrum contrast from cluster objects, with spatial line colouring and topograpies.

   :param xvect: Frequency vector
   :type xvect: array_like
   :param psd: Spectrum values
   :type psd: array_like
   :param clusters: List of cluster objects
   :type clusters: list
   :param info: MNE-Python info object
   :type info: dict
   :param ax: Axis to plot into (Default value = None)
   :type ax: {None or axis handle}
   :param freqs: Which frequencies to plot topos for (Default value = 'auto')
   :type freqs: {list, tuple or 'auto'}
   :param base: The x-axis scaling, set to 0.5 for sqrt freq axis (Default value = 1)
   :type base: float
   :param topo_scale: Whether to fix topomap colour scales across all topos ('joint') or
                      leave them individual (Default value = 'joint')
   :type topo_scale: {'joint' or None}
   :param lw: Line width(Default value = 0.5)
   :type lw: float
   :param ylabel: Y-axis label(Default value = 'Power')
   :type ylabel: str
   :param title: Plot title(Default value = None)
   :type title: str
   :param ylim: min and max values for y-axis (Default value = None)
   :type ylim: {tuple or list}
   :param xtick_skip: Number of xaxis ticks to skip, useful for tight plots (Default value = 1)
   :type xtick_skip: int
   :param topo_prop: Proportion of plot dedicted to topomaps(Default value = 1/3)
   :type topo_prop: float
   :param topo_cmap: Colormap to use for plotting (Default is 'RdBu_r' if pooled topo data range
                     is positive and negative, otherwise 'Reds' or 'Blues' depending on sign of
                     pooled data range)
   :type topo_cmap: {None or matplotlib colormap}


.. py:function:: plot_source_topo(data_map, parcellation_file=None, mask_file='MNI152_T1_8mm_brain.nii.gz', axis=None, cmap=None, vmin=None, vmax=None, alpha=0.7)

   Plot a data map on a cortical surface. Wrapper for nilearn.plotting.plot_glass_brain.

   :param data_map: Vector of data values to plot (nparc,)
   :type data_map: array_like
   :param parcellation_file: Filepath of parcellation file to plot data on
   :type parcellation_file: str
   :param mask_file: Filepath of mask file to plot data on (Default value = 'MNI152_T1_8mm_brain.nii.gz')
   :type mask_file: str
   :param axis: Axis to plot into (Default value = None)
   :type axis: {None or axis handle}
   :param cmap: Colormap to use for plotting (Default value = None)
   :type cmap: {None or matplotlib colormap}
   :param vmin: Minimum value for colormap (Default value = None)
   :type vmin: {None or float}
   :param vmax: Maximum value for colormap (Default value = None)
   :type vmax: {None or float}
   :param alpha: Alpha value for colormap (Default value = None)
   :type alpha: {None or float}

   :returns: **image** -- AxesImage object
   :rtype: :py:class:`matplotlib.image.AxesImage <matplotlib.image.AxesImage>`


.. py:function:: plot_joint_spectrum(xvect, psd, info, ax=None, freqs='auto', base=1, topo_scale='joint', lw=0.5, ylabel='Power', title='', ylim=None, xtick_skip=1, topo_prop=1 / 5, topo_cmap=None, topomap_args=None)

   Plot a GLM-Spectrum contrast with spatial line colouring and topograpies.

   :param xvect: Vector of frequency values for x-axis
   :type xvect: array_like
   :param psd: Array of spectrum values to plot
   :type psd: array_like
   :param info: MNE-Python info object
   :type info: :py:class:`mne.Info <mne.Info>`
   :param ax: Axis to plot into (Default value = None)
   :type ax: {None or axis handle}
   :param freqs: Which frequencies to plot topos for (Default value = 'auto')
   :type freqs: {list, tuple or 'auto'}
   :param base: The x-axis scaling, set to 0.5 for sqrt freq axis (Default value = 1)
   :type base: float
   :param topo_scale: Whether to fix topomap colour scales across all topos ('joint') or
                      leave them individual (Default value = 'joint')
   :type topo_scale: {'joint' or None}
   :param lw: Line width(Default value = 0.5)
   :type lw: flot
   :param ylabel: Y-axis label(Default value = 'Power')
   :type ylabel: str
   :param title: Plot title(Default value = None)
   :type title: str
   :param ylim: min and max values for y-axis (Default value = None)
   :type ylim: {tuple or list}
   :param xtick_skip: Number of xaxis ticks to skip, useful for tight plots (Default value = 1)
   :type xtick_skip: int
   :param topo_prop: Proportion of plot dedicted to topomaps(Default value = 1/3)
   :type topo_prop: float
   :param topo_cmap: Colormap to use for plotting (Default value is 'RdBu_r' if pooled topo data range
                     is positive and negative, otherwise 'Reds' or 'Blues' depending on sign of
                     pooled data range)
   :type topo_cmap: {None or matplotlib colormap}


.. py:function:: plot_sensor_spectrum(xvect, psd, info, ax=None, sensor_proj=False, xticks=None, xticklabels=None, lw=0.5, title=None, sensor_cols=True, base=1, ylabel=None, xtick_skip=1)

   Plot a GLM-Spectrum contrast with spatial line colouring.

   :param xvect: Vector of frequency values for x-axis
   :type xvect: array_like
   :param psd: Array of spectrum values to plot
   :type psd: array_like
   :param info: Sensor info for spatial map
   :type info: MNE Raw info
   :param ax: Axis to plot into (Default value = None)
   :type ax: {None or axis handle}
   :param sensor_proj: Whether to plot a topomap inset (Default value = False)
   :type sensor_proj: bool
   :param xticks: xtick positions (Default value = None)
   :type xticks: array_like
   :param xticklabels: xtick labels (Default value = None)
   :type xticklabels: array_like of str
   :param lw: Line width(Default value = 0.5)
   :type lw: flot
   :param title: Plot title(Default value = None)
   :type title: str
   :param sensor_cols: Whether to colour lines by sensor (Default value = True)
   :type sensor_cols: bool
   :param base: The x-axis scaling, set to 0.5 for sqrt freq axis (Default value = 1)
   :type base: float
   :param ylabel: Y-axis label(Default value = None)
   :type ylabel: str
   :param xtick_skip: Number of xaxis ticks to skip, useful for tight plots (Default value = 1)
   :type xtick_skip: int


.. py:function:: plot_sensor_proj(info, ax=None, cmap=None)


.. py:function:: plot_sensor_data(xvect, data, info, ax=None, lw=0.5, xticks=None, xticklabels=None, sensor_cols=True, base=1, xtick_skip=1)

   Plot sensor data with spatial line colouring.




.. py:function:: prep_scaled_freq(base, freq_vect)

   Prepare frequency vector for plotting with a given scaling.

   :param base: The x-axis scaling, set to 0.5 for sqrt freq axis (Default value = 1)
   :type base: float
   :param freq_vect: Vector of frequency values for x-axis
   :type freq_vect: array_like

   :returns: * **fx** (*array_like*) -- Scaled frequency vector
             * **ftick** (*array_like*) -- Normal frequency ticks
             * **ftickscaled** (*array_like*) -- Scaled frequency ticks

   .. rubric:: Notes

   Assuming ephy freq ranges for now - around 1-40Hz


.. py:function:: get_source_colors(parcellation_file, cmap='viridis')


.. py:function:: get_mne_sensor_cols(info)

   Get sensor colours from MNE info object.

   :param info: MNE-Python info object
   :type info: :py:class:`mne.Info <mne.Info>`

   :returns: * **colors** (*array_like*) -- Array of RGB values for each sensor
             * **pos** (*array_like*) -- Sensor positions
             * **outlines** (*array_like*) -- Sensor outlines


.. py:function:: plot_channel_layout(ax, info, size=30, marker='o')

   Plot sensor layout.

   :param ax: Axis to plot into
   :type ax: :py:class:`matplotlib.axes <matplotlib.axes>`
   :param info: MNE-Python info object
   :type info: :py:class:`mne.Info <mne.Info>`
   :param size: Size of sensor § (Default value = 30)
   :type size: int
   :param marker: Marker type (Default value = 'o')
   :type marker: str


.. py:function:: plot_with_cols(ax, data, xvect, cols=None, lw=0.5)

   Plot data with spatial line colouring.

   :param ax: Axis to plot into
   :type ax: :py:class:`matplotlib.axes <matplotlib.axes>`
   :param data: Data to plot
   :type data: array_like
   :param xvect: Vector of frequency values for x-axis
   :type xvect: array_like
   :param cols: Array of RGB values for each sensor (Default value = None)
   :type cols: array_like
   :param lw: Line width(Default value = 0.5)
   :type lw: flot


.. py:function:: decorate_spectrum(ax, ylabel='Power')

   Decorate a spectrum plot.

   :param ax: Axis to plot into
   :type ax: :py:class:`matplotlib.axes <matplotlib.axes>`
   :param ylabel: Y-axis label(Default value = 'Power')
   :type ylabel: str


