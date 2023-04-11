from z3 import *

# Create a Z3 optimize instance
opt = Optimize()

# Define variables
x, y = Ints('x y')

# Add hard constraints to the problem
opt.add(x + y <= 10)
opt.add(x >= 0)
opt.add(y >= 0)

# Define the optimization objective
opt.minimize(x + y)

# Add a soft constraint with a weight
opt.add_soft(x <= 5, weight=1)

# Solve the optimization problem
result = opt.check()
if result == sat:
    print("Optimal solution found:")
    model = opt.model()
    print(f"x = {model[x]}, y = {model[y]}")
else:
    print("No solution found.")