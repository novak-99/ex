
idct
=====

.. cpp:function:: constexpr std::vector<Complex> dct(const std::vector<Complex>& X, int type = 2) noexcept

   Calculates the inverse discrete cosine transform [1]_ of a complex sequence. 

**Parameters**

    .. cpp:var:: const std::vector<Complex>& X

        A complex sequence.

    .. cpp:var:: int type

        Optional integer specifying the type of IDCT. Set to 2 by default.

**Returns**

    .. cpp:type:: std::vector<Complex>

        A complex sequence.

The inverse discrete cosine transform returns itself for DCT types 1 and 4, returns DCT type 3 for DCT type 2, and returns DCT type 2 for DCT type 3.

**Example**

.. code-block:: cpp

    std::vector<Complex> X = {1 + 2_j, 2 + 3_j, 3, 4, 5};
    std::vector<Complex> Y = idct(X, 2); // it's 2 by default.

    for(int i = 0; i < Y.size(); i++){
        std::cout << Y[i] << "\n";
    }

Output:

.. code-block:: cpp

    17.4508 + 7.70634j
    -14.2016 + 5.52671j
    5 + 2j
    -3.68696 - 1.52671j
    0.437764 - 3.70634j

**References**

.. [1] "Discrete cosine transform", Wikipedia,
        https://en.wikipedia.org/wiki/Discrete_cosine_transform