from z3 import *

# Define a List structure in Z3
List = Datatype('List')
List.declare('cons', ('value', IntSort()), ('next', List))
List.declare('nil')
List = List.create()

# Helper functions to construct and manipulate lists in Z3
def cons(x, l):
    return List.cons(x, l)

def value(l):
    return List.value(l)

def next(l):
    return List.next(l)

def nil():
    return List.nil

def is_nil(l):
    return List.is_nil(l)

# Define a recursive function to sum the values of a list in Z3
sum_list = RecFunction('sum_list', List, IntSort())
l = Const('l', List)

sum_list_def = RecAddDefinition(sum_list, l, If(is_nil(l), 0, value(l) + sum_list(next(l))))

x1, x2, x3, x4, x5, x6 = Ints('x1 x2 x3 x4 x5 x6')

# Example usage
l1 = cons(x1, cons(x2, cons(x3, cons(x4, cons(x5, cons(x6, nil()))))))
s = Solver()

# Check if the sum of values in the list l1 is equal to 20
s.add(sum_list(l1) == 20)
s.add(x1 > 0)
s.add(x2 > 0)
s.add(x3 > 0)
s.add(x4 > 0)
s.add(x5 > 0)
s.add(x6 > 0)

if s.check() == sat:
    print(s.model())
else:
    print("The sum of values in the list is not equal to 20")