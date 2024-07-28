
Digamma
=====

.. cpp:function:: constexpr Complex digamma(const Complex& z) noexcept

   Evaluates the digamma function [1]_ for a complex input. It has the same definition as the :ref:`psi` function. 

**Parameters**

    .. cpp:var:: const Complex& z

        A complex number. 

**Returns**

    .. cpp:type:: Complex

        A complex number. 

The digamma function is the derivative of the natural log of the gamma function. It is defined as:

.. math::
   \psi(z) = \frac{\Gamma'(z)}{\Gamma(z)}


**Example**

.. code-block:: cpp

   Complex z = 1.0 + 1_j;
   std::cout << digamma(z) << "\n";

Output:

.. code-block:: cpp

   0.0946503 + 1.07667j

**References**

.. [1] "Digamma function", Wikipedia,
        https://en.wikipedia.org/wiki/Digamma_function