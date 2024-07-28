
sigmoid
=====

.. cpp:function:: constexpr Complex sigmoid(const Complex& z) noexcept

   Evaluates the sigmoid function [1]_ for a complex input.

**Parameters**

    .. cpp:var:: const Complex& z

        A complex number. 

**Returns**

    .. cpp:type:: Complex

        A complex number. 

The sigmoid function is an s-shaped function commonly used in machine learning and statistics. It is defined as:

.. math::
   
   \sigma(z) = \frac{1}{1 + e^{-z}}


**Example**

.. code-block:: cpp

   Complex z = 1.0 + 1_j;
   std::cout << sigmoid(z) << "\n";

Output:

.. code-block:: cpp

   0.782042 + 0.201948j

**References**

.. [1] "Sigmoid function", Wikipedia,
        https://en.wikipedia.org/wiki/Sigmoid_function