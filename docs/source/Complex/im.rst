
im
=====

.. cpp:function:: constexpr double im() const noexcept

   Gets the imaginary component :code:`y`.

**Returns**

    .. cpp:type:: double

        A real number. 

Gets the imaginary component of the complex object.

**Example**

.. code-block:: cpp

    Complex z(1, 4); 
    std::cout << z.im() << "\n";

Output:

.. code-block:: cpp

    4