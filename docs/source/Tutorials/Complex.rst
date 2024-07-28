Complex
=====

The complex class is the basis behind cpplex as it defines its complex data type.

Let's begin by importanting the correct header file and creating a complex object:

.. code-block:: cpp

    #include <Complex/Complex.hpp>
    #include <iostream>
    int main(){
       Complex z(4, 3);

       return 0; 
    }

The above code creates a complex number :math:`z = 4 + 3i`.

If you prefer to use complex literals, you may either use cpplex's complex literal :code:`_j`, or C++'s complex literal :code:`i`:

.. code-block:: cpp

    #include <Complex/Complex.hpp>
    #include <iostream>
    using namespace std::complex_literals; // for C++'s literals
    
    int main(){
       Complex z = 4 + 3_j; 
       Complex z = 4 + 3i;

       return 0;
    }

You can do the same operations with complex numbers as with any other numerical type in C++. For example, you can easily print a cpplex Complex number as follows:

.. code-block:: cpp

    #include <Complex/Complex.hpp>
    #include <iostream>
    using namespace std::complex_literals; // for C++'s literals
    
    int main(){
        Complex z = 4 + 3_j; 
        std::cout << z << "\n";

        return 0;
    }

Output:

.. code-block:: cpp

   4 + 3_j

You may also :code:`cin` a complex number just as easily:

.. code-block:: cpp

    #include <Complex/Complex.hpp>
    #include <iostream>
    using namespace std::complex_literals; // for C++'s literals
    
    int main(){
        Complex z;
        std::cin >> z; 
        std::cout << z << "\n";

        return 0; 
    }

Input:

.. code-block:: cpp

   4 + 3_j

Output:

.. code-block:: cpp

   4 + 3_j

Various arithmetic operations are also supported:

.. code-block:: cpp

    #include <Complex/Complex.hpp>
    #include <iostream>
    using namespace std::complex_literals; // for C++'s literals
    
    int main(){
        Complex z1 = 4 + 3_j; 
        Complex z2 = 2 + 2_j;
        std::cout << z1 + z2 << "\n";
        std::cout << z1 - z2 << "\n";
        std::cout << z1 * z2 << "\n";
        std::cout << z1 * 2 << "\n";
        std::cout << -z1 << "\n";

        return 0;
    }

Output:

.. code-block:: cpp

    6 + 5j
    2 + 1j
    2 + 14j
    8 + 6j
    -4 - 3j