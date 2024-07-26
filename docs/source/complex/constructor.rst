
constructor
=====

.. cpp:function:: constexpr Complex() noexcept
.. cpp:function:: constexpr Complex(const double x) noexcept
.. cpp:function:: constexpr Complex(const double x, const double y) noexcept
.. cpp:function:: constexpr Complex(const Complex& z) noexcept
.. cpp:function:: template <class T> constexpr \ Complex(const std::complex<T>& z) noexcept

   Instantiates an object for the :code:`Complex` class.

**Parameters**

    .. cpp:var:: const double x

        A real number, the real argument.

    .. cpp:var:: const double y

        A real number, the imaginary argument.

    .. cpp:var:: const Complex& z

        A complex number. 

    .. cpp:var:: const std::complex<T>& z

        A standard C++ complex number.

Initializes a :code:`Complex` object with real and imaginary components. If unspecified by the user, the respective component will be set to :code:`0`.

**Example**

.. code-block:: cpp

    std::cout << Complex(5, 4) << "\n";

Output:

.. code-block:: cpp

    5 + 4j

**References**

.. [1] "Gauss–Kronrod quadrature formula", Wikipedia,
        https://en.wikipedia.org/wiki/Gauss%E2%80%93Kronrod_quadrature_formula