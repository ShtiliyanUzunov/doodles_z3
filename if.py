from z3 import *

x = Int('x')
y = Int('y')
z = If(x > 0, 5, 10)
d = z + 2

solve(x == 2,y == 1, d != 7)