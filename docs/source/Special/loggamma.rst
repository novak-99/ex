
loggamma
=====

.. cpp:function:: constexpr Complex loggamma(const Complex& z) noexcept

   Evaluates the natural log of the gamma function [1]_. 

**Parameters**

    .. cpp:var:: const Complex& z

        A complex number. 

**Returns**

    .. cpp:type:: Complex

        A complex number. 

This function simply evaluates :math:`\ln(\Gamma(z))`. 


**Example**

.. code-block:: cpp

   Complex z = 1.0 + 1_j;
   std::cout << loggamma(z) << "\n";

Output:

.. code-block:: cpp

   -0.650923 - 0.30164j

**References**

.. [1]  Weisstein, Eric W. "Log Gamma Function." From MathWorld--A Wolfram Web Resource. 
        https://mathworld.wolfram.com/LogGammaFunction.html