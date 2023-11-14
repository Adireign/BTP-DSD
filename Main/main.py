from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import Facts

def generate_question(level):
    # Your logic to generate a question based on the level
    # Return the generated question
    ques = ["Q1","Q2","Q3"];
    return ques

def generate_pdf(num_questions, level):
    filename = f"questions_{num_questions}_level_{level}.pdf"
    document_title = f"Generated Questions - Level {level}"

    # Create PDF
    c = canvas.Canvas(filename, pagesize=letter)
    c.setTitle(document_title)

    # Add questions to the PDF
    depth = 700
    for _ in range(num_questions):
        question, options, answer = Facts.generate_question_facts(level)
        c.drawString(100, depth - _ * 50, f"Q{_ + 1}: {question}")
        depth-=20
        for option in options:
            c.drawString(100, depth - _ * 50, f" {option}")
            depth -= 20


    # Save the PDF
    c.save()
    print(f"PDF '{filename}' generated successfully.")

if __name__ == "__main__":
    num_questions = int(input("Enter the number of questions: "))
    level = int(input("Enter the level: "))

    generate_pdf(num_questions, level)