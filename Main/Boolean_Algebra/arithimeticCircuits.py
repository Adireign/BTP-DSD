import random


# returns an option as answer
def generate_question_arithimetic_circuits(level):
    # Define possible values for A and B bits
    A_values = ['0', '1']
    B_values = ['0', '1']

    # Randomly generate values for A and B
    A = ''.join(random.choice(A_values) for _ in range(4))
    B = ''.join(random.choice(B_values) for _ in range(4))

    # Perform addition to calculate C_G and C_P
    C_G = str(int(A[3]) & int(B[3]))
    C_P = str(int(A[3]) | int(B[3]))

    # Determine the correct answer
    correct_answer = f"a). C_G = Logic {C_G} ; C_P = Logic {C_P}"

    # Define the options
    options = [
        correct_answer,
        "b). C_G = Logic 0 ; C_P = Logic 0",
        "c). C_G = Logic 0 ; C_P = Logic 1",
        "d). C_G = Logic 1 ; C_P = Logic 0"
    ]

    # Randomly shuffle the options, excluding the correct answer
    options.remove(correct_answer)
    random.shuffle(options)
    options.insert(0, correct_answer)
    print(f"Which of the following represents logic values of Carry generation (C_G) and carry propagation (C_P) after the addition of A1 and B1 bits in an adder circuit if A3A2A1A0 = {A} and B3B2B1B0 = {B} are inputs to the adder?")
    for option in options:
        print(option)
    ans = "Solution: The correct answer is option a."
    return ans

def main():
    # Print the solution
    ans = generate_question_arithimetic_circuits(2)
    print(ans)
    


if __name__ == "__main__":
    main()