Signal
=====

The Signal module includes various discrete transforms necessary for signal processing.

Let's define a two Complex sequences:

.. code-block:: cpp

    #include <Signal/Signal.hpp>
    #include <Complex>
    #include <iostream>
    #include <vector>

    int main(){
        std::vector<Complex> X = {1, 2 + 2_j, 3 + 4_j, 5, 6 + 1_j};
        std::vector<Complex> Y = {3, 4, 7, 8, 1 + 1_j};
        return 0; 
    }

And apply a 1D convolution:

.. code-block:: cpp

    #include <Signal/Signal.hpp>
    #include <Complex>
    #include <iostream>
    #include <vector>
    
    int main(){
        std::vector<Complex> X = {1, 2 + 2_j, 3 + 4_j, 5, 6 + 1_j};
        std::vector<Complex> Y = {3, 4, 7, 8, 1 + 1_j};
        std::vector<Complex> Z = conv(X, Y);

        for(int i = 0; i < Z.size(); i++){
            std::cout << Z[i] << "\n";
        }
       return 0;
    }

Output:

.. code-block:: cpp

    3 - 2.21058e-14j
    10 + 6j
    24 + 20j
    49 + 30j
    76 + 48j
    83 + 40j
    81 + 14j
    53 + 13j
    5 + 7j

The 1D convolution is defined as the following operation:

.. math::

    (X * Y)[n] = \sum_{-\infty}^{\infty}X[m]Y[n - m]

If an index is less than zero, or greater than the size of the array (meaning that it doesn't exist!) we can simply set it to zero.

A very similar operation is the cross-correlation operation, defined as:

.. math::

    \newcommand{\compconj}[1]{%
    \overline{#1}%
    }
    (X \star Y)[n] = \sum_{-\infty}^{\infty}\compconj{X[m]}Y[n + m]

Where the horizontal line notation indicates the conjugate of the complex sequence :math:`X`. We can implement it in the same way:

.. code-block:: cpp

    #include <Signal/Signal.hpp>
    #include <Complex>
    #include <iostream>
    #include <vector>

    int main(){
        std::vector<Complex> X = {1, 2 + 2_j, 3 + 4_j, 5, 6 + 1_j};
        std::vector<Complex> Y = {3, 4, 7, 8, 1 + 1_j};
        std::vector<Complex> Z = crosscorr(X, Y);

        for(int i = 0; i < Z.size(); i++){
            std::cout << Z[i] << "\n";
        }
       return 0;
    }

Output:

.. code-block:: cpp

    1 - 1j
    12 - 6.35623e-14j
    30 + 17j
    47 + 41j
    79 + 31j
    101 + 30j
    71 + 19j
    39 + 4j
    18 + 3j

Finally, the auto-correlation operation, defined as a cross-correlation by a sequence with itself, may be implemented in a similar manner:

.. code-block:: cpp

    #include <Signal/Signal.hpp>
    #include <Complex>
    #include <iostream>
    #include <vector>

    int main(){
        std::vector<Complex> X = {1, 2 + 2_j, 3 + 4_j, 5, 6 + 1_j};
        std::vector<Complex> Z = autocorr(X);

        for(int i = 0; i < Z.size(); i++){
            std::cout << Z[i] << "\n";
        }
       return 0;
    }

Output:

.. code-block:: cpp

    6 - 1j
    19 + 10j
    35 + 27j
    61 + 11j
    96 + 5.88879e-16j
    61 - 11j
    35 - 27j
    19 - 10j
    6 + 1j