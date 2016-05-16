import json
import requests
import random
from difflib import SequenceMatcher
import re

def check_answer(correct, answer): #Checks the ratio of the the answer compared to the correct answer
    s = SequenceMatcher(None, correct.upper(), answer.upper())

    if s.ratio() >= 0.8:
        return True
    else:
        return False



def category(cate): #Return the number of the category corresponding to the database at jservice

    d = {'Sports' : 42, 'Animals' : 21, 'History' : 114, 'Brand Names' : 2537,
         'Pop Music' : 770, 'Stupid Answers' : 136, 'People' : 442}

    return d[cate]

def getDifficulty(dif): #Return the difficulty number corresponding to the difficulty level at jservice
     d = {'Easy' : 300, 'Medium' : 600, 'Hard' : 900}
     return d[dif]

def generate_questions(amount, cate, diff): #Generates question from jservice database that fit the given criteria
    
    d = []
    correct_diff = []
    doc = requests.get("http://jservice.io/api/category?id="+str(cate))
    questions = json.loads(doc.text)['clues']

    for i, v in enumerate(questions):
        if v['value'] != None and v['value'] <= diff:
            correct_diff.append(questions[i])
    numbers = random.sample(range(1, len(correct_diff)), amount)


    for i in range(len(numbers)):
        ans = correct_diff[numbers[i]]['answer'] 
        if re.search("<", ans):
            ans = ans[3:-4]

        if ans.find("(") != -1:
            ans = ans[0:ans.find("(")]
        
        d.append((correct_diff[numbers[i]]['question'], ans))
    
    return d
    
    










