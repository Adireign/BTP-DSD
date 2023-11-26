import random
# import binaryArithimetic
import binaryCodes
import conversions
import floatingNumbers

def generate_question_number_system(level):
    number_system_topic_list = [1,2]
    selected_topic = random.choice(number_system_topic_list)
    if selected_topic == 1:
        return conversions.generate_question_conversion(level)
    elif selected_topic == 2:
        return binaryCodes.generate_question_binary_codes(level)

    


if __name__ == "__main__":
    ans = generate_question_number_system(1)
    print(ans)
