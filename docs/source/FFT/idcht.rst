
idcht
=====

.. cpp:function:: constexpr std::vector<Complex> idcht(const std::vector<Complex>& X, int type = 2) noexcept

   Calculates the inverse discrete Chebyshev transform [1]_ of a complex sequence. 

**Parameters**

    .. cpp:var:: const std::vector<Complex>& X

        A complex sequence.

**Returns**

    .. cpp:type:: std::vector<Complex>

        A complex sequence.

The discrete Chebyshev transform may be calculated by scaling the input sequence by a factor of :math:`\sqrt{N/2}` and the first element by :math:`\sqrt{2}` and applying an IDCT type 2 to the result.

**Example**

.. code-block:: cpp

    std::vector<Complex> X = {1 + 2_j, 2 + 3_j, 3, 4, 5};
    std::vector<Complex> Y = idcht(X); 

    for(int i = 0; i < Y.size(); i++){
        std::cout << Y[i] << "\n";
    }

Output:

.. code-block:: cpp

    27.129 + 11.2586j
    -22.9178 + 7.81229j
    7.44259 + 2.23607j
    -6.2927 - 3.34015j
    0.229061 - 6.78645j

**References**

.. [1] "Discrete Chebyshev transform", Wikipedia,
        https://en.wikipedia.org/wiki/Discrete_Chebyshev_transform