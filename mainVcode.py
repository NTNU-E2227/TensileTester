from time import sleep
from turtle import color, screensize
from designerfiles.mainWindow import *
from designerfiles.geometricDialog import Ui_Dialog as geo_Ui_Dialog
from designerfiles.resetgraphDialog import Ui_Dialog as graph_Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
import service.backend as backend
from PyQt5.QtCore import QObject, QThread, pyqtSignal


QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)    #use highdpi icons

class stressWorker(QObject):#[ES]
    updatePort = pyqtSignal(bool)
    newData = pyqtSignal(bool)
    def __init__(self, s):
        super().__init__()
        self.source = s

    def run(self):
        generator = self.source.generator()
        while True:
            if next(generator):
                self.newData.emit(True)
            else:
                self.updatePort.emit(False)

class extendWindow(Ui_MainWindow,QtWidgets.QWidget):
    def __init__(self): #[JBT,ES,ØLS]
        super().__init__()     
        self.setupUi(MainWindow)
        self.mcu = backend.com_obj()

        ## ------ ResetGraph dialog init ------ ## 
        self.resetgraphDialog = QtWidgets.QDialog()
        self.resetgraphDialog.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint,False)
        self.resetgraphDialog.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        self.resetgraphDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        self.reset_Ui = graph_Ui_Dialog() 
        self.reset_Ui.setupUi(self.resetgraphDialog)
        self.resetgraphDialog.setWindowTitle("Warning")
        self.resetgraphDialog.setWindowIcon(QtGui.QIcon("resources/icon.svg"))

        ## ------ GeometricData dialog init ------ ##
        self.geometricDialog = QtWidgets.QDialog()
        self.geometricDialog.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint,False)
        self.geometricDialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowTitleHint)
        self.geo_Ui = geo_Ui_Dialog() 
        self.geo_Ui.setupUi(self.geometricDialog)
        self.geometricDialog.setWindowTitle("Set Geometric Data")
        self.geometricDialog.setWindowIcon(QtGui.QIcon("resources/icon.svg"))

        ## ------ Buttonfunctions ------ ##
        self.startButton.clicked.connect(self.start_func)
        self.stopButton.clicked.connect(self.stop_func)
        self.tensileButton.clicked.connect(self.tensile_func)
        self.compressButton.clicked.connect(self.compress_func)
        self.resetGraphButton.clicked.connect(self.resetgraphWindow)
        self.reset_Ui.yesButton.clicked.connect(self.resetgraphPlot)
        self.reset_Ui.noButton.clicked.connect(self.resetgraphDialog.close)
        self.setZeroButton.clicked.connect(self.mcu.set_length_zero)
        self.dataloggingButton.clicked.connect(self.dataLogging)
        self.actionGeometry.triggered.connect(self.geometricWindow)
        self.actionReset_ADC.triggered.connect(self.mcu.adc_reset)
        self.actionExport.triggered.connect(self.exportSave)
        
        ## ------ Read/Write Data ------ ##
        self.RWmaxForce.editingFinished.connect(self.writeUpdate)
        self.RWtensileSpeed.editingFinished.connect(self.writeUpdate)
        self.RWlengthRange.editingFinished.connect(self.writeUpdate)
        self.strengthRangeCbox.currentTextChanged.connect(self.strengthRange)

        ## ------ Geometric Data ------- ##
        self.geo_Ui.RWL0.editingFinished.connect(self.geometric_update)
        self.geo_Ui.RWL1.editingFinished.connect(self.geometric_update)
        self.geo_Ui.RWH0.editingFinished.connect(self.geometric_update)
        self.geo_Ui.RWH1.editingFinished.connect(self.geometric_update)
        self.geo_Ui.RWE0.editingFinished.connect(self.geometric_update)

        #### --- StressGraph setup --- ####
        self.stressPlothWidget = pg.PlotWidget()
        self.stressPlothWidget.setBackground((33,33,33))
        
        font=QtGui.QFont()
        font.setPixelSize(12)
        self.stressPlothWidget.getAxis('top').setStyle(showValues=False)
        self.stressPlothWidget.setLabel('top', text=' ')
        
        self.stressPlothWidget.getAxis('right').setStyle(showValues=False)
        self.stressPlothWidget.setLabel('right', text=' ')

        self.stressPlothWidget.getAxis("bottom").tickFont = font
        self.stressPlothWidget.getAxis("bottom").setStyle(tickTextOffset = 8)
        self.stressPlothWidget.setLabel('bottom', "<span style=\"color:#FFFFFF;font-size:20px\">"+"ɛ"+"</span>")
              
        self.stressPlothWidget.getAxis("left").tickFont = font
        self.stressPlothWidget.getAxis("left").setStyle(tickTextOffset = 8)
        self.stressPlothWidget.setLabel('left', "<span style=\"color:#FFFFFF;font-size:20px\">"+"σ [MPa]"+"</span>")
        
        self.stressPlothWidget.showGrid(x=1,y=1,alpha=0.8)
        self.stressPlothWidget.setYRange(0, 3000/(self.mcu.conf["E0"]*self.mcu.conf["H0"]), padding=0.03)
        self.stressPlothWidget.setXRange(0, 1500 / (self.mcu.conf["L0"] * 1e3), padding=0.01)
        
        self.stressPlotWidgetCurve = pg.PlotCurveItem(pen=pg.mkPen(color="#03818a", width=2))
        self.stressPlothWidget.addItem(self.stressPlotWidgetCurve)
        self.gridLayout_9.addWidget(self.stressPlothWidget,0,0,1,1)
        
        #### --- ForceGraph setup --- ####
        self.forcePlothWidget = pg.PlotWidget()
        self.forcePlothWidget.setBackground((33,33,33))
          
        font=QtGui.QFont()
        font.setPixelSize(12)
        self.forcePlothWidget.getAxis('top').setStyle(showValues=False)
        self.forcePlothWidget.setLabel('top', text=' ')
        
        self.forcePlothWidget.getAxis('right').setStyle(showValues=False)
        self.forcePlothWidget.setLabel('right', text=' ')

        self.forcePlothWidget.getAxis("bottom").tickFont = font
        self.forcePlothWidget.getAxis("bottom").setStyle(tickTextOffset = 8)
        self.forcePlothWidget.setLabel('bottom', "<span style=\"color:#FFFFFF;font-size:20px\">"+"L [μm]"+"</span>")
              
        self.forcePlothWidget.getAxis("left").tickFont = font
        self.forcePlothWidget.getAxis("left").setStyle(tickTextOffset = 8)
        self.forcePlothWidget.setLabel('left', "<span style=\"color:#FFFFFF;font-size:20px\">"+"F [N]"+"</span>")
        
        self.forcePlothWidget.showGrid(x=1,y=1,alpha=0.8)
        self.forcePlothWidget.setXRange(0, 1500, padding=0.01)
        self.forcePlothWidget.setYRange(0, 3000, padding=0.03)

        self.forcePlotWidgetCurve = pg.PlotCurveItem(pen=pg.mkPen(color="#03818a", width=2))
        self.forcePlothWidget.addItem(self.forcePlotWidgetCurve)
        self.gridLayout_10.addWidget(self.forcePlothWidget,0,0,1,1)
        
        ## --- Set program icon --- ##
        MainWindow.setWindowIcon(QtGui.QIcon("resources/icon.svg"))
        MainWindow.setWindowTitle("Tensile testing")    

        ## --- Set COM-ports  --- ##
        self.updatePortSelector()
 
        self.sThread = QThread()
        self.generator = stressWorker(self.mcu)
        self.generator.moveToThread(self.sThread)
        self.sThread.started.connect(self.generator.run)
        self.generator.newData.connect(self.graphPlot)
        self.generator.updatePort.connect(self.updatePortSelector)
        self.sThread.start()

        ## --- Startup actions  --- ##
        self.stop_func() 
        self.compress_func()

    def strengthRange(self):#[JBT,ES]
        d = self.strengthRangeCbox.currentText()
        if d == "S1 - 3KN":
            self.mcu.sRange = "1"
            self.forcePlothWidget.setYRange(0, 3000, padding=0.03)
            self.stressPlothWidget.setYRange(0, 3000/(self.mcu.conf["E0"]*self.mcu.conf["H0"]), padding=0.03)
        elif d == "S2 - 5KN":
            self.mcu.sRange = "2"
            self.forcePlothWidget.setYRange(0, 5000, padding=0.03)
            self.stressPlothWidget.setYRange(0, 5000/(self.mcu.conf["E0"]*self.mcu.conf["H0"]), padding=0.03)
        elif d == "S3 - 10KN":
            self.mcu.sRange = "3"
            self.forcePlothWidget.setYRange(0, 10000, padding=0.03)
            self.stressPlothWidget.setYRange(0, 10000/(self.mcu.conf["E0"]*self.mcu.conf["H0"]), padding=0.03)

    def updatePortSelector(self):#[JBT,ES]
        if self.mcu.update_ports():
            self.action_group = QtWidgets.QActionGroup(self)
            self.action_group.setExclusive(True)
            self.menuCOM_Port.clear()
            for port in sorted(self.mcu.portList):
                action = QtWidgets.QAction(port, self)
                action.setCheckable(True)
                if self.mcu.port != None and port == self.mcu.port.name:
                    action.setChecked(True)
                self.menuCOM_Port.addAction(action)
                self.action_group.addAction(action)
            self.action_group.triggered.connect(self.updateportSelect)



    def exportSave(self):#[JBT]
        exportDialog = QtWidgets.QFileDialog.getSaveFileName(MainWindow, 'Save File','', 'CSV files (*.csv)')
        if not exportDialog[0] == '':
            self.mcu.export(exportDialog[0])
              
    def updateportSelect(self, action):#[JBT,ØLS]
        self.mcu.set_port(action.text())

    def graphPlot(self):#[JBT,ES,ØLS]
        self.timeRead.setValue(int(self.mcu.latest_data[0]))
        self.lengthRead.setValue(int(self.mcu.latest_data[1]))
        self.forceRead.setValue(int(self.mcu.latest_data[2]))
        self.espilonRead.setValue(self.mcu.latest_data[3])
        self.stressRead.setValue(int(self.mcu.latest_data[4]))
        if self.RWlengthRange.value() != 0 and abs(self.mcu.latest_data[1]) > self.RWlengthRange.value():
            self.stop_func() 
        if self.RWmaxForce.value() != 0 and (self.mcu.latest_data[2]) > self.RWmaxForce.value():
            self.stop_func() 
        if self.mcu.datalog:
            self.forcePlotWidgetCurve.setData(self.mcu.datalist[1],self.mcu.datalist[2])
            self.stressPlotWidgetCurve.setData(self.mcu.datalist[3],self.mcu.datalist[4])
            
    def resetgraphPlot(self):#[JBT,ES,ØLS]
        self.mcu.reset_data()
        self.mcu.set_time_zero()
        self.stressPlotWidgetCurve.setData(self.mcu.datalist[1],self.mcu.datalist[2])
        self.forcePlotWidgetCurve.setData(self.mcu.datalist[3],self.mcu.datalist[4])
        self.resetgraphDialog.close()

    def writeUpdate(self):#[JBT]
        self.mcu.set_speed(self.RWtensileSpeed.value())

    def geometricWindow(self):#[JBT,ØLS]
        self.geo_Ui.RWH0.setValue(self.mcu.conf["H0"])
        self.geo_Ui.RWH1.setValue(self.mcu.conf["H1"])
        self.geo_Ui.RWL0.setValue(self.mcu.conf["L0"])
        self.geo_Ui.RWL1.setValue(self.mcu.conf["L1"])
        self.geo_Ui.RWE0.setValue(self.mcu.conf["E0"])
        
        self.geometricDialog.show()
    
    def geometric_update(self):#[JBT,ØLS]
        self.mcu.conf["H0"] = self.geo_Ui.RWH0.value()
        self.mcu.conf["H1"] = self.geo_Ui.RWH1.value()
        self.mcu.conf["L0"] = self.geo_Ui.RWL0.value()
        self.mcu.conf["L1"] = self.geo_Ui.RWL1.value()
        self.mcu.conf["E0"] = self.geo_Ui.RWE0.value()

    def dataLogging(self):#[ES]
        if self.mcu.datalog:
            self.mcu.datalog = False
            self.dataloggingButton.setStyleSheet('background-color : rgb(70, 70, 70)')
        else:
            self.mcu.datalog = True
            self.dataloggingButton.setStyleSheet('background-color :  #03818a')

    def resetgraphWindow(self):#[JBT]
        self.resetgraphDialog.show()
        
    def start_func(self):#[JBT,ES,ØLS]
        self.startButton.setStyleSheet('background-color :  #03818a')
        self.stopButton.setStyleSheet('background-color : rgb(70, 70, 70)')
        self.mcu.motor_run()

    def stop_func(self):#[JBT,ES,ØLS]
        self.stopButton.setStyleSheet('background-color : #03818a')
        self.startButton.setStyleSheet('background-color : rgb(70, 70, 70)')
        if self.mcu.port != None:
            self.mcu.motor_stop()

    def tensile_func(self):#[JBT,ES,ØLS]
        self.mcu.set_direction(b'l')
        self.tensileButton.setStyleSheet('background-color : #03818a')
        self.compressButton.setStyleSheet('background-color : rgb(70, 70, 70)')

    def compress_func(self):#[JBT,ES,ØLS]
        self.mcu.set_direction(b'u')
        self.compressButton.setStyleSheet('background-color : #03818a')
        self.tensileButton.setStyleSheet('background-color : rgb(70, 70, 70)')

    
if __name__ == "__main__":#[JBT]
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = extendWindow()
    app.aboutToQuit.connect(ui.stop_func)
    MainWindow.showMaximized()
    sys.exit(app.exec_())
