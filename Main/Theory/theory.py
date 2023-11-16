import random

questions = [
    {
        "question": " RTL is primarily concerned with defining the flow of signals between",
        "options": ["A. Registers", "B. Clock", "C. Inverters", "D. None of the above"],
        "correct_answer": "A. Registers",
    },
    {
        "question": " RTL Design only contains combinational circuits and does not include any sequential component",
        "options": ["A. True", "B. False"],
        "correct_answer": "B. False",
    },
    {
        "question": " Maximum clock frequency is independent of critical path",
        "options": ["A. True", "B. False"],
        "correct_answer": "B. False",
    },
    {
        "question": "32-bit IEEE 754 floating point representation adds a bias of",
        "options": ["A. 127 to mantissa", "B. 127 to exponent", "C. 128 to mantissa", "D. 128 to exponent"],
        "correct_answer": "B. 127 to exponent",
    },
    {
        "question": "The smallest and largest number that can be represented by IEEE single precision format is",
        "options": ["A. 10^-126 and 10^127", "B. 10^-127 and 10^127", "C. 2^-126 and 2^127", "D. 2^-127 and 2^127"],
        "correct_answer": "C. 2^-126 and 2^127",
    },
    
]
# returns a question statement and answer option
def generate_question_theory(level):

    # if level == 1:
    #     filtered_question = list(filter(lambda questions: questions[level] == 1, questions))
    #     selected_question = random.choice(questions)
    # else:
    #     selected_question = random.choice(questions)
    #     filtered_question = list(filter(lambda questions: questions.level == "2", questions))
    selected_question = random.choice(questions)

    question_text = selected_question["question"]
    options = selected_question["options"]
    correct_answer = selected_question["correct_answer"]
    return question_text, options, correct_answer