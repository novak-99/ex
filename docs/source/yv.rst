
Yv
=====

.. cpp:function:: constexpr Complex yv(const double v, const Complex& z) noexcept

   Evaluates the Bessel function of the second kind [1]_ for a complex input and real order.

**Parameters**

    .. cpp:var:: const double v

        A real number. 

    .. cpp:var:: const Complex& z

        A complex number. 

**Returns**

    .. cpp:type:: Complex

        A complex number. 

The Bessel functions of the second kind are the solutions to the following differential equation: 

.. math::
   x^2 \frac{d^2y}{dx^2} + x \frac{dy}{dx} + (x^2 - v^2)y = 0

For a real order :math:`v`, the following integral representation [2]_ can be used:

.. math::
   Y_v(z) = \frac{(\frac{1}{2}z)^v}{\pi^\frac{1}{2}\Gamma(v + \frac{1}{2})}\int_{0}^{\pi}\cos(z\cos\theta)(\sin\theta)^{2v}d\theta

for :math:`\Re(v) > -\frac{1}{2}` and :math:`\DeclareMathOperator\erf{erf} v > -\frac{1}{2}\pi`

**Example**

.. code-block:: cpp

    int n = 0.5; 
    Complex z = 1 + 1_j;
    std::cout << yv(n, z) << "\n";

Output:

.. code-block:: cpp

   -0.261856 + 0.828685j

**References**

.. [1] "Bessel function", Wikipedia,
        https://en.wikipedia.org/wiki/Bessel_function
.. [2] NIST, Digital Library of Mathematical Functions,
        https://dlmf.nist.gov/10.9