from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import random
from logo import logo

print(logo)
question_bank = []

random.shuffle(question_data)
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("\n\n-----------------------------QUIZ COMPLETED-----------------------------")
print(f"Final Score : {quiz.score}/10")
