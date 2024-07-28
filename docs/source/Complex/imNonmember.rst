
im
=====

.. cpp:function:: constexpr double im() const noexcept

   Gets the imaginary component :code:`y`.

**Parameters**

    .. cpp:var:: const Complex& z

        A complex number.

**Returns**

    .. cpp:type:: double

        A real number. 

Gets the imaginary component of a complex object.

**Example**

.. code-block:: cpp

    Complex z(1, 4); 
    std::cout << im(z) << "\n";

Output:

.. code-block:: cpp

    4