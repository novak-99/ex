
binaryEntropy
=====

.. cpp:function:: inline double binaryEntropy(const double p) noexcept

   Calculates the discrete binary entropy [1]_ of a probability.

**Parameters**

    .. cpp:var:: const double p

        A real number between 0 and 1 inclusive.

**Returns**

    .. cpp:type:: double

        A real number.

The binary entropy of a probability :math:`p` is defined as follows:

.. math::

    \DeclareMathOperator\H{H}
    H(X) = -p\log(p) + (1 - p)\log(1 - p)

**Example**

.. code-block:: cpp

    std::cout << binaryEntropy(0.5) << "\n";

Output:

.. code-block:: cpp

    0.693147

**References**

.. [1] "Binary entropy function", Wikipedia,
        https://en.wikipedia.org/wiki/Binary_entropy_function