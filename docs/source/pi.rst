
Pi
=====

.. cpp:function:: constexpr Complex pi(const Complex& z) noexcept

   Evaluates the pi function [1]_ for a complex input.

**Parameters**

    .. cpp:var:: const Complex& z

        A complex number. 

**Returns**

    .. cpp:type:: Complex

        A complex number. 

The gamma function is an extrapolation of the factorial to complex and decimal inputs. 
It is defined as follows: 

.. math::
   \Pi(z) = \int_{0}^{\infty} t^{z}e^{-t}dt


**Example**

.. code-block:: cpp

   Complex z = 1.0 + 1_j;
   std::cout << pi(z) << "\n";

Output:

.. code-block:: cpp

   0.652965 + 0.343066j

**References**

.. [1] "Gamma function", Wikipedia,
        https://en.wikipedia.org/wiki/Gamma_function