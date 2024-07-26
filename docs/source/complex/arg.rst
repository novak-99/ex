
arg
=====

.. cpp:function:: constexpr double arg(const Complex& z) noexcept

   Returns the magnitude [1]_ of a complex number :math:`z`.

**Parameters**

   .. cpp:var:: const Complex& z

        A complex number. 

**Returns**

    .. cpp:type:: Complex

        A complex number. 

The arg, or argument of a complex number, is defined as follows:

.. math::
   \DeclareMathOperator\arg{arg}
   \DeclareMathOperator\atan2{atan2}
   \arg(z) = \atan2(x, y)


**Example**

.. code-block:: cpp

   Complex z = 3 + 4_j;
   std::cout << arg(z) << "\n";

Output:

.. code-block:: cpp

   0.927295

**References**

.. [1] "Argument (complex analysis)", Wikipedia,
        https://en.wikipedia.org/wiki/Argument_(complex_analysis)