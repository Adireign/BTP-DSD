import random
import Distractors.distractors
import Utilities.binaryOperations


# Question type-1
def generate_question_conversion(level):
    options = []
    correct_answer = "error"
    initial_value = ''
    if level != 0:
        conversion_start = random.choice(["binary","hexadecimal","octal","decimal"])
        conversion_end = "binary"
        
        if conversion_start == "decimal":
            decimal = random.randint(0,255)
            initial_value = decimal
            conversion_end = random.choice(["hexadecimal","octal","binary"])
            if conversion_end == "binary":
                correct_answer = Utilities.binaryOperations.decimal_to_binary(decimal)
                options,correct_answer = Distractors.distractors.generate_binary_options(correct_answer)
                
            elif conversion_end == "octal":
                correct_answer = Utilities.binaryOperations.decimal_to_octal(decimal)
                options,correct_answer = Distractors.distractors.generate_octal_options(correct_answer)
            else:
                correct_answer = Utilities.binaryOperations.decimal_to_hexadecimal(decimal)
                options,correct_answer = Distractors.distractors.generate_hexadecimal_options(correct_answer)

            
        elif conversion_start == "hexadecimal":
            hexadecimal = format(random.randint(0, 255), 'x')
            initial_value = hexadecimal
            conversion_end = random.choice(["decimal", "octal", "binary"])
            if conversion_end == "binary":
                correct_answer = Utilities.binaryOperations.hexadecimal_to_binary(hexadecimal)
                options,correct_answer = Distractors.distractors.generate_binary_options(correct_answer)

            elif conversion_end == "decimal":
                correct_answer = Utilities.binaryOperations.hexadecimal_to_decimal(hexadecimal)
                options,correct_answer = Distractors.distractors.generate_decimal_options(correct_answer)

            else:
                correct_answer = Utilities.binaryOperations.hexadecimal_to_octal(hexadecimal)
                options,correct_answer = Distractors.distractors.generate_octal_options(correct_answer)


        elif conversion_start == "octal":
            octal = oct(random.randint(0, 255))[2:]
            initial_value = octal
            conversion_end = random.choice(["hexadecimal","decimal","binary"])
            if conversion_end == "binary":
                correct_answer = Utilities.binaryOperations.octal_to_binary(octal)
                options,correct_answer = Distractors.distractors.generate_binary_options(correct_answer)

            elif conversion_end == "decimal":
                correct_answer = Utilities.binaryOperations.octal_to_decimal(octal)
                options,correct_answer = Distractors.distractors.generate_decimal_options(correct_answer)

            else:
                correct_answer = Utilities.binaryOperations.octal_to_hexadecimal(octal)
                options,correct_answer = Distractors.distractors.generate_hexadecimal_options(correct_answer)
            


        elif conversion_start == "binary":
            binary = bin(random.randint(0, 255))[2:]
            initial_value = binary
            conversion_end = random.choice(["hexadecimal","decimal","octal"])
            if conversion_end == "octal":
                correct_answer = Utilities.binaryOperations.binary_to_octal(binary)
                options,correct_answer = Distractors.distractors.generate_octal_options(correct_answer)

            elif conversion_end == "decimal":
                correct_answer = Utilities.binaryOperations.binary_to_decimal(binary)
                options,correct_answer = Distractors.distractors.generate_decimal_options(correct_answer)

            else:
                correct_answer = Utilities.binaryOperations.binary_to_hexadecimal(binary)
                options,correct_answer = Distractors.distractors.generate_hexadecimal_options(correct_answer)
            
        question_text = question_text = f"What is the {conversion_end} representation of {initial_value} (in {conversion_start})? "
        return question_text,options,correct_answer   
            


if __name__ == "__main__":
    ans = generate_question_conversion(1)
    print(ans)
