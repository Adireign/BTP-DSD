import random

def decimal_to_binary(decimal):
    return bin(decimal)[2:]

def decimal_to_octal(decimal):
    return oct(decimal)[2:]

def decimal_to_hexadecimal(decimal):
    return hex(decimal)[2:]

def octal_to_decimal(octal):
    return int(octal, 8)

def octal_to_binary(octal):
    decimal = octal_to_decimal(octal)
    return bin(decimal)[2:]

def octal_to_hexadecimal(octal):
    decimal = octal_to_decimal(octal)
    return hex(decimal)[2:]

def binary_to_decimal(binary):
    return int(binary, 2)

def binary_to_octal(binary):
    decimal = binary_to_decimal(binary)
    return oct(decimal)[2:]

def binary_to_hexadecimal(binary):
    decimal = binary_to_decimal(binary)
    return hex(decimal)[2:]

def hexadecimal_to_decimal(hexadecimal):
    return int(hexadecimal, 16)

def hexadecimal_to_octal(hexadecimal):
    decimal = hexadecimal_to_decimal(hexadecimal)
    return oct(decimal)[2:]

def hexadecimal_to_binary(hexadecimal):
    decimal = hexadecimal_to_decimal(hexadecimal)
    return bin(decimal)[2:]

# takes level as input
def generate_question_conversion(level):

    if level == 1:
        conversion_start = random.choice(["binary","hexadecimal","octal","decimal"])
        conversion_end = "binary"
        correct_answer = 0
        
        if conversion_start == "decimal":
            decimal = random.randint(0,255)
            conversion_end = random.choice(["hexadecimal","octal","binary"])
            if conversion_end == "binary":
                correct_answer = decimal_to_binary(decimal)
            elif conversion_end == "octal":
                correct_answer = decimal_to_octal(decimal)
            else:
                correct_answer = decimal_to_hexadecimal(decimal)
            
            return conversion_start, decimal, conversion_end, correct_answer

            
        elif conversion_start == "hexadecimal":
            hexadecimal = format(random.randint(0, 255), 'x')
            conversion_end = random.choice(["decimal", "octal", "binary"])
            if conversion_end == "binary":
                correct_answer = hexadecimal_to_binary(hexadecimal)
            elif conversion_end == "decimal":
                correct_answer = hexadecimal_to_decimal(hexadecimal)
            else:
                correct_answer = hexadecimal_to_octal(hexadecimal)
            
            return conversion_start, hexadecimal, conversion_end, correct_answer


        elif conversion_start == "octal":
            octal = oct(random.randint(0, 255))[2:]
            conversion_end = random.choice(["hexadecimal","decimal","binary"])
            if conversion_end == "binary":
                correct_answer = octal_to_binary(octal)
            elif conversion_end == "decimal":
                correct_answer = octal_to_decimal(octal)
            else:
                correct_answer = octal_to_hexadecimal(octal)
            
            return conversion_start, octal, conversion_end, correct_answer


        elif conversion_start == "binary":
            binary = bin(random.randint(0, 255))[2:]
            conversion_end = random.choice(["hexadecimal","decimal","octal"])
            if conversion_end == "octal":
                correct_answer = binary_to_octal(binary)
            elif conversion_end == "decimal":
                correct_answer = binary_to_decimal(binary)
            else:
                correct_answer = binary_to_hexadecimal(binary)
            
            return conversion_start, binary, conversion_end, correct_answer
            

        
def main():
    number_of_questions = input("Enter the number of questions and level:")
    num = int(number_of_questions)
    
    for _ in range(num):
        conversion_start, start_value, conversion_end, correct_answer = generate_question_conversion(1)
        user_answer = input(f"What is the {conversion_end} representation of {start_value} (in {conversion_start})? ").strip()
        UA = str(user_answer)
        CA = str(correct_answer)

        if UA == CA:
            print("Correct!\n")
        else:
            print(f"Wrong. The correct answer is {correct_answer}.\n")



if __name__ == "__main__":
    main()
