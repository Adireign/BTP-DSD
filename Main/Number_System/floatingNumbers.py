import random
import math

def generate_question_floating_no1():
    min_decimal = 10**(-86)
    max_decimal = 10**(86)

    # Find the minimum and maximum binary exponent
    min_exponent = int(math.floor(math.log2(min_decimal)))
    max_exponent = int(math.ceil(math.log2(max_decimal)))

    # Calculate the number of bits required for the exponent
    min_exponent_bits = len(bin(min_exponent)) - 2  # Subtract 2 to remove '0b' prefix
    max_exponent_bits = len(bin(max_exponent)) - 2

    print(f"Minimum Exponent: {min_exponent}")
    print(f"Maximum Exponent: {max_exponent}")
    print(f"Number of Bits Required for Exponent (Min): {min_exponent_bits}")
    print(f"Number of Bits Required for Exponent (Max): {max_exponent_bits}")


# def generate_question_floating_no2():
    


def main():
    number_of_questions = input("Enter the number of questions and level:")
    num = int(number_of_questions)
    
    for _ in range(num):
        
        question_type = random.choice(["1","2","3","4"])
        if question_type=="1":
            generate_question_floating_no1()

        else:
            generate_question_floating_no1()
       



if __name__ == "__main__":
    main()