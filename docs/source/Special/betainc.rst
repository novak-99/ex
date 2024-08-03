
betainc
=====

.. cpp:function:: constexpr double betainc(const double x, const double a, const double b) noexcept

   Evaluates the incomplete beta function [1]_.

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

The incomplete gamma function is a generalization of the beta function defined as:

.. math::
   B(x; a, b) = \int_{0}^{x} t^{a - 1}(1 - t)^{b - 1}dt


**Example**

.. code-block:: cpp

   double a = 1;
   double b = 1;
   double x = 1; 
   std::cout << betainc(x, a, b) << "\n";

Output:

.. code-block:: cpp

   1

**References**

.. [1] "Incomplete beta function", Wikipedia,
        https://en.wikipedia.org/wiki/Beta_function