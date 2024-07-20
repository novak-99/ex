
Laplace
=====

.. cpp:function:: constexpr Complex laplace(Complex (*f)(Complex), const Complex& z, const Complex& a = 1) noexcept

   Performs the Laplace integral transform on a complex function.

**Parameters**

    .. cpp:var:: Complex (*f)(Complex)

        A complex function. 

    .. cpp:var:: const Complex& z

        A complex number.

    .. cpp:var:: const Complex& a

        A complex number, optional.

**Returns**

    .. cpp:type:: Complex

        A complex number. 

The Laplace transform performs the following integral transform on a function :math:`f`:

.. math::
   \mathcal{L}{f}(z) = \int_{0}^{\infty}f(t)e^{-zt}dt


**Example**

.. code-block:: cpp

   auto fn = [](Complex t) { return sin(t); };


   Complex z = 1; 
   std::cout << laplace(fn, z) << "\n";

Output:

.. code-block:: cpp

   0.501173 + 0j // True result: 1 / (z^2 + a^2) = 0.5 + 0j

**References**

.. [1] "Laplace transform", Wikipedia,
        https://en.wikipedia.org/wiki/Laplace_transform