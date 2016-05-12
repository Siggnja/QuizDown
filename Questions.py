import json
import requests
from bs4 import BeautifulSoup
from pprint import pprint as pp
import random
from difflib import SequenceMatcher



'''
ans = 'y'

print("Welcome to this question game")
print("A question will appear, type the correct answer .. or be stuck in an infinite game!")




while ans == 'y':
    generate = requests.get("http://jservice.io/api/random")
    question = json.loads(generate.text)[0]
    answer = False
    hint = 3
    
    while answer == False:
    
        print(question['question'])

        t = input()

        if t.upper() == question['answer'].upper():
            answer = True
            print("That is correct!!!!")
            print("Press 'y' if you want to play again!")
            ans = input()
        else:
            print("That is incorrect, please guess again!")
            print("Hint: ", question['answer'][0:hint])
            hint += 3

'''



def setup_game(lis):

##    FÆ:
##        Magn spurning    -    amount
##        Category         -    cate
##        Erfiðleikastig   -    difficulty
    amount = int(l[2])
    cate = category(lis[1])
    difficulty = 200
    cate_id = category(cate)


    questions = generate_questions(amount, cate_id, difficulty)

    
    
    








def check_answer(correct, answer):
    s = SequenceMatcher(None, correct.upper(), answer.upper())

    if s.ratio() >= 0.8:
        return True
    else:
        return False



def category(cate):

    d = {'Sports' : 42, 'Animals' : 21, 'History' : 114, 'Brand Names' : 2537,
         'Pop Music' : 770}

    return d[cate]




def generate_questions(amount, cate, diff):
    
    d = []

    correct_diff = []
    
    doc = requests.get("http://jservice.io/api/category?id="+str(cate))
    questions = json.loads(doc.text)['clues']

    for i, v in enumerate(questions):
        if v['value'] != None and v['value'] <= diff:
            correct_diff.append(questions[i])
    
    numbers = random.sample(range(1, len(correct_diff)), amount)

    for i, val in enumerate(numbers):
        d.append((correct_diff[val]['question'],correct_diff[val]['answer']))
    
    return d
    
    










