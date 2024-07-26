
polar
=====

.. cpp:function:: constexpr double polar(const double r, const double theta) noexcept

   Returns a complex number given a magnitude :math:`r` and a phase angle :math:`theta`.

**Parameters**

    .. cpp:var:: const double r

        A real number. 

    .. cpp:var:: const double theta

        A real number. 

**Returns**

    .. cpp:type:: Complex

        A complex number. 

A complex number may be obtained from a magnitude :math:`r` and a phase angle :math:`\theta` by evaluating the following:

.. math::

   z = r\cos\theta + ir\sin\theta

**Example**

.. code-block:: cpp

    double r = 4; 
    double theta = 0.5; 
    std::cout << polar(r, theta) << "\n";

Output:

.. code-block:: cpp

   3.51033 + 1.9177j

**References**

.. [1] "Polar coordinate system", Wikipedia,
        https://en.wikipedia.org/wiki/Polar_coordinate_system