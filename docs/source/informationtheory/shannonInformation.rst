
Entropy
=====

.. cpp:function:: constexpr double shannonInformation(const Complex& z) noexcept

   Calculates the Shannon information content [1]_ of a complex sequence. 

**Parameters**

    .. cpp:var:: const Complex& z

        A complex number.

**Returns**

    .. cpp:type:: double

        A real number.

In information theory, the Shannon information of a discrete random variable is defined as: 

.. math::

    \DeclareMathOperator\I{I}
    I(X) = -\log p(x)

The function returns :math:`-\infty` if the probability is negative or 0. 

**Example**

.. code-block:: cpp

    Complex z = 0.5 + 0.5_j; 

    std::cout << shannonInformation(z) << "\n";

Output:

.. code-block:: cpp

    1.38629

**References**

.. [1] "Information content", Wikipedia,
        https://en.wikipedia.org/wiki/Information_content