import random

def gate_operations():
    gates = ['AND', 'OR', 'NOT', 'NAND', 'NOR', 'XOR']
    
    # Select a random gate type
    gate_type = random.choice(gates)
    
    # Generate random input values
    input_values = [random.choice([True, False]) for _ in range(2)]
    
    # Evaluate the gate operation
    if gate_type == 'AND':
        output = all(input_values)
    elif gate_type == 'OR':
        output = any(input_values)
    elif gate_type == 'NOT':
        output = not input_values[0]
    elif gate_type == 'NAND':
        output = not all(input_values)
    elif gate_type == 'NOR':
        output = not any(input_values)
    elif gate_type == 'XOR':
        output = sum(input_values) % 2 == 1
    
    # Generate the question string
    question = f"What is the output of the {gate_type} gate with inputs {input_values[0]} and {input_values[1]}?"
    
    # Generate options
    options = ['True', 'False']
    correct_answer = str(int(output))
    random.shuffle(options)
    
    # Generate options text
    options_text = "Options:\n"
    for i, option in enumerate(options):
        options_text += f"{i+1}. {option}\n"
    
    return question, options_text, correct_answer
    
    
def gate_equivalence():
    # Define the gate types for the circuits
    gates = ['AND', 'OR', 'NOT', 'NAND', 'NOR', 'XOR']
    
    # Generate two random logic circuits
    circuit_1 = [random.choice(gates) for _ in range(3)]
    circuit_2 = [random.choice(gates) for _ in range(3)]
    
    # Ensure that the circuits are not identical
    while circuit_1 == circuit_2:
        circuit_2 = [random.choice(gates) for _ in range(3)]
    
    # Generate the question string
    question = "Are the following logic circuits equivalent?\n\n"
    question += "Circuit 1: " + " -> ".join(circuit_1) + "\n"
    question += "Circuit 2: " + " -> ".join(circuit_2) + "\n"
    
    # Determine the correct answer
    correct_answer = "Yes" if set(circuit_1) == set(circuit_2) else "No"
    options = ['Yes','No',]
    
    return question, options, correct_answer
    

question_list={
    1: gate_operations,
    2: gate_equivalence,
}

def generate_question_logic_gates(level):
    q,o,a = question_list[random.randint(1,2)]()
    return q,o,a

if __name__ == "__main__":
    ans = generate_question_logic_gates(1)
    print(ans)