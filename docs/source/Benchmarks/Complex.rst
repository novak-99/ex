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
     - 0.893s
     - 0.887s
   * - :code:`operator-`
     - 0.893s
     - 0.894s
   * - :code:`operator*`
     - 0.894s
     - 1.193s
   * - :code:`operator/`
     - 0.895s
     - 8.495s
   * - :code:`mod` / :code:`abs`
     - 0.910s
     - 0.916s
   * - :code:`arg`
     - 0.885s
     - 0.891s
   * - :code:`conj`
     - 0.917s
     - 0.910s
   * - :code:`proj`
     - 0.916s
     - 0.916s
   * - :code:`polar`
     - 0.897s
     - 0.904s
   * - :code:`exp`
     - 0.911
     - 0.9s
   * - :code:`log`
     - 0.901
     - 0.896
   * - :code:`pow`
     - 0.902s
     - 8.649s