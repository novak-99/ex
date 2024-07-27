Complex
=====

.. cpp:class:: Complex

   The cpplex complex data type. 

This class defines the libray's complex data type. To initialize it, you may use its various constructors, the standard C++ complex literal :code:`i`, or our complex literal :code:`_j`.

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

Non-member Functions
--------

.. toctree::
   :maxdepth: 2

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
   
**Example**

.. code-block:: cpp

   Complex z1 = 5 + 4_j; 
   Complex z2 = 5 + 3i;    
   std::cout << z1 + conj(z2) << "\n";

Output:

.. code-block:: cpp

   10 + 1j