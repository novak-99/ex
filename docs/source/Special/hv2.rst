
Hv2
=====

.. cpp:function:: constexpr Complex hv2(const double v, const Complex& z) noexcept

   Evaluates the Hankel function of the second kind [1]_ for a complex input and real order.

**Parameters**

    .. cpp:var:: const double v

        A real number. 

    .. cpp:var:: const Complex& z

        A complex number. 

**Returns**

    .. cpp:type:: Complex

        A complex number. 

The Hankel functions of the second kind are defined as:

.. math::
   H_{n}^{(1)}(z) = J_n(z) - iY_n(z)

**Example**

.. code-block:: cpp

    int n = 0.5; 
    Complex z = 1 + 1_j;
    std::cout << hv2(n, z) << "\n";

Output:

.. code-block:: cpp

    1.79659 + 0.32206j

**References**

.. [1]  Weisstein, Eric W. "Hankel Function of the Second Kind." From MathWorld--A Wolfram Web Resource. 
        https://mathworld.wolfram.com/HankelFunctionoftheSecondKind.html