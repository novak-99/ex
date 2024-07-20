
Hartley
=====

.. cpp:function:: constexpr Complex laplace(Complex (*f)(Complex), const Complex& z) noexcept

   Performs the Hartley integral transform [1]_ of a complex function.

**Parameters**

    .. cpp:var:: Complex (*f)(Complex)

        A complex function. 

    .. cpp:var:: const Complex& z

        A complex number.

**Returns**

    .. cpp:type:: Complex

        A complex number. 

The Hartley transform performs the following integral transform on a function :math:`f`:

.. math::

    \DeclareMathOperator\cas{cas}
    H(\omega) = \{\mathcal{H}f\}(\omega) = \frac{1}{\sqrt(2\pi)}\int_{-\infty}^{\infty}f(t)\cas(\omega t)dt

where :math:`\DeclareMathOperator\cas{cas} \cas(t)` is defined as:

.. math::

    \DeclareMathOperator\cas{cas}
    \cas(t) = \cos(t) + \sin(t)

**Example**

.. code-block:: cpp

   auto fn = [](Complex t) { return exp(-t * t); };


   Complex z = 1; 
   std::cout << hartley(fn, z) << "\n";

Output:

.. code-block:: cpp

   0.550782 + 0j // True result: 0.550695 + 0j 

**References**

.. [1] "Hartley transform", Wikipedia,
        https://en.wikipedia.org/wiki/Hartley_transform