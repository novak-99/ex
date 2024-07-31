Complex
=====

Many of cpplex's operations are many times faster than those in standard C++.

While this is mostly due to C++'s NaN-checking, it is important to note that for most use cases, this is unnecessary, and causes many functions to perform very slowly.

The following table shows a list of results of benchmarks comparing operations for :code:`cpplex::Complex` and :code:`std::complex`. Please note that for operations with multiple definitions, the definition where all arguments are complex numbers is used for testing.

Each benchmark performs the operation :code:`N = 1e+9` times while compound assigning to and printing a dummy variable to ensure volatility. Each benchmark is an average of 3 runs.

Runs for which cpplex demonstrates nonnegligible speed gains over C++ are bolded.

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
     - **0.894s**
     - **1.193s**
   * - :code:`operator/`
     - **0.895s**
     - **8.495s**
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
     - 0.911s
     - 0.9s
   * - :code:`log`
     - 0.901s
     - 0.898s
   * - :code:`log10`
     - 0.901s
     - 0.905s
   * - :code:`pow`
     - **0.902s**
     - **8.649s**
   * - :code:`sqrt`
     - **0.911s**
     - **9.134s**
   * - :code:`sin`
     - 0.899s
     - 0.899s
   * - :code:`cos`
     - 0.893s
     - 0.896s
   * - :code:`tan`
     - 0.908s
     - 0.906s
   * - :code:`asin`
     - **0.901s**
     - **35.928s**
   * - :code:`acos`
     - **0.906s**
     - **42.850s**
   * - :code:`atan`
     - **0.901s**
     - **25.061s**
   * - :code:`sinh`
     - 0.901s
     - 0.902s
   * - :code:`cosh`
     - 0.905s
     - 0.908s
   * - :code:`tanh`
     - 0.9s
     - 0.9s
   * - :code:`asinh`
     - **0.911s**
     - **35.977s**
   * - :code:`acosh`
     - **0.917s**
     - **43.233s**
   * - :code:`atanh`
     - **0.908s**
     - **25.853s**