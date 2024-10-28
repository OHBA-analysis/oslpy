:py:mod:`osl_ephys.glm.glm_base`
================================

.. py:module:: osl_ephys.glm.glm_base


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   osl_ephys.glm.glm_base.GLMBaseResult
   osl_ephys.glm.glm_base.GroupGLMBaseResult
   osl_ephys.glm.glm_base.BaseSensorPerm
   osl_ephys.glm.glm_base.SensorMaxStatPerm
   osl_ephys.glm.glm_base.SensorClusterPerm



Functions
~~~~~~~~~

.. autoapisummary::

   osl_ephys.glm.glm_base.plot_joint_clusters
   osl_ephys.glm.glm_base.plot_sensor_erp
   osl_ephys.glm.glm_base.plot_sensor_proj
   osl_ephys.glm.glm_base.plot_sensor_data
   osl_ephys.glm.glm_base.get_mne_sensor_cols
   osl_ephys.glm.glm_base.decorate_spectrum
   osl_ephys.glm.glm_base.get_source_colors
   osl_ephys.glm.glm_base.plot_channel_layout
   osl_ephys.glm.glm_base.plot_with_cols
   osl_ephys.glm.glm_base.plot_source_topo



.. py:class:: GLMBaseResult(model, design, info, data=None)


   A class for GLM-Epochs fitted to MNE-Python Raw objects.

   .. py:method:: save_pkl(outname, overwrite=True, save_data=False)

      Save GLM-Epochs result to a pickle file.

      :param outname: Filename or full file path to write pickle to
      :type outname: str
      :param overwrite: Overwrite previous file if one exists? (Default value = True)
      :type overwrite: bool
      :param save_data: Save epoch data in pickle? This is omitted by default to save disk
                        space (Default value = False)
      :type save_data: bool



.. py:class:: GroupGLMBaseResult(model, design, info, config, fl_contrast_names=None, data=None)


   A class for group level GLM-Epochs fitted across mmultiple first-level
   GLM-Epochs computed from MNE-Python Raw objects

   .. py:method:: get_channel_adjacency(dist=40)

      Return adjacency matrix of channels.

      :param dist: Distance in mm between parcel centroids to consider neighbours.
                   Only used if data is parcellated.
      :type dist: float

      :returns: * **adjacency** (*scipy.sparse.csr_matrix*) -- The adjacency matrix.
                * **ch_names** (*list of str*) -- The channel names.



.. py:class:: BaseSensorPerm


   A base class for sensor x frequency and sensor x time permutation tests computed from a
   group level GLM-Spectrum.

   .. py:method:: save_pkl(outname, overwrite=True, save_data=False)

      Save GLM-Epochs result to a pickle file.

      :param outname: Filename or full file path to write pickle to
      :type outname: str
      :param overwrite: Overwrite previous file if one exists? (Default value = True)
      :type overwrite: bool
      :param save_data: Save epoch data in pickle? This is omitted by default to save disk
                        space (Default value = False)
      :type save_data: bool



.. py:class:: SensorMaxStatPerm(glmsp, gl_con, fl_con=0, nperms=1000, tstat_args=None, metric='tstats', nprocesses=1, pooled_dims=(1, 2), tmin=None, tmax=None, fmin=None, fmax=None, picks=None)


   Bases: :py:obj:`BaseSensorPerm`

   A class holding the result for sensor x frequency or sensor x time max-stat permutation test computed
   from a group level GLM-Spectrum or GLM-Epochs

   .. py:method:: get_sig_clusters(thresh)

      Return the significant clusters at a given threshold.

      :param thresh: The threshold to consider a cluster significant eg 95 or 99
      :type thresh: float

      :returns: * *clusters* -- A list containing the significant clusters. Each list item contains
                  a tuple of three items - the cluster statistic, the cluster
                  percentile relative to the null and the spatial/spectral indices of
                  the cluster.
                * *obs_stat* -- The observed statistic.


   .. py:method:: plot_sig_clusters(thresh, ax=None, min_extent=1)

      Plot the significant clusters at a given threshold.

      :param thresh: The threshold to consider a cluster significant eg 95 or 99
      :type thresh: float
      :param ax: Matplotlib axes to plot on. (Default value = None)
      :type ax: :py:class:`matplotlib.axes <matplotlib.axes>`



