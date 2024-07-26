
proj
=====

.. cpp:function:: constexpr double conj(const Complex& z) noexcept

   Projects a complex number onto the Riemann sphere. Performs the same operation as :code:`std::proj`. [1]_ 

**Parameters**

   .. cpp:var:: const Complex& z

**Returns**

    .. cpp:type:: Complex

        A complex number. 

If :code:`z` is a complex infinity, the function returns :code:`Complex(INF, 0.0)` or :code:`Complex(INF, -0.0)`, with the sign bit on the zero corresponding to the sign of :math:`\Im(z)` Otherwise, :code:`z` is returned.

**Example**

.. code-block:: cpp

   Complex z(INF.real(), -1);
   std::cout << proj(z) << "\n";

Output:

.. code-block:: cpp

   inf - 0j

**References**

.. [1] "Complex conjugate", Wikipedia,
        https://en.cppreference.com/w/cpp/numeric/complex/proj