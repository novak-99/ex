
dhat
=====

.. cpp:function:: constexpr std::vector<Complex> dhat(const std::vector<Complex>& X, int type = 2) noexcept

   Calculates the discrete Hartley transform [1]_ of a complex sequence. 

**Parameters**

    .. cpp:var:: const std::vector<Complex>& X

        A complex sequence.

**Returns**

    .. cpp:type:: std::vector<Complex>

        A complex sequence.

The discrete Hartley transform may be calculated by multiplying the result of an FFT on the input by :math:`1 + 1i`.

**Example**

.. code-block:: cpp

    std::vector<Complex> X = {1 + 2_j, 2 + 3_j, 3, 4, 5};
    std::vector<Complex> Y = dhat(X); 

    for(int i = 0; i < Y.size(); i++){
        std::cout << Y[i] << "\n";
    }

Output:

.. code-block:: cpp

    15 + 5j
    -5.94095 + 5.78022j
    -3.3123 + 1.3363j
    -1.6877 - 2.19041j
    0.940955 + 0.0738814j

**References**

.. [1] "Discrete Hartley transform", Wikipedia,
        https://en.wikipedia.org/wiki/Discrete_Hartley_transform