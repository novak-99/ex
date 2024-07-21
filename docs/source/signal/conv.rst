
Conv
=====

.. cpp:function:: constexpr std::vector<Complex> conv(const std::vector<Complex>& X, const std::vector<Complex>& Y) noexcept

   Performs the discrete convolution operation [1]_ on two complex sequences. 

**Parameters**

    .. cpp:var:: const std::vector<Complex>& X

        A complex sequence. 

    .. cpp:var:: const std::vector<Complex>& Y

        A complex sequence. 

    .. cpp:var:: const std::vector<Complex>& X

        A complex sequence

**Returns**

    .. cpp:type:: Complex

        A complex number. 

The discrete convolution operation performs the following operation on two complex sequences :math:`X` of size :math:`M` and :math:`Y` of size :math:`N`:

.. math::

    (X * Y)[n] = \sum_{-\infty}^{\infty}X[m]Y[n - m]

Undefined elements :math:`X[i]` and :math:`Y[j]` are simply set to 0. The implementation is made to be of order :math:`O(\log n)` by using the convolution theorem [2]_. Namely:

.. math::

    (X * Y)[n] = \mathcal{F}^{-1}\{\mathcal{F}\{X\} \cdot \mathcal{F}\{Y\}\}[n]

**Example**

.. code-block:: cpp

    std::vector<Complex> X = {1,2,3,4,5};
    std::vector<Complex> Y = {6,7,8,9,10}; 

    std::vector<Complex> Z = conv(X, Y); 

    for(int i = 0; i < Z.size(); i++){
        std::cout << Z[i] << "\n";
    }

Output:

.. code-block:: cpp

    6 - 6.31594e-14j
    19 - 8.76899e-14j
    40 - 6.86494e-14j
    70 - 7.37113e-14j
    110 - 4.24525e-14j
    114 - 7.15218e-14j
    106 + 2.82558e-14j
    85 - 3.46293e-14j
    50 + 1.14414e-14j

**References**

.. [1] "Convolution", Wikipedia,
        https://en.wikipedia.org/wiki/Convolution
.. [1] "Convolution theorem", Wikipedia,
        https://en.wikipedia.org/wiki/Convolution_theorem