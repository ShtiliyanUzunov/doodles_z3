from z3 import *

x = Int('x')
y = Int('y')
z = If(x > 0, 5, 10)
d = z + 2

solve(x == -2, y == 1, d != 7)

arr = Array('arr', IntSort(), IntSort())

arr = Store(arr, 0, 5)
arr = Store(arr, 1, 5)
arr = Store(arr, 2, 2)
arr = Store(arr, 3, 5)
arr = Store(arr, 4, x)

solve(Sum([Select(arr, i) for i in range(5)]) <= 18, x > 0)

idx = Int('idx')
solve(Select(arr, idx) % 2 == 0, x > 0, x < 12, x % 3 == 0, idx != 4)

F, H, A, B, C = Bools('F H A B C')
s = Solver()
s.add(F, H, Implies(A, B))
print(s)
