
Wofz
=====

.. cpp:function:: constexpr Complex wofz(const Complex& z) noexcept

   Evaluates the Faddeeva function [1]_ for a complex input.

**Parameters**

    .. cpp:var:: const Complex& z

        A complex number. 

**Returns**

    .. cpp:type:: Complex

        A complex number. 

This function simply evaluates :math:`\DeclareMathOperator\erfc{erfc} e^{-z^2}\erfc(iz)`. 


**Example**

.. code-block:: cpp

   Complex z = 1.0 + 1_j;
   std::cout << wofz(z) << "\n";

Output:

.. code-block:: cpp

   0.304744 + 0.208219j

**References**

.. [1] "Faddeeva function", Wikipedia,
        https://en.wikipedia.org/wiki/Faddeeva_function