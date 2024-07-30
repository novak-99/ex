Complex
=====

Many of cpplex's operations are many times faster than those in standard C++.

While this is mostly due to C++'s NaN-checking, it is important to note that for most use cases, this is unnecessary, and causes many functions to perform very slowly.

The following table shows a list of results of benchmarks comparing operation for :code:`cpplex::Complex` and :code:`std::complex`. 

Each benchmark performs the operation :code:`N = 1e+9` times while compound assigning to and printing a dummy variable to ensure volatility. Each benchmark is an average of 3 runs.

.. list-table::
   :widths: 25 25 25
   :header-rows: 1

   * - Function Name
     - Heading row 1, column 2
     - Heading row 1, column 3
   * - :code:`cpplex::Complex`
     -
     - Row 1, column 3
   * - :code:`std::complex`
     - Row 2, column 2
     - Row 2, column 3