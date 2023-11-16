

# function which generates the question
import Generator

class question_tags:
    def __init__(self, text, tags):
        self.text = text
        self.tags = tags

tags = [
    question_tags("tag-1", ["Number-System"]),
    question_tags("tag-2", ["Boolean-algebra"]),
    question_tags("tag-3", ["Gates"]),
    question_tags("tag-4", ["Flip-flops"]),
    question_tags("tag-5",["Theory"])
    # Add more questions with different tags
]

if __name__ == "__main__":
    # print("Please select the topics you want to include from the available tags-")
    available_tags = set(tag for question in tags for tag in question.tags)

    print("Available tags:", available_tags)
    selected_tags = input("Select tags (comma-separated): ").split(',')    

    num_questions = int(input("Enter the number of questions: "))
    level = int(input("Enter the level: "))
    # question_tags = int(input())

    # generate_pdf(num_questions, level)
    Generator.generate_pdf(num_questions,level,selected_tags)
