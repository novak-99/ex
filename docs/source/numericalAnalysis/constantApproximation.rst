
ConstantApproximation
=====

.. cpp:function:: constexpr Complex constantApproximation(Complex (*f)(Complex), const Complex& z) noexcept

   Evaluates the constant Taylor approximation of a complex function at a point :math:`z` [1]_.

**Parameters**

    .. cpp:var:: Complex (*f)(Complex)

        The function to approximate. 

    .. cpp:var:: const Complex& z0

        The complex point at which to center the approximation. 

**Returns**

    .. cpp:type:: Complex

        A complex number. 

This function simply returns the function :math:`f` evaluated at a point :math:`z_0`, that is:

.. math::
   f(z) \approx f(z_0)

**Example**

.. code-block:: cpp

    auto fn = [](Complex z) { return sin(z); }; 
    std::cout << constantApproximation(fn, 1 + 1_j) << "\n";

Output:

.. code-block:: cpp

    1.29846 + 0.634964j

**References**

.. [1] "3.4: Approximating Functions Near a Specified Point — Taylor Polynomials", LibreTexts,
        https://math.libretexts.org/Bookshelves/Calculus/CLP-1_Differential_Calculus_(Feldman_Rechnitzer_and_Yeager)/04%3A_Applications_of_derivatives/4.04%3A_Approximating_Functions_Near_a_Specified_Point__Taylor_Polynomials