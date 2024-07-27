ContinuousDistribution
=====

.. cpp:class:: ContinuousDistribution

   The generic cpplex continuous distribution type.

This module implements various complex continuous distributions.

Defined in header :code:`<ContinuousDistribution/ContinuousDistribution.hpp>`.

.. note::

   All complex continuous distribution classes make the assumption that the real and complex components are an independent, joint distribution. 

Functions
--------

.. cpp:function:: virtual constexpr double pdf(const Complex& z) const noexcept = 0

.. cpp:function:: virtual constexpr double cdf(const Complex& z) const noexcept = 0

.. cpp:function:: inline double logpdf(const Complex& z) const noexcept

.. cpp:function:: inline double logcdf(const Complex& z) const noexcept

.. cpp:function:: virtual constexpr std::vector<Complex> rand(const int numSamples) const noexcept = 0

.. cpp:function:: virtual constexpr double entropy() const noexcept = 0

Child Classes
--------

    .. cpp:class:: Cauchy : public ContinuousDistribution
    .. cpp:class:: Cauchy : public Chi
    .. cpp:class:: Cauchy : public ChiSquared
    .. cpp:class:: Cauchy : public Exponential
    .. cpp:class:: Cauchy : public Gamma
    .. cpp:class:: Cauchy : public Laplace
    .. cpp:class:: Cauchy : public Logistic
    .. cpp:class:: Cauchy : public LogNormal
    .. cpp:class:: Cauchy : public MaxwellBoltzman
    .. cpp:class:: Cauchy : public Normal
    .. cpp:class:: Cauchy : public Pareto
    .. cpp:class:: Cauchy : public Rayleigh
    .. cpp:class:: Cauchy : public Triangular
    .. cpp:class:: Cauchy : public Uniform
    .. cpp:class:: Cauchy : public Weibull