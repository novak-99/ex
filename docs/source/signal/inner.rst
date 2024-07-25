
inner
=====

.. cpp:function:: constexpr std::vector<Complex> inner(const std::vector<Complex>& X, const std::vector<Complex>& Y) noexcept

   Performs the discrete inner product [1]_ on two complex sequences. 

**Parameters**

    .. cpp:var:: const std::vector<Complex>& X

        A complex sequence. 

    .. cpp:var:: const std::vector<Complex>& Y

        A complex sequence. 

**Returns**

    .. cpp:var:: Complex

        A complex number. 

The discrete inner product performs the following operation on two sequences :math:`X` and :math:`Y`:

.. math::

    \newcommand{\compconj}[1]{%
    \overline{#1}%
    }
    \langle X, Y \rangle = X \cdot \compconj{Y}

**Example**

.. code-block:: cpp

    std::vector<Complex> X = {1, 2, 3, 4, 5};
    std::vector<Complex> Y = {1 + 5_j, 2 + 1_j, 3, 4, 5};

    std::cout << inner(X, Y) << "\n"; 

Output:

.. code-block:: cpp

    55 - 7j

**References**

.. [1] "Inner product space", Wikipedia,
        https://en.wikipedia.org/wiki/Inner_product_space