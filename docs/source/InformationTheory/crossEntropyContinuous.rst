
crossEntropy (Continuous)
=====

.. cpp:function:: constexpr double crossEntropy(Complex (*fr)(Complex), Complex (*fi)(Complex), Complex (*gr)(Complex), Complex (*gi)(Complex), double a, double b) noexcept

   Calculates the continuous cross-entropy [1]_ of a function.  

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

In information theory, the cross entropy of two continuous probability distributions is defined as: 

.. math::

    H(p, q) = -\int_{\mathcal{X}}p(x)\log q(x)dx

**Example**

.. code-block:: cpp

    auto pdfRe1 = [](Complex z) { return exp(-z * z); }; // Example real PDF 1. 
    auto pdfRe2 = [](Complex z) { return exp(-z * z); }; // Example real PDF 2. 
    auto pdfIm1 = [](Complex z) { return exp(-z * z); }; // Example im PDF 1. 
    auto pdfIm2 = [](Complex z) { return exp(-z * z); }; // Example im PDF 2. 
    std::cout << crossEntropy(pdfRe1, pdfIm1, pdfRe2, pdfIm2, -INF.real(), INF.real()) << "\n";

Output:

.. code-block:: cpp

    -1.60699e-07

**References**

.. [1] "Cross-entropy", Wikipedia,
        https://en.wikipedia.org/wiki/Cross-entropy