from question_model import Question
from data import question_data
from quiz_brain import Brain
question_bank = []


for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question=question_text, correct_answer=question_answer)
    questions = question_bank.append(new_question)


quiz = Brain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print(f"Your final score is {quiz.score}/{quiz.question_number}")










