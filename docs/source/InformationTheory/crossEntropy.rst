
crossEntropy
=====

.. cpp:function:: constexpr double crossEntropy(const std::vector<Complex>& X, const std::vector<Complex>& Y) noexcept

   Calculates the cross-entropy [1]_ of two complex sequences.

**Parameters**

    .. cpp:var:: const std::vector<Complex>& X

        A complex sequence.

    .. cpp:var:: const std::vector<Complex>& Y

        A complex sequence.

**Returns**

    .. cpp:type:: double

        A real number.

In information theory, the cross-entropy of two discrete random variables is defined as: 

.. math::

    H(p, q) = -\sum_{x \in \mathcal{X}}p(x)\log q(x)

Both sequences are normalized beforehand.

**Example**

.. code-block:: cpp

    std::vector<Complex> X = {1, 2, 3, 4, 5};
    std::vector<Complex> Y = {1, 2, 3, 4, 5};

    std::cout << klDiv(X, Y) << "\n";

Output:

.. code-block:: cpp

    1.48975

**References**

.. [1] "Cross-entropy", Wikipedia,
        https://en.wikipedia.org/wiki/Cross-entropy