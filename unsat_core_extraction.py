from z3 import *

# This piece of code fins which constraints are responsible for the unsatisfiability of a problem.

# Create a solver instance
s = Solver()

# Create some integer variables
a, b, c, d = Ints('a b c d')

# Add constraints with tracking identifiers
s.assert_and_track(a > b, "a_greater_than_b")
s.assert_and_track(b > c, "b_greater_than_c")
s.assert_and_track(c > a, "c_greater_than_a")
s.assert_and_track(a > d, "a_greater_than_d")
s.assert_and_track(d > 25, "d_greater_than_25")

# Check if the problem is satisfiable
if s.check() == unsat:
    #Get the unsat core
    unsat_core = s.unsat_core()

    print("Unsat core:")
    for constraint in unsat_core:
        print(constraint)
else:
    print("The problem is satisfiable.")