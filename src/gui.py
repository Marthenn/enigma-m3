# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        MainWindow.setMinimumSize(QtCore.QSize(800, 800))
        MainWindow.setMaximumSize(QtCore.QSize(800, 800))
        MainWindow.setStyleSheet("background-color: #1746A2")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.header = QtWidgets.QFrame(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(0, 0, 801, 91))
        self.header.setStyleSheet("background-color: #5F9DF7;")
        self.header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header.setObjectName("header")
        self.title_text = QtWidgets.QLabel(self.header)
        self.title_text.setGeometry(QtCore.QRect(0, 0, 800, 90))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.title_text.setFont(font)
        self.title_text.setStyleSheet("color: white;")
        self.title_text.setAlignment(QtCore.Qt.AlignCenter)
        self.title_text.setObjectName("title_text")
        self.setting = QtWidgets.QFrame(self.centralwidget)
        self.setting.setGeometry(QtCore.QRect(560, 110, 221, 271))
        self.setting.setStyleSheet("background-color: #5F9DF7;\n"
"border-radius: 25px;")
        self.setting.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setting.setFrameShadow(QtWidgets.QFrame.Raised)
        self.setting.setObjectName("setting")
        self.left_rotor = QtWidgets.QComboBox(self.setting)
        self.left_rotor.setGeometry(QtCore.QRect(120, 50, 69, 22))
        self.left_rotor.setStyleSheet("background-color: white")
        self.left_rotor.setObjectName("left_rotor")
        self.label = QtWidgets.QLabel(self.setting)
        self.label.setGeometry(QtCore.QRect(20, 50, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white")
        self.label.setObjectName("label")
        self.middle_rotor = QtWidgets.QComboBox(self.setting)
        self.middle_rotor.setGeometry(QtCore.QRect(120, 80, 69, 22))
        self.middle_rotor.setStyleSheet("background-color: white")
        self.middle_rotor.setObjectName("middle_rotor")
        self.label_2 = QtWidgets.QLabel(self.setting)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white")
        self.label_2.setObjectName("label_2")
        self.right_rotor = QtWidgets.QComboBox(self.setting)
        self.right_rotor.setGeometry(QtCore.QRect(120, 110, 69, 22))
        self.right_rotor.setStyleSheet("background-color: white")
        self.right_rotor.setObjectName("right_rotor")
        self.label_3 = QtWidgets.QLabel(self.setting)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: white")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.setting)
        self.label_4.setGeometry(QtCore.QRect(20, 200, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: white")
        self.label_4.setObjectName("label_4")
        self.middle_position = QtWidgets.QComboBox(self.setting)
        self.middle_position.setGeometry(QtCore.QRect(120, 170, 69, 22))
        self.middle_position.setStyleSheet("background-color: white")
        self.middle_position.setObjectName("middle_position")
        self.label_5 = QtWidgets.QLabel(self.setting)
        self.label_5.setGeometry(QtCore.QRect(20, 170, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: white")
        self.label_5.setObjectName("label_5")
        self.left_position = QtWidgets.QComboBox(self.setting)
        self.left_position.setGeometry(QtCore.QRect(120, 140, 69, 22))
        self.left_position.setStyleSheet("background-color: white")
        self.left_position.setObjectName("left_position")
        self.right_position = QtWidgets.QComboBox(self.setting)
        self.right_position.setGeometry(QtCore.QRect(120, 200, 69, 22))
        self.right_position.setStyleSheet("background-color: white")
        self.right_position.setObjectName("right_position")
        self.label_6 = QtWidgets.QLabel(self.setting)
        self.label_6.setGeometry(QtCore.QRect(20, 140, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: white")
        self.label_6.setObjectName("label_6")
        self.setting_header_3 = QtWidgets.QLabel(self.setting)
        self.setting_header_3.setGeometry(QtCore.QRect(50, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.setting_header_3.setFont(font)
        self.setting_header_3.setStyleSheet("color: white;")
        self.setting_header_3.setObjectName("setting_header_3")
        self.turingButton = QtWidgets.QPushButton(self.setting)
        self.turingButton.setGeometry(QtCore.QRect(20, 230, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.turingButton.setFont(font)
        self.turingButton.setStyleSheet("color: white;\n"
"background-color: #1746A2;\n"
"border: none;\n"
"border-radius: 15px;\n"
"padding: 8px;")
        self.turingButton.setObjectName("turingButton")
        self.input = QtWidgets.QFrame(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(20, 110, 521, 231))
        self.input.setStyleSheet("background-color: #5F9DF7;\n"
"border-radius: 25px;")
        self.input.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.input.setFrameShadow(QtWidgets.QFrame.Raised)
        self.input.setObjectName("input")
        self.input_text = QtWidgets.QTextEdit(self.input)
        self.input_text.setGeometry(QtCore.QRect(20, 10, 481, 201))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.input_text.setFont(font)
        self.input_text.setStyleSheet("color: white;")
        self.input_text.setInputMethodHints(QtCore.Qt.ImhMultiLine|QtCore.Qt.ImhPreferLatin|QtCore.Qt.ImhUppercaseOnly)
        self.input_text.setPlaceholderText("")
        self.input_text.setObjectName("input_text")
        self.output = QtWidgets.QFrame(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(20, 350, 521, 231))
        self.output.setStyleSheet("background-color: #5F9DF7;\n"
"border-radius: 25px;")
        self.output.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.output.setFrameShadow(QtWidgets.QFrame.Raised)
        self.output.setObjectName("output")
        self.outputText = QtWidgets.QTextBrowser(self.output)
        self.outputText.setGeometry(QtCore.QRect(10, 10, 501, 192))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.outputText.setFont(font)
        self.outputText.setAutoFillBackground(False)
        self.outputText.setStyleSheet("")
        self.outputText.setObjectName("outputText")
        self.steps = QtWidgets.QFrame(self.centralwidget)
        self.steps.setGeometry(QtCore.QRect(560, 390, 221, 401))
        self.steps.setStyleSheet("background-color: #5F9DF7;\n"
"border-radius: 25px;")
        self.steps.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.steps.setFrameShadow(QtWidgets.QFrame.Raised)
        self.steps.setObjectName("steps")
        self.label_8 = QtWidgets.QLabel(self.steps)
        self.label_8.setGeometry(QtCore.QRect(20, 50, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: white")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.steps)
        self.label_9.setGeometry(QtCore.QRect(20, 80, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: white")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.steps)
        self.label_10.setGeometry(QtCore.QRect(20, 110, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: white")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.steps)
        self.label_11.setGeometry(QtCore.QRect(20, 140, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: white")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.steps)
        self.label_12.setGeometry(QtCore.QRect(20, 170, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: white")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.steps)
        self.label_13.setGeometry(QtCore.QRect(20, 200, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: white")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.steps)
        self.label_14.setGeometry(QtCore.QRect(20, 230, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: white")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.steps)
        self.label_15.setGeometry(QtCore.QRect(20, 260, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: white")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.steps)
        self.label_16.setGeometry(QtCore.QRect(20, 290, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: white")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.steps)
        self.label_17.setGeometry(QtCore.QRect(20, 320, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: white")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.steps)
        self.label_18.setGeometry(QtCore.QRect(20, 350, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: white")
        self.label_18.setObjectName("label_18")
        self.setting_header_4 = QtWidgets.QLabel(self.steps)
        self.setting_header_4.setGeometry(QtCore.QRect(50, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.setting_header_4.setFont(font)
        self.setting_header_4.setStyleSheet("color: white;")
        self.setting_header_4.setObjectName("setting_header_4")
        self.output_plugboard_step = QtWidgets.QLabel(self.steps)
        self.output_plugboard_step.setGeometry(QtCore.QRect(120, 320, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.output_plugboard_step.setFont(font)
        self.output_plugboard_step.setStyleSheet("color: white")
        self.output_plugboard_step.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.output_plugboard_step.setObjectName("output_plugboard_step")
        self.output_step = QtWidgets.QLabel(self.steps)
        self.output_step.setGeometry(QtCore.QRect(120, 350, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.output_step.setFont(font)
        self.output_step.setStyleSheet("color: white")
        self.output_step.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.output_step.setObjectName("output_step")
        self.right_rotor_reverse_step = QtWidgets.QLabel(self.steps)
        self.right_rotor_reverse_step.setGeometry(QtCore.QRect(120, 290, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.right_rotor_reverse_step.setFont(font)
        self.right_rotor_reverse_step.setStyleSheet("color: white")
        self.right_rotor_reverse_step.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.right_rotor_reverse_step.setObjectName("right_rotor_reverse_step")
        self.left_rotor_reverse_step = QtWidgets.QLabel(self.steps)
        self.left_rotor_reverse_step.setGeometry(QtCore.QRect(120, 230, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.left_rotor_reverse_step.setFont(font)
        self.left_rotor_reverse_step.setStyleSheet("color: white")
        self.left_rotor_reverse_step.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.left_rotor_reverse_step.setObjectName("left_rotor_reverse_step")
        self.reflector_step = QtWidgets.QLabel(self.steps)
        self.reflector_step.setGeometry(QtCore.QRect(120, 200, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.reflector_step.setFont(font)
        self.reflector_step.setStyleSheet("color: white")
        self.reflector_step.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.reflector_step.setObjectName("reflector_step")
        self.input_step = QtWidgets.QLabel(self.steps)
        self.input_step.setGeometry(QtCore.QRect(120, 50, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.input_step.setFont(font)
        self.input_step.setStyleSheet("color: white")
        self.input_step.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.input_step.setObjectName("input_step")
        self.middle_rotor_step = QtWidgets.QLabel(self.steps)
        self.middle_rotor_step.setGeometry(QtCore.QRect(120, 140, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.middle_rotor_step.setFont(font)
        self.middle_rotor_step.setStyleSheet("color: white")
        self.middle_rotor_step.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.middle_rotor_step.setObjectName("middle_rotor_step")
        self.left_rotor_step = QtWidgets.QLabel(self.steps)
        self.left_rotor_step.setGeometry(QtCore.QRect(120, 170, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.left_rotor_step.setFont(font)
        self.left_rotor_step.setStyleSheet("color: white")
        self.left_rotor_step.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.left_rotor_step.setObjectName("left_rotor_step")
        self.middle_rotor_reverse_step = QtWidgets.QLabel(self.steps)
        self.middle_rotor_reverse_step.setGeometry(QtCore.QRect(120, 260, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.middle_rotor_reverse_step.setFont(font)
        self.middle_rotor_reverse_step.setStyleSheet("color: white")
        self.middle_rotor_reverse_step.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.middle_rotor_reverse_step.setObjectName("middle_rotor_reverse_step")
        self.input_plugboard_step = QtWidgets.QLabel(self.steps)
        self.input_plugboard_step.setGeometry(QtCore.QRect(120, 80, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.input_plugboard_step.setFont(font)
        self.input_plugboard_step.setStyleSheet("color: white")
        self.input_plugboard_step.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.input_plugboard_step.setObjectName("input_plugboard_step")
        self.right_rotor_step = QtWidgets.QLabel(self.steps)
        self.right_rotor_step.setGeometry(QtCore.QRect(120, 110, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.right_rotor_step.setFont(font)
        self.right_rotor_step.setStyleSheet("color: white")
        self.right_rotor_step.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.right_rotor_step.setObjectName("right_rotor_step")
        self.plugboard = QtWidgets.QFrame(self.centralwidget)
        self.plugboard.setGeometry(QtCore.QRect(20, 590, 521, 201))
        self.plugboard.setStyleSheet("background-color: #5F9DF7;\n"
"border-radius: 25px;")
        self.plugboard.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.plugboard.setFrameShadow(QtWidgets.QFrame.Raised)
        self.plugboard.setObjectName("plugboard")
        self.qButton = QtWidgets.QPushButton(self.plugboard)
        self.qButton.setGeometry(QtCore.QRect(20, 60, 31, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.qButton.setFont(font)
        self.qButton.setStyleSheet("background-color: white")
        self.qButton.setObjectName("qButton")
        self.wButton = QtWidgets.QPushButton(self.plugboard)
        self.wButton.setGeometry(QtCore.QRect(70, 60, 31, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.wButton.setFont(font)
        self.wButton.setStyleSheet("background-color: white")
        self.wButton.setObjectName("wButton")
        self.eButton = QtWidgets.QPushButton(self.plugboard)
        self.eButton.setGeometry(QtCore.QRect(120, 60, 31, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.eButton.setFont(font)
        self.eButton.setStyleSheet("background-color: white")
        self.eButton.setObjectName("eButton")
        self.rButton = QtWidgets.QPushButton(self.plugboard)
        self.rButton.setGeometry(QtCore.QRect(170, 60, 31, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.rButton.setFont(font)
        self.rButton.setStyleSheet("background-color: white")
        self.rButton.setObjectName("rButton")
        self.tButton = QtWidgets.QPushButton(self.plugboard)
        self.tButton.setGeometry(QtCore.QRect(220, 60, 31, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tButton.setFont(font)
        self.tButton.setStyleSheet("background-color: white")
        self.tButton.setObjectName("tButton")
        self.yButton = QtWidgets.QPushButton(self.plugboard)
        self.yButton.setGeometry(QtCore.QRect(270, 60, 31, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.yButton.setFont(font)
        self.yButton.setStyleSheet("background-color: white")
        self.yButton.setObjectName("yButton")
        self.uButton = QtWidgets.QPushButton(self.plugboard)
        self.uButton.setGeometry(QtCore.QRect(320, 60, 31, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.uButton.setFont(font)
        self.uButton.setStyleSheet("background-color: white")
        self.uButton.setObjectName("uButton")
        self.iButton = QtWidgets.QPushButton(self.plugboard)
        self.iButton.setGeometry(QtCore.QRect(370, 60, 31, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.iButton.setFont(font)
        self.iButton.setStyleSheet("background-color: white")
        self.iButton.setObjectName("iButton")
        self.oButton = QtWidgets.QPushButton(self.plugboard)
        self.oButton.setGeometry(QtCore.QRect(420, 60, 31, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.oButton.setFont(font)
        self.oButton.setStyleSheet("background-color: white")
        self.oButton.setObjectName("oButton")
        self.pButton = QtWidgets.QPushButton(self.plugboard)
        self.pButton.setGeometry(QtCore.QRect(470, 60, 31, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pButton.setFont(font)
        self.pButton.setStyleSheet("background-color: white")
        self.pButton.setObjectName("pButton")
        self.jButton = QtWidgets.QPushButton(self.plugboard)
        self.jButton.setGeometry(QtCore.QRect(350, 100, 31, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.jButton.setFont(font)
        self.jButton.setStyleSheet("background-color: white")
        self.jButton.setObjectName("jButton")
        self.gButton = QtWidgets.QPushButton(self.plugboard)
        self.gButton.setGeometry(QtCore.QRect(250, 100, 31, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.gButton.setFont(font)
        self.gButton.setStyleSheet("background-color: white")
        self.gButton.setObjectName("gButton")
        self.lButton = QtWidgets.QPushButton(self.plugboard)
        self.lButton.setGeometry(QtCore.QRect(450, 100, 31, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lButton.setFont(font)
        self.lButton.setStyleSheet("background-color: white")
        self.lButton.setObjectName("lButton")
        self.fButton = QtWidgets.QPushButton(self.plugboard)
        self.fButton.setGeometry(QtCore.QRect(200, 100, 31, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.fButton.setFont(font)
        self.fButton.setStyleSheet("background-color: white")
        self.fButton.setObjectName("fButton")
        self.hButton = QtWidgets.QPushButton(self.plugboard)
        self.hButton.setGeometry(QtCore.QRect(300, 100, 31, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.hButton.setFont(font)
        self.hButton.setStyleSheet("background-color: white")
        self.hButton.setObjectName("hButton")
        self.sButton = QtWidgets.QPushButton(self.plugboard)
        self.sButton.setGeometry(QtCore.QRect(100, 100, 31, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sButton.setFont(font)
        self.sButton.setStyleSheet("background-color: white")
        self.sButton.setObjectName("sButton")
        self.kButton = QtWidgets.QPushButton(self.plugboard)
        self.kButton.setGeometry(QtCore.QRect(400, 100, 31, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.kButton.setFont(font)
        self.kButton.setStyleSheet("background-color: white")
        self.kButton.setObjectName("kButton")
        self.aButton = QtWidgets.QPushButton(self.plugboard)
        self.aButton.setGeometry(QtCore.QRect(50, 100, 31, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.aButton.setFont(font)
        self.aButton.setStyleSheet("background-color: white")
        self.aButton.setObjectName("aButton")
        self.dButton = QtWidgets.QPushButton(self.plugboard)
        self.dButton.setGeometry(QtCore.QRect(150, 100, 31, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.dButton.setFont(font)
        self.dButton.setStyleSheet("background-color: white")
        self.dButton.setObjectName("dButton")
        self.vButton = QtWidgets.QPushButton(self.plugboard)
        self.vButton.setGeometry(QtCore.QRect(250, 140, 31, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.vButton.setFont(font)
        self.vButton.setStyleSheet("background-color: white")
        self.vButton.setObjectName("vButton")
        self.nButton = QtWidgets.QPushButton(self.plugboard)
        self.nButton.setGeometry(QtCore.QRect(350, 140, 31, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.nButton.setFont(font)
        self.nButton.setStyleSheet("background-color: white")
        self.nButton.setObjectName("nButton")
        self.bButton = QtWidgets.QPushButton(self.plugboard)
        self.bButton.setGeometry(QtCore.QRect(300, 140, 31, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bButton.setFont(font)
        self.bButton.setStyleSheet("background-color: white")
        self.bButton.setObjectName("bButton")
        self.xButton = QtWidgets.QPushButton(self.plugboard)
        self.xButton.setGeometry(QtCore.QRect(150, 140, 31, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.xButton.setFont(font)
        self.xButton.setStyleSheet("background-color: white")
        self.xButton.setObjectName("xButton")
        self.cButton = QtWidgets.QPushButton(self.plugboard)
        self.cButton.setGeometry(QtCore.QRect(200, 140, 31, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cButton.setFont(font)
        self.cButton.setStyleSheet("background-color: white")
        self.cButton.setObjectName("cButton")
        self.mButton = QtWidgets.QPushButton(self.plugboard)
        self.mButton.setGeometry(QtCore.QRect(400, 140, 31, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.mButton.setFont(font)
        self.mButton.setStyleSheet("background-color: white")
        self.mButton.setObjectName("mButton")
        self.zButton = QtWidgets.QPushButton(self.plugboard)
        self.zButton.setGeometry(QtCore.QRect(100, 140, 31, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.zButton.setFont(font)
        self.zButton.setStyleSheet("background-color: white")
        self.zButton.setObjectName("zButton")
        self.plugboard_header = QtWidgets.QLabel(self.plugboard)
        self.plugboard_header.setGeometry(QtCore.QRect(20, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.plugboard_header.setFont(font)
        self.plugboard_header.setStyleSheet("color: white;")
        self.plugboard_header.setObjectName("plugboard_header")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title_text.setText(_translate("MainWindow", "ENIGMA MACHINE SIMULATOR"))
        self.label.setText(_translate("MainWindow", "Left Rotor"))
        self.label_2.setText(_translate("MainWindow", "Middle Rotor"))
        self.label_3.setText(_translate("MainWindow", "Right Rotor"))
        self.label_4.setText(_translate("MainWindow", "Right Position"))
        self.label_5.setText(_translate("MainWindow", "Middle Position"))
        self.label_6.setText(_translate("MainWindow", "Left Position"))
        self.setting_header_3.setText(_translate("MainWindow", "Rotors Setting"))
        self.turingButton.setText(_translate("MainWindow", "Alan Turing"))
        self.input_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.outputText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Open Sans\',\'Arial\',\'sans-serif\'; font-size:14px; color:#ffffff;\">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus in arcu nec magna venenatis semper ac in neque. Praesent vulputate, ipsum nec vestibulum ultrices, eros felis suscipit enim, in sodales mauris metus sit amet nisi. Phasellus condimentum mi tellus, sed bibendum ante rutrum nec. Aliquam sed sapien nec augue gravida ornare id sit amet odio. Mauris malesuada, diam at molestie ornare, justo nisi scelerisque mi, quis auctor augue tortor ac purus. Nunc non ullamcorper nisi. Donec malesuada vel nisi nec mollis. Morbi posuere felis non augue ornare, a auctor eros fringilla. Nulla vitae malesuada mauris. Vestibulum risus leo, ultricies sit amet augue sit amet, consequat congue felis. Phasellus sed magna nec justo convallis faucibus sit amet a lorem. Suspendisse venenatis convallis gravida.</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "Input"))
        self.label_9.setText(_translate("MainWindow", "Plugboard"))
        self.label_10.setText(_translate("MainWindow", "Right Rotor"))
        self.label_11.setText(_translate("MainWindow", "Middle Rotor"))
        self.label_12.setText(_translate("MainWindow", "Left Rotor"))
        self.label_13.setText(_translate("MainWindow", "Reflector"))
        self.label_14.setText(_translate("MainWindow", "Left Rotor"))
        self.label_15.setText(_translate("MainWindow", "Middle Rotor"))
        self.label_16.setText(_translate("MainWindow", "Right Rotor"))
        self.label_17.setText(_translate("MainWindow", "Plugboard"))
        self.label_18.setText(_translate("MainWindow", "Output"))
        self.setting_header_4.setText(_translate("MainWindow", "Enigma Steps"))
        self.output_plugboard_step.setText(_translate("MainWindow", "placeholder"))
        self.output_step.setText(_translate("MainWindow", "placeholder"))
        self.right_rotor_reverse_step.setText(_translate("MainWindow", "placeholder"))
        self.left_rotor_reverse_step.setText(_translate("MainWindow", "placeholder"))
        self.reflector_step.setText(_translate("MainWindow", "placeholder"))
        self.input_step.setText(_translate("MainWindow", "placeholder"))
        self.middle_rotor_step.setText(_translate("MainWindow", "placeholder"))
        self.left_rotor_step.setText(_translate("MainWindow", "placeholder"))
        self.middle_rotor_reverse_step.setText(_translate("MainWindow", "placeholder"))
        self.input_plugboard_step.setText(_translate("MainWindow", "placeholder"))
        self.right_rotor_step.setText(_translate("MainWindow", "placeholder"))
        self.qButton.setText(_translate("MainWindow", "Q"))
        self.wButton.setText(_translate("MainWindow", "W"))
        self.eButton.setText(_translate("MainWindow", "E"))
        self.rButton.setText(_translate("MainWindow", "R"))
        self.tButton.setText(_translate("MainWindow", "T"))
        self.yButton.setText(_translate("MainWindow", "Y"))
        self.uButton.setText(_translate("MainWindow", "U"))
        self.iButton.setText(_translate("MainWindow", "I"))
        self.oButton.setText(_translate("MainWindow", "O"))
        self.pButton.setText(_translate("MainWindow", "P"))
        self.jButton.setText(_translate("MainWindow", "J"))
        self.gButton.setText(_translate("MainWindow", "G"))
        self.lButton.setText(_translate("MainWindow", "L"))
        self.fButton.setText(_translate("MainWindow", "F"))
        self.hButton.setText(_translate("MainWindow", "H"))
        self.sButton.setText(_translate("MainWindow", "S"))
        self.kButton.setText(_translate("MainWindow", "K"))
        self.aButton.setText(_translate("MainWindow", "A"))
        self.dButton.setText(_translate("MainWindow", "D"))
        self.vButton.setText(_translate("MainWindow", "V"))
        self.nButton.setText(_translate("MainWindow", "N"))
        self.bButton.setText(_translate("MainWindow", "B"))
        self.xButton.setText(_translate("MainWindow", "X"))
        self.cButton.setText(_translate("MainWindow", "C"))
        self.mButton.setText(_translate("MainWindow", "M"))
        self.zButton.setText(_translate("MainWindow", "Z"))
        self.plugboard_header.setText(_translate("MainWindow", "Plugboard"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
