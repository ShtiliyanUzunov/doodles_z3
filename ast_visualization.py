from z3 import *
from graphviz import Digraph


def expr_to_graph(expr, graph=None, parent=None):
    if graph is None:
        graph = Digraph()

    node_label = str(expr.decl())
    node_id = f'node{expr.get_id()}'
    graph.node(node_id, node_label)

    if parent is not None:
        graph.edge(parent, node_id)

    for child in expr.children():
        expr_to_graph(child, graph, node_id)

    return graph


# Create a Z3 expression
x = Int('x')
y = Int('y')
z = x + y * 2

# Convert the Z3 expression to a Graphviz graph
graph = expr_to_graph(z)

# Save the graph to a file and display it
graph.render('graphs/example_sum', view=True, cleanup=True, format='png')