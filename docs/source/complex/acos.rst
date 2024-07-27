
acos
=====

.. cpp:function:: constexpr Complex acos(const Complex& z) noexcept

   Returns the complex inverse cos [1]_ of a complex number :math:`z`.

**Parameters**

   .. cpp:var:: const Complex& z

        A complex number. 
        
**Returns**

    .. cpp:type:: Complex

        A complex number. 

The inverse cosine function of a complex number is defined as:

.. math::
   \cos^{-1}(z) =  \frac{1}{2} + i \log(iz + \sqrt{1 - z^2})

**Example**

.. code-block:: cpp

   Complex z = 3 + 4_j;
   std::cout << acos(z) << "\n";

Output:

.. code-block:: cpp

   0.936812 - 2.30551j

**References**

.. [1]  Weisstein, Eric W. "Inverse Cosine." From MathWorld--A Wolfram Web Resource. 
        https://mathworld.wolfram.com/InverseCosine.html