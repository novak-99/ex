
Ei
=====

.. cpp:function:: constexpr Complex ei(const Complex& z) noexcept

   Evaluates the exponential integral [1]_ for a complex input.

**Parameters**

    .. cpp:var:: const Complex& z

        A complex number. 

**Returns**

    .. cpp:type:: Complex

        A complex number. 

The exponential integral for real inputs is defined as: 

.. math::
   \DeclareMathOperator\Ei{Ei}
   \Ei(z) = -\int_{-x}^{\infty} \frac{e^{-t}}{t}dt

The definition can be extended to complex numbers as follows [2]_: 

.. math::
   \Ei(z) = \int_{0}^{z} \frac{e^{t} - 1}{t}dt + \frac{1}{2}(\log(z) - \log(\frac{1}{z})) + \gamma

**Example**

.. code-block:: cpp

   Complex z = 1.0 + 1_j;
   std::cout << ei(z) << "\n";

Output:

.. code-block:: cpp

   1.76463 + 2.38777j

**References**

.. [1] "Exponential integral", Wikipedia,
        https://en.wikipedia.org/wiki/Exponential_integral
.. [2] "ExpIntegralEi", Wolfram, 
        https://functions.wolfram.com/GammaBetaErf/ExpIntegralEi/07/01/01/0001/