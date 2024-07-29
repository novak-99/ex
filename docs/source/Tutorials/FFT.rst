FFT
=====

The FFT module contains the fast fourier transform as well as various releated discrete transforms.

Let's begin by defining a complex sequence. This is done by using the :code:`std::vector<Complex>` type:

.. code-block:: cpp

    #include <FFT/FFT.hpp>
    #include <iostream>
    #include <vector>

    int main(){
        std::vector<Complex> X = {1, 2 + 2_j, 3 + 4_j, 5, 6 + 1_j};
        return 0; 
    }

Let's perform an FFT and print out the result:

.. code-block:: cpp

    #include <FFT/FFT.hpp>
    #include <iostream>
    #include <vector>
    
    int main(){
        std::vector<Complex> X = {1, 2 + 2_j, 3 + 4_j, 5, 6 + 1_j};
        std::vector<Complex> Y = fft(X);

        for(int i = 0; i < Y.size(); i++){
            std::cout << Y[i] << "\n";
        }
       return 0;
    }

Output:

.. code-block:: cpp

    17 + 7j
    0.302198 + 2.67078j
    -6.21644 - 0.741955j
    0.216441 - 1.64001j
    -6.3022 - 7.28881j

Notice that if we perform an IFFT on the result of the FFT we get back the original sequence:

.. code-block:: cpp

    #include <FFT/FFT.hpp>
    #include <iostream>
    #include <vector>

    int main(){
        std::vector<Complex> X = {1, 2 + 2_j, 3 + 4_j, 5, 6 + 1_j};
        std::vector<Complex> X_ = ifft(fft(X));

        for(int i = 0; i < X_.size(); i++){
            std::cout << X_[i] << "\n";
        }
       return 0;
    }


Output:

.. code-block:: cpp

    1 + 1.77636e-16j
    2 + 2j
    3 + 4j
    5 - 1.35162e-15j
    6 + 1j

Other transforms, including the DCT and the DST, are also included in this module:

.. code-block:: cpp

    #include <FFT/FFT.hpp>
    #include <iostream>
    #include <vector>

    int main(){
        std::vector<Complex> X = {1, 2 + 2_j, 3 + 4_j, 5, 6 + 1_j};
        std::vector<Complex> dctY = dct(X);
        std::vector<Complex> dstY = dst(X);

        for(int i = 0; i < dctY.size(); i++){
            std::cout << dctY[i] << "\n";
        }
        std::cout << "\n";

        for(int i = 0; i < dstY.size(); i++){
            std::cout << dstY[i] << "\n";
        }
       return 0;
    }

Output:

.. code-block:: cpp

    34 + 14j
    -13.0373 + 0.449028j
    1 - 7.61803j
    -0.171513 - 4.9798j
    -1 + 5.38197j

    21.6525 + 11.8541j
    -11.5842 + 2.62866j
    9.65248 - 5.1459j
    -5.98385 - 4.25325j
    6 + 6j

Both transforms are automatically set to being of type 2. You can change this by modifying the optional :code:`type` parameter. Types 1-4 are available for both DST and DCT.

.. code-block:: cpp

    #include <FFT/FFT.hpp>
    #include <iostream>
    #include <vector>

    int main(){
        std::vector<Complex> X = {1, 2 + 2_j, 3 + 4_j, 5, 6 + 1_j};
        std::vector<Complex> dctY = dct(X, 3);
        std::vector<Complex> dstY = dst(X, 3);

        for(int i = 0; i < dctY.size(); i++){
            std::cout << dctY[i] << "\n";
        }
        std::cout << "\n";

        for(int i = 0; i < dstY.size(); i++){
            std::cout << dstY[i] << "\n";
        }
       return 0;
    }

Output:

.. code-block:: cpp

    19.2444 + 10.8944j
    -17.7217 - 1.73903j
    7 - 6j
    -3.40288 - 6.44131j
    -0.119773 + 3.28594j

    23.3338 + 9.82328j
    -4.60149 + 5.27636j
    2 - 7j
    -0.454238 - 2.33209j
    -0.38957 + 5.12099j

Many more discrete transforms with the same mechanics are also implemented in this module. Please see the documentation for more details.