from z3 import *

# Create a Z3 solver instance
solver = Solver()

# Create a Z3 real variable for BMI
bmi = Real('bmi')

# Add the range constraint for BMI (it should be a positive value)
solver.add(bmi > 0)

# Define the weight status category constraints
underweight = bmi < 18.5
normal_weight = And(bmi >= 18.5, bmi <24.9)
overweight = And(bmi >= 24.9, bmi < 29.9)
obesity = bmi >= 29.9

# Add a constraint that asserts a BMI value falls into multiple categories
solver.add(Or(
    And(underweight, normal_weight),
    And(underweight, overweight),
    And(underweight, obesity),
    And(normal_weight, overweight),
    And(normal_weight, obesity),
    And(overweight, obesity)
))

# Check if the solver can find a solution
result = solver.check()
if result == unsat:
    print("The categorization logic is consistent.")
else:
    print("The categorization logic is inconsistent.")