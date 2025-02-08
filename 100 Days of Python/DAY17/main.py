from question_model import Question
from data import question_data

question_bank = []

# My solution
#for questions_num in range(len(question_data)):
#    questions = Question(question_data[questions_num]["text"], question_data[questions_num]["answer"])
#    question_bank.append(questions)

# Angelas solution 
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_questions = Question(question_text, question_answer)
    question_bank.append(new_questions)

print(question_bank)
print(len(question_bank))
print(question_bank[0].text)