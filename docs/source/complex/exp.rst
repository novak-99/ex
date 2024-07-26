
exp
=====

.. cpp:function:: constexpr double exp(const Complex& z) noexcept

   Returns the complex exponential function [1]_ of a complex number :math:`z`.

**Parameters**

   .. cpp:var:: const Complex& z

        A complex number. 
        
**Returns**

    .. cpp:type:: Complex

        A complex number. 

The exponential of a complex number is defined as:

.. math::
    \exp(x)\exp(\cosy + i\siny)

for :math:`\Re(z) = x` and :math:`\Im(z) = y`.

**Example**

.. code-block:: cpp

   Complex z = 3 + 4_j;
   std::cout << conj(z) << "\n";

Output:

.. code-block:: cpp

   3 - 4j

**References**

.. [1] "Exponential function", Wikipedia,
        https://en.wikipedia.org/wiki/Exponential_function