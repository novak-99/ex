
Hv1
=====

.. cpp:function:: constexpr Complex hv1(const double v, const Complex& z) noexcept

   Evaluates the Hankel function of the first kind [1]_ for a complex input and real order.

**Parameters**

    .. cpp:var:: const double v

        A real number. 

    .. cpp:var:: const Complex& z

        A complex number. 

**Returns**

    .. cpp:type:: Complex

        A complex number. 

The Hankel functions of the first kind are defined as:

.. math::
   H_{n}^{(1)}(z) = J_n(z) + iY_n(z)

**Example**

.. code-block:: cpp

    int n = 0.5; 
    Complex z = 1 + 1_j;
    std::cout << hv1(n, z) << "\n";

Output:

.. code-block:: cpp

   0.139216 - 0.201651j

**References**

.. [1]  Weisstein, Eric W. "Hankel Function of the First Kind." From MathWorld--A Wolfram Web Resource. 
        https://mathworld.wolfram.com/HankelFunctionoftheFirstKind.html