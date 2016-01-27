import sympy as sy
import numpy as np

def fun_1( your_id ):
    ans = hex(your_id)
    return ans

def my_integral():
    x = sy.Symbol('x')
    ans = sy.integrate( x**6*sy.exp(-x**2), (x,0, sy.oo))
    return ans

def my_solution():
    A = np.array([[2,3,5,6,1,0,2,1,3,4],
                  [1,6,3,2,3,1,0,6,7,2],
                  [5,1,2,3,6,2,2,1,6,8],
                  [2,5,1,1,0,3,2,1,3,2],
                  [1,4,0,2,0,4,1,3,4,6],
                  [1,3,7,4,3,2,0,1,1,0],
                  [7,2,4,5,7,1,0,3,1,2],
                  [6,1,1,2,2,7,0,1,3,3],
                  [3,2,2,4,5,1,0,6,3,1],
                  [1,2,3,0,3,2,5,1,0,8]])
    b = np.array([10,12,17,9,6,9,12,8,7,8])
    x = np.linalg.solve(A,b) # Solve Ax = b
    return x


if __name__ == '__main__':
    your_id = 1303444
    print('Hexadecimal representation of %d is %s'%( your_id, fun_1( your_id)))
    print('Integral = ', my_integral())
    print('Solution = ', my_solution())
