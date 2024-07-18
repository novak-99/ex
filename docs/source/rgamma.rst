
Gamma
=====

.. cpp:function:: constexpr Complex rgamma(const Complex& z) noexcept

   Evaluates the reciprocal of the gamma function [1]_. 

**Parameters**

    .. cpp:var:: const Complex& z

        A complex number. 

**Returns**

    .. cpp:type:: Complex

        A complex number. 



This function simply evaluates :math:`1/(\Gamma(z))`. 


**Example**

.. code-block:: cpp

   Complex z = 1.0 + 1_j;
   std::cout << rgamma(z) << "\n";

Output:

.. code-block:: cpp

   1.83074 + 0.569608j

**References**

.. [1] "Reciprocal gamma function", Wikipedia,
        https://en.wikipedia.org/wiki/Reciprocal_gamma_function