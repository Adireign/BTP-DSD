import random

def decimal_to_bcd(decimal_digit):
    binary_digit = bin(decimal_digit)[2:].zfill(4)
    return binary_digit

def decimal_to_excess_3_bcd(decimal_digit):
    excess_3_digit = (decimal_digit + 3) % 10  # Add 3 and take modulo 10
    binary_digit = bin(excess_3_digit)[2:].zfill(4)
    return binary_digit

def generate_random_bcd_no1():
    decimal_number = random.randint(0, 99)
    print(f"How do you represent decimal number {decimal_number} in 8421 BCD code")
    tens_digit = decimal_number // 10
    ones_digit = decimal_number % 10
    tens_bcd = decimal_to_bcd(tens_digit)
    ones_bcd = decimal_to_bcd(ones_digit)
    bcd_representation = tens_bcd + ones_bcd
    # print(f"BCD Representation: {bcd_representation}")
    return bcd_representation

def generate_random_bcd_no2():
    decimal_number = random.randint(0,99)
    print(f"How do you represent decimal number {decimal_number} in excess 3 BCD code")
    tens_digit = decimal_number // 10
    ones_digit = decimal_number % 10
    tens_excess_3_bcd = decimal_to_excess_3_bcd(tens_digit)
    ones_excess_3_bcd = decimal_to_excess_3_bcd(ones_digit)
    excess_3_bcd_representation = tens_excess_3_bcd + ones_excess_3_bcd
    # print(f"Excess-3 BCD Representation: {excess_3_bcd_representation}")
    return excess_3_bcd_representation


def main():
    number_of_questions = input("Enter the number of questions and level:")
    num = int(number_of_questions)
    
    for _ in range(num):
        
        question_type = random.choice(["1","2","3","4"])
        if question_type=="1":
            generate_random_bcd_no1()

        else:
            generate_random_bcd_no2()
       


if __name__ == "__main__":
    main()