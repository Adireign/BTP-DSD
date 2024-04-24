import random
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

# Function to generate logic gate questions

# first type - Diagrams
def generate_complicated_question_with_image():
    gates = ['AND', 'OR', 'NOT', 'NAND', 'NOR', 'XOR']
    
    # Generate gates at first level
    first_level_gate_1 = random.choice(gates)
    first_level_gate_2 = random.choice(gates)
    first_level_gate_3 = random.choice(gates)
    
    # Generate gates at second level
    second_level_gate = random.choice(gates)
    
    # Generate input names and values
    input_names = ['A', 'B', 'C']
    input_values = [random.choice([True, False]) for _ in range(len(input_names))]
    
    # Generate question
    question = "What is the output of the following circuit?\n"
    question += f"{first_level_gate_1} gate with inputs {input_names[0]} and {input_names[1]}\n"
    question += f"{first_level_gate_2} gate with inputs {input_names[1]} and {input_names[2]}\n"
    question += f"{first_level_gate_3} gate with inputs {input_names[0]} and {input_names[2]}\n"
    question += f"{second_level_gate} gate with inputs output_{first_level_gate_1}, output_{first_level_gate_2}, and output_{first_level_gate_3}\n"
    
    # Generate gate images
    gate_images = []
    gate_images.append(draw_gate_image(first_level_gate_1, [input_names[0], input_names[1]], f"output_{first_level_gate_1}", input_values[0], input_values[1]))
    gate_images.append(draw_gate_image(first_level_gate_2, [input_names[1], input_names[2]], f"output_{first_level_gate_2}", None, input_values[1]))
    gate_images.append(draw_gate_image(first_level_gate_3, [input_names[0], input_names[2]], f"output_{first_level_gate_3}", input_values[0], input_values[2]))
    gate_images.append(draw_gate_image(second_level_gate, [f"output_{first_level_gate_1}", f"output_{first_level_gate_2}", f"output_{first_level_gate_3}"], "Output", None, None))
    
    # Generate correct answer
    correct_answer = evaluate_gate_sequence([first_level_gate_1, first_level_gate_2, first_level_gate_3, second_level_gate], input_values)
    
    return question, correct_answer, gate_images

# Function to evaluate gate sequence
def evaluate_gate_sequence(gate_sequence, input_values):
    stack = input_values.copy()
    for gate_type in gate_sequence:
        if gate_type == 'AND':
            stack.append(all(stack))
        elif gate_type == 'OR':
            stack.append(any(stack))
        elif gate_type == 'NOT':
            stack[-1] = not stack[-1]
        elif gate_type == 'NAND':
            stack.append(not all(stack))
        elif gate_type == 'NOR':
            stack.append(not any(stack))
        elif gate_type == 'XOR':
            stack.append(sum(stack) % 2 == 1)
    return stack[-1]

# Function to draw gate image
def draw_gate_image(gate_type, input_names, output_name, input_value1=None, input_value2=None):
    width = 200
    height = max(len(input_names) * 50 + 20, 100)
    image = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    
    # Draw input and output lines
    input_spacing = height // (len(input_names) + 1)
    for i, input_name in enumerate(input_names):
        draw.text((5, (i + 1) * input_spacing - 10), input_name, fill='black', font=font)
        draw.line([(0, (i + 1) * input_spacing), (10, (i + 1) * input_spacing)], fill='black')
    
    # Draw input values
    if input_value1 is not None:
        draw.text((5, height // 2 - 10), f"{input_names[0]} = {str(input_value1)}", fill='black', font=font)
    if input_value2 is not None and input_value2 != input_value1:
        draw.text((5, height // 2 + 10), f"{input_names[1]} = {str(input_value2)}", fill='black', font=font)
    
    draw.text((width - 25, height // 2 - 10), output_name, fill='black', font=font)
    draw.line([(width - 10, height // 2), (width, height // 2)], fill='black')
    
    # Draw gate shape
    draw.rectangle([10, 10, width - 10, height - 10], outline='black')
    draw.text((width // 2 - 10, height // 2 - 10), gate_type, fill='black', font=font)
    
    return image


# Example usage
question, correct_answer, gate_images = generate_complicated_question_with_image()

print(question)

print("Correct answer:", correct_answer)

# Display gate images
plt.figure(figsize=(len(gate_images) * 5, 5))
for i, image in enumerate(gate_images):
    plt.subplot(1, len(gate_images), i + 1)
    plt.imshow(image)
    plt.axis('off')
plt.show()

