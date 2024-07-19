
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

Chebyshev polynomials of the second kind can be defined as follows:

.. math::
   T_n(z) = \frac{\sin((n + 1)\cos^{-1}(z))}{\sin(\cos^{-1}(z))}


**Example**

.. code-block:: cpp

   Complex z = 1.0 + 1_j;
   int n = 1; 
   std::cout << un(n, z) << "\n";

Output:

.. code-block:: cpp

   2 + 2j

**References**

.. [1] "Chebyshev polynomials", Wikipedia,
        https://en.wikipedia.org/wiki/Chebyshev_polynomials