# -*- coding: utf-8 -*-

# This is the main file where all the computations are made
#
# Created by: artidemima aristidemima@gmail.com
#
# Enjoy the code


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QMessageBox
from keras.models import load_model
from tensorflow import device
from keras import backend as K
import numpy as np
from pickle import load

#Globals variables
# Inporting all models and Scalers , that has been trained and saved

Models = {'Abuja':{'Hourly prediction': 'model_Abuja_hour.h5', 'Daily Prediction': 'model_Abuja_day.h5'},
          'Lagos':{'Hourly prediction': 'model_Lagos_hour.h5', 'Daily Prediction': 'model_Abuja_day.h5'},
          'Bauchi':{'Hourly prediction': 'model_bauchi_hour.h5', 'Daily Prediction': 'model_bauchi_day.h5'},
          'Enugu':{'Hourly prediction': 'model_ENUGU_hour.h5', 'Daily Prediction': 'model_ENUGU_day.h5'},
          'Porthacourt':{'Hourly prediction': 'model_Porthacourt_hour.h5', 'Daily Prediction': 'model_Porthacourt_day.h5'},
          'Anyigba':{'Hourly prediction': 'model_ANYIGBA_hour.h5', 'Daily Prediction': 'model_ANYIGBA_day.h5'},
          }
