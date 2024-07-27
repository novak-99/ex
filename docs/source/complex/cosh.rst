
cosh
=====

.. cpp:function:: constexpr Complex cosh(const Complex& z) noexcept

   Returns the complex cosh [1]_ of a complex number :math:`z`.

**Parameters**

   .. cpp:var:: const Complex& z

        A complex number. 
        
**Returns**

    .. cpp:type:: Complex

        A complex number. 

The cosh function of a complex number is defined as:

.. math::
   \cosh z = \sinh x \cosh y - i\sin x \sinh y

for :math:`\Re(z) = x` and :math:`\Im(z) = y`.

**Example**

.. code-block:: cpp

   Complex z = 3 + 4_j;
   std::cout << cosh(z) << "\n";

Output:

.. code-block:: cpp

   -6.58066 - 7.58155j

**References**

.. [1] "Hyperbolic functions", Wikipedia,
        https://en.wikipedia.org/wiki/Hyperbolic_functions