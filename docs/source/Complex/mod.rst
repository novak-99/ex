
mod
=====

.. cpp:function:: constexpr double mod(const Complex& z) noexcept

   Returns the magnitude [1]_ of a complex number :math:`z`.

**Parameters**

    .. cpp:var:: const Complex& z

        A complex number. 

**Returns**

    .. cpp:type:: Complex

        A complex number. 

The mod, or magnitude of a complex number, is defined as follows:

.. math::
   |z| = \sqrt{x^2 + y^2}

for :math:`\Re(z) = x` and :math:`\Im(z) = y`. 


**Example**

.. code-block:: cpp

   Complex z = 3 + 4_j;
   std::cout << mod(z) << "\n";

Output:

.. code-block:: cpp

   5

**References**

.. [1] "Complex number", Wikipedia,
        https://en.wikipedia.org/wiki/Complex_number