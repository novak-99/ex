
real
=====

.. cpp:function:: constexpr double real(const Complex& z) noexcept

   Gets the real component :code:`x`.

**Parameters**

    .. cpp:var:: const Complex& z

        A complex number.

**Returns**

    .. cpp:type:: double

        A real number. 

Gets the real component of a complex object.

**Example**

.. code-block:: cpp

    Complex z(1, 4); 
    std::cout << real(z) << "\n";

Output:

.. code-block:: cpp

    1