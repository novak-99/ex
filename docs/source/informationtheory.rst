Information Theory
=====

This module implements various functions related to information theory. In particular, it features various entropy functions.

Defined in header <InformationTheory/InformationTheory.hpp>.

.. note::

   All discrete entropy functions make the assumption that the real and complex components are an independent, joint distribution.
   All continuous entropy functions make the assumption that you are using PDFs of the bivariate real-complex distribution.

Functions
--------

.. toctree::
   :maxdepth: 2

   informationtheory/probNorm
   informationtheory/entropy
   informationtheory/klDiv
   informationtheory/jsDiv
   informationtheory/shannonInformation