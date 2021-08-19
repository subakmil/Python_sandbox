# class User:
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.id = username
#         self.followers = 0
#         self.following = 0

#     def follow(self, user):
#         user.followers += 1
#         self.following += 1


# user_1 = User("009", "Milous")
# user_2 = User("005", "Lenous")

# user_1.follow(user_2)
# print(user_1.followers)
# print(user_1.following)
# print(user_2.followers)
# print(user_2.following)

import sys
sys.path.append(
    "C:/Users/Milos Subak/OneDrive/VS Code projects/_Python_sandbox/day16_OOP_Coffe_Machine")
from d17_question_model import Question
from d17_data import question_data
from d17_quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_bank.append(
        Question(question["question"], question["correct_answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

quiz.completed_quiz()
