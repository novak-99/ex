
Gammaincc
=====

.. cpp:function:: constexpr double gammaincc(const double a, const double x) noexcept

   Evaluates the upper incomplete gamma function [1]_.

**Parameters**

    .. cpp:var:: const double a

        A real number.

    .. cpp:var:: const double x

        A real number.

**Returns**

    .. cpp:type:: double

        A complex number. 

The upper incomplete gamma function evaluates the upper portion of the gamma integral from :math:`x` to :math:`\infty`. It is defined as:

.. math::
   \Gamma(a, x) = \int_{x}^{\infty} t^{x - 1}e^{-t}dt


**Example**

.. code-block:: cpp

   double a = 1;
   double x = 1; 
   std::cout << gammaincc(a, x) << "\n";

Output:

.. code-block:: cpp

   0.367875

**References**

.. [1] "Incomplete gamma function", Wikipedia,
        https://en.wikipedia.org/wiki/Incomplete_gamma_function