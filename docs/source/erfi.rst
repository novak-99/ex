
Erfi
=====

.. cpp:function:: constexpr Complex erfi(const Complex& z) noexcept

   Evaluates the erfi function [1]_ for a complex input.

**Parameters**

    .. cpp:var:: const Complex& z

        A complex number. 

**Returns**

    .. cpp:type:: Complex

        A complex number. 

The erfi, or imaginary error function, is closely related to the error function and is defined as:

.. math::
   
   \DeclareMathOperator\erfi{erfi}
   \erfi(z) = \frac{2}{\sqrt{\pi}} \int_{0}^{z}e^{t^2}dt


**Example**

.. code-block:: cpp

   Complex z = 1.0 + 1_j;
   std::cout << erfi(z) << "\n";

Output:

.. code-block:: cpp

   0.190453 + 1.31615j

**References**

.. [1] "Error function", Wikipedia,
        https://en.wikipedia.org/wiki/Error_function