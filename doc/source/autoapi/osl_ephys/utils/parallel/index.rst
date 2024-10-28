:py:mod:`osl_ephys.utils.parallel`
==================================

.. py:module:: osl_ephys.utils.parallel

.. autoapi-nested-parse::

   Utility functions for parallel processing.



Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   osl_ephys.utils.parallel.dask_parallel_bag



Attributes
~~~~~~~~~~

.. autoapisummary::

   osl_ephys.utils.parallel.osl_logger


.. py:data:: osl_logger

   

.. py:function:: dask_parallel_bag(func, iter_args, func_args=None, func_kwargs=None)

   A maybe more consistent alternative to ``dask_parallel``.

   :param func: The function to run in parallel.
   :type func: function
   :param iter_args: A list of iterables to pass to func.
   :type iter_args: list
   :param func_args: A list of positional arguments to pass to func.
   :type func_args: list, optional
   :param func_kwargs: A dictionary of keyword arguments to pass to func.
   :type func_kwargs: dict, optional

   :returns: **flags** -- A list of return values from func.
   :rtype: list

   .. rubric:: References

   https://docs.dask.org/en/stable/bag.html


