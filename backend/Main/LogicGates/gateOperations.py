import random

# Function to generate a question involving a simple gate operation
def generate_simple_gate_operation_question():
    # Define available gate types
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

# Example usage
question, options, correct_answer = generate_simple_gate_operation_question()
print(question)
print(options)
print("Correct answer:", correct_answer)
