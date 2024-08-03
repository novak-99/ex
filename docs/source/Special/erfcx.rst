
erfcx
=====

.. cpp:function:: constexpr Complex erfcx(const Complex& z) noexcept

   Evaluates the scaled complementary erf function, erfcx. 

**Parameters**

    .. cpp:var:: const Complex& z

        A complex number. 

**Returns**

    .. cpp:type:: Complex

        A complex number. 

This function simply evaluates :math:`\DeclareMathOperator\erfc{erfc} e^{z^2}\erfc(z)`. 


**Example**

.. code-block:: cpp

   Complex z = 1.0 + 1_j;
   std::cout << erfcx(z) << "\n";

Output:

.. code-block:: cpp

  0.304744 - 0.208219j

**References**

.. [1] "Error function", Wikipedia,
        https://en.wikipedia.org/wiki/Error_function