
operators
=====

.. cpp:function:: constexpr Complex& operator=(const Complex& z) noexcept

   Sets a complex number equal to another complex number :math:`z`.

.. cpp:function:: constexpr Complex& operator=(const double alpha) noexcept

   Sets a complex number equal to a real number :math:`\alpha`.

.. cpp:function:: constexpr Complex& operator+=(const Complex& z) noexcept

   Compound assignment addition operator for a complex number :math:`z`.

.. cpp:function:: constexpr Complex& operator-=(const Complex& z) noexcept

   Compound assignment subtraction operator for a complex number :math:`z`.

.. cpp:function:: constexpr Complex& operator*=(const Complex& z) noexcept

   Compound assignment multiplication operator for a complex number :math:`z`.

.. cpp:function:: constexpr Complex& operator/=(const Complex& z) noexcept

   Compound assignment division operator for a complex number :math:`z`.

.. cpp:function:: constexpr Complex& operator+=(const Complex& alpha) noexcept

   Compound assignment addition operator for a real number :math:`\alpha`.

.. cpp:function:: constexpr Complex& operator-=(const Complex& alpha) noexcept

   Compound assignment subtraction operator for a real number :math:`\alpha`.

.. cpp:function:: constexpr Complex& operator*=(const Complex& alpha) noexcept

   Compound assignment multiplication operator for a real number :math:`\alpha`.

.. cpp:function:: constexpr Complex& operator/=(const Complex& alpha) noexcept

   Compound assignment division operator for a real number :math:`\alpha`.

**Parameters**

   .. cpp:var:: const Complex& z

        A complex number. 
        
**Returns**

    .. cpp:type:: Complex& z

        The complex number :code:`*this`.

This module defines 2 assignment operators and 8 compound assignment operators for complex addition, subtraction, multiplication, and division.

**Example**

.. code-block:: cpp

   Complex z = 3 + 4_j;
   z += 2; 
   z /= 2_j;
   z *= 2;
   std::cout << z << "\n";

Output:

.. code-block:: cpp

   4 - 5j