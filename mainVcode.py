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


class extendWindow(Ui_MainWindow,QtWidgets.QWidget):
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
        

        ## -------- Add graph ---------- ##
        #self.graphWdiget = pg.PlotWidget()
        #self.graphWdiget.setBackground(background= (33, 33, 33))
        #self.graphWdiget.setRange(xRange=(0,100), yRange=(0,100))
        #self.gridLayout_6.addWidget(self.graphWdiget, 1, 1, 1, 1)

        #### --- Newest graph setup --- ####
        self.stressPlothWidget = pg.PlotWidget()
        self.stressPlothWidget.setBackground((33,33,33))
        
        font=QtGui.QFont()
        font.setPixelSize(12)
        self.stressPlothWidget.getAxis("bottom").tickFont = font
        self.stressPlothWidget.getAxis("bottom").setStyle(tickTextOffset = 8)
        self.stressPlothWidget.setLabel('bottom', "<span style=\"color:#FFFFFF;font-size:20px\">"+"ɛ"+"</span>")
              
        self.stressPlothWidget.getAxis("left").tickFont = font
        self.stressPlothWidget.getAxis("left").setStyle(tickTextOffset = 8)
        self.stressPlothWidget.setLabel('left', "<span style=\"color:#FFFFFF;font-size:20px\">"+"δ [MPa]"+"</span>")
        
        self.stressPlothWidget.showGrid(x=1,y=1,alpha=0.8)
        self.stressPlothWidget.setTitle("<span style=\"color:#FFFFFF;font-size:20px\">"+"Stress Graph"+"</span>")
        # --------------------------------------------------------------------- #
        self.stressPlotWidgetCurve = pg.PlotCurveItem(pen=pg.mkPen(color="#03818a", width=2))
        self.stressPlothWidget.addItem(self.stressPlotWidgetCurve)
        self.gridLayout_6.addWidget(self.stressPlothWidget,0,0,1,1)
        #self.gridLayout_10.addWidget(self.stressPlothWidget,0,0,1,1)  <--- gridlayout til Forcegraf
        ###############################################
        self.forcePlothWidget = pg.PlotWidget()
        self.forcePlothWidget.setBackground((33,33,33))
        
        font=QtGui.QFont()
        font.setPixelSize(12)
        self.forcePlothWidget.getAxis("bottom").tickFont = font
        self.forcePlothWidget.getAxis("bottom").setStyle(tickTextOffset = 8)
        self.forcePlothWidget.setLabel('bottom', "<span style=\"color:#FFFFFF;font-size:20px\">"+"L [μm]"+"</span>")
              
        self.forcePlothWidget.getAxis("left").tickFont = font
        self.forcePlothWidget.getAxis("left").setStyle(tickTextOffset = 8)
        self.forcePlothWidget.setLabel('left', "<span style=\"color:#FFFFFF;font-size:20px\">"+"F [N]"+"</span>")
        
        self.forcePlothWidget.showGrid(x=1,y=1,alpha=0.8)
        self.forcePlothWidget.setTitle("<span style=\"color:#FFFFFF;font-size:20px\">"+"Force Graph"+"</span>")
        # --------------------------------------------------------------------- #
        self.forcePlotWidgetCurve = pg.PlotCurveItem(pen=pg.mkPen(color="#03818a", width=2))
        self.forcePlothWidget.addItem(self.forcePlotWidgetCurve)
        self.gridLayout_7.addWidget(self.forcePlothWidget,0,0,1,1)
        #self.gridLayout_10.addWidget(self.stressPlothWidget,0,0,1,1)  <--- gridlayout til Forcegraf
        
        ## --- Autoadjust minimum size widgets -- ##
        screen_resolution = app.desktop().screenGeometry()
        height, width = screen_resolution.height(), screen_resolution.width()
        print(height)
        print(width)
        MainWindow.setMinimumSize(((0.6)*width), ((0.6)*height))
        #self.TitleBox.setMinimumWidth() 

        ## --- Set program icon --- ##
        MainWindow.setWindowIcon(QtGui.QIcon("icon.png"))
        MainWindow.setWindowTitle("Hovedvindu - Strekktest")    

        self.sThread = QThread()
        self.generator = stressWorker()
        self.generator.moveToThread(self.sThread)
        self.sThread.started.connect(self.generator.run)
        self.generator.newData.connect(self.stressGraphPlot)
        self.sThread.start()

    def stressGraphPlot(self, x, y):
        self.stressDataX.append(x)
        self.stressDataY.append(y)
        self.stressPlotWidgetCurve.setData(self.stressDataX,self.stressDataY)
        self.forcePlotWidgetCurve.setData(self.stressDataX,self.stressDataY)
        #self.graphWdiget.plot(self.stressDataX, self.stressDataY, pen=(4,3))

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