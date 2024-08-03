
jsDiv (Continuous)
=====

.. cpp:function:: constexpr double jsDiv(Complex (*fr)(Complex), Complex (*fi)(Complex), Complex (*gr)(Complex), Complex (*gi)(Complex), double a, double b) noexcept

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

In information theory, the Jensen-Shannon divergence of two continuous probability distributions is defined as: 

.. math::

    \DeclareMathOperator\JSD{JSD}
    JSD(P || Q) = \frac{1}{2}D(P || M) + \frac{1}{2}D(Q || M)

where :math:`M = \frac{1}{2}(P + Q)` and where `D(P || Q)` is the Kullback-Leibler divergence.

**Example**

.. code-block:: cpp

    auto pdfRe1 = [](Complex z) { return exp(-z * z); }; // Example real PDF 1. 
    auto pdfRe2 = [](Complex z) { return exp(-z * z); }; // Example real PDF 2. 
    auto pdfIm1 = [](Complex z) { return exp(-z * z); }; // Example im PDF 1. 
    auto pdfIm2 = [](Complex z) { return exp(-z * z); }; // Example im PDF 2. 
    std::cout << jsDiv(pdfRe1, pdfIm1, pdfRe2, pdfIm2, -INF.real(), INF.real()) << "\n";

Output:

.. code-block:: cpp

    -1.60699e-07

**References**

.. [1] "Jensen–Shannon divergence", Wikipedia,
        https://en.wikipedia.org/wiki/Jensen%E2%80%93Shannon_divergence