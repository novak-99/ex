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

Distributions
--------

    .. cpp:class:: ContinuousDistribution : public ContinuousDistribution
    .. cpp:class:: Chi : public ContinuousDistribution
    .. cpp:class:: ChiSquared : public ContinuousDistribution
    .. cpp:class:: Exponential : public ContinuousDistribution
    .. cpp:class:: Gamma : public ContinuousDistribution
    .. cpp:class:: Laplace : public ContinuousDistribution
    .. cpp:class:: Logistic : public ContinuousDistribution
    .. cpp:class:: LogNormal : public ContinuousDistribution
    .. cpp:class:: MaxwellBoltzman : public ContinuousDistribution
    .. cpp:class:: Normal : public ContinuousDistribution
    .. cpp:class:: Pareto : public ContinuousDistribution
    .. cpp:class:: Rayleigh : public ContinuousDistribution
    .. cpp:class:: Triangular : public ContinuousDistribution
    .. cpp:class:: Uniform : public ContinuousDistribution
    .. cpp:class:: Weibull : public ContinuousDistribution