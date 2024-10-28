:py:mod:`osl_ephys.source_recon.sign_flipping`
==============================================

.. py:module:: osl_ephys.source_recon.sign_flipping

.. autoapi-nested-parse::

   Functions for fixing the dipole sign ambiguity of beamformed data.



Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   osl_ephys.source_recon.sign_flipping._get_parc_chans
   osl_ephys.source_recon.sign_flipping.find_flips
   osl_ephys.source_recon.sign_flipping.load_covariances
   osl_ephys.source_recon.sign_flipping.find_template_subject
   osl_ephys.source_recon.sign_flipping.covariance_matrix_correlation
   osl_ephys.source_recon.sign_flipping.randomly_flip
   osl_ephys.source_recon.sign_flipping.apply_flips_to_covariance
   osl_ephys.source_recon.sign_flipping.apply_flips
   osl_ephys.source_recon.sign_flipping.time_embed
   osl_ephys.source_recon.sign_flipping.std_data



.. py:function:: _get_parc_chans(raw)

   Get parcel channels names in an mne.Raw or mne.Epochs object.

   :param raw: Raw or Epochs object.
   :type raw: mne.Raw or mne.Epochs

   :returns: **parc_chans** -- Parcel channel names. If no channels called 'parcel_X' are found in the raw object then we return 'misc'.
   :rtype: list of str or str


.. py:function:: find_flips(cov, template_cov, n_embeddings, n_init, n_iter, max_flips, use_tqdm=True)

   Find channels to flip.

   We search for the channels to flip by randomly flipping them and saving the flips that maximise the correlation of the covariance matrices between subjects.

   :param cov: Covariance matrix we would like to sign flip.
   :type cov: numpy.ndarray
   :param template_cov: Template covariance matrix.
   :type template_cov: numpy.ndarray
   :param n_embeddings: Number of time-delay embeddings.
   :type n_embeddings: int
   :param n_init: Number of initializations.
   :type n_init: int
   :param n_iter: Number of sign flipping iterations per subject to perform.
   :type n_iter: int
   :param max_flips: Maximum number of channels to flip in an iteration.
   :type max_flips: int
   :param use_tqdm: Should we display a tqdm progress bar?
   :type use_tqdm: bool

   :returns: * **best_flips** (*numpy.ndarray*) -- A (n_channels,) array of 1s and -1s indicating whether or not to flip a channels.
             * **metrics** (*numpy.ndarray*) -- Evaluation metric (correlation between covariance matrices) as a function of iterations. Shape is (n_iter + 1,).


.. py:function:: load_covariances(parc_files, n_embeddings=1, standardize=True, loader=None, use_tqdm=True)

   Loads data and returns its covariance matrix.

   :param parc_files: List of paths to parcellated data files to load.
   :type parc_files: list of str
   :param n_embeddings: Number of time-delay embeddings to perform.
   :type n_embeddings: int
   :param standardize: Should we standardize the data?
   :type standardize: bool
   :param loader: Custom function to load parcellated data files.
   :type loader: function
   :param use_tqdm: Should we display a tqdm progress bar?
   :type use_tqdm: bool

   :returns: **covs** -- Covariance matrices.
   :rtype: numpy.ndarray


.. py:function:: find_template_subject(covs, diag_offset=0)

   Find a good template subject to use to align dipoles.

   We select the median subject after calculating the similarity between the covariances of each subject.

   :param covs: Covariance of each subject. Shape much be (n_subjects, n_channels, n_channels).
   :type covs: numpy.ndarray
   :param diag_offset: Offset to apply when getting the upper triangle of the covariance matrix before calculating the correlation between covariances.
   :type diag_offset: int

   :returns: **index** -- Index for the template subject.
   :rtype: int


.. py:function:: covariance_matrix_correlation(M1, M2, diag_offset=0, mode=None)

   Calculates the Pearson correlation between covariance matrices.

   :param M1: First covariance matrix.
   :type M1: numpy.ndarray
   :param M2: Second covariance matrix.
   :type M2: numpy.ndarray
   :param diag_offset: To calculate the distance we take the upper triangle.
                       This argument allows us to specify an offet from the diagonal
                       so we can choose not to take elements near the diagonal.
   :type diag_offset: int
   :param mode: Either 'abs', 'sign' or None.
   :type mode: str


.. py:function:: randomly_flip(flips, max_flips)

   Randomly flips some channels.

   :param flips: Vector of 1s and -1s indicating which channels to flip.
   :type flips: numpy.ndarray
   :param max_flips: Maximum number of channels to change in this function.
   :type max_flips: int

   :returns: **new_flips** -- Vector of 1s and -1s indicating which channels to flip.
   :rtype: numpy.ndarray


.. py:function:: apply_flips_to_covariance(cov, flips, n_embeddings=1)

   Applies flips to a covariance matrix.

   :param cov: Covariance matrix to apply flips to. Shape must be (n_channels*n_embeddings, n_channels*n_embeddings).
   :type cov: numpy.ndarray
   :param flips: Vector of 1s and -1s indicating whether or not to flip a channels. Shape must be (n_channels,).
   :type flips: numpy.ndarray
   :param n_embeddings: Number of embeddings used when calculating the covariance.
   :type n_embeddings: int

   :returns: **cov** -- Flipped covariance matrix.
   :rtype: numpy.ndarray


.. py:function:: apply_flips(outdir, subject, flips, epoched=False)

   Saves the sign flipped data.

   :param outdir: Path to source reconstruction directory.
   :type outdir: str
   :param subject: Subject name/id.
   :type subject: str
   :param flips: Flips to apply.
   :type flips: numpy.ndarray
   :param epoched: Are we performing sign flipping on parc-raw.fif (epoched=False) or parc-epo.fif files (epoched=True)?
   :type epoched: bool


.. py:function:: time_embed(x, n_embeddings)

   Performs time-delay embedding.

   :param x: Time series data. Shape must be (n_samples, n_channels).
   :type x: numpy.ndarray
   :param n_embeddings: Number of samples in which to shift the data. Must be an odd number.
   :type n_embeddings: int

   :returns: Time embedded data. Shape is (n_samples, n_channels * n_embeddings).
   :rtype: sliding_window_view


.. py:function:: std_data(x)

   Standardize (z-transform) the data.

   :param x: Data. Shape must be (n_samples, n_channels).
   :type x: numpy.ndarray

   :returns: **std_x** -- Standardized time series.
   :rtype: numpy.ndarray


