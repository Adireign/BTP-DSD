import random
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

import Number_System.numerSystemFinal
import Boolean_Algebra.booleanAlgebraFinal
import FlipFlops.flipflops
import Theory.theory
import io
import os
pdf_folder = "./PDF"

# Here we generate question based on tags and then generate a PDF
def generate_pdf(num_questions, level, tags):
    filename = f"questions_{num_questions}_level_{level}.pdf"
    document_title = f"Generated Questions - Level {level}"

    # Create PDF
    pdf_path = os.path.join(pdf_folder, filename)
    pdf_buffer = io.BytesIO()
    c = canvas.Canvas(pdf_buffer)
    c.setTitle(document_title)

    # Set up initial depth
    depth = 700

    # Number of questions per page
    questions_per_page = 5

    # Convert num_questions to an integer
    num_questions = int(num_questions)
    right_padding = 50

    for question_num in range(num_questions):
        # Check if a new page is needed
        if question_num > 0 and question_num % questions_per_page == 0:
            c.showPage()  # Start a new page
            depth = 700  # Reset depth for the new page

        question, options, answer = generate_question(level, tags)
        question_x = 100
        option_x = 120
        question_1 = ""
        question_2 = ""
        if len(question) >= 70:
            question_1 = question[:70]
            question_2 = question[70:]
            c.drawString(question_x, depth, f"Q{question_num + 1}: {question_1}")
            depth -= 20
            c.drawString(question_x, depth, f"{question_2}")
        else:
            c.drawString(question_x, depth, f"Q{question_num + 1}: {question}")

        depth -= 20

        for option in options:
            c.drawString(option_x, depth, f" {option}")
            depth -= 20
            
        # depth -= 20
        c.drawString(option_x, depth, f"Correct answer: {answer}")
        depth -= 30

    # Saving the file
    c.save()
    with open(pdf_path, 'wb') as pdf_file:
            pdf_file.write(pdf_buffer.getvalue())
    print(f"PDF '{filename}' generated successfully.")


def generate_question(level,tags):
    print(level,tags)
    random_list = []
    tag1 = "Number-System"
    tag2 = "Boolean-algebra"
    tag3 = "Gates"
    tag4 = "Flip-flops"
    tag5 = "Theory"
    
    print("tags are")
    print(tags)
    for tag in tags:
        print(tag)
        if tag == tag1:
            random_list.append(1)
        elif tag == tag2:
            random_list.append(2)
        elif tag == tag3:
            random_list.append(3)
        elif tag == tag4:
            random_list.append(4)
        elif tag == tag5:
            random_list.append(5)

    flag = random.choice(random_list)
    
    print("It goes like..")
    # print(tags)
    print(random_list)
    if flag == 1:
        return Number_System.numerSystemFinal.generate_question_number_system(level)
    elif flag == 2:
        return Boolean_Algebra.booleanAlgebraFinal.generate_question_boolean_algebra(level)
    elif flag == 3:
        return FlipFlops.flipflops.generate_question_flipflops(level)
    elif flag == 4:
        return FlipFlops.flipflops.generate_question_flipflops(level)
    elif flag == 5:
        return Theory.theory.generate_question_theory(level)




