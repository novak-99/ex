
dawsn
=====

.. cpp:function:: constexpr Complex dawsn(const Complex& z) noexcept

   Evaluates the Dawson integral [1]_ for a complex input.

**Parameters**

    .. cpp:var:: const Complex& z

        A complex number. 

**Returns**

    .. cpp:type:: Complex

        A complex number. 

The Dawson integral is defined as: 

.. math::
   
   D_{+}(x) = e^{-z^2}\int_{0}^{z}e^{t^2}dt


**Example**

.. code-block:: cpp

   Complex z = 1.0 + 1_j;
   std::cout << dawsn(z) << "\n";

Output:

.. code-block:: cpp

   0.990373 - 0.638873j

**References**

.. [1] "Dawson function", Wikipedia,
        https://en.wikipedia.org/wiki/Dawson_function