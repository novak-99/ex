
getX
=====

.. cpp:function:: constexpr double getX() const noexcept

   Gets the real component :code:`x`.

**Returns**

    .. cpp:type:: double

        A real number. 

Gets the real component of the complex object.

**Example**

.. code-block:: cpp

    Complex z(1, 4); 
    std::cout << z.getX() << "\n";

Output:

.. code-block:: cpp

    1