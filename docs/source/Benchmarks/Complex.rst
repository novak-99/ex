Complex
=====

Many of cpplex's operations are many times faster than those in standard C++.

While this is mostly due to C++'s NaN-checking, it is important to note that for most use cases, this is unnecessary, and causes many functions to perform very slowly.

The following table shows a list of results of benchmarks comparing operations for :code:`cpplex::Complex` and :code:`std::complex`. Please note that for operations with multiple definitions, the definition where all arguments are complex numbers is used for testing.

Each benchmark performs the operation :code:`N = 1e+9` times while compound assigning to and printing a dummy variable to ensure volatility. Each benchmark is an average of 3 runs.

.. list-table::
   :widths: 25 25 25
   :header-rows: 1

   * - Function
     - :code:`cpplex::Complex`
     - :code:`std::complex`
   * - :code:`operator+`
     - 0.893
     - 0.887
   * - :code:`operator-`
     - 0.893
     - 0.894
   * - :code:`operator*`
     - 0.894
     - 1.193
   * - :code:`operator/`
     - 0.895
     - 8.495
   * - :code:`mod` / :code:`abs`
     - 0.910
     - 0.916
   * - :code:`arg`
     - 0.885
     - 0.891
   * - :code:`conj`
     - 0.917
     - 0.910
   * - :code:`proj`
     - 0.916
     - 0.916
   * - :code:`polar`
     - 0.897
     - 0.904
   * - :code:`pow`
     - 0.902
     - 8.649