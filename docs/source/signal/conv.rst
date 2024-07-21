
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

    (X * Y)[n] = \sum_{-\infty}^{\infty}X(m)Y(n - m)

Undefined elements :math:`X[i]` and :math:`Y[j]` are simply set to 0. The implementation is made to be of order :math:`O(\log n)` by using the convolution theorem [2]_. Namely:

.. math::

    (X * Y)[n] = \mathcal{F}^-1{\mathcal{F}(X) \cdot \mathcal{F}{Y}}[n]

**Example**

.. code-block:: cpp

   auto f = [](Complex t) { return exp(-t * t); };
   auto g = [](Complex t) { return exp(-t * t); };


   Complex z = 1; 
   std::cout << conv(f, g, z) << "\n";

Output:

.. code-block:: cpp

   0.760276 + 0j

**References**

.. [1] "Convolution", Wikipedia,
        https://en.wikipedia.org/wiki/Convolution
.. [1] "Convolution theorem", Wikipedia,
        https://en.wikipedia.org/wiki/Convolution_theorem