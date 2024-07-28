
beta
=====

.. cpp:function:: constexpr double Complex beta(const double a, const double b) noexcept

   Evaluates the beta function [1]_ for a complex input.

**Parameters**

    .. cpp:var:: const int a

        A real number.

    .. cpp:var:: const int b

        A real number.

**Returns**

    .. cpp:type:: double

        A real number. 

The beta function is defined as follows:

.. math::
   B(a, b) = \frac{\Gamma(a)\Gamma(b)}{\Gamma(a + b)}


**Example**

.. code-block:: cpp

   double a = 1; 
   double b = 1; 
   std::cout << beta(a, b) << "\n";

Output:

.. code-block:: cpp

   1

**References**

.. [1]  Weisstein, Eric W. " Beta Function." From MathWorld--A Wolfram Web Resource. 
        https://mathworld.wolfram.com/BetaFunction.html