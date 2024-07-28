
invhartley
=====

.. cpp:function:: constexpr Complex invhartley(Complex (*f)(Complex), const Complex& z) noexcept

   Performs the inverse Hartley integral transform [1]_ of a complex function.

**Parameters**

    .. cpp:var:: Complex (*f)(Complex)

        A complex function. 

    .. cpp:var:: const Complex& z

        A complex number.

**Returns**

    .. cpp:type:: Complex

        A complex number. 

As the Hartley transform is its own inverse, this function simply performs the hartley transform. 

**Example**

.. code-block:: cpp

   auto fn = [](Complex t) { return exp(-t * t); };


   Complex z = 1; 
   std::cout << invhartley(fn, z) << "\n";

Output:

.. code-block:: cpp

   0.550782 + 0j // True result: 0.550695 + 0j 

**References**

.. [1] "Hartley transform", Wikipedia,
        https://en.wikipedia.org/wiki/Hartley_transform