import random

# Function to generate a question involving gate equivalence
def generate_gate_equivalence_question():
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
    
    return question, correct_answer

# Example usage
question, correct_answer = generate_gate_equivalence_question()
print(question)
print("Correct answer:", correct_answer)
