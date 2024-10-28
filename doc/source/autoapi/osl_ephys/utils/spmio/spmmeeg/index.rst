:py:mod:`osl_ephys.utils.spmio.spmmeeg`
=======================================

.. py:module:: osl_ephys.utils.spmio.spmmeeg

.. autoapi-nested-parse::

   Classes for loading SPM files.



Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   osl_ephys.utils.spmio.spmmeeg.SPMMEEG
   osl_ephys.utils.spmio.spmmeeg.TrialParameters



Functions
~~~~~~~~~

.. autoapisummary::

   osl_ephys.utils.spmio.spmmeeg._get_trial_trigger_value



.. py:class:: SPMMEEG(filename)


   .. py:property:: size


   .. py:property:: chantype


   .. py:property:: n_good_samples


   .. py:method:: get_data(montage=None)

      Return memorymapped data and optionally apply a montage.


   .. py:method:: epoch_data(data)


   .. py:method:: define_trial(event_type, pre_stim, post_stim)


   .. py:method:: mark_artefacts_as_bad()


   .. py:method:: _channel_property(property_)


   .. py:method:: full_index(channel_type)


   .. py:method:: reindex_good_samples()


   .. py:method:: reindex_event_samples()


   .. py:method:: print_info()


   .. py:method:: _find_dat_file()


   .. py:method:: indchantype(channel_type)


   .. py:method:: indsample(t)


   .. py:method:: indtrial(cond)



.. py:function:: _get_trial_trigger_value(t)

   Return value of first STI event in trial.


.. py:class:: TrialParameters


   .. py:attribute:: event_type
      :type: str

      

   .. py:attribute:: pre_stim
      :type: float

      

   .. py:attribute:: post_stim
      :type: float

      


