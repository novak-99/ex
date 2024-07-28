
GammaincReg
=====

.. cpp:function:: constexpr double gammaincReg(const double a, const double x) noexcept

   Evaluates the regularized lower incomplete gamma function [1]_.

**Parameters**

    .. cpp:var:: const double a

        A real number.

    .. cpp:var:: const double x

        A real number.

**Returns**

    .. cpp:type:: double

        A real number. 

This regularized version is defined as: 

.. math::
   P(a, x) = \frac{\gamma(a, x)}{\Gamma(a)}


**Example**

.. code-block:: cpp

   double a = 1;
   double x = 1; 
   std::cout << gammaincReg(a, x) << "\n";

Output:

.. code-block:: cpp

   0.632121

**References**

.. [1] "Incomplete gamma function", Wikipedia,
        https://en.wikipedia.org/wiki/Incomplete_gamma_function