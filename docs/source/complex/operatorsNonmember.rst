
operators
=====

.. cpp:function:: constexpr Complex operator+(const Complex& z) noexcept

   Unary positive operator.

.. cpp:function:: constexpr Complex operator-(const Complex& z) noexcept

   Unary negative operator.

.. cpp:function:: constexpr Complex operator+(const Complex& z1, const Complex& z2) noexcept

   Arithmetic addition operator between two complex numbers.

.. cpp:function:: constexpr Complex operator-(const Complex& z1, const Complex& z2) noexcept

   Arithmetic subtraction operator between two complex numbers.

.. cpp:function:: constexpr Complex operator*(const Complex& z1, const Complex& z2) noexcept

   Arithmetic multiplication operator between two complex numbers.

.. cpp:function:: constexpr Complex operator/(const Complex& z1, const Complex& z2) noexcept

   Arithmetic division operator between two complex numbers.

.. cpp:function:: constexpr Complex operator+(const Complex& z, const double alpha) noexcept

   Arithmetic addition operator between a complex number and a real number.

.. cpp:function:: constexpr Complex operator-(const Complex& z, const double alpha) noexcept

   Arithmetic subtraction operator between a complex number and a real number.

.. cpp:function:: constexpr Complex operator*(const Complex& z, const double alpha) noexcept

   Arithmetic multiplication operator between a complex number and a real number.

.. cpp:function:: constexpr Complex operator/(const Complex& z, const double alpha) noexcept

   Arithmetic division operator between a complex number and a real number.

.. cpp:function:: constexpr Complex operator+(const double alpha, const Complex& z) noexcept

   Arithmetic addition operator between a complex number and a real number.

.. cpp:function:: constexpr Complex operator-(const double alpha, const Complex& z) noexcept

   Arithmetic subtraction operator between a complex number and a real number.

.. cpp:function:: constexpr Complex operator*(const double alpha, const Complex& z) noexcept

   Arithmetic multiplication operator between a complex number and a real number.

.. cpp:function:: constexpr Complex operator/(const double alpha, const Complex& z) noexcept

   Arithmetic division operator between a complex number and a real number.

.. cpp:function:: constexpr bool operator==(const Complex& z1, const Complex& z2) noexcept

   Equality operator between two complex numbers.

.. cpp:function:: constexpr bool operator==(const Complex& z, const double alpha) noexcept

   Equality operator between a complex number and a real number.

.. cpp:function:: constexpr bool operator==(const double alpha, const Complex& z) noexcept

   Equality operator between a complex number and a real number.

.. cpp:function:: constexpr bool operator!=(const Complex& z1, const Complex& z2) noexcept

   Inequality operator between two complex numbers.

.. cpp:function:: constexpr bool operator!=(const Complex& z, const double alpha) noexcept

   Inequality operator between a complex number and a real number.

.. cpp:function:: constexpr bool operator!=(const double alpha, const Complex& z) noexcept

   Inequality operator between a complex number and a real number.

.. cpp:function:: constexpr std::ostream& operator<< (std::ostream& ostream, const Complex& z) noexcept

   Serializes a complex number.

.. cpp:function:: constexpr std::istream& operator>> (std::istream& istream, const Complex& z) noexcept

   Deserializes a complex number.

.. cpp:function:: Complex operator "" _j(const unsigned long long y) noexcept

   The cpplex complex literal :code:`_j`.

.. cpp:function:: Complex operator "" _j(const long double y) noexcept

   The cpplex complex literal :code:`_j`.

**Parameters**

   .. cpp:var:: const Complex& z

        A complex number. 
        
**Returns**

    .. cpp:type:: Complex

        A complex number. 

This module defines 2 assignment operators and 8 compound assignment operators for complex addition, subtraction, multiplication, and division.

**Example**

.. code-block:: cpp

   Complex z = 3 + 4_j;
   std::cout << z + 5 << "\n";

Output:

.. code-block:: cpp

   8 + 4j