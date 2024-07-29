InformationTheory
=====

The information theory module includes various functions related to entropy. 

We can first begin by creating a complex sequence:

.. code-block:: cpp

    #include <InformationTheory/InformationTheory.hpp>
    #include <iostream>
    #include <vector>

    std::vector

    int main(){

        std::vector<Complex> P = {0.25 + 0.5_j, 0.25 + 0.5_j, 0.25, 0.25};
        return 0; 
    }

This complex sequence defines two discrete probability distributions for the complex and real components. All discrete entropy functions assume that these distributions are independent. 

The entropy of this distribution can be calculated as follows:

.. code-block:: cpp

    #include <InformationTheory/InformationTheory.hpp>
    #include <iostream>
    #include <vector>
    
    int main(){
        std::vector<Complex> P = {0.25 + 0.5_j, 0.25 + 0.5_j, 0.25, 0.25};
        std::cout << entropy(P) << "\n";

       return 0;
    }

Output:

.. code-block:: cpp

   2.07944

Also useful is calculating the Shannon information content of a single probability :math:`p`:. It is defined as:

.. math::
    I(x) = -\log(P)

and can be implemented by doing the following:

.. code-block:: cpp

    #include <InformationTheory/InformationTheory.hpp>
    #include <iostream>
    #include <vector>

    int main(){
        Complex p = 0.5 + 0.5_j; 
        std::cout << shannonInformation(p) << "\n";
    }

Output:

.. code-block:: cpp

   1.38629

The KL divergence is defined as how different one probability distribution :math:`P` is different from another distribution :math:`Q`, and is implemented as such:

.. code-block:: cpp

    #include <InformationTheory/InformationTheory.hpp>
    #include <iostream>
    #include <vector>
    
    int main(){
        std::vector<Complex> P = {0.25 + 0.5_j, 0.25 + 0.5_j, 0.25, 0.25};
        std::vector<Complex> Q = {0.4 + 0.5_j, 0.2 + 0.5_j, 0.2, 0.2};
        std::cout << klDiv(P, Q) << "\n";

       return 0;
    }

Output:

.. code-block:: cpp

   0.0498568

The information theory module also featuers continuous versions of these functions. The continuous versions assume you are using the joint PDF.

.. code-block:: cpp

    #include <InformationTheory/InformationTheory.hpp>
    #include <Constants/Constants.hpp> // for negative and positive INF.
    #include <iostream>
    #include <vector>
    
    int main(){
        auto f = [](Complex t) { return exp(-t * t); }; // Gaussian function.
        std::cout << entropy(f, NINF.real(), INF.real()) << "\n";

       return 0;
    }

Output:

.. code-block:: cpp

    -0.88551

A continuous version of the KL divergence can also be easily implemented:

.. code-block:: cpp

    #include <InformationTheory/InformationTheory.hpp>
    #include <Constants/Constants.hpp> // for negative and positive INF.
    #include <iostream>
    #include <vector>
    
    int main(){
        auto f = [](Complex t) { return exp(-t * t); }; // Gaussian function.
        auto g = [](Complex t) { return exp(-t * t); }; // Gaussian function. 
        std::cout << klDiv(f, g, NINF.real(), INF.real()) << "\n"; // Should be ~ 0 (epsilon value included in logs may influence precision).

       return 0;
    }

Output:

.. code-block:: cpp

    -8.03496e-08