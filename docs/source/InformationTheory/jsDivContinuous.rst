
jsDiv (Continuous)
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

In information theory, the Jensen-Shannon divergence of two continuous probability distributions is defined as: 

.. math::

    \DeclareMathOperator\JSD{JSD}
    JSD(P || Q) = \frac{1}{2}D(P || M) + \frac{1}{2}D(Q || M)

where :math:`M = \frac{1}{2}(P + Q)` and where `D(P || Q)` is the Kullback-Leibler divergence.

**Example**

.. code-block:: cpp

    auto pdf1 = [](Complex z) { return exp(-z * z); }; // Example PDF 1. 
    auto pdf2 = [](Complex z) { return exp(-z * z); }; // Example PDF 2. 
    std::cout << klDiv(pdf1, pdf2, -INF.real(), INF.real()) << "\n";

Output:

.. code-block:: cpp

    -8.03496e-08

**References**

.. [1] "Jensen–Shannon divergence", Wikipedia,
        https://en.wikipedia.org/wiki/Jensen%E2%80%93Shannon_divergence