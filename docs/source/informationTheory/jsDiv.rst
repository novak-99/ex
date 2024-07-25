
jsDiv
=====

.. cpp:function:: constexpr double jsDiv(const std::vector<Complex>& X, const std::vector<Complex>& Y) noexcept

   Calculates the Jensen-Shannon divergence [1]_ of two complex sequences.

**Parameters**

    .. cpp:var:: const std::vector<Complex>& X

        A complex sequence.

    .. cpp:var:: const std::vector<Complex>& Y

        A complex sequence.

**Returns**

    .. cpp:type:: double

        A real number.

In information theory, the Jensen-Shannon divergence of two discrete random variables is defined as: 

.. math::

    \DeclareMathOperator\JSD{JSD}
    JSD(P || Q) = \frac{1}{2}D(P || M) + \frac{1}{2}D(Q || M)

where :math:`M = \frac{1}{2}(P + Q)` and where `D(P || Q)` is the Kullback-Leibler divergence. Both sequences are normalized beforehand.

**Example**

.. code-block:: cpp

    std::vector<Complex> X = {1, 2, 3, 4, 5};
    std::vector<Complex> Y = {1, 2, 3, 4, 5};

    std::cout << jsDiv(X, Y) << "\n";

Output:

.. code-block:: cpp

    0

**References**

.. [1] "Jensen-Shannon divergence", Wikipedia,
        https://en.wikipedia.org/wiki/Jensen%E2%80%93Shannon_divergence