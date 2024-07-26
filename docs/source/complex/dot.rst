
dot
=====

.. cpp:function:: constexpr double dot(const Complex& z) noexcept

   Returns the magnitude [1]_ of a complex number :math:`z`.

**Parameters**

   .. cpp:var:: const Complex& z1

        A complex number. 

   .. cpp:var:: const Complex& z2

        A complex number. 

**Returns**

    .. cpp:type:: double

        A real number. 

The dot product of two complex numbers :math:`z_1` and :math:`z_2` is defined as:

.. math::
   z_1 \cdot z_2 = x_1x_2 + y_1y_2

for :math:`\Re(z_1) = x_1`, :math:`\Im(z_1) = y_1` and so on. 

**Example**

.. code-block:: cpp

   Complex z = 3 + 4_j;
   std::cout << arg(z) << "\n";

Output:

.. code-block:: cpp

   0.927295

**References**

.. [1] "Dot product", Wikipedia,
        https://en.wikipedia.org/wiki/Dot_product