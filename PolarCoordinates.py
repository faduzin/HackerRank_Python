from math import sqrt
import cmath

if __name__ == '__main__' :
    complex = complex(input())
    x = complex.real
    y = complex.imag
    r = sqrt((x**2) + (y**2))
    phi = cmath.phase(complex)
    print(r)
    print(phi)

# What I learned:
# 1. How to deal with complex numbers
# 2. How to turn them in real numbers
# 3. cmath library
# 4. How to call sqrt function