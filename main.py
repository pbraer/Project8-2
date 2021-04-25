print("""
Project #8 Multiplication Tester
Разработчик:
Браер П.С.
""")

import random as r


# creating a dictionary


def create_dict(file):
    dict_questions = {}
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line[:line.find('\n')]
            line = line.split(' ')
            dict_questions[line[0]] = line[1]
    return dict_questions


# creating questions


def create_questions(dict_questions):
    question = []
    for key in dict_questions:
        question.append(key)
    return question


# recursive tester function


def main(dict_questions, question, num, step):
    if step > 3:
        return test(dict_questions, question)
    if num > 10:
        print()
        return print('END')
    print(num, '. ', sep='', end='')
    question_num = r.randint(0, 71)
    print(questions[question_num])
    answer = int(input())
    if answer != int(dict_question[questions[question_num]]):
        return main(dict_question, questions, num, step + 1)
    return main(dict_question, questions, num + 1, 1)


# tester function


def test(dict_questions, question):
    print('START')
    print()
    num = 1
    return main(dict_questions, question, 1, 1)


dict_question = create_dict('MultiplicationTable')
questions = create_questions(dict_question)
test(dict_question, questions)
