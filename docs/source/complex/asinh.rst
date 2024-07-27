
asinh
=====

.. cpp:function:: constexpr Complex asinh(const Complex& z) noexcept

   Returns the complex inverse sinh [1]_ of a complex number :math:`z`.

**Parameters**

   .. cpp:var:: const Complex& z

        A complex number. 
        
**Returns**

    .. cpp:type:: Complex

        A complex number. 

The inverse sinh function of a complex number is defined as:

.. math::

   \sinh{^-1}z = \log(z + \sqrt{z^2 + 1})

**Example**

.. code-block:: cpp

   Complex z = 3 + 4_j;
   std::cout << asinh(z) << "\n";

Output:

.. code-block:: cpp

   2.29991 + 0.917617j

**References**

.. [1] "Inverse hyperbolic functions", Wikipedia,
        https://en.wikipedia.org/wiki/Inverse_hyperbolic_functions