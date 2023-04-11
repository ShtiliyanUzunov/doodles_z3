import z3
from z3 import *


f = Function('f', IntSort(), IntSort(), IntSort())
x = Int('x')
y = Int('y')
solve(ForAll([x, y], f(x, y) == x + y), f(x,y) == x * y, f(x,y) == -x -y, show=True)

x = Int('x')
#print ((x + 1).hash())
#print ((1 + x).hash())
#print (x.sort().hash())

x = Int('x')
print("is expression: ", is_expr(x))
n = x + 2
print("is application:", is_app(n))
print("decl:          ", n.decl())
print("num args:      ", n.num_args())
for i in range(n.num_args()):
    print("arg(", i, ") ->", n.arg(i))