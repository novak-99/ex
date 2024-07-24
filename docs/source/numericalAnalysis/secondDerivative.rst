
SecondDerivative
=====

.. cpp:function:: constexpr Complex secondDerivative(Complex (*f)(Complex), const Complex& z) noexcept

   Evaluates the second derivative of a complex function at a point :math:`z`. The second derivative is implemented using finite differences [1]_.

**Parameters**

    .. cpp:var:: Complex (*f)(Complex)

        The function to differentiate.

    .. cpp:var:: const Complex& z

        A complex number. 

**Returns**

    .. cpp:type:: Complex

        A complex number. 

This function simply returns the second derivative of a function :math:`f` evaluated at a point :math:`z`, that is:

.. math::
   \left. \frac{d^2f(x)}{dx^2} \right|_{x = z} = \lim_{h\to 0} \frac{f(z + h) - 2f(z) + f(z - h)}{h^2}

To approxiate the derivative, we set :math:`h = 10^{-5}`.

**Example**

.. code-block:: cpp

    auto fn = [](Complex z) { return sin(z); };
    std::cout << secondDerivative(fn, 1 + 1_j) << "\n";
    std::cout << -sin(1 + 1_j) << "\n";

Output:

.. code-block:: cpp

    -0.83373 + 0.988898j
    -0.83373 + 0.988898j

**References**

.. [1] "Finite difference", Wikipedia,
        https://en.wikipedia.org/wiki/Finite_difference