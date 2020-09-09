# -*- coding: utf-8 -*-

# This is the launch file
#
# Created by: artidemima aristidemima@gmail.com
#
# Enjoy the code


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Loading(object):
    def setupUi(self, Loading):
        Loading.setObjectName("Loading")
        Loading.resize(626, 329)
        self.centralwidget = QtWidgets.QWidget(Loading)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 631, 331))
        self.frame.setStyleSheet("QFrame {\n"
" \n"
"    background-color: #2ab7ca ;    \n"
"    border-radius: 20px;\n"
"    color: rgb(11, 126, 136)\n"
"\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 601, 91))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(100, 110, 451, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect(90, 210, 461, 23))
        self.progressBar.setStyleSheet("QProgressBar\n"
"{\n"
"    background-color: rgb(206, 206, 206);\n"
"    border-style: none;\n"
"    color: rgb(102, 0, 153);\n"
"    text-align: center;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    border-radius: 20px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.011, y1:0.460227, x2:1, y2:0.466, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 255, 255, 255))\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(90, 240, 451, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(310, 300, 451, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        Loading.setCentralWidget(self.centralwidget)

        self.retranslateUi(Loading)
        QtCore.QMetaObject.connectSlotsByName(Loading)

    def retranslateUi(self, Loading):
        _translate = QtCore.QCoreApplication.translate
        Loading.setWindowTitle(_translate("Loading", "MainWindow"))
        self.label_2.setText(_translate("Loading", "<html><head/><body><p><span style=\" font-weight:600;\">WEATHER FORECASTING APP</span></p></body></html>"))
        self.label.setText(_translate("Loading", "Application for weather prediction over Nigeria"))
        self.label_3.setText(_translate("Loading", "Loading..."))
        self.label_4.setText(_translate("Loading", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; font-style:italic;\">Aristide Mima</span></p></body></html>"))
