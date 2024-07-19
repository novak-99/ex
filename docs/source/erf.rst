
Erf
=====

.. cpp:function:: constexpr Complex erf(const Complex& z) noexcept

   Evaluates the erf function [1]_ for a complex input.

**Parameters**

    .. cpp:var:: const Complex& z

      A complex number. 

**Returns**

    .. cpp:type:: Complex

      A complex number. 

The erf, or error function, is a scaled, nonelementary integral commonly used in probability and statistics. It is defined as:

.. math::
   \erf(z) = \frac{2}{\sqrt(\pi)} \int_{0}^{z}e^{-t^2}dt


**Example**

.. code-block:: cpp

   Complex z = 1.0 + 1_j;
   std::cout << erf(z) << "\n";

Output:

.. code-block:: cpp

   1.31615 + 0.190453j

**References**

.. [1] "Error function", Wikipedia,
        https://en.wikipedia.org/wiki/Error_function