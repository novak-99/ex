
entropy (Continuous)
=====

.. cpp:function:: constexpr double entropy(Complex (*fr)(Complex), Complex (*fi)(Complex), double a, double b) noexcept

   Calculates the continuous entropy [1]_ of a function.  

**Parameters**

    .. cpp:var:: Complex (*fr)(Complex)

        The PDF of the real distribution.

    .. cpp:var:: Complex (*fi)(Complex)

        The PDF of the imaginary distribution.

    .. cpp:var:: double a

        A real number.

    .. cpp:var:: double b

        A real number.

**Returns**

    .. cpp:type:: double

        A real number.

In information theory, the entropy of a continuous random variable is defined as: 

.. math::

    \DeclareMathOperator\H{H}
    H(X) = -\int_{\mathcal{X}}f(x)\log f(x)dx

**Example**

.. code-block:: cpp

    auto pdfRe = [](Complex z) { return exp(-z * z); }; // Example PDF. 
    auto pdfIm = [](Complex z) { return exp(-z * z); }; // Example PDF. 
    std::cout << entropy(pdfRe, pdfIm, -INF.real(), INF.real()) << "\n";
    std::cout << -std::sqrt(M_PI) << "\n";

Output:

.. code-block:: cpp

    -1.77102
    -1.77245

**References**

.. [1] "Differential entropy", Wikipedia,
        https://en.wikipedia.org/wiki/Differential_entropy