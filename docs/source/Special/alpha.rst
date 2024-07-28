
alpha
=====

.. cpp:function:: constexpr double Complex alpha(const int n, const double x) noexcept

   Evaluates the alpha function [1]_ for a complex input.

**Parameters**

    .. cpp:var:: const int n

        A nonnegative number. 

    .. cpp:var:: const double x

        A real number. 

**Returns**

    .. cpp:type:: double

        A real number. 

The alpha function is defined as follows:

.. math::
   \alpha_n(x) = \int_{1}^{\infty} t^{n}e^{-xt}dt


**Example**

.. code-block:: cpp

   int n = 1; 
   double x = 1; 
   std::cout << alpha(n, x) << "\n";

Output:

.. code-block:: cpp

   0.735758

**References**

.. [1]  Weisstein, Eric W. "Alpha Function." From MathWorld--A Wolfram Web Resource. 
        https://mathworld.wolfram.com/AlphaFunction.html