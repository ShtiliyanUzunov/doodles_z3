from z3 import *

def group_numbers(numbers):
    n = len(numbers)
    if n % 3 != 0:
        raise ValueError("The number of elements must be a multiple of 3.")

    num_groups = n // 3
    groups = [IntVector(f'group{i}', 3) for i in range(num_groups)]

    s = Solver()

    # Equality constraints for each group
    for i in range(num_groups):
        for j in range(3):
            s.add(Or([groups[i][j] == numbers[k] for k in range(n)]))

    # Distinct numbers in each group
    for group in groups:
        s.add(Distinct(group))

    # No repetitions across groups
    for i in range(num_groups):
        for j in range(num_groups):
            if i != j:
                for k in range(3):
                    s.add(Distinct(groups[i][k], groups[j][k]))

    if s.check() == sat:
        result = []
        m = s.model()
        for group in groups:
            group_values = [m.evaluate(g).as_long() for g in group]
            result.append(group_values)
        return result
    else:
        raise ValueError("No solution found.")

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    grouped_numbers = group_numbers(numbers)
    print("Grouped numbers:", grouped_numbers)