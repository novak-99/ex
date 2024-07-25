
crossEntropy (Continuous)
=====

.. cpp:function:: constexpr double crossEntropy(Complex (*f)(Complex), Complex (*g)(Complex), double a, double b) noexcept

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

In information theory, the Jensen-Shannon divergence of two discrete random variables is defined as: 

.. math::

    \DeclareMathOperator\JSD{JSD}
    H(p, q) = -\int_{\mathcal{X}}p(x)\log q(x)dx

**Example**

.. code-block:: cpp

    auto pdf1 = [](Complex z) { return exp(-z * z); }; // Example PDF 1. 
    auto pdf2 = [](Complex z) { return exp(-z * z); }; // Example PDF 2. 
    std::cout << crossEntropy(pdf1, pdf2, -INF.real(), INF.real()) << "\n";

Output:

.. code-block:: cpp

    0.88551

**References**

.. [1] "Cross-entropy", Wikipedia,
        https://en.wikipedia.org/wiki/Cross-entropy