
Entropy
=====

.. cpp:function:: constexpr double entropy(const std::vector<Complex>& X) noexcept

   Calculates the discrete entropy [1]_ of a complex sequence. 

**Parameters**

    .. cpp:var:: const std::vector<Complex>& X

        A real sequence.

**Returns**

    .. cpp:type:: double

        A real number.

In information theory, the entropy of a discrete random variable is defined as: 

.. math::

    \DeclareMathOperator\H{H}
    H(X) = -\sum_{x \in \mathcal{X}}p(x)\log p(x)

The sequence X is normalized beforehand. The summand is defined to be :math:`0` for :math:`p(x) = 0` and the summation is set to :math:`-\infty` if a negative probability is present.

**Example**

.. code-block:: cpp

    std::vector<Complex> X = {1 + 1_j, 2, 3, 4, 5};

    std::cout << entropy(X) << "\n";

Output:

.. code-block:: cpp

    1.48975

**References**

.. [1] "Entropy (information theory)", Wikipedia,
        https://en.wikipedia.org/wiki/Entropy_(information_theory)