
sgn
=====

.. cpp:function:: constexpr Complex sgn(const Complex& z) noexcept

   Returns the complex sign function [1]_ of a complex number :math:`z`.

**Parameters**

   .. cpp:var:: const Complex& z

        A complex number. 
        
**Returns**

    .. cpp:type:: Complex

        A complex number. 

The sign function of a complex number is defined as:

.. math::

   \DeclareMathOperator\sgn{sgn}
   \sgn(z) = \frac{z}{|z|}

**Example**

.. code-block:: cpp

   Complex z = 3 + 4_j;
   std::cout << sgn(z) << "\n";

Output:

.. code-block:: cpp

   0.6 + 0.8j

**References**

.. [1]  Weisstein, Eric W. "Sign." From MathWorld--A Wolfram Web Resource. 
        https://mathworld.wolfram.com/Sign.html