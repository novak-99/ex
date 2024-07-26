
setY
=====

.. cpp:function:: constexpr void setY(const double y) noexcept

   Sets the imaginary component :code:`y`.

**Parameters**

    .. cpp:var:: const double y

        A real number.

Sets the imaginary component of the complex object.

**Example**

.. code-block:: cpp

    Complex z; 
    z.setY(1); 
    std::cout << z << "\n";

Output:

.. code-block:: cpp

    0 + 1j