
Psi
=====

.. cpp:function:: constexpr Complex psi(const Complex& z) noexcept

   Evaluates the psi function [1]_ for a complex input.

**Parameters**

    .. cpp:var:: const Complex& z

        A complex number. 

**Returns**

    .. cpp:type:: Complex

        A complex number. 

The gamma function is the derivative of the natural log of the gamma function. In other words, in can be defined as:

.. math::
   \psi(z) = \frac{\Gamma'(z)}{\Gamma(z)}


**Example**

.. code-block:: cpp

   Complex z = 1.0 + 1_j;
   std::cout << psi(z) << "\n";

Output:

.. code-block:: cpp

   0.0946503 + 1.07667j

**References**

.. [1] "Digamma function", Wikipedia,
        https://en.wikipedia.org/wiki/Gamma_function