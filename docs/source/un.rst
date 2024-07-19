
Un
=====

.. cpp:function:: constexpr Complex un(int n, const Complex& z) noexcept

   Evaluates the nth Chebyshev polynomial of the second kind [1]_ for a complex input.

**Parameters**

    .. cpp:var:: const Complex& z

        A complex number. 

    .. cpp:var:: const int n

        A nonnegative integer. 

**Returns**

    .. cpp:type:: Complex

        A complex number. 

Chebyshev polynomials of the first kind can be defined as follows:
sin((n + 1) * acos(z))) / (sin(acos(z)));
.. math::
   T_n(z) = \frac{\sin((n + 1)\cos^{-1}(z))}{\sin(\cos^{-1}(z))}


**Example**

.. code-block:: cpp

   Complex z = 1.0 + 1_j;
   int n = 1; 
   std::cout << tn(n, z) << "\n";

Output:

.. code-block:: cpp

   1 + 1j

**References**

.. [1] "Gamma function", Wikipedia,
        https://en.wikipedia.org/wiki/Chebyshev_polynomials