import random

class Question:
    def __init__(self, text, tags):
        self.text = text
        self.tags = tags

# Example questions with tags
questions = [
    Question("What is the capital of France?", ["Number System"]),
    Question("Who wrote Romeo and Juliet?", ["literature"]),
    Question("What is the powerhouse of the cell?", ["biology"]),
    Question("What is the largest planet in our solar system?", ["astronomy"]),
    # Add more questions with different tags
]

# Get available tags from all questions
available_tags = set(tag for question in questions for tag in question.tags)

# Ask the user to select tags
print("Available tags:", available_tags)
selected_tags = input("Select tags (comma-separated): ").split(',')

# Filter questions based on selected tags
filtered_questions = [question for question in questions if any(tag in selected_tags for tag in question.tags)]

# Check if there are questions based on selected tags
if filtered_questions:
    # Select a random question from the filtered list
    random_question = random.choice(filtered_questions)

    # Print the selected question
    print("\nGenerated Question:")
    print(random_question.text)
    print("Tags:", random_question.tags)
else:
    print("No questions available for the selected tags.")
