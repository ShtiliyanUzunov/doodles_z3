from z3 import *
a = Int('a')
b = Int('b')

s = Solver()
s.add(1 <= a)
s.add(a <= 6)
s.add(1 <= b)
s.add(b <= 5)
s.add(a >= 2*b)

while s.check() == sat:
  print(s.model())
  # prevent next model from using the same assignment as a previous model
  s.add(Or(a != s.model()[a], b != s.model()[b]))