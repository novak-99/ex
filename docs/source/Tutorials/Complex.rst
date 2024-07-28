Complex
=====

The complex class is the basis behind cpplex as it defines its complex data type.

Let's begin by importanting the correct header file and creating a complex object:

.. code-block:: cpp

    #include <Complex/Complex.hpp>
    int main(){
       Complex z(4, 3); 
    }

The above code creates a complex number :math:`z = 4 + 3i`.

If you prefer to use complex literals, you may either use cpplex's complex literal :code:`_j`, or C++'s complex literal :code:`i`:

.. code-block:: cpp
    #include <Complex/Complex.hpp>
    using namespace std::complex_literals; // for C++'s literals
    
    int main(){
       Complex z = 4 + 3_j; 
       Complex z = 4 + 3i;
    }

.. Output:

.. .. code-block:: cpp

..    10 + 1j