
conj
=====

.. cpp:function:: constexpr double conj(const Complex& z) noexcept

   Returns the complex conjugates [1]_ of a complex number :math:`z`.

**Parameters**

   .. cpp:var:: const Complex& z

**Returns**

    .. cpp:type:: Complex

        A complex number. 

The conjugate of a complex number is defined as:

.. math::

   \newcommand{\compconj}[1]{%
   \overline{#1}%
   }

   \compconj{z} = x - iy

for :math:`\Re(z) = x` and :math:`\Im(z) = y`.

**Example**

.. code-block:: cpp

   Complex z = 3 + 4_j;
   std::cout << conj(z) << "\n";

Output:

.. code-block:: cpp

   3 - 4j

**References**

.. [1] "Complex conjugate", Wikipedia,
        https://en.wikipedia.org/wiki/Complex_conjugate