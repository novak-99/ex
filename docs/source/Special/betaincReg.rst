
BetaincReg
=====

.. cpp:function:: constexpr double betaincReg(const double x, const double a, const double b) noexcept

   Evaluates the regularized incomplete beta function [1]_.

**Parameters**

    .. cpp:var:: const double x

        A real number.

    .. cpp:var:: const double a

        A real number.

    .. cpp:var:: const double b

        A real number.

**Returns**

    .. cpp:type:: double

        A real number. 

This regularized version is defined as: 

.. math::
   I_x(a, b) = \frac{B(x; a, b)}{B(a, b)}


**Example**

.. code-block:: cpp

   double x = 1; 
   double a = 1;
   double b = 1;
   std::cout << betaincReg(x, a, b) << "\n";

Output:

.. code-block:: cpp

   1

**References**

.. [1] "Incomplete beta function", Wikipedia,
        https://en.wikipedia.org/wiki/Beta_function