:py:mod:`osl_ephys.source_recon.rhino.fsl_utils`
================================================

.. py:module:: osl_ephys.source_recon.rhino.fsl_utils

.. autoapi-nested-parse::

   Wrappers for fsleyes.



Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   osl_ephys.source_recon.rhino.fsl_utils.setup_fsl
   osl_ephys.source_recon.rhino.fsl_utils.check_fsl
   osl_ephys.source_recon.rhino.fsl_utils.fsleyes
   osl_ephys.source_recon.rhino.fsl_utils.fsleyes_overlay



.. py:function:: setup_fsl(directory)

   Setup FSL.

   :param directory: Path to FSL installation.
   :type directory: str


.. py:function:: check_fsl()

   Check FSL is installed.


.. py:function:: fsleyes(image_list)

   Displays list of niftii's using external command line call to fsleyes.

   :param image_list: Niftii filenames or tuple of niftii filenames
   :type image_list: string | tuple of strings

   .. rubric:: Examples

   fsleyes(image)
   fsleyes((image1, image2))


.. py:function:: fsleyes_overlay(background_img, overlay_img)

   Displays overlay_img and background_img using external command line call to fsleyes.

   :param background_img: Background niftii filename
   :type background_img: string
   :param overlay_img: Overlay niftii filename
   :type overlay_img: string


