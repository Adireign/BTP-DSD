import random

# Function to generate truth table construction questions
def generate_truth_table_question(num_inputs):
    # Generate random input values for the truth table
    input_values = [[random.choice([True, False]) for _ in range(num_inputs)] for _ in range(2**num_inputs)]
    
    # Generate the question string
    question = "Construct the truth table for the following logic circuit:\n"
    for i in range(num_inputs):
        question += f"Input_{i+1}\t"
    question += "Output\n"
    
    # Generate truth table rows
    truth_table = []
    for values in input_values:
        input_str = "\t".join([str(int(value)) for value in values])
        output = evaluate_circuit(values)
        truth_table.append((input_str, str(int(output))))
    
    # Shuffle the truth table rows
    random.shuffle(truth_table)
    
    # Generate options
    options = [truth_table[i][1] for i in range(4)]
    correct_answer = str(options.index(truth_table[0][1]) + 1)
    random.shuffle(options)
    
    # Generate the question text with options
    question_text = question
    for i in range(len(truth_table)):
        question_text += f"{truth_table[i][0]}\n"
    
    # Generate options text
    options_text = ""
    for i, option in enumerate(options):
        options_text += f"{i+1}. {option}\n"
    
    return question_text, options_text, correct_answer

# Function to evaluate the circuit for a given set of input values
def evaluate_circuit(input_values):
    # Example logic circuit: OR of all input values
    return any(input_values)

# Example usage
num_inputs = 3  # Number of inputs for the logic circuit
question, options, correct_answer = generate_truth_table_question(num_inputs)
print(question)
print("Options:")
print(options)
print("Correct answer:", correct_answer)
