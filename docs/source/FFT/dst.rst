
dst
=====

.. cpp:function:: constexpr std::vector<Complex> dst(const std::vector<Complex>& X, int type = 2) noexcept

   Calculates the discrete sine transform [1]_ of a complex sequence. 

**Parameters**

    .. cpp:var:: const std::vector<Complex>& X

        A complex sequence.

    .. cpp:var:: int type

        Optional integer specifying the type of DST. Set to 2 by default.

**Returns**

    .. cpp:type:: std::vector<Complex>

        A complex sequence.

The discrete sine transform performs the following operation:

.. math::

    \DeclareMathOperator\H{H}
    X_k = \sum_{n = 0}^{N - 1}x_n \sin[\frac{\pi}{N}(n + \frac{1}{2})(k + 1)] \quad k = 0, \ldots, n-1,

The formula slightly modified depending on the type.

**Example**

.. code-block:: cpp

    std::vector<Complex> X = {1 + 2_j, 2 + 3_j, 3, 4, 5};
    std::vector<Complex> Y = dst(X, 2); // it's 2 by default.

    for(int i = 0; i < Y.size(); i++){
        std::cout << Y[i] << "\n";
    }

Output:

.. code-block:: cpp

    19.4164 + 6.09017j
    -8.50651 + 8.05748j
    7.41641 + 5.09017j
    -5.25731 + 0.277515j
    6 - 2j

**References**

.. [1] "Discrete sine transform", Wikipedia,
        https://en.wikipedia.org/wiki/Discrete_sine_transform