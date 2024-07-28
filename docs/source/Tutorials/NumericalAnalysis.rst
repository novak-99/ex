NumericalAnalysis
=====

The numerical analysis allows for numerical techniques to approach differentiation, integration, Taylor series approximations, and root-finding.

Let's begin by importing the correct header file and creating a function to differentiate:

.. code-block:: cpp

    #include <Complex/Complex.hpp>
    #include <iostream>

    Complex f(Complex z) {
        return z*z; 
    }

    int main(){

       return 0; 
    }

We have just defined a complex function :math:`f(z) = z^2`. You may also define it using C++ lambdas:

.. code-block:: cpp

    #include <Complex/Complex.hpp>
    #include <iostream>
    
    int main(){
        auto f = [](Complex z) { return z*z };

       return 0;
    }

We may differentiate the function above and evaluate it at the point :math:`z = 1 + 1i`, which will yield `f'(z) = 2z + 2 + 2i`.

.. code-block:: cpp

    #include <Complex/Complex.hpp>
    #include <iostream>

    Complex f(Complex z) {
        return z*z; 
    }

    int main(){
        std::cout << derivative(f, 1 + 1i) << "\n";
        return 0; 
    }

Output:

.. code-block:: cpp

   2 + 2j

We may also integrate this function from :math:`a = 0` to :math:`b = 1 + 1i`:

.. code-block:: cpp

    #include <Complex/Complex.hpp>
    #include <iostream>

    Complex f(Complex z) {
        return z*z; 
    }

    int main(){
        std::cout << integral(f, 0, 1 + 1i) << "\n";
        return 0; 
    }

Output:

.. code-block:: cpp

   -0.666667 + 0.666667j

Also important in complex analysis are Taylor series approximations, which approximate a function using its derivatives. Cpplex contains approximations of constant, linear, and quadratic orders:

.. code-block:: cpp

    #include <Complex/Complex.hpp>
    #include <iostream>
    using namespace std::complex_literals; // for C++'s literals
    
    #include <Complex/Complex.hpp>
    #include <iostream>

    Complex f(Complex z) {
        return sin(z);
    }

    int main(){
        std::cout << constantApproximation(f, 0) << "\n";
        std::cout << linearApproximation(f, 0, 0.5) << "\n";
        std::cout << quadraticApproximation(f, 0, 0.5) << "\n";
        std::cout << f(0.5) << "\n";
        return 0; 
    }

Output:

.. code-block:: cpp

    0 + 0j
    0.5 + 0j
    0.5 + 0j
    0.479426 + 0j

Finally, the numerical analysis module contians tools for root-finding and optimization. Here, we demonstrate Newton's method, using :math:`1000` epochs and an initial guess of :math:`2i`:

.. code-block:: cpp

    #include <Complex/Complex.hpp>
    #include <iostream>

    Complex f(Complex z) {
        return sin(z - 5_j);
    }

    int main(){
        std::cout << newtonsMethod(f, 2_j, 1000) << "\n";

        return 0;
    }

Output:

.. code-block:: cpp

    0 + 5j