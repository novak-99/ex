
dct
=====

.. cpp:function:: constexpr std::vector<Complex> dct(const std::vector<Complex>& X, int type = 2) noexcept

   Calculates the discrete cosine transform [1]_ of a complex sequence. 

**Parameters**

    .. cpp:var:: const std::vector<Complex>& X

        A complex sequence.

    .. cpp:var:: int type

        Optional integer specifying the type of DCT. Set to 2 by default.

**Returns**

    .. cpp:type:: std::vector<Complex>

        A complex sequence.

The discrete cosine transform performs the following operation:

.. math::

    \DeclareMathOperator\H{H}
    X_k = \sum_{n = 0}^{N - 1}x_n \cos[\frac{\pi}{N}(n + \frac{1}{2})k] \quad k = 0, \ldots, n-1,

The formula slightly modified depending on the type. DCT type 4 was implemented using the algorithm described here [2]_.

**Example**

.. code-block:: cpp

    std::vector<Complex> X = {1 + 2_j, 2 + 3_j, 3, 4, 5};
    std::vector<Complex> Y = dct(X, 2); // it's 2 by default.

    for(int i = 0; i < Y.size(); i++){
        std::cout << Y[i] << "\n";
    }

Output:

.. code-block:: cpp

    30 + 10j
    -9.95959 + 7.33094j
    2.61516e-15 + 1.38197j
    -0.898056 - 3.3552j
    -2.94604e-15 - 3.61803j

**References**

.. [1] "Discrete cosine transform", Wikipedia,
        https://en.wikipedia.org/wiki/Discrete_cosine_transform
.. [2] https://github.com/ARM-software/CMSIS_4/blob/master/CMSIS/DSP_Lib/Source/TransformFunctions/arm_dct4_f32.c