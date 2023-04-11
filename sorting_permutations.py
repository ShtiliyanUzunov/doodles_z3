from z3 import *

def get_unsorted_permutations(sorted_list):
    # Create a Z3 solver instance
    solver = Solver()

    # Create a list of Z3 integer variables representing the unsorted list
    unsorted_list = [Int(f'element_{i}') for i in range(len(sorted_list))]

    # Add the constraint that the elements of the unsorted list must be equal to those in the sorted list
    for elem in sorted_list:
        solver.add(Sum([If(elem == unsorted_list[i], 1, 0) for i in range(len(sorted_list))]) == 1)

    # Add the sorting constraint
    for i in range(len(sorted_list) - 1):
        solver.add(sorted_list[i] <= sorted_list[i + 1])

    # Find all possible unsorted permutations
    unsorted_permutations = []
    while solver.check() == sat:
        model = solver.model()
        unsorted_permutation = [model[unsorted_list[i]].as_long() for i in range(len(sorted_list))]
        unsorted_permutations.append(unsorted_permutation)

        # Add a constraint to exclude the current solution and search for a new one
        solver.add(Or([unsorted_list[i] != unsorted_permutation[i] for i in range(len(sorted_list))]))

    return unsorted_permutations

# Example usage
sorted_list = [1, 2, 3, 4]
unsorted_permutations = get_unsorted_permutations(sorted_list)
print("Unsorted permutations:")
for permutation in unsorted_permutations:
    print(permutation)