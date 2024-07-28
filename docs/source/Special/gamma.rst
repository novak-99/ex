
gamma
=====

.. cpp:function:: constexpr Complex gamma(const Complex& z) noexcept

   Evaluates the gamma function [1]_ for a complex input. Uses the Lanczos approximation [2]_.

**Parameters**

    .. cpp:var:: const Complex& z

        A complex number. 

**Returns**

    .. cpp:type:: Complex

        A complex number. 

The gamma function is an extrapolation of the factorial to complex and decimal inputs. 
It is defined as follows: 

.. math::
   \Gamma(z) = \int_{0}^{\infty} t^{z - 1}e^{-t}dt


**Example**

.. code-block:: cpp

   Complex z = 1.0 + 1_j;
   std::cout << gamma(z) << "\n";

Output:

.. code-block:: cpp

   0.498016 - 0.15495j

**References**

.. [1] "Gamma function", Wikipedia,
        https://en.wikipedia.org/wiki/Gamma_function
.. [2] "Lanczos approximation", Wikipedia,
        https://en.wikipedia.org/wiki/Lanczos_approximation