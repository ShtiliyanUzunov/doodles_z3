from z3 import *

# Input unsorted list of integers
unsorted_list = [5, 1, 4, 10, 2, -2]

# Create a solver instance
s = Solver()

# Create a list of integer variables with the same length as the input list
variables_source = [Int(f'x_{i}') for i in range(len(unsorted_list))]
variables_target = [Int(f'y_{i}') for i in range(len(unsorted_list))]


# Add constraints to ensure the variables are equal to the values of the input list
for i in range(len(unsorted_list)):
    s.add(variables_source[i] == unsorted_list[i])
    s.add(Or([var == variables_source[i] for var in variables_target]))


# Add constraints to ensure the variables are sorted in non-decreasing order
for i in range(len(variables_target) - 1):
    s.add(variables_target[i] < variables_target[i + 1])

#Check if the problem is satisfiable
if s.check() == sat:
    # Get the model
    model = s.model()

    # Extract the sorted list from the model
    sorted_list = [model.evaluate(var).as_long() for var in variables_source]
    # Target list
    target_list = [model.evaluate(var).as_long() for var in variables_target]

    print(f"Source list: {unsorted_list}")
    print(f"Source variables: {sorted_list}")
    print(f"Target variables: {target_list}")
else:
    raise Exception("Failed to sort the list using Z3.")