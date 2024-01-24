import Generator

def generateAssessment(tags,numQuestions,level):
    print("hello")
    numQuestions = int(numQuestions)
    questionDetails = []
    for question_num in range(numQuestions):
        question, options, answer = Generator.generate_question(level,tags)
        newQuestionDetail = {"question": question,"options": options,"answer": answer}
        questionDetails.append(newQuestionDetail)
    return questionDetails