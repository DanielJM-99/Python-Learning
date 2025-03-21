# Creaete a class for the brain
class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        # Creates an object/attribute that will have a list
        self.question_list = q_list

    def still_have_questions(self):
        return self.question_number < len(self.question_list)
        #if self.question_number == len(self.question_list):
        #    return False
        #else:
        #    return True

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True or False)?: ")
        self.check_anwer(user_answer, current_question.answer)

    def check_anwer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("")
        