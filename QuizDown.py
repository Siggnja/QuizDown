# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QuizDown.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(946, 749)
        Form.setStyleSheet("background-image: url(:/new/prefix1/Graphics/Background Clean.png);")
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setObjectName("tabWidget")
        self.front_tab = QtWidgets.QWidget()
        self.front_tab.setEnabled(True)
        self.front_tab.setObjectName("front_tab")
        self.gridLayout = QtWidgets.QGridLayout(self.front_tab)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.front_tab)
        self.pushButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton.setToolTipDuration(0)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/new/prefix1/Graphics/Start_quiz.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(150, 75))
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_5.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_5, 3, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.quest_label = QtWidgets.QLabel(self.front_tab)
        self.quest_label.setStyleSheet("font: 14pt \"Gill Sans Ultra Bold\";")
        self.quest_label.setObjectName("quest_label")
        self.verticalLayout.addWidget(self.quest_label, 0, QtCore.Qt.AlignHCenter)
        self.ques_combo = QtWidgets.QComboBox(self.front_tab)
        self.ques_combo.setMaximumSize(QtCore.QSize(100, 16777215))
        self.ques_combo.setStyleSheet("font: 12pt \"Arial Rounded MT Bold\";")
        self.ques_combo.setObjectName("ques_combo")
        self.verticalLayout.addWidget(self.ques_combo, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.dif_label = QtWidgets.QLabel(self.front_tab)
        self.dif_label.setStyleSheet("font: 14pt \"Gill Sans Ultra Bold\";")
        self.dif_label.setObjectName("dif_label")
        self.verticalLayout_2.addWidget(self.dif_label, 0, QtCore.Qt.AlignHCenter)
        self.diff_combo = QtWidgets.QComboBox(self.front_tab)
        self.diff_combo.setMinimumSize(QtCore.QSize(150, 0))
        self.diff_combo.setMaximumSize(QtCore.QSize(300, 16777215))
        self.diff_combo.setStyleSheet("font: 12pt \"Arial Rounded MT Bold\";")
        self.diff_combo.setObjectName("diff_combo")
        self.verticalLayout_2.addWidget(self.diff_combo, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem6)
        self.cata_label = QtWidgets.QLabel(self.front_tab)
        self.cata_label.setStyleSheet("font: 14pt \"Gill Sans Ultra Bold\";")
        self.cata_label.setObjectName("cata_label")
        self.verticalLayout_3.addWidget(self.cata_label, 0, QtCore.Qt.AlignHCenter)
        self.cata_combo = QtWidgets.QComboBox(self.front_tab)
        self.cata_combo.setMinimumSize(QtCore.QSize(150, 0))
        self.cata_combo.setMaximumSize(QtCore.QSize(200, 16777215))
        self.cata_combo.setStyleSheet("font: 12pt \"Arial Rounded MT Bold\";")
        self.cata_combo.setObjectName("cata_combo")
        self.verticalLayout_3.addWidget(self.cata_combo, 0, QtCore.Qt.AlignHCenter)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem7)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 2)
        spacerItem8 = QtWidgets.QSpacerItem(20, 70, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem8, 4, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(10, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem9, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.front_tab)
        self.label_2.setMinimumSize(QtCore.QSize(0, 250))
        self.label_2.setStyleSheet("image: url(:/new/prefix1/Graphics/Logo2.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.front_tab, "")
        self.quest_tab = QtWidgets.QWidget()
        self.quest_tab.setEnabled(False)
        self.quest_tab.setObjectName("quest_tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.quest_tab)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Player_1 = QtWidgets.QLabel(self.quest_tab)
        self.Player_1.setMaximumSize(QtCore.QSize(100, 100))
        self.Player_1.setText("")
        self.Player_1.setPixmap(QtGui.QPixmap(":/new/prefix1/Graphics/player 1.png"))
        self.Player_1.setScaledContents(True)
        self.Player_1.setObjectName("Player_1")
        self.gridLayout_3.addWidget(self.Player_1, 0, 5, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 280, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem10, 0, 3, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem11 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem11)
        self.ans_lineEdit = QtWidgets.QLineEdit(self.quest_tab)
        self.ans_lineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.ans_lineEdit.setStyleSheet("font: 18pt \"Gadugi\";")
        self.ans_lineEdit.setObjectName("ans_lineEdit")
        self.horizontalLayout_2.addWidget(self.ans_lineEdit)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem12)
        self.check_answer_button = QtWidgets.QPushButton(self.quest_tab)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/new/prefix1/Graphics/Check_answer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.check_answer_button.setIcon(icon1)
        self.check_answer_button.setIconSize(QtCore.QSize(55, 55))
        self.check_answer_button.setFlat(True)
        self.check_answer_button.setObjectName("check_answer_button")
        self.horizontalLayout_2.addWidget(self.check_answer_button)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem13)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 2, 0, 2, 7)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem14)
        self.skip_button = QtWidgets.QPushButton(self.quest_tab)
        self.skip_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/new/prefix1/Graphics/skip_question.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.skip_button.setIcon(icon2)
        self.skip_button.setIconSize(QtCore.QSize(100, 50))
        self.skip_button.setFlat(True)
        self.skip_button.setObjectName("skip_button")
        self.horizontalLayout.addWidget(self.skip_button)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem15)
        self.cont_button = QtWidgets.QPushButton(self.quest_tab)
        self.cont_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/new/prefix1/Graphics/next_question.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cont_button.setIcon(icon3)
        self.cont_button.setIconSize(QtCore.QSize(100, 50))
        self.cont_button.setFlat(True)
        self.cont_button.setObjectName("cont_button")
        self.horizontalLayout.addWidget(self.cont_button)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem16)
        self.gridLayout_3.addLayout(self.horizontalLayout, 5, 0, 3, 7)
        spacerItem17 = QtWidgets.QSpacerItem(15, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem17, 8, 3, 1, 1)
        self.hint_button = QtWidgets.QPushButton(self.quest_tab)
        self.hint_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/new/prefix1/Graphics/Hint_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.hint_button.setIcon(icon4)
        self.hint_button.setIconSize(QtCore.QSize(40, 40))
        self.hint_button.setFlat(True)
        self.hint_button.setObjectName("hint_button")
        self.gridLayout_3.addWidget(self.hint_button, 4, 3, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(420, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem18, 4, 0, 1, 3)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem19, 0, 6, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(420, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem20, 4, 4, 1, 3)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem21, 0, 4, 1, 1)
        self.tab_quest_label = QtWidgets.QTextBrowser(self.quest_tab)
        self.tab_quest_label.setStyleSheet("font: 18pt \"Gadugi\";\n"
"background-image: url(:/new/prefix1/Graphics/Background Grey.png);")
        self.tab_quest_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tab_quest_label.setCursorWidth(1)
        self.tab_quest_label.setPlaceholderText("")
        self.tab_quest_label.setObjectName("tab_quest_label")
        self.gridLayout_3.addWidget(self.tab_quest_label, 1, 1, 1, 5)
        self.label = QtWidgets.QLabel(self.quest_tab)
        self.label.setMaximumSize(QtCore.QSize(16777215, 225))
        self.label.setStyleSheet("image: url(:/new/prefix1/Graphics/Logo2.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 3)
        self.tabWidget.addTab(self.quest_tab, "")
        self.results_tab = QtWidgets.QWidget()
        self.results_tab.setEnabled(False)
        self.results_tab.setObjectName("results_tab")
        self.finish_button = QtWidgets.QPushButton(self.results_tab)
        self.finish_button.setGeometry(QtCore.QRect(600, 450, 75, 23))
        self.finish_button.setObjectName("finish_button")
        self.result_label = QtWidgets.QLabel(self.results_tab)
        self.result_label.setGeometry(QtCore.QRect(100, 40, 511, 311))
        self.result_label.setObjectName("result_label")
        self.tabWidget.addTab(self.results_tab, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "QuizDown"))
        self.quest_label.setText(_translate("Form", "Number of questions"))
        self.dif_label.setText(_translate("Form", "Difficulty"))
        self.cata_label.setText(_translate("Form", "Category"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.front_tab), _translate("Form", "QuizDown"))
        self.ans_lineEdit.setPlaceholderText(_translate("Form", "Please enter your answer.."))
        self.tab_quest_label.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gadugi\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.quest_tab), _translate("Form", "Questions"))
        self.finish_button.setText(_translate("Form", "Finish"))
        self.result_label.setText(_translate("Form", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.results_tab), _translate("Form", "Results"))

import myndir_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