.. py:class:: SensorClusterPerm(glmsp, gl_con, fl_con=0, nperms=1000, cluster_forming_threshold=3, tstat_args=None, metric='tstats', tmin=None, tmax=None, fmin=None, fmax=None, picks=None, nprocesses=1)


   Bases: :py:obj:`BaseSensorPerm`

   A class holding the result for sensor x frequency or sensor x time cluster stats computed
   from a group level GLM-Spectrum or GLM-Epochs

   .. py:method:: get_sig_clusters(thresh)

      Return the significant clusters at a given threshold.

      :param thresh: The threshold to consider a cluster significant eg 95 or 99
      :type thresh: float

      :returns: * *clusters* -- A list containing the significant clusters. Each list item contains
                  a tuple of three items - the cluster statistic, the cluster
                  percentile relative to the null and the spatial/spectral indices of
                  the cluster.
                * *obs_stat* -- The observed statistic.


   .. py:method:: plot_sig_clusters(thresh, ax=None, min_extent=1)

      Plot the significant clusters at a given threshold.

      :param thresh: The threshold to consider a cluster significant eg 95 or 99
      :type thresh: float
      :param ax: Matplotlib axes to plot on. (Default value = None)
      :type ax: :py:class:`matplotlib.axes <matplotlib.axes>`



.. py:function:: plot_joint_clusters(xvect, erp, clusters, info, ax=None, times='auto', topo_scale='joint', lw=0.5, ylabel='Power', title='', ylim=None, xtick_skip=1, topo_prop=1 / 5, topo_cmap=None, topomap_args=None)

   Plot a GLM-Epochs contrast from cluster objects, with spatial line colouring and topograpies.

   :param xvect: Time vector
   :type xvect: array_like
   :param erp: epochs values
   :type erp: array_like
   :param clusters: List of cluster objects
   :type clusters: list
   :param info: MNE-Python info object
   :type info: dict
   :param ax: Axis to plot into (Default value = None)
   :type ax: {None or axis handle}
   :param times: Which times to plot topos for (Default value = 'auto')
   :type times: {list, tuple or 'auto'}
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


.. py:function:: plot_sensor_erp(xvect, erp, info, ax=None, sensor_proj=False, xticks=None, xticklabels=None, lw=0.5, title=None, sensor_cols=True, ylabel=None, xtick_skip=1)

   Plot a GLM-Spectrum contrast with spatial line colouring.

   :param xvect: Vector of time values for x-axis
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
   :param ylabel: Y-axis label(Default value = None)
   :type ylabel: str
   :param xtick_skip: Number of xaxis ticks to skip, useful for tight plots (Default value = 1)
   :type xtick_skip: int


.. py:function:: plot_sensor_proj(info, ax=None, cmap=None)


.. py:function:: plot_sensor_data(xvect, data, info, ax=None, lw=0.5, xticks=None, xticklabels=None, sensor_cols=True, xtick_skip=1)

   Plot sensor data with spatial line colouring.




.. py:function:: get_mne_sensor_cols(info)

   Get sensor colours from MNE info object.

   :param info: MNE-Python info object
   :type info: :py:class:`mne.Info <mne.Info>`

   :returns: * **colors** (*array_like*) -- Array of RGB values for each sensor
             * **pos** (*array_like*) -- Sensor positions
             * **outlines** (*array_like*) -- Sensor outlines


.. py:function:: decorate_spectrum(ax, ylabel='Amplitude')

   Decorate a spectrum plot.

   :param ax: Axis to plot into
   :type ax: :py:class:`matplotlib.axes <matplotlib.axes>`
   :param ylabel: Y-axis label(Default value = 'Power')
   :type ylabel: str


.. py:function:: get_source_colors(parcellation_file, cmap='viridis')


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
   :param xvect: Vector of time values for x-axis
   :type xvect: array_like
   :param cols: Array of RGB values for each sensor (Default value = None)
   :type cols: array_like
   :param lw: Line width(Default value = 0.5)
   :type lw: flot


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


