
crosscorr
=====

.. cpp:function:: constexpr Complex crosscorr(Complex (*f)(Complex), Complex (*g)(Complex), const Complex& z) noexcept

   Performs the cross-correlation operation [1]_ on two complex functions. 

**Parameters**

    .. cpp:var:: Complex (*f)(Complex)

        A complex function. 

    .. cpp:var:: Complex (*g)(Complex)

        A complex function. 

    .. cpp:var:: const Complex& z

        A complex number.

**Returns**

    .. cpp:type:: Complex

        A complex number. 

The cross-correlation operation performs the following integral transform on two functions :math:`f` and :math:`g`:

.. math::

    \newcommand{\compconj}[1]{%
    \overline{#1}%
    }
    (f \star g)(t) = \int_{-\infty}^{\infty}\compconj{f(\tau)}g(t + \tau)d\tau


**Example**

.. code-block:: cpp

   auto f = [](Complex t) { return exp(-t * t); };
   auto g = [](Complex t) { return exp(-t * t); };


   Complex z = 1; 
   std::cout << crosscorr(f, g, z) << "\n";

Output:

.. code-block:: cpp

   0.760276 + 0j

**References**

.. [1] "Cross-correlation", Wikipedia,
        https://en.wikipedia.org/wiki/Cross-correlation