
Erfc
=====

.. cpp:function:: constexpr Complex erfc(const Complex& z) noexcept

   Evaluates the complementary erf function, erfc. 

**Parameters**

    .. cpp:var:: const Complex& z

        A complex number. 

**Returns**

    .. cpp:type:: Complex

        A complex number. 

This function simply evaluates :math:`\DeclareMathOperator\erf{erf} 1 - \erf(z)`. 


**Example**

.. code-block:: cpp

   Complex z = 1.0 + 1_j;
   std::cout << erfc(z) << "\n";

Output:

.. code-block:: cpp

  -0.316151 - 0.190453j

**References**

.. [1] "Error function", Wikipedia,
        https://en.wikipedia.org/wiki/Error_function