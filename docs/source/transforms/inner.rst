
Inner
=====

.. cpp:function:: constexpr Complex inner(Complex (*f)(Complex), Complex (*g)(Complex), const Complex& z, const Complex& a, const Complex& b) noexcept

   Performs the cross-correlation operation [1]_ on two complex functions. 

**Parameters**

    .. cpp:var:: Complex (*f)(Complex)

        A complex function. 

    .. cpp:var:: Complex (*g)(Complex)

        A complex function. 

    .. cpp:var:: const Complex& z

        A complex number.

    .. cpp:var:: const Complex& a

        A complex number.

    .. cpp:var:: const Complex& b

        A complex number.

**Returns**

    .. cpp:type:: Complex

        A complex number. 

The inner product of two complex functions :math:`f`: and :math:`g` is defined as:

.. math::

    \newcommand{\compconj}[1]{%
    \overline{#1}%
    }
    \langle f, g \rangle = \int_{a}^{b}f(t)\compconj{g(t)}dt


**Example**

.. code-block:: cpp

   auto f = [](Complex t) { return exp(-t * t); };
   auto g = [](Complex t) { return exp(-t * t); };


   Complex z = 1; 
   Complex a = 0; 
   Complex b = 1; 
   std::cout << inner(f, g, z, a, b) << "\n";

Output:

.. code-block:: cpp

   0.598144 + 0j

**References**

.. [1] "Inner product space", Wikipedia,
        https://en.wikipedia.org/wiki/Inner_product_space