
Factorial
=====

.. cpp:function:: constexpr int factorial(const int k) noexcept

   Evaluates the factorial function. 

**Parameters**

    .. cpp:var:: const int k

        A nonnegative integer. 

**Returns**

    .. cpp:type:: int

        A positive integer.

This function simply evaluates :math:`k!`. 


**Example**

.. code-block:: cpp

   int k = 5; 
   std::cout << factorial(k) << "\n";

Output:

.. code-block:: cpp

  120

**References**

.. [1] "Factorial", Wikipedia,
        https://en.wikipedia.org/wiki/Factorial