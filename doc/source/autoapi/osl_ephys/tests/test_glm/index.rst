:py:mod:`osl_ephys.tests.test_glm`
==================================

.. py:module:: osl_ephys.tests.test_glm

.. autoapi-nested-parse::

   Tests for glm_spectrum and glm_epochs



Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   osl_ephys.tests.test_glm.TestGLMSpectrum




.. py:class:: TestGLMSpectrum(methodName='runTest')


   Bases: :py:obj:`unittest.TestCase`

   A class whose instances are single test cases.

   By default, the test code itself should be placed in a method named
   'runTest'.

   If the fixture may be used for many test cases, create as
   many test methods as are needed. When instantiating such a TestCase
   subclass, specify in the constructor arguments the name of the test method
   that the instance is to execute.

   Test authors should subclass TestCase for their own tests. Construction
   and deconstruction of the test's environment ('fixture') can be
   implemented by overriding the 'setUp' and 'tearDown' methods respectively.

   If it is necessary to override the __init__ method, the base class
   __init__ method must always be called. It is important that subclasses
   should not change the signature of their __init__ method, since instances
   of the classes are instantiated automatically by parts of the framework
   in order to be run.

   When subclassing TestCase, you can set these attributes:
   * failureException: determines which exception will be raised when
       the instance's assertion methods fail; test methods raising this
       exception will be deemed to have 'failed' rather than 'errored'.
   * longMessage: determines whether long messages (including repr of
       objects used in assert methods) will be printed on failure in *addition*
       to any explicit message passed.
   * maxDiff: sets the maximum length of a diff in failure messages
       by assert methods using difflib. It is looked up as an instance
       attribute so can be configured by individual tests if required.

   .. py:method:: setUpClass()
      :classmethod:

      Hook method for setting up class fixture before running tests in the class.


   .. py:method:: tearDownClass()
      :classmethod:

      Hook method for deconstructing the class fixture after running all tests in the class.


   .. py:method:: test_glm_spectrum()


   .. py:method:: test_glm_irasa()



