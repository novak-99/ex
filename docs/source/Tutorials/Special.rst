Special
=====

The special module includes various special mathematical functions for complex inputs.

The gamma function, defined as:

.. math::
   \Gamma(z) = \int_{0}^{\infty} t^{z - 1}e^{-t}dt

is an important function in complex analysis, and various related functions are also included:

.. code-block:: cpp

    #include <Special.hpp>
    #include <Complex.hpp>
    #include <iostream>

    int main(){
        z = 5 + 5_j;
        std::cout << gamma(z) << "\n";
        std::cout << loggamma(z) << "\n"; // ln(gamma(z))
        std::cout << rgamma(z) << "\n"; // 1 / gamma(z)
        std::cout << pi(z) << "\n"; // gamma(z + 1)

        return 0; 
    }

Output:

.. code-block:: cpp

    -0.974395 + 2.00669j
    0.802338 + 2.02284j
    -0.195809 - 0.403253j
    -14.9054 + 5.16147j

The error function, defined as: 

.. math::
   
   \DeclareMathOperator\erf{erf}
   \erf(z) = \frac{2}{\sqrt{\pi}} \int_{0}^{z}e^{-t^2}dt

is also included, as are its many variants:

.. code-block:: cpp

    #include <Special.hpp>
    #include <Complex.hpp>
    #include <iostream>
    
    int main(){
        Complex z = 5 + 5_j;
        std::cout << erf(z) << "\n";
        std::cout << erfc(z) << "\n";
        std::cout << erfcx(z) << "\n";
        std::cout << erfci(z) << "\n";
        std::cout << wofz(z) << "\n";

       return 0;
    }

Output:

.. code-block:: cpp

    3.02657 + 2.85507j
    -2.02657 - 2.85507j
    -2.70467 - 2.22333j
    2.85507 + 3.02657j
    -2.70467 + 2.22333j

Important integrals, including the Dawson and Fresnel integrals, are also included:

.. code-block:: cpp

    #include <Special.hpp>
    #include <Complex.hpp>
    #include <iostream>

    int main(){
        Complex z = 1 + 1_j;

        auto [S, C] = fresnel(z);
        std::cout << S << "\n";
        std::cout << C << "\n";
        std::cout << dawsn(z) << "\n";

        return 0; 
    }

Output:

.. code-block:: cpp

    -2.06189 + 2.06189j
    2.55579 + 2.55579j
    0.990373 - 0.638873j

Finally, the Lambert W function, or productlog function, and the related Wright omega function function, are also included:

.. code-block:: cpp

    #include <Special.hpp>
    #include <Complex.hpp>
    #include <iostream>

    int main(){
        Complex z = 1 + 1_j;

        std::cout << productlog(z) << "\n";
        std::cout << weightomega(z) << "\n";

        return 0;
    }

Output:

.. code-block:: cpp

    0.656966 + 0.32545j
    0.937208 + 0.505421j

Keep in mind that both of these functions are implemented using Newton's method.