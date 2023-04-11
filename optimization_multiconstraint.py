from z3 import *

# Create a Z3 optimize instance
opt = Optimize()

# Define variables
x, y, z = Ints('x y z')

# Add hard constraints to the problem
opt.add(x + y + z <= 10)
opt.add(x >= 0)
opt.add(y >= 0)
opt.add(z >= 0)

# Define multiple optimization objectives
objective1 = opt.maximize(x)  # Maximize x
objective2 = opt.minimize(y)  # Minimize y
objective3 = opt.maximize(z)  # Minimize z

# Set the solving strategy to "pareto" or "lex" for handling multiple objectives
opt.set(priority="pareto")

# Add multiple soft constraints with different weights
opt.add_soft(x <= 5, weight=1)
opt.add_soft(y <= 5, weight=1)
opt.add_soft(z <= 2, weight=1)

# Solve the optimization problem
result = opt.check()
if result == sat:
    print("Optimal solution found:")
    model = opt.model()
    print(f"x = {model[x]}, y = {model[y]} , z = {model[z]}")
else:
    print("No solution found.")