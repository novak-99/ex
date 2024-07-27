
log10
=====

.. cpp:function:: constexpr double log10(const Complex& z) noexcept

   Returns the complex common logarithm function [1]_ of a complex number :math:`z`.

**Parameters**

   .. cpp:var:: const Complex& z

        A complex number. 
        
**Returns**

    .. cpp:type:: Complex

        A complex number. 

The common logarithm of a complex number is defined as:

.. math::
   \DeclareMathOperator\arg{arg}
   \log_10(z) = \frac{log(z)}{log(10)}

**Example**

.. code-block:: cpp

   Complex z = 3 + 4_j;
   std::cout << log10(z) << "\n";

Output:

.. code-block:: cpp

   0.69897 + 0.402719j

**References**

.. [1] "Common logarithm", Wikipedia,
        https://en.wikipedia.org/wiki/Common_logarithm