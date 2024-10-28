:py:mod:`osl_ephys.utils.simulation_config.simulate`
====================================================

.. py:module:: osl_ephys.utils.simulation_config.simulate


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   osl_ephys.utils.simulation_config.simulate.simulate_data
   osl_ephys.utils.simulation_config.simulate.simulate_raw_from_template
   osl_ephys.utils.simulation_config.simulate.simulate_rest_mvar



.. py:function:: simulate_data(model, num_samples=1000, num_realisations=1, use_cov=True)


.. py:function:: simulate_raw_from_template(sim_samples, bad_segs=None)


.. py:function:: simulate_rest_mvar(raw, sim_samples, mvar_pca=32, mvar_order=12, picks=None, modalities=None, drop_dig=False)

   Best used on low sample rate data <200Hz. fiff only for now.


