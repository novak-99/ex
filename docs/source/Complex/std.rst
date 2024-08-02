
std
=====

.. cpp:function:: constexpr std::complex<double> std() noexcept

   Converts a :code:`cpplex::Complex` object into a :code:`std::complex<double>` object.

**Returns**

    .. cpp:type:: std::complex<double>

        A standard C++ complex object.

Converts a standard C++ complex number to a cpplex complex number.

**Example**

.. code-block:: cpp

    Complex z(1, 4); 
    std::cout << z.std() << "\n";

Output:

.. code-block:: cpp

    (1,4)