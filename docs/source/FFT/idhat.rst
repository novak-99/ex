
idhat
=====

.. cpp:function:: constexpr std::vector<Complex> dhat(const std::vector<Complex>& X, int type = 2) noexcept

   Calculates the inverse discrete Hartley transform [1]_ of a complex sequence. 

**Parameters**

    .. cpp:var:: const std::vector<Complex>& X

        A complex sequence.

**Returns**

    .. cpp:type:: std::vector<Complex>

        A complex sequence.

The discrete inverse Hartley transform may be calculated by applying the discrete Hartley transform on the input sequence and scaling the result by :math:`1/N`.

**Example**

.. code-block:: cpp

    std::vector<Complex> X = {1 + 2_j, 2 + 3_j, 3, 4, 5};
    std::vector<Complex> Y = idhat(X); 

    for(int i = 0; i < Y.size(); i++){
        std::cout << Y[i] << "\n";
    }

Output:

.. code-block:: cpp

    3 + 1j
    -1.18819 + 1.15604j
    -0.66246 + 0.267261j
    -0.33754 - 0.438081j
    0.188191 + 0.0147763j

**References**

.. [1] "Discrete Hartley transform", Wikipedia,
        https://en.wikipedia.org/wiki/Discrete_Hartley_transform