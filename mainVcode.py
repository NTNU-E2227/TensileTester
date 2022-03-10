from turtle import color, screensize
from mainWindow import *
from PyQt5 import QtCore, QtGui, QtWidgets
from  pyqtgraph.flowchart import Flowchart
from pyqtgraph import PlotWidget
import pyqtgraph as pg
import numpy as np
import tmp
from PyQt5.QtCore import QObject, QThread, pyqtSignal

class stressWorker(QObject):
    newData = pyqtSignal(float,float)

    def run(self):
        generator = tmp.plot_generator()
        while True:
            d = next(generator)
            self.newData.emit(d[0],d[1])


class extendWindow(Ui_MainWindow):
    direction = "l"
    motorRunning = False
    stressDataX = []
    stressDataY = []
    def __init__(self):
        super().__init__()     
        self.setupUi(MainWindow)
        
        ## ------ Buttonfunctions ------ ##
        self.startButton.clicked.connect(self.start_func)
        self.stopButton.clicked.connect(self.stop_func)
        self.tensileButton.clicked.connect(self.tensile_func)
        self.compressButton.clicked.connect(self.compress_func)

        ## ------ Read/Write Data ------ ##
        self.RWmaxForce.editingFinished.connect(self.writeUpdate)
        self.RWtensileSpeed.editingFinished.connect(self.writeUpdate)
        self.RWlengthRange.editingFinished.connect(self.writeUpdate)
        self.RWinitialForce.editingFinished.connect(self.writeUpdate)
        

        #self.graphbutton = QtWidgets.QPushButton(self.stressWidget)
        #self.graphbutton.setObjectName('test')
        #self.graphbutton.setMinimumSize(QtCore.QSize(0, 25))
        #self.gridLayout_6.addWidget(self.graphbutton, 1, 1, 1, 1)
        #self.gridLayout_3.addWidget(self.saveGraphButton, 9, 0, 1, 1)
        #self.graphbutton.raise_()
        #self.startButton.clicked.connect(self.startButtonclicked)

        ## -------- Add graph ---------- ##
        ## Create flowchart, define input/output terminals
        #fc = Flowchart(terminals={
        #    'dataIn': {'io': 'in'},
        #    'dataOut': {'io': 'out'}    
        #})
        #w = fc.widget()
        #self.gridLayout_6.addWidget(w, 1, 1, 1, 1)
        ################################################

        x = np.arange(1000)
        y = np.random.normal(size=(3, 1000))
        #plotWidget = pg.plot(title="Three plot curves")
        
        
        #self.graphWdiget = pg.PlotWidget(viewBox = pg.ViewBox(border = pg.mkPen(color='#000000'))
        self.graphWdiget = pg.PlotWidget()
        self.graphWdiget.setBackground(background= (33, 33, 33))
        self.graphWdiget.setRange(xRange=(0,100), yRange=(0,100))
        #self.graphWdiget.plot(x, y[2], pen=(4,3))
        
        self.gridLayout_6.addWidget(self.graphWdiget, 1, 1, 1, 1)
        
        
        #print(screensize())
        
        ###############################################
        #self.qView = pg.GraphicsView()

        self.sThread = QThread()
        self.generator = stressWorker()
        self.generator.moveToThread(self.sThread)
        self.sThread.started.connect(self.generator.run)
        self.generator.newData.connect(self.stressGraphPlot)
        self.sThread.start()

    def stressGraphPlot(self, x,y):
        self.stressDataX.append(x)
        self.stressDataY.append(y)
        self.graphWdiget.plot(self.stressDataX, self.stressDataY, pen=(4,3))
        
    def writeUpdate(self):
        if self.motorRunning:
            tmp.run_motor(self.direction,self.RWtensileSpeed.value())

        

    def start_func(self):
        self.motorRunning = True
        tmp.run_motor(self.direction,self.RWtensileSpeed.value())
        self.graphWdiget.plot(self.stressDataX, self.stressDataY, pen=(4,3))

    def stop_func(self):
        self.motorRunning = False
        tmp.stop_motor()

    def tensile_func(self):
        self.direction = "l"
        if self.motorRunning:
            tmp.run_motor(self.direction,self.RWtensileSpeed.value())


    def compress_func(self):
        self.direction = "u"
        if self.motorRunning:
            tmp.run_motor(self.direction,self.RWtensileSpeed.value())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = extendWindow()
    MainWindow.show()
    sys.exit(app.exec_())