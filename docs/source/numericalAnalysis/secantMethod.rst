
secantMethod
=====

.. cpp:function:: constexpr Complex secantMethod(Complex (*f)(Complex), const Complex& z0, const double alpha, const int epochs) noexcept

   Performs the Secant method algortihm on a complex function.

**Parameters**

    .. cpp:var:: Complex (*f)(Complex)

        The function to root-find.

    .. cpp:var:: const Complex& z0

        The first starting point.

    .. cpp:var:: const Complex& z1

        The second starting point.

    .. cpp:var:: const int epochs
        
        The number of iterations.

**Returns**

    .. cpp:type:: Complex

        A complex number. 

This function root-finds the given complex function :math:`f` using the following update rule:

.. math::
    z_{k+1} = z_k - f(z_k)\frac{z_k - z_{k - 1}}{f(z_k) - f(z_{k - 1})}

**Example**

.. code-block:: cpp

    auto fn = [](Complex z) { return sin(z); };
    Complex z = secantMethod(fn, 0.1, 0.05, 1000); 
    std::cout << z << "\n";
    std::cout << sin(z) << "\n";

Output:

.. code-block:: cpp

    -4.94066e-323 + 0j
    -4.94066e-323 + 0j

**References**

.. [1] "Secant method", Wikipedia,
        https://en.wikipedia.org/wiki/Secant_method