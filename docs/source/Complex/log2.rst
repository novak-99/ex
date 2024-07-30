
log2
=====

.. cpp:function:: constexpr double log2(const Complex& z) noexcept

   Returns the complex binary logarithm function [1]_ of a complex number :math:`z`.

**Parameters**

   .. cpp:var:: const Complex& z

        A complex number. 
        
**Returns**

    .. cpp:type:: Complex

        A complex number. 

The binary logarithm of a complex number is defined as:

.. math::
   \DeclareMathOperator\arg{arg}
   \log_{2}(z) = \frac{\log(z)}{\log(2)}

**Example**

.. code-block:: cpp

   Complex z = 3 + 4_j;
   std::cout << log2(z) << "\n";

Output:

.. code-block:: cpp

   0.69897 + 0.402719j

**References**

.. [1] "Common logarithm", Wikipedia,
        https://en.wikipedia.org/wiki/Common_logarithm