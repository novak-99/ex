
klDiv (Continuous)
=====

.. cpp:function:: constexpr double klDiv(Complex (*fr)(Complex), Complex (*fi)(Complex), Complex (*gr)(Complex), Complex (*gi)(Complex), double a, double b) noexcept

   Calculates the continuous Kullback-Leibler (KL) divergence [1]_ of a function.  

**Parameters**

    .. cpp:var:: Complex (*fr)(Complex)

        The PDF of the first real distribution.

    .. cpp:var:: Complex (*fi)(Complex)

        The PDF of the first imaginary distribution.

    .. cpp:var:: Complex (*gr)(Complex)

        The PDF of the second real distribution.

    .. cpp:var:: Complex (*gi)(Complex)

        The PDF of the second imaginary distribution.

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

    auto pdfRe1 = [](Complex z) { return exp(-z * z); }; // Example real PDF 1. 
    auto pdfRe2 = [](Complex z) { return exp(-z * z); }; // Example real PDF 2. 
    auto pdfIm1 = [](Complex z) { return exp(-z * z); }; // Example im PDF 1. 
    auto pdfIm2 = [](Complex z) { return exp(-z * z); }; // Example im PDF 2. 
    std::cout << klDiv(pdfRe1, pdfIm1, pdfRe2, pdfIm2, -INF.real(), INF.real()) << "\n";

Output:

.. code-block:: cpp

    -1.60699e-07

**References**

.. [1] "Kullback–Leibler divergence", Wikipedia,
        https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence