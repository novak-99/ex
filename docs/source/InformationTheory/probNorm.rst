
probNorm
=====

.. cpp:function:: constexpr std::vector<double> probNorm(const std::vector<double>& X) noexcept

   Normalizes a sequence.

**Parameters**

    .. cpp:var:: const std::vector<double>& X

        A real sequence.

**Returns**

    .. cpp:type:: std::vector<double>

        A real sequence.

This function normalizes a sequence such that its elements sum to one. 


**Example**

.. code-block:: cpp

    std::vector<double> X = {1, 2, 3, 4, 5};

    std::vector<double> normX = probNorm(X); 

    for(int i = 0; i < normX.size(); i++){
        std::cout << normX[i] << "\n";
    }

Output:

.. code-block:: cpp

   0.0666667
   0.133333
   0.2
   0.266667
   0.333333