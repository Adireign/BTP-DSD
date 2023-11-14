import random

# returns question and correct answer
def generate_question_expressions():
    identities = [
        ("(x ⊕ y) ⊕ z = x ⊕ (y ⊕ z)", "Valid"),
        ("(x + y) ⊕ z = x ⊕ (y + z)", "Invalid"),
        ("x ⊕ y = x + y, if xy = 0", "Valid"),
        ("x ⊕ y = (xy + x′y′)′", "Valid"),
    ]

    question, correct_answer = random.choice(identities)
    return question, correct_answer

def main():
    num_questions = 5

    print("Random Logic Identity Questions:")
    for i in range(1, num_questions + 1):
        question, correct_answer = generate_question_expressions()
        print(f"Question {i}: Is the following identity valid or invalid?")
        print(f"Identity: {question}")
        user_answer = input("Your answer (Valid/Invalid): ").strip()

        if user_answer.lower() == correct_answer.lower():
            print("Correct!\n")
        else:
            print(f"Wrong. The correct answer is {correct_answer}.\n")

if __name__ == "__main__":
    main()
