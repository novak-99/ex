
QuadraticApproximation
=====

.. cpp:function:: constexpr Complex quadraticApproximation(Complex (*f)(Complex), const Complex& z) noexcept

   Evaluates the quadratic Taylor approximation of a complex function at a point :math:`z` [1]_.

**Parameters**

    .. cpp:var:: Complex (*f)(Complex)

        The function to approximate. 

    .. cpp:var:: const Complex& z0

        The complex point at which to center the approximation. 

    .. cpp:var:: const Complex& z

        The complex point at which to evaluate the approximation.

**Returns**

    .. cpp:type:: Complex

        A complex number. 

This function simply returns the quadratic approximation of :math:`f` evaluated at a point :math:`z`, that is:

.. math::
   f(z) \approx f(z_0) + f'(z_0)(z - z_0) + \frac{1}{2}f''(z_0)(z - z_0)^2

**Example**

.. code-block:: cpp

    auto fn = [](Complex z) { return sin(z); }; // Example PDF 1. 
    std::cout << quadraticApproximation(fn, 1 + 1_j, 1) << "\n";

Output:

.. code-block:: cpp

    0.958789 + 0.118717j

**References**

.. [1] "3.4: Approximating Functions Near a Specified Point — Taylor Polynomials", LibreTexts,
        https://math.libretexts.org/Bookshelves/Calculus/CLP-1_Differential_Calculus_(Feldman_Rechnitzer_and_Yeager)/04%3A_Applications_of_derivatives/4.04%3A_Approximating_Functions_Near_a_Specified_Point__Taylor_Polynomials