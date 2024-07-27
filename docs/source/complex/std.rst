
std
=====

.. cpp:function:: constexpr std::complex<double> std() noexcept

   Converts a :code:`cpplex::Complex` object to a :code:`std::complex<double>` object.

**Returns**

    .. cpp:type:: std::complex<double>

        A standard C++ complex object.

Gets the imaginary component of the complex object.

**Example**

.. code-block:: cpp

    Complex z(1, 4); 
    std::cout << z.std() << "\n";

Output:

.. code-block:: cpp

    (1,4)