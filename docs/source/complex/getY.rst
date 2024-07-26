
getY
=====

.. cpp:function:: constexpr double getY() const noexcept

   Gets the real component :code:`x`.

**Returns**

    .. cpp:type:: double

        A imaginary number. 

Gets the imaginary component of the complex object.

**Example**

.. code-block:: cpp

    Complex z(1, 4); 
    std::cout << z.getY() << "\n";

Output:

.. code-block:: cpp

    4