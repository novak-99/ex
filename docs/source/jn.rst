
Jn
=====

.. cpp:function:: constexpr Complex jn(const int n, const Complex& z) noexcept

   Evaluates the Bessel function of the first kind [1]_ for a complex input.

**Parameters**

    .. cpp:var:: const int n

        An integer.

    .. cpp:var:: const Complex& z

        A complex number. 

**Returns**

    .. cpp:type:: Complex

        A complex number. 

The Bessel function of the first kind are the solutions to the following differential equation: 

.. math::
   x^2 \frac{d^2y}{dx^2} + x \frac{dy}{dx} + (x^2 - n^2) = 0

For an integer order :math:`n`, the following integral representation can be used:

.. math::
   J_n(z) = \frac{1}{\pi}\int_{0}{\pi}\cos(z\sin(\theta) - n\theta)d\theta

**Example**

.. code-block:: cpp

    int n = 1; 
    Complex z = 1_j;
    std::cout << jn(n, z) << "\n";

Output:

.. code-block:: cpp

   0.498016 - 0.15495j

**References**

.. [1]  Weisstein, Eric W. "Bessel Function of the First Kind." From MathWorld--A Wolfram Web Resource. 
        https://mathworld.wolfram.com/BesselFunctionoftheFirstKind.html