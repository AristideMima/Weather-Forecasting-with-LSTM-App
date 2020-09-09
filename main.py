
# This is the welcome file
#
# Created by: artidemima aristidemima@gmail.com
#
# Enjoy the code

import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from main_app import Ui_Loading
from prediction__app import Ui_MainWindow


#Global variable
#Counter: to count loading of our application
counter = 0


class MainApp(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

class LAUNCH_CLASS(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Loading()
        self.ui.setupUi(self)


        #Remove Title Bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        #Drop Shadow Effect
        self.shadow =  QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.frame.setGraphicsEffect(self.shadow)

        ## QTIME
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)

        self.timer.start(35)

        #Change Text

        self.ui.label.setText("Welcome in my weather prediction application")


        QtCore.QTimer.singleShot(1500, lambda: self.ui.label.setText("<i>Loading Abuja Model</i>"))
        QtCore.QTimer.singleShot(2000, lambda: self.ui.label.setText("<i>Loading Lagos Model</i>"))
        QtCore.QTimer.singleShot(2500, lambda: self.ui.label.setText("<i>Loading Bauchi Model</strong>"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label.setText("<i>Loading Enugu Model</i>"))
        QtCore.QTimer.singleShot(3500, lambda: self.ui.label.setText("<i>Loading Porthacourt Model</i>"))
        QtCore.QTimer.singleShot(4000, lambda: self.ui.label.setText("<i>Loading Anyigba Model</i>"))


        # Show main window
        self.show()

    def progress(self):

        global counter

        #Set Value to progressBar
        self.ui.progressBar.setValue(counter)

        # Close Loading App

        if counter > 100:

            #Stop Time
            self.timer.stop()

            #Show Main Window
            self.main = MainApp()
            self.main.show()

            #Close
            self.close()

        #Increase Counter
        counter +=1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LAUNCH_CLASS()
    sys.exit(app.exec())