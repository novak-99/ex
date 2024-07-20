
Productlog
=====

.. cpp:function:: constexpr Complex productlog(const Complex& z) noexcept

   Evaluates the Lambert W function [1]_ for a complex input.

**Parameters**

    .. cpp:var:: const Complex& z

        A complex number. 

**Returns**

    .. cpp:type:: Complex

        A complex number. 

The Lambert W function is defined as the inverse of the following function: 

.. math::
   f(z) = ze^z

For :math:`w = W(z)`, where :math:`W(z)` is the Lambert W function, then it holds that: 

.. math::

   \begin{flalign*}
   we^w &= z \\
   we^w - z &= 0
   \end{flalign*}

Thus a numerical approximation of the Lambert W function can be found by using Newton's method [2]_ to root-find the above equation. 

**Example**

.. code-block:: cpp

   Complex z = 1.0 + 1_j;
   std::cout << productlog(z) << "\n";

Output:

.. code-block:: cpp

   0.656966 + 0.32545j

**References**

.. [1] "Lambert W function", Wikipedia,
        https://en.wikipedia.org/wiki/Lambert_W_function
.. [2] "Newton's method", Wikipedia
        https://en.wikipedia.org/wiki/Newton%27s_method