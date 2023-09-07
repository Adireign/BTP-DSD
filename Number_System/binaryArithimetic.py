import random


def generate_random_decimal(bit_length):
    # Generate a random decimal number within the specified bit length
    min_value = -2 ** (bit_length - 1)
    max_value = 2 ** (bit_length - 1) - 1
    return random.randint(min_value, max_value)


def decimal_to_twos_complement(number, bit_length):
    if number >= 0:
        # If the number is positive, convert it to binary and pad with zeros to the desired bit length
        binary_repr = bin(number)[2:].zfill(bit_length)
    else:
        # If the number is negative, calculate its 2's complement
        positive_number = abs(number)
        binary_repr = bin(2 ** bit_length - positive_number)[2:]

    return binary_repr

def main():
    # Input the bit length for the random number
    bit_length = int(input("Enter the bit length for the random number: "))
    
    # Generate a random decimal number within the specified bit length
    random_decimal = generate_random_decimal(bit_length)
    print(f"Generated random decimal number: {random_decimal}")

    # Convert the random decimal number to its 2's complement
    twos_complement = decimal_to_twos_complement(random_decimal, bit_length)

    # Ask the user to enter their guess for the 2's complement
    user_input = input(f"Enter the 2's complement for {random_decimal} (in binary form): ")

    # Check if the user's input is correct
    if user_input == twos_complement:
        print("Correct! The 2's complement is as expected.")
    else:
        print("Incorrect! The 2's complement is not as expected.")


if __name__ == "__main__":
    main()