
tan
=====

.. cpp:function:: constexpr Complex tan(const Complex& z) noexcept

   Returns the complex tan [1]_ of a complex number :math:`z`.

**Parameters**

   .. cpp:var:: const Complex& z

        A complex number. 
        
**Returns**

    .. cpp:type:: Complex

        A complex number. 

The sin function of a complex number is defined as:

.. math::
   \tan z = \frac{\sin z}{\cos z}

**Example**

.. code-block:: cpp

   Complex z = 3 + 4_j;
   std::cout << tan(z) << "\n";

Output:

.. code-block:: cpp

   -0.000187346 + 0.999356j

**References**

.. [1]  Weisstein, Eric W. "Tangent." From MathWorld--A Wolfram Web Resource. 
        https://mathworld.wolfram.com/Tangent.html