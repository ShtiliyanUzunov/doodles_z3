import z3
from z3 import *

from ast_visualization import expr_to_graph

mast_height = 7
antennas = [2, 1.7, 1.2]
spacing = 0.2

z3_mast_height = z3.Real('mast_height')
z3_antenna_heights = [z3.Real('a%d' % i) for i in range(len(antennas))]
z3_spacing = z3.Real('spacing')

z3_top_points = [z3.Real('top_point%d' % i) for i in range(len(antennas))]
z3_bottom_points = [z3.Sum(z3_top_points[i], z3_antenna_heights[i]) for i in range(len(z3_top_points))]

assignments = [z3_antenna_heights[i] == antennas[i] for i in range(0, len(antennas))] + \
              [z3_spacing == spacing, z3_mast_height == mast_height]
heights_sum = [z3.Sum([z3.Sum(z3_antenna_heights[i], z3_spacing) for i in range(0, len(antennas))]) <= mast_height]
overlaps = []
val_constraints = [z3.And(z3_top_points[i] > z3_antenna_heights[i], z3_top_points[i] <= z3_mast_height) for i in range(len(z3_top_points))]
start_from_top = [z3.Or([z3_top_points[i] == z3_mast_height for i in range(len(z3_top_points))])]

for i in range(len(z3_bottom_points)):
    top_point = z3_top_points[i]
    bottom_point = z3_bottom_points[i]
    for j in range(i + 1, len(z3_bottom_points)):
        check_point = z3_top_points[j]
        overlaps.append(z3.Or(check_point > bottom_point, check_point < top_point))

solver = z3.Solver()
all_constraints = assignments + heights_sum + overlaps + val_constraints + start_from_top

graph = expr_to_graph(And(all_constraints))

# Save the graph to a file and display it
graph.render('graphs/antenna_positioning_constraints', view=True, cleanup=True, format='png')


solver.add(all_constraints)
result = solver.check()
model = solver.model()
print(model)
# res = model.get_interp(z3_top_points[0])
# print(res.as_decimal())
#
# result = z3.solve(assignments + heights_sum + overlaps + val_constraints + start_from_top)
# print(result)
