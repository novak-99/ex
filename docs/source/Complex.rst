Complex
=====

.. cpp:class:: Complex

   The cpplex complex data type. 

This class defines the libray's complex data type. To initialize it, you may use its various constructors, the standard C++ complex literal :code:`i`, or cpplex's complex literal :code:`_j`.

Defined in header :code:`<Complex.hpp>`.

Functions
--------

.. toctree::
   :maxdepth: 2

   Complex/constructor
   Complex/setX
   Complex/setY
   Complex/getX
   Complex/getY
   Complex/real
   Complex/im
   Complex/operators
   Complex/std

Non-member Functions
--------

.. toctree::
   :maxdepth: 2

   Complex/operatorsNonmember
   Complex/realNonmember
   Complex/imNonmember
   Complex/mod
   Complex/arg
   Complex/norm
   Complex/conj
   Complex/dot
   Complex/proj
   Complex/polar
   Complex/exp
   Complex/log
   Complex/log10
   Complex/log2
   Complex/pow
   Complex/sqrt
   Complex/sin
   Complex/cos
   Complex/tan
   Complex/asin
   Complex/acos
   Complex/atan
   Complex/sinh
   Complex/cosh
   Complex/tanh
   Complex/asinh
   Complex/acosh
   Complex/atanh
   Complex/sgn
   Complex/rootsOfUnity
   Complex/isNan
   
**Example**

.. code-block:: cpp

   Complex z1 = 5 + 4_j; 
   Complex z2 = 5 + 3i;    
   std::cout << z1 + conj(z2) << "\n";

Output:

.. code-block:: cpp

   10 + 1j