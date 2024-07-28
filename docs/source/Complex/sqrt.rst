
sqrt
=====

.. cpp:function:: constexpr double sqrt(const Complex& z) noexcept

   Returns the complex square root [1]_ of a complex number :math:`z`.

**Parameters**

   .. cpp:var:: const Complex& z

        A complex number. 
        
**Returns**

    .. cpp:type:: Complex

        A complex number. 

The square root of a complex number is defined as:

.. math::

   \DeclareMathOperator\arg{arg}
   \sqrt{z} = \sqrt{|z|}(\cos{\frac{\arg(z)}{2}} + i\sin{\frac{\arg(z)}{2}})

**Example**

.. code-block:: cpp

   Complex z = 3 + 4_j;
   std::cout << sqrt(z) << "\n";

Output:

.. code-block:: cpp

   2 + 1j

**References**

.. [1] "Square root", Wikipedia,
        https://en.wikipedia.org/wiki/Square_root