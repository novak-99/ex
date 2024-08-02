
atanh
=====

.. cpp:function:: constexpr Complex atanh(const Complex& z) noexcept

   Returns the complex inverse tanh [1]_ of a complex number :math:`z`.

**Parameters**

   .. cpp:var:: const Complex& z

        A complex number. 
        
**Returns**

    .. cpp:type:: Complex

        A complex number. 

The inverse tanh function of a complex number is defined as:

.. math::

   \tanh^{-1}z = \frac{1}{2}\log(\frac{1 + z}{1 - z})

**Example**

.. code-block:: cpp

   Complex z = 3 + 4_j;
   std::cout << atanh(z) << "\n";

Output:

.. code-block:: cpp

   0.117501 + 1.40992j

**References**

.. [1] "Inverse hyperbolic functions", Wikipedia,
        https://en.wikipedia.org/wiki/Inverse_hyperbolic_functions