
Conj
=====

.. cpp:function:: constexpr std::vector<double> probNorm(const std::vector<double>& X){

   Returns the conjugate of a complex sequence.

**Parameters**

    .. cpp:var:: const std::vector<Complex>& X

        A complex sequence.

**Returns**

    .. cpp:type:: std::vector<Complex>

**Example**

.. code-block:: cpp

    std::vector<Complex> X = {1 + 2_j, 2 + 3_j, 3, 4, 5};
    std::vector<Complex> conjX = conj(X);

    for(int i = 0; i < conjX.size(); i++){
        std::cout << conjX[i] << "\n";
    }

Output:

.. code-block:: cpp

    1 - 2j
    2 - 3j
    3 - 0j
    4 - 0j
    5 - 0j