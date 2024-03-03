from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

def main():

    question_bank = []

    for que in question_data:
        question_bank.append(Question(que["text"], que["answer"]))

    quiz = QuizBrain(question_bank)

    while quiz.ans != "exit" and quiz.que_avialibility():
        quiz.next_que()
        quiz.check_ans()

    print("Great !! You have completed the Quiz . . ")


if __name__ == "__main__":
    main()
