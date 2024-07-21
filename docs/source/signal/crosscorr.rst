
Crosscorr
=====

.. cpp:function:: constexpr std::vector<Complex> crosscorr(const std::vector<Complex>& X, const std::vector<Complex>& Y) noexcept

   Performs the discrete cross-correlation operation [1]_ on two complex sequences. 

**Parameters**

    .. cpp:var:: const std::vector<Complex>& X

        A complex sequence. 

    .. cpp:var:: const std::vector<Complex>& Y

        A complex sequence. 

**Returns**

    .. cpp:var:: std::vector<Complex>

        A complex sequence. 

The discrete cross-correlation operation performs the following operation on two complex sequences :math:`X` of size :math:`M` and :math:`Y` of size :math:`N`:

.. math::

    \newcommand{\compconj}[1]{%
    \overline{#1}%
    }
    (X \star Y)[n] = \sum_{-\infty}^{\infty}\compconj{X[m]}Y[n + m]

Undefined elements :math:`X[i]` and :math:`Y[j]` are simply set to :math:`0`. The implementation is made to be of order :math:`O(\log n)` by using the FFT and IFFT operations. 

**Example**

.. code-block:: cpp

    std::vector<Complex> X = {1,2,3,4,5};
    std::vector<Complex> Y = {6,7,8,9,10}; 

    std::vector<Complex> Z = crosscorr(X, Y); 

    for(int i = 0; i < Z.size(); i++){
        std::cout << Z[i] << "\n";
    }

Output:

.. code-block:: cpp

    10 - 4.42115e-14j
    29 - 7.30271e-14j
    56 - 7.34605e-14j
    90 - 7.28331e-14j
    130 - 5.1625e-14j
    110 - 6.48994e-14j
    86 + 1.72943e-14j
    59 + 5.11417e-15j
    30 + 1.30617e-14j

**References**

.. [1] "Cross-correlation", Wikipedia,
        https://en.wikipedia.org/wiki/Cross-correlation