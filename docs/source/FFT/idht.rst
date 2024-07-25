
idht
=====

.. cpp:function:: constexpr std::vector<Complex> idht(const std::vector<Complex>& X, int type = 2) noexcept

   Calculates the inverse discrete Hilbert transform [1]_ of a complex sequence. 

**Parameters**

    .. cpp:var:: const std::vector<Complex>& X

        A complex sequence.

**Returns**

    .. cpp:type:: std::vector<Complex>

        A complex sequence.

**Example**

.. code-block:: cpp

    std::vector<Complex> X = {1 + 2_j, 2 + 3_j, 3, 4, 5};
    std::vector<Complex> Y = idht(X); 

    for(int i = 0; i < Y.size(); i++){
        std::cout << Y[i] << "\n";
    }

Output:

.. code-block:: cpp

    0.425325 - 0.461653j
    -0.344095 + 0.307768j
    -0.16246 + 0.388998j
    -0.344095 - 0.0363271j
    0.425325 - 0.198787j

**References**

.. [1] "Hilbert transform", Wikipedia,
        https://en.wikipedia.org/wiki/Hilbert_transform