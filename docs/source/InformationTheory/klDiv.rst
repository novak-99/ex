
klDiv
=====

.. cpp:function:: constexpr double klDiv(const std::vector<Complex>& X, const std::vector<Complex>& Y) noexcept

   Calculates the Kullback–Leibler (KL) divergence [1]_ of two complex sequences.

**Parameters**

    .. cpp:var:: const std::vector<Complex>& X

        A complex sequence.

    .. cpp:var:: const std::vector<Complex>& Y

        A complex sequence.

**Returns**

    .. cpp:type:: double

        A real number.

In information theory, the KL divergence of two discrete random variables is defined as: 

.. math::

    \DeclareMathOperator\KL{KL}
    D_{\KL}(P || Q) = -\sum_{x \in \mathcal{X}}P(x)\log(\frac{P(x)}{Q(x)})

Both sequences are normalized beforehand.

**Example**

.. code-block:: cpp

    std::vector<Complex> X = {1, 2, 3, 4, 5};
    std::vector<Complex> Y = {1, 2, 3, 4, 5};

    std::cout << klDiv(X, Y) << "\n";

Output:

.. code-block:: cpp

    0

**References**

.. [1] "Kullback-Leibler divergence", Wikipedia,
        https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence