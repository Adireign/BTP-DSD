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