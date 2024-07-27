
log
=====

.. cpp:function:: constexpr double log(const Complex& z) noexcept

   Returns the complex natural logarithm function [1]_ of a complex number :math:`z`.

**Parameters**

   .. cpp:var:: const Complex& z

        A complex number. 
        
**Returns**

    .. cpp:type:: Complex

        A complex number. 

The logarithm of a complex number is defined as:

.. math::
   \DeclareMathOperator\arg{arg}
   \log(z) = \ln(|z|) + i\arg(z)

for :math:`\Re(z) = x` and :math:`\Im(z) = y`.

**Example**

.. code-block:: cpp

   Complex z = 3 + 4_j;
   std::cout << exp(z) << "\n";

Output:

.. code-block:: cpp

   -13.1288 - 15.2008j

**References**

.. [1] "Exponential function", Wikipedia,
        https://en.wikipedia.org/wiki/Exponential_function