import tkinter as tk
import random

def generate_gate_diagram():
    canvas.delete("all")
    
    gate_types = ['AND', 'OR', 'NOT']
    gate_type = random.choice(gate_types)
    
    if gate_type == 'AND':
        canvas.create_text(50, 50, text="A")
        canvas.create_text(50, 100, text="B")
        canvas.create_text(150, 75, text="AND")
        canvas.create_line(75, 50, 75, 100, arrow=tk.LAST)
        canvas.create_line(75, 75, 125, 75, arrow=tk.LAST)
    elif gate_type == 'OR':
        canvas.create_text(50, 50, text="A")
        canvas.create_text(50, 100, text="B")
        canvas.create_text(150, 75, text="OR")
        canvas.create_line(75, 50, 75, 100, arrow=tk.LAST)
        canvas.create_oval(100, 75, 115, 90)
    elif gate_type == 'NOT':
        canvas.create_text(50, 75, text="A")
        canvas.create_text(150, 75, text="NOT")
        canvas.create_line(75, 75, 125, 75, arrow=tk.LAST)
        canvas.create_oval(125, 60, 140, 90)

root = tk.Tk()
root.title("Random Gate Diagram Generator")

canvas = tk.Canvas(root, width=200, height=150)
canvas.pack()

generate_button = tk.Button(root, text="Generate Diagram", command=generate_gate_diagram)
generate_button.pack()

root.mainloop()
