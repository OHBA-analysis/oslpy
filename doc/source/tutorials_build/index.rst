:orphan:

Welcome to the osl tutorials
============================

The following tutorials illustrate basic usage and analysis that can be done with osl.
For the tutorials we will use the publicly available multimodal dataset (Wakeman & Henson, 2014). 
This dataset contains simultaneous MEG, EEG, (and fMRI) data from 19 subjects (6 sessions each) 
performing a simple visual task. Subject were watching pictures of famous, unfamiliar, and scrambled
faces. They had to indicate whether the picture was symettrical or not.


Preprocessing
=============


.. raw:: html

    <div class="sphx-glr-thumbnails">

.. thumbnail-parent-div-open

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="In this tutorial we will use the config that we created in the previous tutorial for batch processing all data in one call (it should be located in Preprocessing/config.yaml - if not, you can download it here. We will also explore how you could use multiple cores of your computer to parallelize the computations. This tutorial looks as follows:">

.. only:: html

  .. image:: /tutorials_build/images/thumb/sphx_glr_preprocessing_batch_thumb.png
    :alt:

  :ref:`sphx_glr_tutorials_build_preprocessing_batch.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Batch preprocessing and parallelization</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="What is coregistration??    In MEG/EEG analysis we have a number of coordinate systems including:    MEG (Device) space - defined with respect to  the MEG dewar.  Polhemus (Head) space - defined with respect to the locations of the fiducial locations (LPA, RPA and Nasion). The fiducial locations in polhemus space are typically acquired prior to the MEG scan, using a polhemus device.  sMRI (Native) space - defined with respect to the structural MRI scan.  MNI space - defined with respect to the MNI standard space brain.   In order to compute foward models and carry out source reconstruction we need to have all of the necessary things (MEG sensors, dipoles, scalp surface etc.) in a common coordinate space. However, prior to coregistration, this is not the case. For example, we only have the MEG sensors located in MEG (device) space.   Coregistration is the process of learning a mapping between each pair of coordinate systems. To do this, we make use of landmarks (these act as a kind of Rosetta stone) whose locations are known in two different coordinate systems. Knowing where these landmarks are in two coordinate systems allows us to learn a mapping between the coordinate systems.   For example, the fiducials (LPA, RPA and Nasion) are known in both sMRI (Native) space and Polhemus (Head) space, and provide the information we need to learn a linear (affine) transform betwen sMRI (Native) space and Polhemus (Head) space.   The different landmarks, and the coordinate systems they are known in prior to coregistration, are summarised here:">

.. only:: html

  .. image:: /tutorials_build/images/thumb/sphx_glr_source-recon_coreg_thumb.png
    :alt:

  :ref:`sphx_glr_tutorials_build_source-recon_coreg.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Coregistration</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="In this tutorial, we will step through how to do source reconstruction (and parcellation) on a single session of data from a subject in the Wakeman-Henson task MEG dataset. This is a public dataset consisting of 19 healthy individuals who performed a simple visual perception task. See Wakeman &amp; Henson for more details.   The steps we will follow are:   1. Downloading the data from OSF 2. Setup file names 3. Compute surfaces, perform coregistration, and compute forward model using batching 4. Temporal Filtering 5. Compute beamformer weights 6. Apply beamformer weights 7. Parcellation 8. Epoching">

.. only:: html

  .. image:: /tutorials_build/images/thumb/sphx_glr_source-recon_subject_thumb.png
    :alt:

  :ref:`sphx_glr_tutorials_build_source-recon_subject.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Single Subject Source Reconstruction Tutorial</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="One cause of bad co-registrations can be due to the presence of  misleading or erroneous headshape points. These can be caused by errors in the recording of the headshape points when the experimenter was using the polhemus system.">

.. only:: html

  .. image:: /tutorials_build/images/thumb/sphx_glr_source-recon_deleting-headshape-points_thumb.png
    :alt:

  :ref:`sphx_glr_tutorials_build_source-recon_deleting-headshape-points.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Deleting Headshape Points</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="In this tutorial we will move the preprocessing pipeline that we built in the first tutorial to a osl-ephys config. The config is the most concise way to represent a full pipeline, and can be easily shared with other researchers. This tutorial looks as follows:">

.. only:: html

  .. image:: /tutorials_build/images/thumb/sphx_glr_preprocessing_automatic_thumb.png
    :alt:

  :ref:`sphx_glr_tutorials_build_preprocessing_automatic.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Automatic preprocessing using an osl-ephys config</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="In this tutorial we will build a preprocessing pipeline using functions from MNE-Python and osl-ephys. Both packages can be used for MEG and EEG data analysis, irrespective of the manufacturer of the recording equipment.  From our experience, preprocessing pipelines are rarely directly generalizable between different datasets. This can be due to different study designs, different sources of noise, different study populations, etc. As such, we recommend to always interact with your data initially.  This can for example be done by applying preprocessing steps one by one and visualising the data each time to see what effects every step has on your data. In this section we will do just that; starting from the raw data.">

.. only:: html

  .. image:: /tutorials_build/images/thumb/sphx_glr_preprocessing_manual_thumb.png
    :alt:

  :ref:`sphx_glr_tutorials_build_preprocessing_manual.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Manual preprocessing in Python with MNE-Python and osl-ephys</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="GLM-Spectrum with MEG Data">

.. only:: html

  .. image:: /tutorials_build/images/thumb/sphx_glr_glm_sensor_thumb.png
    :alt:

  :ref:`sphx_glr_tutorials_build_glm_sensor.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">GLM-Spectrum with MEG Data</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Frequency-domain analyses of oscillations in electrophysiological recordings of brain activity contain information about rhythms in the underlying neuronal activity. Many aspects of these rhythms are of interest to neuroscientists studying EEG and MEG time series. Many advanced methods for spectrum estimation have been developed in recent years, but the core approach has been the same for many years.">

.. only:: html

  .. image:: /tutorials_build/images/thumb/sphx_glr_glm_simulation_thumb.png
    :alt:

  :ref:`sphx_glr_tutorials_build_glm_simulation.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Frequency Spectrum Estimation - Simulations & General Linear Models</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="In this tutorial, we will perform a group analysis of parcellated source-space task MEG data using the Wakeman-Henson dataset. This is a public dataset consisting of 19 healthy individuals who performed a simple visual perception task. See Wakeman &amp; Henson (2015) for more details.">

.. only:: html

  .. image:: /tutorials_build/images/thumb/sphx_glr_source-recon_batch_thumb.png
    :alt:

  :ref:`sphx_glr_tutorials_build_source-recon_batch.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Group Analysis of Source-space Data</div>
    </div>


.. thumbnail-parent-div-close

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /tutorials_build/preprocessing_batch
   /tutorials_build/source-recon_coreg
   /tutorials_build/source-recon_subject
   /tutorials_build/source-recon_deleting-headshape-points
   /tutorials_build/preprocessing_automatic
   /tutorials_build/preprocessing_manual
   /tutorials_build/glm_sensor
   /tutorials_build/glm_simulation
   /tutorials_build/source-recon_batch


.. only:: html

  .. container:: sphx-glr-footer sphx-glr-footer-gallery

    .. container:: sphx-glr-download sphx-glr-download-python

      :download:`Download all examples in Python source code: tutorials_build_python.zip </tutorials_build/tutorials_build_python.zip>`

    .. container:: sphx-glr-download sphx-glr-download-jupyter

      :download:`Download all examples in Jupyter notebooks: tutorials_build_jupyter.zip </tutorials_build/tutorials_build_jupyter.zip>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