Scalers = {'Abuja':{'Hourly prediction': 'Abuja-scaler-hour.pkl', 'Daily Prediction': 'Abuja-scaler-day.pkl'},
          'Lagos':{'Hourly prediction': 'Lagos-scaler-hour.pkl', 'Daily Prediction': 'Lagos-scaler-day.pkl'},
          'Bauchi':{'Hourly prediction': 'BAUCHI-scaler-hour.pkl', 'Daily Prediction': 'BAUCHI-scaler-day.pkl'},
          'Enugu':{'Hourly prediction': 'ENUGU-scaler-hour.pkl', 'Daily Prediction': 'ENUGU-scaler-day.pkl'},
          'Porthacourt':{'Hourly prediction': 'Porthacourt-scaler-hour.pkl', 'Daily Prediction': 'Porthacourt-scaler-day.pkl'},
          'Anyigba':{'Hourly prediction': 'ANYIGBA-scaler-hour.pkl', 'Daily Prediction': 'ANYIGBA-scaler-day.pkl'},
          }

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(957, 793)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 961, 801))
        self.frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frame.setStyleSheet("QFrame{\n"
"    background-color:   #6b81cb  ;\n"
"    border-radius: 30px;\n"
"    color: white;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(250, 10, 421, 41))
        font = QtGui.QFont()
        font.setFamily("cambria")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel\n"
"{\n"
" font-family: cambria;\n"
"font-weight: bold;\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 621, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(40, 90, 471, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(40, 120, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.values1 = QtWidgets.QPlainTextEdit(self.frame)
        self.values1.setEnabled(True)
        self.values1.setGeometry(QtCore.QRect(280, 240, 551, 31))
        self.values1.setStyleSheet("QPlainTextEdit\n"
"{\n"
"background-color: rgb(255, 255, 255); \n"
"color: black; font-size:15px;\n"
"font-family: Arial;\n"
"color: #6b4ebc;\n"
"letter-spacing: 8px;\n"
"font-weight: bold;\n"
"}")
        self.values1.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.values1.setPlainText("")
        self.values1.setObjectName("values1")
        self.values2 = QtWidgets.QPlainTextEdit(self.frame)
        self.values2.setGeometry(QtCore.QRect(280, 280, 551, 31))
        self.values2.setStyleSheet("QPlainTextEdit\n"
"{\n"
"background-color: rgb(255, 255, 255); \n"
"color: black; font-size:15px;\n"
"font-family: Arial;\n"
"color: #6b4ebc;\n"
"letter-spacing: 8px;\n"
"font-weight: bold;\n"
"}")
        self.values2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.values2.setObjectName("values2")
        self.values3 = QtWidgets.QPlainTextEdit(self.frame)
        self.values3.setGeometry(QtCore.QRect(280, 320, 551, 31))
        self.values3.setStyleSheet("QPlainTextEdit\n"
"{\n"
"background-color: rgb(255, 255, 255); \n"
"color: black; font-size:15px;\n"
"font-family: Arial;\n"
"color: #6b4ebc;\n"
"letter-spacing: 8px;\n"
"font-weight: bold;\n"
"}")
        self.values3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.values3.setObjectName("values3")
        self.predict_mod = QtWidgets.QComboBox(self.frame)
        self.predict_mod.setGeometry(QtCore.QRect(280, 361, 551, 31))
        self.predict_mod.setStyleSheet("QComboBox\n"
"{\n"
"      \n"
"     font-family: Arial;\n"
"     font-size: 14px;\n"
"    padding: auto;\n"
"    background-color: #846bc7;\n"
"    border-style: none;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    text-align: center;\n"
"}")
        self.predict_mod.setDuplicatesEnabled(False)
        self.predict_mod.setFrame(True)
        self.predict_mod.setObjectName("predict_mod")
        self.predict_mod.addItem("")
        self.predict_mod.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(280, 440, 551, 31))
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: #6b4ebc;;\n"
"    color: white;\n"
"    font-family: Arial;\n"
"    font-size: 18px;\n"
"}\n"
"\n"
"QPushButton::chunck{\n"
"    border-radius: 25px;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.predict_location = QtWidgets.QComboBox(self.frame)
        self.predict_location.setGeometry(QtCore.QRect(280, 400, 551, 31))
        self.predict_location.setStyleSheet("QComboBox\n"
"{\n"
"      \n"
"     font-family: Arial;\n"
"     font-size: 14px;\n"
"    padding: auto;\n"
"    background-color: #846bc7;\n"
"    border-style: none;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    text-align: center;\n"
"}")
        self.predict_location.setDuplicatesEnabled(False)
        self.predict_location.setFrame(True)
        self.predict_location.setObjectName("predict_location")
        self.predict_location.addItem("")
        self.predict_location.addItem("")
        self.predict_location.addItem("")
        self.predict_location.addItem("")
        self.predict_location.addItem("")
        self.predict_location.addItem("")
        self.solar_result = QtWidgets.QLabel(self.frame)
        self.solar_result.setGeometry(QtCore.QRect(40, 670, 21, 41))
        self.solar_result.setStyleSheet("QLabel{\n"
" font-size: 30px;\n"
"font-family: Arial;\n"
"text-align: center;\n"
"}")
        self.solar_result.setObjectName("solar_result")
        self.air_result = QtWidgets.QLabel(self.frame)
        self.air_result.setGeometry(QtCore.QRect(280, 670, 21, 41))
        self.air_result.setStyleSheet("QLabel{\n"
" font-size: 30px;\n"
"font-family: Arial;\n"
"text-align: center;\n"
"}")
        self.air_result.setObjectName("air_result")
        self.relative_result = QtWidgets.QLabel(self.frame)
        self.relative_result.setGeometry(QtCore.QRect(520, 670, 21, 41))
        self.relative_result.setStyleSheet("QLabel{\n"
" font-size: 30px;\n"
"font-family: Arial;\n"
"text-align: center;\n"
"}")
        self.relative_result.setObjectName("relative_result")
        self.pressure_result = QtWidgets.QLabel(self.frame)
        self.pressure_result.setGeometry(QtCore.QRect(800, 670, 21, 41))
        self.pressure_result.setStyleSheet("QLabel{\n"
" font-size: 30px;\n"
"font-family: Arial;\n"
"text-align: center;\n"
"}")
        self.pressure_result.setObjectName("pressure_result")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(70, 230, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("QLabel{\n"
"\n"
"font-weight: bold;\n"
"font-family: Arial;\n"
"font-size: 15px;\n"
"}")
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(70, 270, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("QLabel{\n"
"\n"
"font-weight: bold;\n"
"font-family: Arial;\n"
"font-size: 15px;\n"
"}")
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(70, 310, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("QLabel{\n"
"\n"
"font-weight: bold;\n"
"font-family: Arial;\n"
"font-size: 15px;\n"
"}")
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(70, 360, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("QLabel{\n"
"\n"
"font-weight: bold;\n"
"font-family: Arial;\n"
"font-size: 15px;\n"
"}")
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(70, 400, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("QLabel{\n"
"\n"
"font-weight: bold;\n"
"font-family: Arial;\n"
"font-size: 15px;\n"
"}")
        self.label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.solar_text = QtWidgets.QLabel(self.frame)
        self.solar_text.setGeometry(QtCore.QRect(30, 630, 111, 41))
        self.solar_text.setStyleSheet("QLabel{\n"
" font-size: 12px;\n"
"font-family: Arial;\n"
"text-align: center;\n"
"font-weight: bold;\n"
"}")
        self.solar_text.setObjectName("solar_text")
        self.air_text = QtWidgets.QLabel(self.frame)
        self.air_text.setGeometry(QtCore.QRect(270, 630, 111, 41))
        self.air_text.setStyleSheet("QLabel{\n"
" font-size: 12px;\n"
"font-family: Arial;\n"
"text-align: center;\n"
"font-weight: bold;\n"
"}")
        self.air_text.setObjectName("air_text")
        self.relative_text = QtWidgets.QLabel(self.frame)
        self.relative_text.setGeometry(QtCore.QRect(500, 630, 111, 41))
        self.relative_text.setStyleSheet("QLabel{\n"
" font-size: 12px;\n"
"font-family: Arial;\n"
"text-align: center;\n"
"font-weight: bold;\n"
"}")
        self.relative_text.setObjectName("relative_text")
        self.pressure_text = QtWidgets.QLabel(self.frame)
        self.pressure_text.setGeometry(QtCore.QRect(790, 630, 71, 41))
        self.pressure_text.setStyleSheet("QLabel{\n"
" font-size: 12px;\n"
"font-family: Arial;\n"
"text-align: center;\n"
"font-weight: bold;\n"
"}")
        self.pressure_text.setObjectName("pressure_text")
        self.message_result = QtWidgets.QLabel(self.frame)
        self.message_result.setGeometry(QtCore.QRect(190, 560, 581, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.message_result.setFont(font)
        self.message_result.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.message_result.setStyleSheet("QLabel{\n"
" font-size: 18px;\n"
"font-family: \"Times New Roman\";\n"
"text-align: center;\n"
"font-weight: bold;\n"
"font-style: oblique;\n"
"}")
        self.message_result.setObjectName("message_result")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(650, 760, 451, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.hello)

    def hello(self):
            # Loading model

            value1 = self.values1.toPlainText().split()
            value2 = self.values2.toPlainText().split()
            value3 = self.values3.toPlainText().split()

            if len(value1) != len(value2) or len(value2) != len(value3) or len(value3) != 4:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Each textfield must contain 4 values seperated by a space")
                    msg.setInformativeText('Ex: 10 10.5 10 10.8')
                    msg.setWindowTitle("Error")
                    msg.exec_()
            else:
                    try:
                            inputs = np.array([value1, value2, value3], dtype='float32')
                            scal_text = "scalers/" + Scalers[self.predict_location.currentText()][
                                    self.predict_mod.currentText()]
                            scaler = load(open(scal_text, 'rb'))

                            inputs = scaler.transform(inputs)
                            inputs = np.expand_dims(inputs, axis=0)
                            print(inputs)
                            with device('/cpu:0'):
                                    K.clear_session()
                                    a = "models/" + Models[self.predict_location.currentText()][
                                            self.predict_mod.currentText()]
                                    model = load_model(a, compile=False)
                                    predictions = scaler.inverse_transform(model.predict(inputs))
                                    print(predictions.shape)

                                    # Displaying predictions

                                    # result
                                    self.message_result.setText(
                                            self.predict_location.currentText() + " weather parameters for " + self.predict_mod.currentText())
                                    self.message_result.setGeometry(QtCore.QRect(190, 560, 581, 41))
                                    font = QtGui.QFont()
                                    font.setFamily("Times New Roman")
                                    font.setPointSize(-1)
                                    font.setBold(True)
                                    font.setItalic(True)
                                    font.setUnderline(True)
                                    font.setWeight(75)
                                    self.message_result.setFont(font)
                                    self.message_result.setLayoutDirection(QtCore.Qt.LeftToRight)
                                    self.message_result.setStyleSheet("QLabel{\n"

                                                                      " font-size: 25px;\n"
                                                                      "font-family: \"Times New Roman\";\n"
                                                                      "text-align: center;\n"
                                                                      "font-weight: bold;\n"
                                                                      "font-style: oblique;\n"
                                                                      "}")
                                    self.message_result.adjustSize()

                                    # parameters
                                    self.solar_result.setText(str(predictions[0][0]))
                                    self.solar_result.adjustSize()
                                    self.air_result.setText(str(predictions[0][1]))
                                    self.air_result.adjustSize()
                                    self.relative_result.setText(str(predictions[0][2]))
                                    self.relative_result.adjustSize()
                                    self.pressure_result.setText(str(predictions[0][3]))
                                    self.pressure_result.adjustSize()
                    except ValueError:
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Critical)
                            msg.setText("Error You must provide integers or float values")
                            msg.setInformativeText('Ex: 10 or 10.5')
                            msg.setWindowTitle("Error")
                            msg.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Weather forecasting over Nigeria"))
        self.label_2.setText(_translate("MainWindow", "- Enter differents values of the last 3 hours or 3 days seperated by space. (Ex: 10 234 21 10)"))
        self.label_3.setText(_translate("MainWindow", "- Choose the prediction mode (daily or hourly). (Ex: Hourly Prediction)"))
        self.label_4.setText(_translate("MainWindow", "- Choose location you want to predict. (Ex: Abuja)"))
        self.predict_mod.setItemText(0, _translate("MainWindow", "Hourly prediction"))
        self.predict_mod.setItemText(1, _translate("MainWindow", "Daily Prediction"))
        self.pushButton.setText(_translate("MainWindow", "Predict"))
        self.predict_location.setItemText(0, _translate("MainWindow", "Abuja"))
        self.predict_location.setItemText(1, _translate("MainWindow", "Lagos"))
        self.predict_location.setItemText(2, _translate("MainWindow", "Bauchi"))
        self.predict_location.setItemText(3, _translate("MainWindow", "Enugu"))
        self.predict_location.setItemText(4, _translate("MainWindow", "Porthacourt"))
        self.predict_location.setItemText(5, _translate("MainWindow", "Anyigba"))
        self.solar_result.setText(_translate("MainWindow", ""))
        self.air_result.setText(_translate("MainWindow", ""))
        self.relative_result.setText(_translate("MainWindow", ""))
        self.pressure_result.setText(_translate("MainWindow", ""))
        self.label_9.setText(_translate("MainWindow", "4 Values of Day (hour) 1"))
        self.label_10.setText(_translate("MainWindow", "4 Values of Day (hour) 2"))
        self.label_11.setText(_translate("MainWindow", "4 Values of Day (hour) 3"))
        self.label_12.setText(_translate("MainWindow", "Prediction mode"))
        self.label_13.setText(_translate("MainWindow", "Location"))
        self.solar_text.setText(_translate("MainWindow", "SOLAR RADIATION"))
        self.air_text.setText(_translate("MainWindow", "AIR TEMPERATURE"))
        self.relative_text.setText(_translate("MainWindow", "RELATIVE HUMIDITY"))
        self.pressure_text.setText(_translate("MainWindow", "PRESSURE"))
        self.message_result.setText(_translate("MainWindow", ""))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">©</span><span style=\" font-size:10pt; font-weight:600; font-style:italic;\">Aristide Mima</span></p></body></html>"))
