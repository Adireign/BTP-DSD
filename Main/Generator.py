import random
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

import Theory.theory

# Here we generate question based on tags and then generate a PDF
def generate_pdf(num_questions, level,tags):
    filename = f"questions_{num_questions}_level_{level}.pdf"
    document_title = f"Generated Questions - Level {level}"
    # generate_question(level,tags)

    # Create PDF
    c = canvas.Canvas(filename, pagesize=letter)
    c.setTitle(document_title)

    # Add questions to the PDF
    depth = 700
    for _ in range(num_questions):
        question, options, answer = generate_question(level,tags)
        c.drawString(100, depth - _ * 50, f"Q{_ + 1}: {question}")
        depth-=20
        for option in options:
            c.drawString(100, depth - _ * 50, f" {option}")
            depth -= 20


#   Saving the file
    c.save()
    print(f"PDF '{filename}' generated successfully.")

def generate_question(level,tags):
    print(level,tags)
    random_list = []
    tag1 = "Number system"
    tag2 = "Boolean-algebra"
    tag3 = "Gates"
    tag4 = "Flip-flops"
    tag5 = "Theory"
    
    for tag in "tags":
        if tag == tag1:
            random_list.append(1)
        elif tag == tag2:
            random_list.append(2)
        elif tag == tag3:
            random_list.append(3)
        elif tag == tag4:
            random_list.append(4)
        else:
            random_list.append(5)

    flag = random.choice(random_list)
    print(flag)
    if flag == 1:
        print(1)
        # generate_question_numberSystem
    elif flag == 2:
        print(1)
        # generate_question_booleanAlgebra
    elif flag == 3:
        print(1)
        # generate_question_gates
    elif flag == 4:
        print(1)
        # generate_question_flipFlops
    elif flag == 5:
        print("hello")
        return Theory.theory.generate_question_theory(level)




