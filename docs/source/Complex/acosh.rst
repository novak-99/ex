
acosh
=====

.. cpp:function:: constexpr Complex acosh(const Complex& z) noexcept

   Returns the complex inverse cosh [1]_ of a complex number :math:`z`.

**Parameters**

   .. cpp:var:: const Complex& z

        A complex number. 
        
**Returns**

    .. cpp:type:: Complex

        A complex number. 

The inverse cosh function of a complex number is defined as:

.. math::

   \cosh^{-1}z = \log(z + \sqrt{z^2 - 1})

**Example**

.. code-block:: cpp

   Complex z = 3 + 4_j;
   std::cout << acosh(z) << "\n";

Output:

.. code-block:: cpp

   2.30551 + 0.936812j

**References**

.. [1] "Inverse hyperbolic functions", Wikipedia,
        https://en.wikipedia.org/wiki/Inverse_hyperbolic_functions