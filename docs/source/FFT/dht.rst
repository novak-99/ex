
dht
=====

.. cpp:function:: constexpr std::vector<Complex> dht(const std::vector<Complex>& X, int type = 2) noexcept

   Calculates the discrete Hilbert transform [1]_ of a complex sequence. 

**Parameters**

    .. cpp:var:: const std::vector<Complex>& X

        A complex sequence.

**Returns**

    .. cpp:type:: std::vector<Complex>

        A complex sequence.

Cpplex extends the Hilbert transform to accept complex sequences using the method described here [2]_.

**Example**

.. code-block:: cpp

    std::vector<Complex> X = {1 + 2_j, 2 + 3_j, 3, 4, 5};
    std::vector<Complex> Y = dht(X); 

    for(int i = 0; i < Y.size(); i++){
        std::cout << Y[i] << "\n";
    }

Output:

.. code-block:: cpp

    1.7013 - 1.84661j
    -1.37638 + 1.23107j
    -0.649839 + 1.55599j
    -1.37638 - 0.145309j
    1.7013 - 0.795148j

**References**

.. [1] "Hilbert transform", Wikipedia,
        https://en.wikipedia.org/wiki/Hilbert_transform
.. [2] https://dsp.stackexchange.com/questions/29263/is-hilbert-transform-not-defined-for-complex-signals