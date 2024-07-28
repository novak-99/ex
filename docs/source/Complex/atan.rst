
atan
=====

.. cpp:function:: constexpr Complex atan(const Complex& z) noexcept

   Returns the complex inverse tan [1]_ of a complex number :math:`z`.

**Parameters**

   .. cpp:var:: const Complex& z

        A complex number. 
        
**Returns**

    .. cpp:type:: Complex

        A complex number. 

The inverse tangent function of a complex number is defined as:

.. math::

   \tan^{-1}z =  \frac{1}{2}i(\log((1 - iz) - \log(1 + iz)))

**Example**

.. code-block:: cpp

   Complex z = 3 + 4_j;
   std::cout << atan(z) << "\n";

Output:

.. code-block:: cpp

   1.44831 + 0.158997j

**References**

.. [1]  Weisstein, Eric W. "Inverse Tangent." From MathWorld--A Wolfram Web Resource. 
        https://mathworld.wolfram.com/InverseTangent.html