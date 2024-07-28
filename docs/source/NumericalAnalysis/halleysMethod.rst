
halleysMethod
=====

.. cpp:function:: constexpr Complex halleysMethod(Complex (*f)(Complex), const Complex& z0, const double alpha, const int epochs) noexcept

   Performs the Halley's method algortihm on a complex function.

**Parameters**

    .. cpp:var:: Complex (*f)(Complex)

        The function to root-find.

    .. cpp:var:: const Complex& z0

        The starting point.

    .. cpp:var:: const int epochs
        
        The number of iterations.

**Returns**

    .. cpp:type:: Complex

        A complex number. 

This function root-finds the given complex function :math:`f` using the following update rule:

.. math::
    z_{k+1} = z_k - \frac{2f(z_k)f'(z_k)}{2[f'(z_k)]^2 - f(x_k)f''(z_k)}

**Example**

.. code-block:: cpp

    auto fn = [](Complex z) { return sin(z); };
    Complex z = halleysMethod(fn, 0.1, 1000); 
    std::cout << z << "\n";
    std::cout << sin(z) << "\n";

Output:

.. code-block:: cpp

    0 + 0j
    0 + 0j

**References**

.. [1] "Halley's method", Wikipedia,
        https://en.wikipedia.org/wiki/Halley%27s_method