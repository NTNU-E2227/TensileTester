from time import sleep
from turtle import color, screensize
from designerfiles.mainWindow import *
from designerfiles.geometricDialog import Ui_Dialog as geo_Ui_Dialog
from designerfiles.resetgraphDialog import Ui_Dialog as graph_Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
import service.config as config
import pyqtgraph as pg
import service.backend as backend
from PyQt5.QtCore import QObject, QThread, pyqtSignal
import serial.tools.list_ports


QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)    #use highdpi icons

class stressWorker(QObject):
    newData = pyqtSignal(bool)
    def __init__(self, s):
        super().__init__()
        self.source = s

    def run(self):
        generator = self.source.generator()
        while True:
            self.newData.emit( next(generator) )

class extendWindow(Ui_MainWindow,QtWidgets.QWidget):
    def __init__(self):
        super().__init__()     
        self.setupUi(MainWindow)
        self.mcu = backend.com_obj()


        ## ------ ResetGraph dialog init ------ ##
        self.resetgraphDialog = QtWidgets.QDialog()
        self.resetgraphDialog.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        self.resetgraphDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        self.reset_Ui = graph_Ui_Dialog() #Ui_Dialog()
        self.reset_Ui.setupUi(self.resetgraphDialog)
        self.resetgraphDialog.setWindowTitle("Warning")
        self.resetgraphDialog.setWindowIcon(QtGui.QIcon("resources/icon.svg"))

        ## ------ GeometricData dialog init ------ ##
        self.geometricDialog = QtWidgets.QDialog()
        self.geometricDialog.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint,False)
        self.geo_Ui = geo_Ui_Dialog() # Ui_Dialog()
        self.geometricDialog.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
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
        self.actionReset_ADC.triggered.connect(self.mcu.adc_reset)
        self.setZeroButton.clicked.connect(self.mcu.set_length_zero)
        self.actionExport.triggered.connect(self.saveFile)
        

        ## ------ Read/Write Data ------ ##
        self.RWmaxForce.editingFinished.connect(self.writeUpdate)
        self.RWtensileSpeed.editingFinished.connect(self.writeUpdate)
        self.RWlengthRange.editingFinished.connect(self.writeUpdate)
        self.RWinitialForce.editingFinished.connect(self.writeUpdate)

        ## ------ Geometric Data ------- ##
        self.geo_Ui.RWL0.editingFinished.connect(self.geometric_updtate)
        self.geo_Ui.RWL1.editingFinished.connect(self.geometric_updtate)
        self.geo_Ui.RWH0.editingFinished.connect(self.geometric_updtate)
        self.geo_Ui.RWH1.editingFinished.connect(self.geometric_updtate)
        self.geo_Ui.RWE0.editingFinished.connect(self.geometric_updtate)

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

        ## --- Set COM-ports  --- ##
        self.action_group = QtWidgets.QActionGroup(self)
        self.action_group.setExclusive(True)
        ports = serial.tools.list_ports.comports()
        for port in sorted(ports):
            p = format(port[0])
            action = QtWidgets.QAction(p, self)
            action.setCheckable(True)
            if self.mcu.port != None and port.name == self.mcu.port.name:
                action.setChecked(True)
            self.menuCOM_Port.addAction(action)
            self.action_group.addAction(action)
        self.action_group.triggered.connect(self.updateportSelect)

        self.sThread = QThread()
        self.generator = stressWorker(self.mcu)
        self.generator.moveToThread(self.sThread)
        self.sThread.started.connect(self.generator.run)
        self.generator.newData.connect(self.graphPlot)
        self.sThread.start()

        ## --- Startup actions  --- ##
        self.stop_func() 
        self.tensile_func() 
        

    def saveFile(self):
        self.saveFileDialog = QtWidgets.QFileDialog.getSaveFileName(
            parent = self,
            caption = 'Save File')
        open(self.saveFileDialog, 'w')
        


    def updateportSelect(self, action):
        self.mcu.set_port(action.text())

    def graphPlot(self):
        self.stressPlotWidgetCurve.setData(self.mcu.datalist[1],self.mcu.datalist[2])
        self.forcePlotWidgetCurve.setData(self.mcu.datalist[3],self.mcu.datalist[4])
        self.forceRead.setValue(int(self.mcu.datalist[2][-1]))
        self.lengthRead.setValue(int(self.mcu.datalist[1][-1]))
        self.timeRead.setValue(int(self.mcu.datalist[0][-1]))

    def resetgraphPlot(self):
        self.mcu.reset_data()
        self.mcu.set_time_zero()
        self.stressPlotWidgetCurve.setData(self.mcu.datalist[1],self.mcu.datalist[2])
        self.forcePlotWidgetCurve.setData(self.mcu.datalist[3],self.mcu.datalist[4])
        self.resetgraphDialog.close()

    def writeUpdate(self):
        self.mcu.set_speed(self.RWtensileSpeed.value())

    def geometricWindow(self):
        self.geometricDialog.show()
    
    def geometric_updtate(self):
        self.mcu.conf["H0"] = self.geo_Ui.RWH0.value()
        self.mcu.conf["H1"] = self.geo_Ui.RWH1.value()
        self.mcu.conf["L0"] = self.geo_Ui.RWL0.value()
        self.mcu.conf["L1"] = self.geo_Ui.RWL1.value()
        self.mcu.conf["E0"] = self.geo_Ui.RWE0.value()

    def resetgraphWindow(self):
        self.resetgraphDialog.show()
        
    def start_func(self):
        self.startButton.setStyleSheet('background-color :  #03818a')
        self.stopButton.setStyleSheet('background-color : rgb(70, 70, 70)')
        self.mcu.motor_run_percent(self.RWtensileSpeed.value())

    def stop_func(self):
        self.stopButton.setStyleSheet('background-color : #03818a')#rgb(60, 60, 60)')#color="#03818a"
        self.startButton.setStyleSheet('background-color : rgb(70, 70, 70)')
        if self.mcu.port != None:
            self.mcu.motor_stop()

    def tensile_func(self):
        self.mcu.set_direction(b'l')
        self.tensileButton.setStyleSheet('background-color : #03818a')#rgb(60, 60, 60)')#color="#03818a"
        self.compressButton.setStyleSheet('background-color : rgb(70, 70, 70)')

    def compress_func(self):
        self.mcu.set_direction(b'u')
        self.compressButton.setStyleSheet('background-color : #03818a')#rgb(60, 60, 60)')#color="#03818a"
        self.tensileButton.setStyleSheet('background-color : rgb(70, 70, 70)')

    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = extendWindow()
    app.aboutToQuit.connect(ui.stop_func)
    MainWindow.showMaximized()
    sys.exit(app.exec_())
