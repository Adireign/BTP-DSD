

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
def main(selected_tags,num_questions,level):
    print(selected_tags)
    print(num_questions)
    print(level)
    Generator.generate_pdf(num_questions,level,selected_tags)
    

if __name__ == "__main__":
    print("here")
