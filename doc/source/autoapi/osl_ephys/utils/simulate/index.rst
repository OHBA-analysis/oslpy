:py:mod:`osl_ephys.utils.simulate`
==================================

.. py:module:: osl_ephys.utils.simulate

.. autoapi-nested-parse::

   Utility functions for simulating data.



Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   osl_ephys.utils.simulate.simulate_data
   osl_ephys.utils.simulate.simulate_raw_from_template
   osl_ephys.utils.simulate.simulate_rest_mvar



Attributes
~~~~~~~~~~

.. autoapisummary::

   osl_ephys.utils.simulate.fname


.. py:function:: simulate_data(model, num_samples=1000, num_realisations=1, use_cov=True, noise=None)

   Simulate data from a linear model.

   :param model: A linear model object.
   :type model: sails.AbstractLinearModel
   :param num_samples: The number of samples to simulate.
   :type num_samples: int
   :param num_realisations: The number of realisations to simulate.
   :type num_realisations: int
   :param use_cov: Whether to use the residual covariance matrix.
   :type use_cov: bool

   :returns: **Y** -- The simulated data.
   :rtype: ndarray, shape (num_sources, num_samples, num_realisations)


.. py:function:: simulate_raw_from_template(sim_samples, bad_segments=None, bad_channels=None, flat_channels=None, noise=None)

   Simulate raw MEG data from a 306-channel MEGIN template.

   :param sim_samples: The number of samples to simulate.
   :type sim_samples: int
   :param bad_segments: The bad segments to simulate.
   :type bad_segments: list of tuples
   :param bad_channels: The bad channels to simulate.
   :type bad_channels: list of ints
   :param flat_channels: The flat channels to simulate.
   :type flat_channels: list of ints

   :returns: **sim** -- The simulated data.
   :rtype: :py:class:`mne.io.Raw <mne.io.Raw>`


.. py:function:: simulate_rest_mvar(raw, sim_samples, mvar_pca=32, mvar_order=12, picks=None, modalities=None, drop_dig=False)

   Simulate resting state data from a raw object using a reduced MVAR model.

   :param raw: The raw object to simulate from.
   :type raw: :py:class:`mne.io.Raw <mne.io.Raw>`
   :param sim_samples: The number of samples to simulate.
   :type sim_samples: int
   :param mvar_pca: The number of PCA components to use.
   :type mvar_pca: int
   :param mvar_order: The MVAR model order.
   :type mvar_order: int
   :param picks: The picks to use. See :py:func:`mne.pick_types <mne.pick_types>`.
   :type picks: dict
   :param modalities: The modalities to use. See :py:func:`mne.pick_types <mne.pick_types>`.
   :type modalities: list of str
   :param drop_dig: Whether to drop the digitisation points.
   :type drop_dig: bool

   :returns: **sim** -- The simulated data.
   :rtype: :py:class:`mne.io.Raw <mne.io.Raw>`

   .. rubric:: Notes

   Best used on low sample rate data <200Hz. fiff only for now.


.. py:data:: fname
   :value: '/Users/andrew/Projects/ntad/raw_data/meeg_pilots/NTAD_Neo_Pilot2_RSO.fif'

   

