
sinh
=====

.. cpp:function:: constexpr Complex sinh(const Complex& z) noexcept

   Returns the complex sinh [1]_ of a complex number :math:`z`.

**Parameters**

   .. cpp:var:: const Complex& z

        A complex number. 
        
**Returns**

    .. cpp:type:: Complex

        A complex number. 

The sinh function of a complex number is defined as:

.. math::
   
   \sinh z = \sinh x \cos y + i\cosh x \sin y

for :math:`\Re(z) = x` and :math:`\Im(z) = y`.

**Example**

.. code-block:: cpp

   Complex z = 3 + 4_j;
   std::cout << sinh(z) << "\n";

Output:

.. code-block:: cpp

   -6.54812 - 7.61923j

**References**

.. [1] "Hyperbolic functions", Wikipedia,
        https://en.wikipedia.org/wiki/Hyperbolic_functions