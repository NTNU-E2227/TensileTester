#from  pyqtgraph.flowchart import Flowchart
#from pyqtgraph import PlotWidget
from turtle import color, screensize
from designerfiles.mainWindow import *
#from designerfiles.geometricDialog import *
#from designerfiles.resetgraphDialog import *
from designerfiles.geometricDialog import Ui_Dialog as geo_Ui_Dialog
from designerfiles.resetgraphDialog import Ui_Dialog as graph_Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
import numpy as np
import service.backend as backend
from PyQt5.QtCore import QObject, QThread, pyqtSignal

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)    #use highdpi icons

class stressWorker(QObject):
    newData = pyqtSignal(list)

    def run(self):
        generator = backend.stressPlot_generator()
        while True:
            d = next(generator)
            self.newData.emit(d)


class extendWindow(Ui_MainWindow,QtWidgets.QWidget):
    direction = "l"
    motorRunning = False
    stressDataX = []
    stressDataY = []
    forceDataX = []
    forceDataY = []
    def __init__(self):
        super().__init__()     
        self.setupUi(MainWindow)

        ## ------ ResetGraph dialog init ------ ##
        self.resetgraphDialog = QtWidgets.QDialog()
        self.reset_Ui = graph_Ui_Dialog() #Ui_Dialog()
        self.reset_Ui.setupUi(self.resetgraphDialog)
        self.resetgraphDialog.setWindowTitle("Warning")
        self.resetgraphDialog.setWindowIcon(QtGui.QIcon("resources/icon.svg"))

        ## ------ GeometricData dialog init ------ ##
        self.geometricDialog = QtWidgets.QDialog()
        self.geo_Ui = geo_Ui_Dialog() # Ui_Dialog()
        self.geo_Ui.setupUi(self.geometricDialog)
        self.geometricDialog.setWindowTitle("Set Geometric Data")
        self.geometricDialog.setWindowIcon(QtGui.QIcon("resources/icon.svg"))

        ## ------ Buttonfunctions ------ ##
        self.startButton.clicked.connect(self.start_func)
        self.stopButton.clicked.connect(self.stop_func)
        self.tensileButton.clicked.connect(self.tensile_func)
        self.compressButton.clicked.connect(self.compress_func)
        self.actionGeometry.triggered.connect(self.geometricWindow)
        self.resetGraphButton.clicked.connect(self.resetgraphWindow)
        self.reset_Ui.yesButton.clicked.connect(self.resetgraphPlot)
        self.reset_Ui.noButton.clicked.connect(self.resetgraphDialog.close)
        self.actionReset_ADC.triggered.connect(backend.reset)
        

        ## ------ Read/Write Data ------ ##
        self.RWmaxForce.editingFinished.connect(self.writeUpdate)
        self.RWtensileSpeed.editingFinished.connect(self.writeUpdate)
        self.RWlengthRange.editingFinished.connect(self.writeUpdate)
        self.RWinitialForce.editingFinished.connect(self.writeUpdate)

        #### --- StressGraph setup --- ####
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
        
        #### --- ForceGraph setup --- ####
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



        ## --- Set program icon --- ##
        MainWindow.setWindowIcon(QtGui.QIcon("resources/icon.svg"))
        MainWindow.setWindowTitle("Hovedvindu - Strekktest")    

        ## --- Find ready COM-ports --- ##
        coms = backend.port_ready()
        for i in range(len(coms)):
            self.menuCOM_Port.addAction(coms[i])
            

        self.sThread = QThread()
        self.generator = stressWorker()
        self.generator.moveToThread(self.sThread)
        self.sThread.started.connect(self.generator.run)
        self.generator.newData.connect(self.graphPlot)
        self.sThread.start()

    def graphPlot(self, data):
        self.stressDataX.append(data[0])
        self.stressDataY.append(data[1])
        self.stressPlotWidgetCurve.setData(self.stressDataX,self.stressDataY)
        self.forceDataX.append(data[2])
        self.forceDataY.append(data[3])
        self.forcePlotWidgetCurve.setData(self.forceDataX,self.forceDataY)

    def resetgraphPlot(self):
        self.stressDataX = []
        self.stressDataY = []
        self.forceDataX = []
        self.forceDataY = []
        self.stressPlotWidgetCurve.setData(self.stressDataX,self.stressDataY)
        self.forcePlotWidgetCurve.setData(self.forceDataX,self.forceDataY)
        self.resetgraphDialog.close()

    def writeUpdate(self):
        if self.motorRunning:
            backend.run_motor(self.direction,self.RWtensileSpeed.value())

    def geometricWindow(self):
        #self.geometricDialog = QtWidgets.QDialog()
        #self.geometricDialog.setWindowIcon(QtGui.QIcon("icon.svg"))
        #self.ui = geo_Ui_Dialog() # Ui_Dialog()
        #self.ui.setupUi(self.geometricDialog)
        self.geometricDialog.show()

    def resetgraphWindow(self):
        #self.resetgraphDialog = QtWidgets.QDialog()
        #self.resetgraphDialog.setWindowIcon(QtGui.QIcon("icon.svg"))
        #self.ui = graph_Ui_Dialog() #Ui_Dialog()
        #self.ui.setupUi(self.resetgraphDialog)
        self.resetgraphDialog.show()
        
    def start_func(self):
        self.motorRunning = True    
        self.startButton.setStyleSheet('background-color :  #03818a')
        self.stopButton.setStyleSheet('background-color : rgb(70, 70, 70)')
        backend.run_motor(self.direction,self.RWtensileSpeed.value())

    def stop_func(self):
        self.motorRunning = False
        self.stopButton.setStyleSheet('background-color : #03818a')#rgb(60, 60, 60)')#color="#03818a"
        self.startButton.setStyleSheet('background-color : rgb(70, 70, 70)')
        backend.stop_motor()

    def tensile_func(self):
        self.direction = "l"
        self.tensileButton.setStyleSheet('background-color : #03818a')#rgb(60, 60, 60)')#color="#03818a"
        self.compressButton.setStyleSheet('background-color : rgb(70, 70, 70)')
        if self.motorRunning:
            backend.run_motor(self.direction,self.RWtensileSpeed.value())

    def compress_func(self):
        self.direction = "u"
        self.compressButton.setStyleSheet('background-color : #03818a')#rgb(60, 60, 60)')#color="#03818a"
        self.tensileButton.setStyleSheet('background-color : rgb(70, 70, 70)')
        if self.motorRunning:
            backend.run_motor(self.direction,self.RWtensileSpeed.value())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = extendWindow()
    MainWindow.show()
    sys.exit(app.exec_())