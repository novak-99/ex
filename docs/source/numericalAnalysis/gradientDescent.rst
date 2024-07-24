
GradientDescent
=====

.. cpp:function:: constexpr Complex gradientDescent(Complex (*f)(Complex), const Complex& z0, const double alpha, const int epochs) noexcept

   Performs the gradeint descent algortihm on a complex function.

**Parameters**

    .. cpp:var:: Complex (*f)(Complex)

        The function to optimize.

    .. cpp:var:: const Complex& z0

        The starting point.

    .. cpp:var:: const double alpha

        The learning rate.

    .. cpp:var:: const int epochs
        
        The number of training iterations.

**Returns**

    .. cpp:type:: Complex

        A complex number. 

This function optimizes the given complex function :math:`f` using the following update rule:

.. math::
    z_{k+1} = z_k - \alpha \frac{f'(z_k)}

**Example**

.. code-block:: cpp

    auto fn = [](Complex z) { return sin(z); }; // Example PDF 1. 
    Complex z = gradientDescent(fn, 0.1, 0.1, 1000); 
    std::cout << z << "\n";
    std::cout << cos(z) << "\n"; // f'(z) = cos(z)

Output:

.. code-block:: cpp

    -1.5708 + 0j
    3.00294e-10 + 0j

**References**

.. [1] "Gradient descent", Wikipedia,
        https://en.wikipedia.org/wiki/Gradient_descent