
asin
=====

.. cpp:function:: constexpr Complex asin(const Complex& z) noexcept

   Returns the complex inverse sin [1]_ of a complex number :math:`z`.

**Parameters**

   .. cpp:var:: const Complex& z

        A complex number. 
        
**Returns**

    .. cpp:type:: Complex

        A complex number. 

The inverse sine function of a complex number is defined as:

.. math::
   \sin^{-1}z =  -i \log(iz + \sqrt{1 - z^2})

**Example**

.. code-block:: cpp

   Complex z = 3 + 4_j;
   std::cout << asin(z) << "\n";

Output:

.. code-block:: cpp

   -0.633984 - 2.30551j

**References**

.. [1]  Weisstein, Eric W. "Inverse Sine." From MathWorld--A Wolfram Web Resource. 
        https://mathworld.wolfram.com/InverseSine.html