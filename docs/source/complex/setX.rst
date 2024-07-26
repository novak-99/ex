
setX
=====

.. cpp:function:: constexpr void setX(const double x) noexcept

   Sets the real component :code:`x`.

**Parameters**

    .. cpp:var:: const double x

        A real number.

Sets the real component of the complex object.

**Example**

.. code-block:: cpp

    Complex z; 
    z.setX(1); 
    std::cout << z << "\n";

Output:

.. code-block:: cpp

    1 + 0j