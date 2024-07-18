
Zeta
=====

.. cpp:function:: constexpr double zeta(const double x) noexcept

   Evaluates the Riemann zeta function [1]_ for a real input. Approximated via an integral representation [2]_. Suitable for :math:`1 < x \leq 10`.

**Parameters**

    .. cpp:var:: const double z

        A real number. 

**Returns**

    .. cpp:type:: double

        A real number. 

The  Riemann zeta function is an infinite series defined as: 

.. math::
   \zeta(n) = \sum_{n = 1}^{\infty} x^{-n}

It may also be expressed as the following integral:

.. math::
   \zeta(z) = \int_{0}^{\infty} t^{z - 1}e^{-t}dt

for :math:`\Re(z) > 1`. 

**Example**

.. code-block:: cpp

   double z = 2.0;
   std::cout << zeta(z) << "\n";

Output:

.. code-block:: cpp

   1.64494

**References**

.. [1] "Riemann zeta function", Wikipedia,
        https://en.wikipedia.org/wiki/Riemann_zeta_function
.. [2] NIST, Digital Library of Mathematical Functions,
        https://dlmf.nist.gov/25.5#E1