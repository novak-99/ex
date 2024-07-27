
tanh
=====

.. cpp:function:: constexpr Complex tanh(const Complex& z) noexcept

   Returns the complex tanh [1]_ of a complex number :math:`z`.

**Parameters**

   .. cpp:var:: const Complex& z

        A complex number. 
        
**Returns**

    .. cpp:type:: Complex

        A complex number. 

The sinh function of a complex number is defined as:

.. math::
   
   \tanh z = \frac{\sinh z}{\cosh z}

**Example**

.. code-block:: cpp

   Complex z = 3 + 4_j;
   std::cout << tanh(z) << "\n";

Output:

.. code-block:: cpp

   1.00071 + 0.00490826j

**References**

.. [1] "Hyperbolic functions", Wikipedia,
        https://en.wikipedia.org/wiki/Hyperbolic_functions