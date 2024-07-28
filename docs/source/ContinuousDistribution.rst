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

    The PDF of a distribution.

.. cpp:function:: virtual constexpr double cdf(const Complex& z) const noexcept = 0

    The CDF of a distribution.

.. cpp:function:: inline double logpdf(const Complex& z) const noexcept

    The natural log of the PDF of a distribution.

.. cpp:function:: inline double logcdf(const Complex& z) const noexcept

    The natural log of the CDF of a distribution.

.. cpp:function:: virtual constexpr std::vector<Complex> rand(const int numSamples) const noexcept = 0

    Samples from a distribution.

.. cpp:function:: virtual constexpr double entropy() const noexcept = 0

    Returns the entropy of a distribution.

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

**Example**

.. code-block:: cpp

    // Polymorphic implementation.
    DiscreteDistribution* dist; 
    Complex mu = 1 + 1_j; 
    Complex s = 1 + 2_j; 

    Complex z = 0.5 + 0.5_j; 

    Logistic logDist(mu, s); 
    dist = &logDist; 
    std::cout << dist->pdf(z) << "\n";

Output:

.. code-block:: cpp

   0.0289212