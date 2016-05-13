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
dif = ['Easy','Medium','Hard']
questions = ['5','10','15','20']
categories = ['Animals','Brand Names','History','Pop Music','Sports']
def getLineAns(ui,d,counter):
    ans = ui.ans_lineEdit.text()
    if Questions.check_answer(d[counter][1],ans):
        print("correct")
    else:
        ui.ans_lineEdit.setText("")
def clearQuestion(ui,dic,counter):
    counter +=1
    ui.tab_quest_label.setText(dic[counter][0])
def returnCombo(ui):
    res = []
    res.append(ui.diff_combo.currentText())
    res.append(ui.cata_combo.currentText())
    res.append(ui.ques_combo.currentText())
    ui.tabWidget.removeTab(0)
    ui.quest_tab.setEnabled(True)
    ui.cont_button.setEnabled(False)
    count = 0
    dic = Questions.generate_questions(5,42,200)
    ui.tab_quest_label.setText(dic[0][0])
    ui.check_answer_button.pressed.connect(lambda: getLineAns(dic,count))
            
##  
##       ans = u.check_answer_button.clicked.connect(lambda: getLineAns(u))
##    if ans !=None:
##        boo = Questions.check_answer(d[0][1],ans)
##        print(boo)
    
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = QuizDown.Ui_Form()
    ui.setupUi(Form)
    Form.show()
    for i in dif:
        ui.diff_combo.insertItem(4,i)
    for i in questions:
        ui.ques_combo.insertItem(4,i)
    for i in categories:
        ui.cata_combo.insertItem(4,i)  
    ui.pushButton.pressed.connect(lambda: returnCombo(ui))
    sys.exit(app.exec_())

