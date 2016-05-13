import QuizDown
import Questions
import json
import requests
from bs4 import BeautifulSoup
from pprint import pprint as pp
import random
from difflib import SequenceMatcher
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal
import sqlite3
import os,subprocess

dif = ['Easy', 'Medium', 'Hard'] #List of available difficulty levels
questions = ['5', '10', '15', '20'] #List of available numer of questions
categories = ['Animals', 'Brand Names', 'History', 'Pop Music', 'Sports'] #List of available categories

class Quiz:
    def __init__(self):
        self.count = 0
        self.PL1 = 0 #Player 1 score
        self.PL2 = 0 #Player 2 score
        self.ROUND = 1 #Players turn: 1 or 2
        self.HINT = 3 #Hints for questions
        self.QuestionScore = 10 #Highest score available for each
        self.pl1_name = ""
        self.pl2_name = ""
        self.questionCount = 1

    def getHint(self,dic, u): #Gets hint when hint button is displayed
        self.QuestionScore -= 2
        u.ans_lineEdit.setText(dic[self.count][1][0:self.HINT])
        self.HINT += 3


    def clearQuestion(self,dic, u): #Clears a question when answer is correct, or when skip button is clicked
        u.cont_button.setEnabled(False)
        self.count += 1
        if len(dic) > self.count:
            u.tab_quest_label.setText(dic[self.count][0])
            u.ans_lineEdit.setText("")
            self.questionCount+=1
            u.Question_tracker.setText(str(self.questionCount)+" of " + str(len(dic)))
            self.HINT = 0
            self.QuestionScore = 10
        elif len(dic) <= self.count and self.ROUND == 2:
            ui.result_name_p1.setText(self.pl1_name)
            ui.result_name_p2.setText(self.pl2_name)
            ui.result_score_p1.setText(str(int((self.PL1)/(len(dic)*10)*100)) + "%")
            ui.result_score_p2.setText(str(int((self.PL2) / (len(dic) * 10) * 100)) + "%")
            u.stackedWidget.setCurrentIndex(2)
            res = [(self.pl1_name,(self.PL1)/(len(dic)*10)),(self.pl2_name,(self.PL2)/(len(dic)*10))]
            conn = sqlite3.connect("UserData.sqlite")
            c = conn.cursor()
            c.executemany("INSERT INTO UserData ('name','highscore') VALUES(?,?)",res)
            ro =0
            for row in c.execute('SELECT * FROM UserData ORDER BY highscore DESC'):
                print("Zup")
                u.tableWidget.setItem(ro,1,QtWidgets.QTableWidgetItem(row[1]))
                u.tableWidget.setItem(ro, 0, QtWidgets.QTableWidgetItem(str(int((row[2])*100)) + "%"))
                print(row[2],row[1])
                ro+=1
            if self.PL1>=self.PL2:
                u.result_winner_p1.setPixmap(QtGui.QPixmap(":/new/prefix1/Graphics/Winner.png"))
            else:
                u.result_winner_p2.setPixmap(QtGui.QPixmap(":/new/prefix1/Graphics/Winner.png"))
            conn.commit()
            conn.close()
        else:
            self.ROUND = 2
            self.count = 0
            self.hint = 3
            self.questionCount = 1
            u.Question_tracker.setText(str(self.questionCount) + " of " + str(len(dic)))
            u.tab_quest_label.setText(dic[self.count][0])
            u.ans_lineEdit.setText("")
            u.Player_1.setPixmap(QtGui.QPixmap(":/new/prefix1/Graphics/Player 2.png"))


    def getLineAns(self,u, dic): #Collect then asnwer when Check Answer is clicked and checks it's value
        u.pushButton.setEnabled(False)
        ans = u.ans_lineEdit.text()
        print(self.PL1,self.PL2)
        if Questions.check_answer(dic[self.count][1],ans):
            u.cont_button.setEnabled(True)
            if self.ROUND == 1:
                self.PL1 += self.QuestionScore
            else:
                self.PL2 += self.QuestionScore
        else:
            u.ans_lineEdit.setText("")
    def restartMe(self):
        os.popen(os.path.abspath(__file__))
        sys.exit(0)
    def returnCombo(self,u): #Main function - signals for button clickes, creates Info in comboboxes etc...
         self.pl1_name = ui.p1_name.text()
         self.pl2_name = ui.p2_name.text()
         print(self.pl1_name,self.pl2_name)
         u.stackedWidget.setCurrentIndex(1)
         u.cont_button.setEnabled(False)
         selected = self.createCombo(u)
         dic = Questions.generate_questions(int(selected[2]), Questions.category(selected[1]), Questions.getDifficulty(selected[0]))
         u.Question_tracker.setText(str(self.questionCount) + " of " + str(len(dic)))
         u.tab_quest_label.setText(dic[0][0])
         u.skip_button.pressed.connect(lambda: self.clearQuestion(dic, u))
         u.check_answer_button.clicked.connect(lambda: self.getLineAns(u, dic))
         u.cont_button.clicked.connect(lambda: self.clearQuestion(dic, u))
         u.hint_button.clicked.connect(lambda: self.getHint(dic, u))
         u.finish_button.clicked.connect(lambda: self.restartMe())
    def createCombo(self,u):
        res = []
        res.append(u.diff_combo.currentText())
        res.append(u.cata_combo.currentText())
        res.append(u.ques_combo.currentText())
        return res
def insertCombo(ui):
    for i in dif:
        ui.diff_combo.insertItem(4, i)
    for i in questions:
        ui.ques_combo.insertItem(4, i)
    for i in categories:
        ui.cata_combo.insertItem(4, i)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = QuizDown.Ui_Form()
    ui.setupUi(Form)
    insertCombo(ui)
    Form.show()
    quiz = Quiz()
    ui.pushButton.clicked.connect(lambda: quiz.returnCombo(ui))
    sys.exit(app.exec_())

