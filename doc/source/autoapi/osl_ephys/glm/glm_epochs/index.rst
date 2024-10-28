:py:mod:`osl_ephys.glm.glm_epochs`
==================================

.. py:module:: osl_ephys.glm.glm_epochs


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   osl_ephys.glm.glm_epochs.GLMEpochsResult
   osl_ephys.glm.glm_epochs.GroupGLMEpochs



Functions
~~~~~~~~~

.. autoapisummary::

   osl_ephys.glm.glm_epochs.glm_epochs
   osl_ephys.glm.glm_epochs.group_glm_epochs
   osl_ephys.glm.glm_epochs.read_mne_epochs
   osl_ephys.glm.glm_epochs.read_glm_epochs



.. py:class:: GLMEpochsResult(model, design, info, tmin=0, data=None, times=None)


   Bases: :py:obj:`osl_ephys.glm.glm_base.GLMBaseResult`

   A class for first-level GLM-Spectra fitted to MNE-Python Epochs objects

   .. py:method:: save_pkl(outname, overwrite=True, save_data=False)

      Save GLM-Epochs result to a pickle file.

      :param outname: Filename or full file path to write pickle to
      :type outname: str
      :param overwrite: Overwrite previous file if one exists? (Default value = True)
      :type overwrite: bool
      :param save_data: Save epochs data in pickle? This is omitted by default to save disk
                        space (Default value = False)
      :type save_data: bool


   .. py:method:: get_evoked_contrast(contrast=0, metric='copes')

      Get the evoked response for a given contrast.

      :param contrast: Contrast index to return
      :type contrast: int
      :param metric: Which metric to plot (Default value = 'copes')
      :type metric: {'copes', or 'tsats'}

      :returns: The evoked response for the contrast.
      :rtype: :py:class:`mne.Evoked <mne.Evoked>`


   .. py:method:: plot_joint_contrast(contrast=0, metric='copes', title=None)

      Plot the evoked response for a given contrast.

      :param contrast: Contrast index to return
      :type contrast: int
      :param metric: Which metric to plot (Default value = 'copes')
      :type metric: {'copes', or 'tsats'}
      :param title: Title for the plot
      :type title: str



.. py:class:: GroupGLMEpochs(model, design, info, config, fl_contrast_names=None, data=None, tmin=0, times=None)


   Bases: :py:obj:`osl_ephys.glm.glm_base.GroupGLMBaseResult`

   A class for group level GLM-Spectra fitted across mmultiple first-level
   GLM-Spectra computed from MNE-Python Raw objects

   .. py:method:: get_evoked_contrast(gcontrast=0, fcontrast=0, metric='copes')

      Get the evoked response for a given contrast.

      :param contrast: Contrast index to return
      :type contrast: int
      :param metric: Which metric to plot (Default value = 'copes')
      :type metric: {'copes', or 'tsats'}

      :returns: The evoked response for the contrast.
      :rtype: :py:class:`mne.Evoked <mne.Evoked>`


   .. py:method:: plot_joint_contrast(gcontrast=0, fcontrast=0, metric='copes', title=None, joint_args=None)

      Plot the evoked response for a given contrast.

      :param contrast: Contrast index to return
      :type contrast: int
      :param metric: Which metric to plot (Default value = 'copes')
      :type metric: {'copes', or 'tsats'}
      :param title: Title for the plot
      :type title: str


   .. py:method:: get_fl_contrast(fl_con)

      Get the data from a single first level contrast.

      :param fl_con: First level contrast data index to return
      :type fl_con: int

      :rtype: :py:class:`GLMEpochsResult <glmtools.glm_epochs.GLMEpochsResult>`  instance containing a single first level contrast.


   .. py:method:: save_pkl(outname, overwrite=True, save_data=False)

      Save GLM-Epochs result to a pickle file.

      :param outname: Filename or full file path to write pickle to
      :type outname: str
      :param overwrite: Overwrite previous file if one exists? (Default value = True)
      :type overwrite: bool
      :param save_data: Save epochs data in pickle? This is omitted by default to save disk
                        space (Default value = False)
      :type save_data: bool



.. py:function:: glm_epochs(config, epochs)

   Compute a GLM-Epochs from an MNE-Python Epochs object.

   :param config: The design specification for the model
   :type config: glmtools.design.DesignConfig
   :param epochs: The epochs object to use for the model
   :type epochs: str, :py:class:`mne.Epochs <mne.Epochs>`

   :rtype: :py:class:`GLMEpochsResult <glmtools.glm_epochs.GLMEpochsResult>`


.. py:function:: group_glm_epochs(inspectra, design_config=None, datainfo=None, metric='copes', baseline=None)

   Compute a group GLM-Epochs from a set of first-level GLM-Epochs.

   :param inspectra: A list containing either the filepaths of a set of saved GLM-Epochs
                     objects, or the GLM-Epochs objects themselves.
   :type inspectra: list, tuple
   :param design_config: The design specification for the group level model (Default value = None)
   :type design_config: glmtools.design.DesignConfig
   :param datainfo: Dictionary of data values to use as covariates. The length of each
                    covariate must match the number of input GLM-Epochs (Default value =
                    None)
   :type datainfo: dict
   :param metric: Which metric to plot (Default value = 'copes')
   :type metric: {'copes', or 'tsats'}

   :rtype: :py:class:`GroupGLMEpochs <glmtools.glm_epochs.GroupGLMEpochs>`


.. py:function:: read_mne_epochs(X, picks=None)

   Read in an MNE-Python Epochs object and convert it to a GLM data object.

   :param X: The epochs object to use for the model
   :type X: str, :py:class:`mne.Epochs <mne.Epochs>`
   :param picks: List of channels to use for the model (Default value = None)
   :type picks: list

   :returns: The data object used to fit the model.
   :rtype: :py:class:`glmtools.data.TrialGLMData <glmtools.data.TrialGLMData>`


.. py:function:: read_glm_epochs(infile)

   Read in a GLMEpochs object that has been saved as as a pickle.

   :param infile: Filepath of saved object
   :type infile: str

   :rtype: :py:class:`GLMEpochsResult <glmtools.glm_epochs.GLMEpochsResult>`


