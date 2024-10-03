from tensorflow.python.distribute.device_util import current


class QuizBrain:

    def __init__(self,list_of_question):
        self.question_list=list_of_question
        self.score = 0
        self.question_no=0

    def still_has_question(self):
        return self.question_no < len(self.question_list)
        #                       OR
        # if self.question_no < len(self.question_list):
        #     return True
        # else:
        #     return False

    def next_question(self):
        current_question=self.question_list[self.question_no]
        self.question_no+=1
        user_answer = input(f"Q.{self.question_no} : {current_question.text} (True/False) : ")
        self.check_answer(user_answer,current_question.answer)
    def check_answer(self, user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score+=1
            print("you go it right")
        else:
            print("that is wrong")
        print(f"The correct answer was {correct_answer}")
        print(f"your current score is {self.score}/{self.question_no}")
        print(" "*2)