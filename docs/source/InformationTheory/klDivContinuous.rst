
klDiv (Continuous)
=====

.. cpp:function:: constexpr double klDiv(Complex (*f)(Complex), Complex (*g)(Complex), double a, double b) noexcept

   Calculates the continuous Kullback-Leibler (KL) divergence [1]_ of a function.  

**Parameters**

    .. cpp:var:: Complex (*f)(Complex)

        The PDF of the first distribution. 

    .. cpp:var:: Complex (*f)(Complex)

        The PDF of the second distribution.

    .. cpp:var:: double a

        A real number.

    .. cpp:var:: double b

        A real number.

**Returns**

    .. cpp:type:: double

        A real number.

In information theory, the KL divergence of two continuous probability distributions is defined as: 

.. math::

    \DeclareMathOperator\KL{KL}
    D_{\KL}(p(x) || q(x)) = -\int_{\mathcal{X}}p(x)\log{\frac{p(x)}{q(x)}}dx

**Example**

.. code-block:: cpp

    auto pdf1 = [](Complex z) { return exp(-z * z); }; // Example PDF 1. 
    auto pdf2 = [](Complex z) { return exp(-z * z); }; // Example PDF 2. 
    std::cout << klDiv(pdf1, pdf2, -INF.real(), INF.real()) << "\n";

Output:

.. code-block:: cpp

    -8.03496e-08

**References**

.. [1] "Kullback–Leibler divergence", Wikipedia,
        https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence