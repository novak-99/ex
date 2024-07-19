
Li
=====

.. cpp:function:: constexpr Complex li(const Complex& z) noexcept

   Evaluates the logarithmic integral [1]_ for a complex input.

**Parameters**

    .. cpp:var:: const Complex& z

        A complex number. 

**Returns**

    .. cpp:type:: Complex

        A complex number. 

The logarithmic integral is defined as: 

.. math::
   
   \DeclareMathOperator\li{li}
   \li(z) = \int_{0}^{z}\frac{dt}{\ln t}

However, :math:`1/\ln(t)` has a singularity at :math:`t = 1`. This may be avoided by using the offset logarithmic integral, defined as:

.. math::
   
   \DeclareMathOperator\Li{Li}
   \DeclareMathOperator\li{li}
   \Li(z) = \int_{2}^{z}\frac{dt}{\ln t} = \li(z) - \li(2)

And it thereby follows that:

.. math::

   \DeclareMathOperator\Li{Li}
   \DeclareMathOperator\li{li}
   li(z) = Li(z) - li(2)

**Example**

.. code-block:: cpp

   Complex z = 1.0 + 1_j;
   std::cout << li(z) << "\n";

Output:

.. code-block:: cpp

   0.613912 + 2.05958j

**References**

.. [1] "Logarithmic integral function", Wikipedia,
        https://en.wikipedia.org/wiki/Logarithmic_integral_function