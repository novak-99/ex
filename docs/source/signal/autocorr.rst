
Autocorr
=====

.. cpp:function:: constexpr std::vector<Complex> crosscorr(const std::vector<Complex>& X, const std::vector<Complex>& Y) noexcept

   Performs the discrete auto-correlation operation [1]_ on a compelx sequence.

**Parameters**

    .. cpp:var:: const std::vector<Complex>& X

        A complex sequence. 

    .. cpp:var:: const std::vector<Complex>& Y

        A complex sequence. 

**Returns**

    .. cpp:var:: std::vector<Complex>

        A complex sequence. 

The discrete auto-correlation operation simply performs the cross-correlation using a single sequence :math:`X` for both arguments. 

**Example**

.. code-block:: cpp

    std::vector<Complex> X = {1,2,3,4,5};

    std::vector<Complex> Z = autocorr(X); 

    for(int i = 0; i < Z.size(); i++){
        std::cout << Z[i] << "\n";
    }

Output:

.. code-block:: cpp

    5 - 9.86865e-15j
    14 - 2.11467e-14j
    26 - 3.04381e-14j
    40 - 3.16419e-14j
    55 - 1.323e-14j
    40 - 1.64226e-14j
    26 + 8.21365e-15j
    14 + 1.71718e-14j
    5 + 1.86516e-15j

**References**

.. [1] "Autocorrelation", Wikipedia,
        https://en.wikipedia.org/wiki/Autocorrelation