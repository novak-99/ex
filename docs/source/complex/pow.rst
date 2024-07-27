
log
=====

.. cpp:function:: constexpr Complex pow(const Complex& z1, const Complex& z2) noexcept

.. cpp:function:: constexpr pow(const Complex& z, const double alpha) noexcept

.. cpp:function:: constexpr pow(const double alpha, const Complex& z) noexcept

   Returns the complex power function [1]_ using real or complex numbers for either argument.

**Parameters**

   .. cpp:var:: const Complex& z

        A complex number. 

   .. cpp:var:: const Complex& z1

        A complex number. 

   .. cpp:var:: const Complex& z2

        A complex number. 

   .. cpp:var:: const double alpha

        A real number. 
        
**Returns**

    .. cpp:type:: Complex

        A complex number. 

Exponentiation for a complex base :math:`z` and a complex power :math:`w` is deifned as:

.. math::
   z^w  = e^{w\log z}

**Example**

.. code-block:: cpp

   Complex z = 3 + 4_j;
   Complex w = 3 + 1_j;
   std::cout << pow(z, ws) << "\n";

Output:

.. code-block:: cpp

   -15.6062 - 46.9257j

**References**

.. [1] "Exponentiation", Wikipedia,
        https://en.wikipedia.org/wiki/Exponentiation