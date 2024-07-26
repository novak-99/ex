Complex
=====

.. cpp:class:: Complex

   The cpplex complex data type. 



Functions
--------

.. toctree::
   :maxdepth: 2

   complex/constructor

Non-member Functions
--------

**Example**

.. code-block:: cpp

   Complex z1 = 5 + 4_j; 
   Complex z2 = 5 + 3i;    
   std::cout << z1 + conj(z2) << "\n";

Output:

.. code-block:: cpp

   10 + 1j