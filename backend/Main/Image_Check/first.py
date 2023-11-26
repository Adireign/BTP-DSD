from graphviz import Digraph
import random

# Create a Graphviz object
dot = Digraph(comment='Gate Diagram')

# Define gate types
gate_types = ['AND', 'OR', 'NOT']

# Function to generate a random gate diagram
def generate_random_gate_diagram(num_inputs):
    # Initialize gates
    gates = []
    inputs = [f'Input_{i}' for i in range(num_inputs)]

    # Randomly generate gate connections
    for i in range(num_inputs, random.randint(num_inputs + 1, num_inputs + 3)):
        input1, input2 = random.sample(inputs, 2)
        gate_type = random.choice(gate_types)
        output = f'Gate_{i}'
        inputs.remove(input1)
        inputs.remove(input2)
        inputs.append(output)
        gates.append((input1, input2, gate_type, output))

    # Add gates to the Graphviz diagram
    for gate in gates:
        input1, input2, gate_type, output = gate
        dot.node(input1)
        dot.node(input2)
        dot.node(output, label=gate_type)
        dot.edge(input1, output)
        dot.edge(input2, output)

    return dot

# Example: Generate a gate diagram with 4 input variables
num_inputs = 4
generate_random_gate_diagram(num_inputs).render('gate_diagram')
