from z3 import *

x = Int('x')
y = Int('y')
z = Int('z')
f = Function('f', IntSort(), IntSort())

solve(Distinct(x, y, z), x == 4)

int_vector = IntVector('int_vector', 4)

solve(Distinct(int_vector), int_vector[2] == 4, int_vector[3] == x)
