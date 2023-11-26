import random
import math
import struct
import Utilities.binaryOperations
import Distractors.distractors

def binary_to_decimal(binary):
    return int(binary, 2)

def binary_to_hexadecimal(binary):
    decimal = binary_to_decimal(binary)
    return hex(decimal)[2:]

# returns mantissa
def generate_question_floating():
    decimal_number = random.uniform(0, 10)
    decimal_number = 64.5
    float_representation = struct.unpack('f', struct.pack('f', decimal_number))[0]
    binary_representation = format(struct.unpack('!I', struct.pack('!f', float_representation))[0], '032b')

    # Extract the sign bit, exponent, and mantissa
    sign_bit = binary_representation[0]
    exponent = binary_representation[1:9]
    mantissa = binary_representation[9:]
    print(f"Random Decimal Number: {decimal_number}")
    # print(f"Single-Precision Representation: {binary_representation}")
    mantissa = binary_to_hexadecimal(mantissa)
    print(f"Mantissa: 0x{mantissa}")
    return mantissa


# def generate_question_floating_no2():


def main():
    number_of_questions = input("Enter the number of questions and level:")
    num = int(number_of_questions)
    
    for _ in range(num):
        
        question_type = random.choice([1])
        if question_type==1:
            generate_question_floating()

        else:
            generate_question_floating()
       



if __name__ == "__main__":
    main()