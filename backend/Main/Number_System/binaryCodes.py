import random
import Utilities.binaryOperations
import Distractors.distractors

# Question type-1
def generate_question_graycode_to_bcd(level):
    binary_number_length = 8
    binary_number = Utilities.binaryOperations.generate_binary_number(binary_number_length)
    question_text = f"Convert the given Gray code ({binary_number})GRAY into BCD format"
    correct_answer = Utilities.binaryOperations.gray_to_bcd(binary_number)
    options,correct_answer = Distractors.distractors.generate_binary_options(correct_answer)

    return question_text,options,correct_answer

# Question type-2
def generate_question_decimal_to_excess3_bcd(level):
    decimal_number = random.randint(10,99)
    question_text = f"How do you represent decimal number {decimal_number} in excess 3 BCD code"
    tens_digit = decimal_number // 10
    ones_digit = decimal_number % 10
    tens_excess_3_bcd = Utilities.binaryOperations.decimal_to_excess_3_bcd(tens_digit)
    ones_excess_3_bcd = Utilities.binaryOperations.decimal_to_excess_3_bcd(ones_digit)
    correct_answer = tens_excess_3_bcd + ones_excess_3_bcd
    options,correct_answer = Distractors.distractors.generate_binary_options(correct_answer)
    return question_text,options,correct_answer
    
# Question type-3
def generate_question_decimal_to_8421_bcd(level):
    decimal_number = random.randint(10,99)
    question_text = f"How do you represent decimal number {decimal_number} in 8421 BCD code"
    tens_digit = decimal_number // 10
    ones_digit = decimal_number % 10
    tens_bcd = Utilities.binaryOperations.decimal_to_bcd(tens_digit)
    ones_bcd = Utilities.binaryOperations.decimal_to_bcd(ones_digit)
    correct_answer = tens_bcd + ones_bcd
    options,correct_answer = Distractors.distractors.generate_binary_options(correct_answer)
    return question_text,options,correct_answer


def generate_question_binary_codes(level):
    binary_codes_topic_list = [1,2,3]
    selected_topic = random.choice(binary_codes_topic_list)
    if selected_topic == 1:
        return generate_question_graycode_to_bcd(level)
    elif selected_topic == 2:
        return generate_question_decimal_to_excess3_bcd(level)
    elif selected_topic == 3:
        return generate_question_decimal_to_8421_bcd(level)
    

if __name__ == "__main__":
    ans = generate_question_binary_codes(1)
    print(ans)