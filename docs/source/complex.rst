Complex
=====

.. cpp:class:: Complex

   The cpplex complex data type. 

This class defines the libray's complex data type. To initialize it, you may use its various constructors, the standard C++ complex literal :code:`i`, or our complex literal :code:`_j`.

Defined in header :code:`<Complex/Complex.hpp>`.

Functions
--------

.. toctree::
   :maxdepth: 2

   complex/constructor
   complex/setX
   complex/setY
   complex/getX
   complex/getY
   complex/real
   complex/im
   complex/operators

Non-member Functions
--------

.. toctree::
   :maxdepth: 2

   complex/operatorsNonmember
   complex/realNonmember
   complex/imNonmember
   complex/mod
   complex/arg
   complex/norm
   complex/conj
   complex/dot
   complex/proj
   complex/polar
   complex/exp
   complex/log
   complex/log10
   complex/pow
   complex/sqrt
   complex/sin
   complex/cos
   complex/tan
   complex/asin
   complex/acos
   complex/atan
   complex/sinh
   complex/cosh
   complex/tanh
   complex/asinh
   complex/acosh
   complex/atanh
   complex/sgn
   complex/rootsOfUnity
   complex/isNan
   
**Example**

.. code-block:: cpp

   Complex z1 = 5 + 4_j; 
   Complex z2 = 5 + 3i;    
   std::cout << z1 + conj(z2) << "\n";

Output:

.. code-block:: cpp

   10 + 1j