:py:mod:`osl_ephys.utils.logger`
================================

.. py:module:: osl_ephys.utils.logger

.. autoapi-nested-parse::

   Logging module for OSL

   Heavily inspired by logging in OSL.



Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   osl_ephys.utils.logger.set_up
   osl_ephys.utils.logger.set_level
   osl_ephys.utils.logger.get_level
   osl_ephys.utils.logger.log_or_print



Attributes
~~~~~~~~~~

.. autoapisummary::

   osl_ephys.utils.logger.osl_logger
   osl_ephys.utils.logger.default_config


.. py:data:: osl_logger

   

.. py:data:: default_config
   :value: Multiline-String

    .. raw:: html

        <details><summary>Show Value</summary>

    .. code-block:: python

        """
        version: 1
        loggers:
          osl:
            level: DEBUG
            handlers: [console, file]
            propagate: false
        
        handlers:
          console:
            class : logging.StreamHandler
            formatter: brief
            level   : DEBUG
            stream  : ext://sys.stdout
          file:
            class : logging.handlers.RotatingFileHandler
            formatter: verbose
            filename: {log_file}
            backupCount: 3
            maxBytes: 102400
        
        formatters:
          brief:
            format: '{prefix} %(message)s'
          default:
            format: '[%(asctime)s] {prefix} %(levelname)-8s : %(message)s'
            datefmt: '%H:%M:%S'
          verbose:
            format: '[%(asctime)s] {prefix} - %(levelname)s - osl-ephys.%(module)s:%(lineno)s : %(message)s'
            datefmt: '%Y-%m-%d %H:%M:%S'
        
        disable_existing_loggers: true
        
        """

    .. raw:: html

        </details>

   

.. py:function:: set_up(prefix='', log_file=None, level=None, console_format=None, startup=True)

   Initialise the osl-ephys module osl_logger.

   :param prefix: Optional prefix to attach to osl_logger output
   :type prefix: str
   :param log_file: Optional path to a log file to record osl_logger output
   :type log_file: str
   :param level: String indicating initial logging level
   :type level: {'CRITICAL', 'WARNING', 'INFO', 'DEBUG'}
   :param console_format: Formatting string for console logging.
   :type console_format: str


.. py:function:: set_level(level, handler='console')

   Set new logging level for osl-ephys module.

   :param level: String indicating new logging level
   :type level: {'CRITICAL', 'WARNING', 'INFO', 'DEBUG'}
   :param handler: The handler to set the level for. Defaults to 'console'.
   :type handler: str


.. py:function:: get_level(handler='console')

   Return current logging level for osl-ephys module.

   :param handler: The handler to get the level for. Defaults to 'console'.
   :type handler: str

   :returns: **level** -- String indicating current logging level
   :rtype: {'CRITICAL', 'WARNING', 'INFO', 'DEBUG'}


.. py:function:: log_or_print(msg, warning=False)

   Execute logger.info if an OSL logger has been setup, otherwise print.

   :param msg: Message to log/print.
   :type msg: str
   :param warning: Is the msg a warning? Defaults to False, which will print info.
   :type warning: bool


