
wrightomega
=====

.. cpp:function:: constexpr Complex wrightomega(const Complex& z) noexcept

   Evaluates the Wright omega function [1]_ for a complex input.

**Parameters**

    .. cpp:var:: const Complex& z

        A complex number. 

**Returns**

    .. cpp:type:: Complex

        A complex number. 

The Wright omega function is defined as the inverse of the following function: 

.. math::
   f(z) = z + \log(z)

For :math:`\omega = \omega(z)`, where :math:`\omega(z)` is the Wright omega function, then it holds that: 

.. math::

   \begin{flalign}
   z &= \omega + \log(\omega) \\
   0 &= \omega + \log(\omega) - z
   \end{flalign}

Thus a numerical approximation of the Wright omega function can be found by using Newton's method [2]_ to root-find the above equation. 

**Example**

.. code-block:: cpp

   Complex z = 1.0 + 1_j;
   std::cout << wrightomega(z) << "\n";

Output:

.. code-block:: cpp

   0.937208 + 0.505421j

**References**

.. [1] "Wright omega function", Wikipedia,
        https://en.wikipedia.org/wiki/Wright_omega_function
.. [2] "Newton's method", Wikipedia
        https://en.wikipedia.org/wiki/Newton%27s_method