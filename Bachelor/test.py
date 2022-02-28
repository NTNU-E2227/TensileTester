
from PyQt5 import QtWidgets,QtCore, uic
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
from PyQt5.QtCore import QTimer,QDateTime
import os
import threading 
import time




class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        #Load the UI Page
        uic.loadUi('Bachelor.ui', self) 

        self.pushButton_2.clicked.connect(self.ploting)
        self.pushButton_3.clicked.connect(self.reset_action)

        

    def ploting(self):
        self.counter = 0
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start(0)
        

    def update_plot_data(self):
        
        for i in range(10):
                       
            x = [i]
            y = [i]
            self.graphicsView.plot(x,y)
        #self.graphicsView_2.plot(x,y)
        



    def reset_action(self):        
        self.graphicsView.clear()
        self.graphicsView_2.clear()       
    


def main():

    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()