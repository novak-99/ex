
rootsOfUnity
=====

.. cpp:function:: constexpr std::vector<Complex> rootsOfUnity(const int q) noexcept

   Returns the roots of unity [1]_ for a positive integer :math:`q`.

**Parameters**

   .. cpp:var:: const int q

        A positive integer denoting the power.
        
**Returns**

    .. cpp:type:: std::vector<Complex>

        A complex sequence. The list of the roots of unity.

The roots of unity are the complex numbers that satisfy the equation:

.. math::

   z^q = 1

The equation has the following :math:`q` solutions:

.. math::

   1^{1/q} = e^{i2\pi (k/q)} \quad k = 0, \ldots, q-1,

**Example**

.. code-block:: cpp

    int q = 3;
    std::vector<Complex> roots = rootsOfUnity(q); // Cube roots of unity
    for(int i = 0; i < q; i++) {
        std::cout << roots[i] << "\n";
    }

Output:

.. code-block:: cpp

   1 + 0j
   -0.5 + 0.866025j
   -0.5 - 0.866025j

**References**

.. [1] "Complex Analysis", José Figueroa-O'Farrill,
        https://www.maths.ed.ac.uk/~jmf/Teaching/MT3/ComplexAnalysis.pdf