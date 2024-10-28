:py:mod:`osl_ephys.utils.spmio._events`
=======================================

.. py:module:: osl_ephys.utils.spmio._events

.. autoapi-nested-parse::

   Classes relating to the format and storage of MEEG events and trials.



Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   osl_ephys.utils.spmio._events.Trial
   osl_ephys.utils.spmio._events.Event




Attributes
~~~~~~~~~~

.. autoapisummary::

   osl_ephys.utils.spmio._events._logger


.. py:data:: _logger

   

.. py:class:: Trial(label, events, onset, bad, tag, repl, sample_frequency=None)


   .. py:property:: types


   .. py:property:: values


   .. py:property:: durations


   .. py:property:: times


   .. py:property:: offsets


   .. py:property:: end_times


   .. py:property:: samples


   .. py:property:: end_samples


   .. py:property:: good_samples


   .. py:property:: good_end_samples


   .. py:property:: trial_starts


   .. py:method:: calculate_samples(sample_frequency)


   .. py:method:: _event_property(property_)


   .. py:method:: _set_event_property(property_, values)



.. py:class:: Event(type_, value, duration, time, offset)


   .. py:method:: from_dict(event_dict)
      :classmethod:


   .. py:method:: to_dict()


   .. py:method:: __repr__()

      Return repr(self).



