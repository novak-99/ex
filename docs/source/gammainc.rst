
Gammainc
=====

.. cpp:function:: constexpr double gammainc(const double a, const double x) noexcept

   Evaluates the lower incomplete gamma function [1]_.

**Parameters**

    .. cpp:var:: const Complex& z

        A complex number. 

**Returns**

    .. cpp:type:: Complex

        A complex number. 

The lower incomplete gamma function evaluates the lower portion of the gamma integral from :math:`0` to :math:`x`. It is defined as:

.. math::
   \gamma(a, x) = \int_{0}^{x} t^{z - 1}e^{-t}dt


**Example**

.. code-block:: cpp

   double x = 1; 
   std::cout << gammainc(x) << "\n";

Output:

.. code-block:: cpp

   0.632121

**References**

.. [1] "Incomplete gamma function", Wikipedia,
        https://en.wikipedia.org/wiki/Incomplete_gamma_function