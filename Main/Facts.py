import random

questions = [
    {
        "question": " RTL is primarily concerned with defining the flow of signals between",
        "options": ["A. Registers", "B. Clock", "C. Inverters", "D. None of the above"],
        "correct_answer": "A. Registers"
    },
    {
        "question": " RTL Design only contains combinational circuits and does not include any sequential component",
        "options": ["A. True", "B. False"],
        "correct_answer": "B. False"
    },
    {
        "question": " Maximum clock frequency is independent of critical path",
        "options": ["A. True", "B. False"],
        "correct_answer": "B. False"
    },
    {
        "question": "32-bit IEEE 754 floating point representation adds a bias of",
        "options": ["A. 127 to mantissa", "B. 127 to exponent", "C. 128 to mantissa", "D. 128 to exponent"],
        "correct_answer": "B. 127 to exponent"
    },
    
]
# returns a question statement and answer option
def generate_question_facts(level):
    selected_question = random.choice(questions)

    question_text = selected_question["question"]
    options = selected_question["options"]
    correct_answer = selected_question["correct_answer"]
    return question_text, options, correct_answer