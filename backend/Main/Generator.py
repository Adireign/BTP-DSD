import random
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

import Number_System.numerSystemFinal
import Theory.theory

# Here we generate question based on tags and then generate a PDF
def generate_pdf(num_questions, level, tags):
    filename = f"questions_{num_questions}_level_{level}.pdf"
    document_title = f"Generated Questions - Level {level}"

    # Create PDF
    c = canvas.Canvas(filename, pagesize=letter)
    c.setTitle(document_title)

    # Set up initial depth
    depth = 700

    # Number of questions per page
    questions_per_page = 5

    # Convert num_questions to an integer
    num_questions = int(num_questions)

    for question_num in range(num_questions):
        # Check if a new page is needed
        if question_num > 0 and question_num % questions_per_page == 0:
            c.showPage()  # Start a new page
            depth = 700  # Reset depth for the new page

        question, options, answer = generate_question(level, tags)
        c.drawString(100, depth, f"Q{question_num + 1}: {question}")
        depth -= 20

        for option in options:
            c.drawString(100, depth, f" {option}")
            depth -= 20
            
        depth -= 20

    # Saving the file
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
        return Number_System.numerSystemFinal.generate_question_number_system(level)
    elif flag == 2:
        return Number_System.numerSystemFinal.generate_question_number_system(level)
    elif flag == 3:
        return Number_System.numerSystemFinal.generate_question_number_system(level)
    elif flag == 4:
        return Number_System.numerSystemFinal.generate_question_number_system(level)
    elif flag == 5:
        return Number_System.numerSystemFinal.generate_question_number_system(level)




