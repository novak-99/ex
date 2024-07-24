
Decomp
=====

.. cpp:function:: constexpr constexpr std::pair<std::vector<double>, std::vector<double>> decomp(const std::vector<Complex>& X){

   Decomposes complex sequence into its real and imaginary components.

**Parameters**

    .. cpp:var:: const std::vector<Complex>& X

        A complex sequence.

**Returns**

    .. cpp:type:: std::pair<std::vector<double>, std::vector<double>>

        The real and imaginary seqeunces.


**Example**

.. code-block:: cpp

    std::vector<Complex> X = {1 + 2_j, 2 + 3_j, 3, 4, 5};

    int n = X.size();
    auto [reX, imX] = decomp(X);

    for(int i = 0; i < n; i++){
        std::cout << reX[i] << " " << imX[i] << "\n";
    }

Output:

.. code-block:: cpp

    1 2
    2 3
    3 0
    4 0
    5 0