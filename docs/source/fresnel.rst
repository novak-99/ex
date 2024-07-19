
Dawsn
=====

.. cpp:function:: constexpr std::pair<Complex, Complex> fresnel(const Complex& z) noexcept

   Evaluates the Fresnel integrals [1]_ for a complex input.

**Parameters**

    .. cpp:var:: const Complex& z

        A complex number. 

**Returns**

    .. cpp:type:: std::pair<Complex, Complex>

        A pair of complex numbers. 

The Fresnel integrals are defined as:

.. math::
   
   S(z) = \int_{0}^{z}\sin(t^2)dt \\
   C(z) = \int_{0}^{z}\sin(t^2)dt


**Example**

.. code-block:: cpp

   Complex z = 1.0 + 1_j;
   auto [S, C] = fresnel(z);
   std::cout << S << " " << C << "\n";

Output:

.. code-block:: cpp

   -2.06189 + 2.06189j
   2.55579 + 2.55579j

**References**

.. [1] "Fresnel integral", Wikipedia,
        https://en.wikipedia.org/wiki/Fresnel_integral