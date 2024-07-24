
Integral
=====

.. cpp:function:: constexpr Complex integral(Complex (*f)(Complex,  const std::vector<Complex (*)(Complex)>& fargs, std::vector<Complex>), const Complex& a, const Complex& b) noexcept
.. cpp:function:: constexpr Complex integral(Complex (*f)(Complex,  const std::vector<Complex (*)(Complex)>& fargs, std::vector<Complex>), const Complex& a, const Complex& b,  const std::vector<Complex (*)(Complex)>& fargs) noexcept
.. cpp:function:: constexpr Complex integral(Complex (*f)(Complex,  const std::vector<Complex (*)(Complex)>& fargs, std::vector<Complex>), const Complex& a, const Complex& b, const std::vector<Complex>& args) noexcept
.. cpp:function:: constexpr Complex integral(Complex (*f)(Complex,  const std::vector<Complex (*)(Complex)>& fargs, std::vector<Complex>), const Complex& a, const Complex& b,  const std::vector<Complex (*)(Complex)>& fargs, const std::vector<Complex>& args) noexcept

   Evaluates the integral of a complex function at a point :math:`z` from integral bounds :math:`a` to :math:`b`. The integral is implemented using 15-point Gauss-Kronrod quadrature [1]_.

**Parameters**

    .. cpp:var:: Complex (*f)(Complex)

        The function to differentiate.

    .. cpp:var:: const Complex& z

        A complex number. 

    .. cpp:var:: const Complex& a

        Lower integration bound. Use :cpp:`NINF` from <Constants/Constants.hpp> for :math:`-\infty`.

    .. cpp:var:: const Complex& b

        Upper integration bound. Use :cpp:`INF` from <Constants/Constants.hpp> for :math:`\infty`.

    .. cpp:var:: const std::vector<Complex (*)(Complex)>& fargs

        Optional list of function arguments if needed for use of the integrand.

    .. cpp:var:: const std::vector<Complex>& args

        Optional list of variable arguments if needed for use of the integrand.

**Returns**

    .. cpp:type:: Complex

        A complex number. 

This function evaluates the following definite integral of a function :math:`f`:

.. math::
   \int_{a}^{b} f(z) dz

To approxiate the integral, the following numerical quadrature method is used:

.. math::
   \int_{a}^{b} f(z) dz \approx \sum_{i = 1}^{n}w_if(z_i)

for some pre-tabulated Kronrod weights :math:`w` and evaluation points :math:`z`.

**Example**

.. code-block:: cpp

    auto fn = [](Complex z) { return z*z }; // z^2
    std::cout << integral(fn, 0, 1) << "\n"; // z^3/3 |0 -> 1 = 1/3

Output:

.. code-block:: cpp

    0.333333 + 0j

**References**

.. [1] "Gauss–Kronrod quadrature formula", Wikipedia,
        https://en.wikipedia.org/wiki/Gauss%E2%80%93Kronrod_quadrature_formula