
Sgn
=====

.. cpp:function:: constexpr double sgn(const double x) noexcept

   Evaluates the sign function [1]_ for a complex input.

**Parameters**

    .. cpp:var:: const double x

        A real number. 

**Returns**

    .. cpp:type:: double

        A real number. 

The sign function is the derivative of the absolute value function and is defined as:

.. math::
   
   \DeclareMathOperator\sgn{sgn}

   \[ 
      \sgn(x) = 
      \begin{cases} 
         -1 & \text{if } x < 0 \\
         0 & \text{if } x = 0 \\
         1 & \text{if } x > 0
      \end{cases}
   \]


**Example**

.. code-block:: cpp

   double x = 1;
   std::cout << sgn(x) << "\n";

Output:

.. code-block:: cpp

   1

**References**

.. [1] "Sign function", Wikipedia,
        https://en.wikipedia.org/wiki/Sign_function