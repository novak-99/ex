
autocorr
=====

.. cpp:function:: constexpr Complex autocorr(Complex (*f)(Complex) noexcept

   Performs the auto-correlation operation [1]_ on two complex functions. 

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

The auto-correlation simply performs the cross-correlation using a single function :math:`f` for both arguments. 

**Example**

.. code-block:: cpp

   auto f = [](Complex t) { return exp(-t * t); };

   Complex z = 1; 
   std::cout << autocorr(f, z) << "\n";

Output:

.. code-block:: cpp

   0.760276 + 0j

**References**

.. [1] "Autocorrelation", Wikipedia,
        https://en.wikipedia.org/wiki/Autocorrelation