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
count = 0
def clearQuestion(dic,u):
    u.tab_quest_label.setText(dic[count][0])
    u.ans_lineEdit.setText("")
    
def getLineAns(u,dic):
    u.pushButton.setEnabled(False)
    ans = u.ans_lineEdit.text()
    if True:#Questions.check_answer(d[count][1],ans):
        u.cont_button.setEnabled(True)
        global count
        count+=1
        
    else:
        u.ans_lineEdit.setText("")

def returnCombo(u):
    res = []
    res.append(u.diff_combo.currentText())
    res.append(u.cata_combo.currentText())
    res.append(u.ques_combo.currentText())
    u.tabWidget.removeTab(0)
    u.quest_tab.setEnabled(True)
    u.cont_button.setEnabled(False)
    dic = Questions.generate_questions(5,42,200)
    u.tab_quest_label.setText(dic[0][0])
    u.check_answer_button.pressed.connect(lambda: getLineAns(u,dic))
    u.cont_button.pressed.connect(lambda: clearQuestion(dic,u))
    
    
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

