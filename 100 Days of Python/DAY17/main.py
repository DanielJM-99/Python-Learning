from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# My solution
#for questions_num in range(len(question_data)):
#    questions = Question(question_data[questions_num]["text"], question_data[questions_num]["answer"])
#    question_bank.append(questions)

# Angelas solution 
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_questions = Question(question_text, question_answer)
    question_bank.append(new_questions)

#print(question_bank)
#print(len(question_bank))
#print(question_bank[0].text)
#print(question_bank[1].answer)

quiz = QuizBrain(question_bank)

while quiz.still_have_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
