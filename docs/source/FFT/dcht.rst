
dcht
=====

.. cpp:function:: constexpr std::vector<Complex> dcht(const std::vector<Complex>& X, int type = 2) noexcept

   Calculates the discrete Chebyshev transform [1]_ of a complex sequence. 

**Parameters**

    .. cpp:var:: const std::vector<Complex>& X

        A complex sequence.

**Returns**

    .. cpp:type:: std::vector<Complex>

        A complex sequence.

The discrete Chebyshev transform may be calculated by scaling the result of a DCT type 2 by a factor of :math:`\sqrt{2/N}` and the first element by :math:`1/\sqrt{2}`.

**Example**

.. code-block:: cpp

    std::vector<Complex> X = {1 + 2_j, 2 + 3_j, 3, 4, 5};
    std::vector<Complex> Y = dcht(X); 

    for(int i = 0; i < Y.size(); i++){
        std::cout << Y[i] << "\n";
    }

Output:

.. code-block:: cpp

    13.4164 + 4.47214j
    -6.299 + 4.63649j
    1.65398e-15 + 0.874032j
    -0.56798 - 2.12201j
    -1.86324e-15 - 2.2882

**References**

.. [1] "Discrete Chebyshev transform", Wikipedia,
        https://en.wikipedia.org/wiki/Discrete_Chebyshev_transform