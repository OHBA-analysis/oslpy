:py:mod:`osl_ephys.utils.spmio._data`
=====================================

.. py:module:: osl_ephys.utils.spmio._data

.. autoapi-nested-parse::

   Classes relating to the format and storage of MEEG data and sensors.



Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   osl_ephys.utils.spmio._data.Data
   osl_ephys.utils.spmio._data.Channel
   osl_ephys.utils.spmio._data.Montage




Attributes
~~~~~~~~~~

.. autoapisummary::

   osl_ephys.utils.spmio._data.KNOWN_DTYPEIDS
   osl_ephys.utils.spmio._data.chan_types


.. py:data:: KNOWN_DTYPEIDS

   

.. py:class:: Data(fname, dim, dtype, be, offset, pos, scl_slope, scl_inter, permission)


   .. py:method:: __repr__()

      Return repr(self).



.. py:data:: chan_types

   

.. py:class:: Channel(bad=None, label=None, type_=None, x=None, y=None, units=None)


   .. py:method:: from_dict(channel_dict)
      :classmethod:


   .. py:method:: __repr__()

      Return repr(self).



.. py:class:: Montage(name=None, tra=None, labelnew=None, labelorg=None, channels=None)


   .. py:method:: apply(data)



