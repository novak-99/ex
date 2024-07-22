
Entropy (Continuous)
=====

.. cpp:function:: constexpr double entropy(Complex (*f)(Complex), double a, double b)

   Calculates the continuous entropy [1]_ of a function.  

**Parameters**

    .. cpp:var:: Complex (*f)(Complex)

        The PDF of the distribution.

    .. cpp:var:: double a

        A real number.

    .. cpp:var:: double b

        A real number.

**Returns**

    .. cpp:type:: double

        A real number.

In information theory, the entropy of a continuous random variable is defined as: 

.. math::

    \DeclareMathOperator\H{H}
    H(X) = -\int_{\mathcal{X}}f(x)\log f(x)dx

**Example**

.. code-block:: cpp

    std::vector<Complex> X = {1 + 1_j, 2, 3, 4, 5};

    std::cout << entropy(X) << "\n";

Output:

.. code-block:: cpp

    1.48975

**References**

.. [1] "Differential entropy", Wikipedia,
        https://en.wikipedia.org/wiki/Differential_entropy