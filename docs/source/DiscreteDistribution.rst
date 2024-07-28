DiscreteDistribution
=====

.. cpp:class:: DiscreteDistribution

   The generic cpplex continuous distribution type.

This module implements various complex continuous distributions.

Defined in header :code:`<DiscreteDistribution/DiscreteDistribution.hpp>`.

.. note::

   All complex discrete distribution classes make the assumption that the real and complex components are an independent, joint distribution. 

Functions
--------

.. cpp:function:: virtual constexpr double pmf(const Complex& z) const noexcept = 0

    The PMF of a distribution.

.. cpp:function:: virtual constexpr double cdf(const Complex& z) const noexcept = 0

    The CDF of a distribution.

.. cpp:function:: inline double logpmf(const Complex& z) const noexcept

    The natural log of the PMF of a distribution.

.. cpp:function:: inline double logcdf(const Complex& z) const noexcept

    The natural log of the CDF of a distribution.

.. cpp:function:: virtual constexpr std::vector<Complex> rand(const int numSamples) const noexcept = 0

    Samples from a distribution.

.. cpp:function:: virtual constexpr double entropy() const noexcept = 0

    Returns the entropy of a distribution.

Distributions
--------

.. cpp:class:: Bernoulli : public DiscreteDistribution
.. cpp:class:: Binomial : public DiscreteDistribution
.. cpp:class:: Geometric : public DiscreteDistribution
.. cpp:class:: NegativeBinomial : public DiscreteDistribution
.. cpp:class:: Poisson : public DiscreteDistribution

**Example**

.. code-block:: cpp

    // Polymorphic implementation
    DiscreteDistribution* dist; 
    Complex lambda = 5 + 5_j; 

    Complex z = 3 + 3_j; 

    Poisson poissonDist(lambda); 
    dist = &poissonDist; 
    std::cout << dist->pmf(z) << "\n";

Output:

.. code-block:: cpp

   0.0197048