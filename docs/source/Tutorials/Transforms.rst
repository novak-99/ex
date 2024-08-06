Transforms
=====

Unlike various other complex/scientific computing libraries, cpplex contains a Transforms module which includes various continuous transforms.

Let's first define a function :math:`f(z) = e^{-z^2}`:

.. code-block:: cpp

    #include <Transforms.hpp>
    #include <Complex.hpp>
    #include <iostream>

    int main(){
        auto f = [](Complex t) { return exp(-t * t); };
        return 0; 
    }

The Laplace transform is one of the most useful and commonly used continuous integral transforms and is used in fields such as differential equations. It is defined as the following:

.. math::
   \mathcal{L}\{f\}(z) = \int_{0}^{\infty}f(t)e^{-zt}dt

And so we can evaluate this transform for a certain :math:`z` and function :math:`f(z)`:

.. code-block:: cpp

    #include <Transforms.hpp>
    #include <Complex.hpp>
    #include <iostream>
    
    int main(){
        auto f = [](Complex t) { return exp(-t * t); };
        Complex z = 1.0; 
        std::cout << laplace(f, z) << "\n";
       return 0;
    }

Output:

.. code-block:: cpp

    0.545648 + 0j


The true value is :math:`0.54564136 \ldots`

You may also specify the optional argument :code:`a` which corresponds to the Laplace transform of a function :math:`f(az)`:

.. code-block:: cpp

    #include <Transforms.hpp>
    #include <Complex.hpp>
    #include <iostream>
    
    int main(){
        auto f = [](Complex t) { return exp(-t * t); };
        Complex z = 1.0; 
        std::cout << laplace(f, z, 2) << "\n";
       return 0;
    }

Output:

.. code-block:: cpp

    0.341348 + 0j

The true value is :math:`0.34135092 \ldots`

This module also features continuous versions of the discrete transforms featured in the signal module. For example, the continuous convolution transform, defined as:

.. math::

    (f * g)(t) = \int_{-\infty}^{\infty}f(\tau)g(t - \tau)d\tau

can be called on two functions :math:`f` and :math:`g` for a point :math:`t` as such:

.. code-block:: cpp

    #include <Transforms.hpp>
    #include <Complex.hpp>
    #include <iostream>

    int main(){
        auto f = [](Complex t) { return exp(-t * t); };
        auto g = [](Complex t) { return exp(-t * t); };
        Complex t = 1; 
        std::cout << conv(f, g, t) << "\n";

       return 0;
    }

Output:

.. code-block:: cpp

    0.760276 + 0j