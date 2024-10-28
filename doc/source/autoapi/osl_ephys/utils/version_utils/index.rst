:py:mod:`osl_ephys.utils.version_utils`
=======================================

.. py:module:: osl_ephys.utils.version_utils


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   osl_ephys.utils.version_utils._parse_condition
   osl_ephys.utils.version_utils.check_version



Attributes
~~~~~~~~~~

.. autoapisummary::

   osl_ephys.utils.version_utils.osl_logger


.. py:data:: osl_logger

   

.. py:function:: _parse_condition(cond)

   Parse strings defining conditional statements.

   Borrowed from EMD package


.. py:function:: check_version(test_statement, mode='warn')

   Check whether the version of a package meets a specified condition.

   :param test_statement: Package version comparison string in the standard format expected by python installs.
                          eg 'osl-ephys<1.0.0' or 'osl-ephys==0.6.dev0'
   :type test_statement: str
   :param mode: Flag indicating whether to warn the user or raise an error if the comparison fails
   :type mode: {'warn', 'assert'}


