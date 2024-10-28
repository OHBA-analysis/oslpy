:py:mod:`osl_ephys.utils.spmio`
===============================

.. py:module:: osl_ephys.utils.spmio


Submodules
----------
.. toctree::
   :titlesonly:
   :maxdepth: 1

   _data/index.rst
   _events/index.rst
   _spmmeeg_utils/index.rst
   spmmeeg/index.rst


Package Contents
----------------

Classes
~~~~~~~

.. autoapisummary::

   osl_ephys.utils.spmio.SPMMEEG




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



