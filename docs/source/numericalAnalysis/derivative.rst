
Derivative
=====

.. cpp:function:: constexpr Complex derivative(Complex (*f)(Complex), const Complex& z) noexcept

   Evaluates the derivative of a complex function at a point :math:`z`. The derivative is implemented using finite differences [1]_.

**Parameters**

    .. cpp:var:: Complex (*f)(Complex)

        The function to differentiate.

    .. cpp:var:: const Complex& z

        A complex number. 

**Returns**

    .. cpp:type:: Complex

        A complex number. 

This function simply returns the derivative of a function :math:`f` evaluated at a point :math:`z`, that is:

.. math::
   \left. \frac{df(x)}{dx} \right|_{x = z} = \lim_{h\to 0} \frac{f(z + h) - f(z - h)}{2h}

To approxiate the derivative, we set :math:`h = 10^{-8}`.

**Example**

.. code-block:: cpp

    auto fn = [](Complex z) { return sin(z); };
    std::cout << derivative(fn, 1 + 1_j) << "\n";
    std::cout << cos(1 + 1_j) << "\n";

Output:

.. code-block:: cpp

    0.83373 - 0.988898j
    0.83373 - 0.988898j

**References**

.. [1] "Finite difference", Wikipedia,
        https://en.wikipedia.org/wiki/Finite_difference