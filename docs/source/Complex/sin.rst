
sin
=====

.. cpp:function:: constexpr Complex sin(const Complex& z) noexcept

   Returns the complex sin [1]_ of a complex number :math:`z`.

**Parameters**

   .. cpp:var:: const Complex& z

        A complex number. 
        
**Returns**

    .. cpp:type:: Complex

        A complex number. 

The sin function of a complex number is defined as:

.. math::
   \sin z = \sin x \cosh y + i\cos x \sinh y

for :math:`\Re(z) = x` and :math:`\Im(z) = y`.

**Example**

.. code-block:: cpp

   Complex z = 3 + 4_j;
   std::cout << sin(z) << "\n";

Output:

.. code-block:: cpp

   3.85374 - 27.0168j

**References**

.. [1] "Sine and cosine", Wikipedia,
        https://en.wikipedia.org/wiki/Sine_and_cosine