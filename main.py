from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
import random

question_bank = []


for question in question_data:
    question_text=question["text"]
    question_ans=question["answer"]
    new_question = Question(question_text,question_ans)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("you have completed the quiz")
print(f"your final score :{quiz.score}/{quiz.question_no} ")