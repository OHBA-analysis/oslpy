:py:mod:`osl_ephys.utils.package`
=================================

.. py:module:: osl_ephys.utils.package


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   osl_ephys.utils.package.soft_import
   osl_ephys.utils.package.run_package_tests



Attributes
~~~~~~~~~~

.. autoapisummary::

   osl_ephys.utils.package.logger


.. py:data:: logger

   

.. py:function:: soft_import(package)

   Try to import a package raising friendly error if not present.


.. py:function:: run_package_tests()

   Run OSL tests from within python

   https://docs.pytest.org/en/7.1.x/how-to/usage.html

   .. rubric:: Notes

   Calling pytest.main() will result in importing your tests and any modules
   that they import. Due to the caching mechanism of python’s import system,
   making subsequent calls to pytest.main() from the same process will not
   reflect changes to those files between the calls. For this reason, making
   multiple calls to pytest.main() from the same process
   (in order to re-run tests, for example) is not recommended.


