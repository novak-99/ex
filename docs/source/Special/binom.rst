
Binom
=====

.. cpp:function:: constexpr int binom(const int n, const int k) noexcept

   Evaluates the binomial coefficient [1]_ of two given integer numbers. 

**Parameters**

    .. cpp:var:: const int n

        A nonnegative number. 

    .. cpp:var:: const int k

        A nonnegative number. 

**Returns**

    .. cpp:var:: int

        A positive number. 

The binomial coefficient of two positive integers, :math:`n \geq k \geq 0` is defined as:

.. math::
   
   \binom{n}{k} = \frac{n!}{k!(n - k)!}


**Example**

.. code-block:: cpp

   int n = 2; 
   int k = 1; 
   std::cout << binom(n, k) << "\n";

Output:

.. code-block:: cpp

   2

**References**

.. [1] "Binomial coefficient", Wikipedia,
        https://en.wikipedia.org/wiki/Binomial_coefficient