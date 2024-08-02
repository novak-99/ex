Distributions
=====

Cpplex contains two distribution modules: one for discrete distributions, and one for continuous distributions. We will explore both in this tutorial.

We can first begin by creating a discrete distribution object.

.. code-block:: cpp

    #include <DiscreteDistribution/DiscreteDistribution.hpp>
    #include <Complex/Complex.hpp>
    #include <iostream>

    std::vector

    int main(){
        DiscreteDistribution* dist;

        return 0;
    }

We will make it a pointer object so that we can construct a polymorphic implementation.

The full list of discrete distributions is available in the documentation, but for this tutorial, we can select the poisson distribution as an example. Don't forget to include the corresponding header file for the distribution you choose.

.. code-block:: cpp

    #include <DiscreteDistribution/DiscreteDistribution.hpp>
    #include <DiscreteDistribution/PoissonDistribution.hpp>
    #include <Complex/Complex.hpp>
    #include <iostream>
    
    int main(){
        DiscreteDistribution* dist; 
        Complex lambda = 5 + 5_j; 

        Poisson poissonDist(lambda); 
        dist = &poissonDist; 

        return 0;
    }

Note that for each distribution parameter, you need to specify the real and complex components as a complex number. Also keep in mind that discrete distributions assume that the real and imaginary components are independent.

Let's call the PMF for this Poisson distribution for a complex input we provide:

.. code-block:: cpp

    #include <DiscreteDistribution/DiscreteDistribution.hpp>
    #include <DiscreteDistribution/PoissonDistribution.hpp>
    #include <Complex/Complex.hpp>
    #include <iostream>

    int main(){
        DiscreteDistribution* dist; 
        Complex lambda = 5 + 5_j; 

        Poisson poissonDist(lambda); 
        dist = &poissonDist; 

        Complex z = 3 + 3_j; 
        std::cout << dist->pmf(z) << "\n";

        return 0;
    }

Output:

.. code-block:: cpp

   0.0197048

This indicates that for a joint, independent Poisson distribution with :math:`\lambda_R = 5` and :math:`\lambda_I = 5`, the probability of :math:`z = 3 + 3i` occuring is :math:`p = 0.0197048`.

We can similarly implement a continuous distirbution in cpplex, and in this example, we'll use the logistic distribution:

.. code-block:: cpp

    #include <ContinuousDistribution/ContinuousDistribution.hpp>
    #include <ContinuousDistribution/LogisticDistribution.hpp>
    #include <Complex/Complex.hpp>
    #include <iostream>
    
    int main(){
        ContinuousDistribution* dist; 
        Complex mu = 1 + 1_j; 
        Complex s = 1 + 2_j; 

        Complex z = 0.5 + 0.5_j; 

        Logistic logDist(mu, s); 
        dist = &logDist; 
        std::cout << dist->pdf(z) << "\n";

        return 0;
    }

Output:

.. code-block:: cpp

   0.0289212