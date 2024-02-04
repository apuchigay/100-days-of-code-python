from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import html

question_bank = [Question(html.unescape(question["question"]), question["correct_answer"]) for question in question_data]

quiz = QuizBrain(question_bank)

while quiz.still_have_questions():
    quiz.next_question()

print("Quiz completed 🥳🍾")
print(f"Your final score was {quiz.score} correct answers")
# Nota: Repetir la clase 160 y entenderla
