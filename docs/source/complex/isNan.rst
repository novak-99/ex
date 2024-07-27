
isNan
=====

.. cpp:function:: bool isNan(const Complex& z) noexcept

   Determines whether or not a complex number contains a :code:`nan` value.

**Parameters**

   .. cpp:var:: const Complex& z

        A complex number.
        
**Returns**

    .. cpp:type:: std::vector<Complex>

        A boolean.

**Example**

.. code-block:: cpp

   Complex z(NAN, NAN); 
   std::cout << isNan(z) << "\n";

Output:

.. code-block:: cpp
   1