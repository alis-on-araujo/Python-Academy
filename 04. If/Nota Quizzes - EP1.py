from math import inf

def nota_quizzes(q1, q2, q3, q4, q5):

    menor = inf

    if q1 < menor:
        menor = q1

    if q2 < menor:
        menor = q2

    if q3 < menor:
        menor = q3

    if q4 < menor:
        menor = q4

    if q5 < menor:
        menor = q5
    
    res = (q1 + q2 + q3 + q4 + q5 - menor) / 4

    if q1 < 0 or q1 > 10:
            res = 0
    if q2 < 0 or q2 > 10:
            res = 0
    if q3 < 0 or q3 > 10:
            res = 0
    if q4 < 0 or q4 > 10:
            res = 0
    if q5 < 0 or q5 > 10:
            res = 0
    return res
