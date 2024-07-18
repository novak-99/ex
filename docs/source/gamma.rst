
Gamma
=====

.. cpp:concept:: constexpr Complex gamma(const Complex& z) noexcept

   Evaluates the gamma function for a complex input. Uses the Lanczos approximation.

   **Parameters**

   .. cpp:member:: const Complex& z

      A complex number. 

   **Parameters**

   .. cpp:var:: Complex

      A complex number. 


The gamma function is an extrapolation of the factorial to complex and decimal inputs. 
It is defined as follows: 

.. math::
   \Gamma(z) = \int_{0}^{\infty} t^{z - 1}e^{-t}dt


The function may be used as follows: 

.. code-block:: cpp

   Complex z = 1.0
   std::cout << gamma(z) << "\n";
0.498016 - 0.15495j