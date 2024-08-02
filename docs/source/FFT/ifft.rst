
ifft
=====

.. cpp:function:: constexpr std::vector<Complex> ifft(const std::vector<Complex>& X) noexcept

   Calculates the inverse fast Fourier transform [1]_ of a complex sequence. 

**Parameters**

    .. cpp:var:: const std::vector<Complex>& X

        A complex sequence.

**Returns**

    .. cpp:type:: std::vector<Complex>

        A complex sequence.

The fast inverse Fourier transform performs the discrete Fourier transform, defined as follows:

.. math::

    \DeclareMathOperator\H{H}
    X_k = \frac{1}{n}\sum_{m = 0}^{n - 1}x_m e^{2\pi km/n} \quad k = 0, \ldots, n-1,

The transform is made to perform in :math:`O(n\log(n))` time using the Cooley-Tukey algorithm [2]_.

**Example**

.. code-block:: cpp

    std::vector<Complex> X = {1 + 2_j, 2 + 3_j, 3, 4, 5};
    std::vector<Complex> Y = fft(X);

    for(int i = 0; i < Y.size(); i++){
        std::cout << Y[i] << "\n";
    }

Output:

.. code-block:: cpp

    15 + 5j
    0.35317 + 6.36801j
    -0.736644 + 0.385248j
    -4.26336 - 1.23935j
    -5.35317 - 0.513904j

**References**

.. [1] "Fast Fourier transform", Wikipedia,
        https://en.wikipedia.org/wiki/Fast_Fourier_transform
.. [2] "Cooley-Tukey FFT algorithm", Wikipedia,
        https://en.wikipedia.org/wiki/Cooley%E2%80%93Tukey_FFT_algorithm