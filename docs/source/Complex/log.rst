
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

**Example**

.. code-block:: cpp

   Complex z = 3 + 4_j;
   std::cout << log(z) << "\n";

Output:

.. code-block:: cpp

   1.60944 + 0.927295j

**References**

.. [1] "Complex logarithm", Wikipedia,
        https://en.wikipedia.org/wiki/Complex_logarithm