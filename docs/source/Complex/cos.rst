
cos
=====

.. cpp:function:: constexpr Complex cos(const Complex& z) noexcept

   Returns the complex cos [1]_ of a complex number :math:`z`.

**Parameters**

   .. cpp:var:: const Complex& z

        A complex number. 
        
**Returns**

    .. cpp:type:: Complex

        A complex number. 

The cos function of a complex number is defined as:

.. math::
   \cos z = \cos x \cosh y + i\sin x \sinh y

for :math:`\Re(z) = x` and :math:`\Im(z) = y`.

**Example**

.. code-block:: cpp

   Complex z = 3 + 4_j;
   std::cout << cos(z) << "\n";

Output:

.. code-block:: cpp

   -27.0349 - 3.85115j

**References**

.. [1] "Sine and cosine", Wikipedia,
        https://en.wikipedia.org/wiki/Sine_and_cosine