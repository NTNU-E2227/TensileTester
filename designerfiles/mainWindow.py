# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):#[JBT,ØLS]
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1917, 973)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#Backround{\n"
"    background-color: rgb(40, 40, 40);\n"
"}\n"
"#Sone1{\n"
"    background-color: rgb(55, 55, 55);\n"
"}\n"
"#Sone2{\n"
"    background-color: rgb(55, 55, 55);\n"
"}\n"
"#forceGraph{\n"
"        background-color: rgb(55,55,55); \n"
"        border-radius: 4px;\n"
"}\n"
"#stressGraph{\n"
"        background-color: rgb(55,55,55); \n"
"        border-radius: 4px;\n"
"}\n"
"#TitleBox{\n"
"        background-color: rgb(55,55,55);\n"
"}\n"
"#frame{\n"
"        background-color: rgb(55,55,55); \n"
"        border-radius: 4px;\n"
"}\n"
"\n"
"\n"
"#startButton{\n"
"        background-color: rgb(70,70,70); \n"
"        border-radius: 4px;\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#startButton:pressed{\n"
"        background-color:rgb(65,65,65);\n"
"}\n"
"#stopButton{\n"
"        background-color: rgb(70,70,70); \n"
"        border-radius: 4px;\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#stopButton:pressed{\n"
"        background-color:rgb(65,65,65);\n"
"}\n"
"#tensileButton{\n"
"        background-color: rgb(70,70,70); \n"
"        border-radius: 4px;\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#tensileButton:pressed{\n"
"        background-color:rgb(65,65,65);\n"
"}\n"
"#compressButton{\n"
"        background-color: rgb(70,70,70); \n"
"        border-radius: 4px;\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#compressButton:pressed{\n"
"        background-color:rgb(65,65,65);\n"
"}\n"
"#autoZeroButton{\n"
"        background-color: rgb(70,70,70); \n"
"        border-radius: 4px;\n"
"        color: rgb(249,249,249);\n"
"}\n"
"\n"
"#strengthRangeCbox{\n"
"        background-color: rgb(70,70,70);\n"
"        border-radius: 4px;\n"
"        color: rgb(249,249,249);\n"
"}\n"
"\n"
"QListView{\n"
"        background-color: rgb(70,70,70);\n"
"        border-radius: 0px;\n"
"        color: rgb(249,249,249);\n"
"}\n"
"\n"
"#autoZeroButton:pressed{\n"
"        background-color:rgb(65,65,65);\n"
"}\n"
"#dataloggingButton{\n"
"        background-color: rgb(70,70,70); \n"
"        border-radius: 4px;\n"
"        color: rgb(249,249,249);        \n"
"}\n"
"#dataloggingButton:pressed{\n"
"        background-color:rgb(65,65,65);\n"
"}\n"
"\n"
"#resetGraphButton{\n"
"        background-color: rgb(70,70,70); \n"
"        border-radius: 4px;\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#resetGraphButton:pressed{\n"
"        background-color:rgb(65,65,65);\n"
"}\n"
"#releaseMatButton{\n"
"        background-color: rgb(70,70,70); \n"
"        border-radius: 4px;\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#releaseMatButton:pressed{\n"
"        background-color:rgb(65,65,65);\n"
"}\n"
"#saveGraphButton{\n"
"        background-color: rgb(70,70,70); \n"
"        border-radius: 4px;\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#saveGraphButton:pressed{\n"
"        background-color:rgb(65,65,65);\n"
"}\n"
"\n"
"#RWinitialForce{\n"
"        background-color: rgb(55,55,55); \n"
"        border-radius: 4px;\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#RWlengthRange{\n"
"        background-color: rgb(55,55,55); \n"
"        border-radius: 4px;\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#RWtensileSpeed{\n"
"        background-color: rgb(55,55,55); \n"
"        border-radius: 4px;\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#RWmaxForce{\n"
"        background-color: rgb(55,55,55); \n"
"        border-radius: 4px;\n"
"        color: rgb(249,249,249);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"#settingsWindow{\n"
"    background-color: rgb(232, 253, 255);\n"
"}\n"
"#directDataWindow{\n"
"    background-color: rgb(232, 253, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"#title{\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#label{\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#label_1{\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#label_2{\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#label_3{\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#label_4{\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#label_5{\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#label_6{\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#label_7{\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#label_8{\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#label_9{\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#label_10{\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#label_11{\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#label_12{\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#label_13{\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#label_14{\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#label_15{\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#label_16{\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#label_17{\n"
"        color: rgb(249,249,249);\n"
"}\n"
"\n"
"\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Backround = QtWidgets.QWidget(self.centralwidget)
        self.Backround.setStyleSheet("")
        self.Backround.setObjectName("Backround")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Backround)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.Backround)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(450, 0))
        self.frame.setMaximumSize(QtCore.QSize(450, 962))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.sone1_1 = QtWidgets.QWidget(self.frame)
        self.sone1_1.setMinimumSize(QtCore.QSize(0, 465))
        self.sone1_1.setMaximumSize(QtCore.QSize(16777215, 465))
        self.sone1_1.setObjectName("sone1_1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.sone1_1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Sone1 = QtWidgets.QWidget(self.sone1_1)
        self.Sone1.setMaximumSize(QtCore.QSize(16777215, 600))
        self.Sone1.setStyleSheet("")
        self.Sone1.setObjectName("Sone1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Sone1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget_3 = QtWidgets.QWidget(self.Sone1)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.dataloggingButton = QtWidgets.QPushButton(self.widget_3)
        self.dataloggingButton.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dataloggingButton.setFont(font)
        self.dataloggingButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dataloggingButton.setObjectName("dataloggingButton")
        self.gridLayout_12.addWidget(self.dataloggingButton, 0, 0, 1, 2)
        self.resetGraphButton = QtWidgets.QPushButton(self.widget_3)
        self.resetGraphButton.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.resetGraphButton.setFont(font)
        self.resetGraphButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.resetGraphButton.setObjectName("resetGraphButton")
        self.gridLayout_12.addWidget(self.resetGraphButton, 1, 0, 1, 2)
        self.gridLayout_3.addWidget(self.widget_3, 10, 0, 1, 2)
        self.compressButton = QtWidgets.QPushButton(self.Sone1)
        self.compressButton.setMinimumSize(QtCore.QSize(190, 25))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.compressButton.setFont(font)
        self.compressButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.compressButton.setObjectName("compressButton")
        self.gridLayout_3.addWidget(self.compressButton, 7, 1, 1, 1)
        self.startButton = QtWidgets.QPushButton(self.Sone1)
        self.startButton.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.startButton.setFont(font)
        self.startButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.startButton.setObjectName("startButton")
        self.gridLayout_3.addWidget(self.startButton, 6, 0, 1, 1)
        self.tensileButton = QtWidgets.QPushButton(self.Sone1)
        self.tensileButton.setMinimumSize(QtCore.QSize(190, 25))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.tensileButton.setFont(font)
        self.tensileButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tensileButton.setObjectName("tensileButton")
        self.gridLayout_3.addWidget(self.tensileButton, 6, 1, 1, 1)
        self.stopButton = QtWidgets.QPushButton(self.Sone1)
        self.stopButton.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.stopButton.setFont(font)
        self.stopButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stopButton.setObjectName("stopButton")
        self.gridLayout_3.addWidget(self.stopButton, 7, 0, 1, 1)
        self.widget_4 = QtWidgets.QWidget(self.Sone1)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 140))
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.widget_5 = QtWidgets.QWidget(self.widget_4)
        self.widget_5.setMaximumSize(QtCore.QSize(80, 16777215))
        self.widget_5.setObjectName("widget_5")
        self.gridLayout_13.addWidget(self.widget_5, 1, 2, 4, 1)
        self.label_3 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_13.addWidget(self.label_3, 3, 0, 1, 1)
        self.RWtensileSpeed = QtWidgets.QDoubleSpinBox(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.RWtensileSpeed.setFont(font)
        self.RWtensileSpeed.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.RWtensileSpeed.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.RWtensileSpeed.setMaximum(30.0)
        self.RWtensileSpeed.setObjectName("RWtensileSpeed")
        self.gridLayout_13.addWidget(self.RWtensileSpeed, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_13.addWidget(self.label, 2, 0, 1, 1)
        self.RWlengthRange = QtWidgets.QDoubleSpinBox(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.RWlengthRange.setFont(font)
        self.RWlengthRange.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.RWlengthRange.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.RWlengthRange.setMaximum(999999999.0)
        self.RWlengthRange.setObjectName("RWlengthRange")
        self.gridLayout_13.addWidget(self.RWlengthRange, 3, 1, 1, 1)
        self.widget_6 = QtWidgets.QWidget(self.widget_4)
        self.widget_6.setMinimumSize(QtCore.QSize(0, 10))
        self.widget_6.setObjectName("widget_6")
        self.gridLayout_13.addWidget(self.widget_6, 5, 0, 1, 3)
        self.label_10 = QtWidgets.QLabel(self.widget_4)
        self.label_10.setMinimumSize(QtCore.QSize(0, 0))
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_13.addWidget(self.label_10, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_13.addWidget(self.label_2, 1, 0, 1, 1)
        self.RWmaxForce = QtWidgets.QDoubleSpinBox(self.widget_4)
        self.RWmaxForce.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.RWmaxForce.setFont(font)
        self.RWmaxForce.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.RWmaxForce.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.RWmaxForce.setMaximum(15000.0)
        self.RWmaxForce.setObjectName("RWmaxForce")
        self.gridLayout_13.addWidget(self.RWmaxForce, 1, 1, 1, 1)
        self.widget_7 = QtWidgets.QWidget(self.widget_4)
        self.widget_7.setMinimumSize(QtCore.QSize(0, 10))
        self.widget_7.setObjectName("widget_7")
        self.gridLayout_13.addWidget(self.widget_7, 0, 0, 1, 3)
        self.strengthRangeCbox = QtWidgets.QComboBox(self.widget_4)
        self.strengthRangeCbox.setEnabled(True)
        self.strengthRangeCbox.setMinimumSize(QtCore.QSize(0, 0))
        self.strengthRangeCbox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.strengthRangeCbox.setFont(font)
        self.strengthRangeCbox.setAutoFillBackground(False)
        self.strengthRangeCbox.setDuplicatesEnabled(False)
        self.strengthRangeCbox.setFrame(True)
        self.strengthRangeCbox.setObjectName("strengthRangeCbox")
        self.strengthRangeCbox.addItem("")
        self.strengthRangeCbox.addItem("")
        self.strengthRangeCbox.addItem("")
        self.gridLayout_13.addWidget(self.strengthRangeCbox, 4, 1, 1, 1)
        self.gridLayout_3.addWidget(self.widget_4, 8, 0, 1, 2)
        self.tensileButton.raise_()
        self.compressButton.raise_()
        self.stopButton.raise_()
        self.startButton.raise_()
        self.widget_4.raise_()
        self.widget_3.raise_()
        self.gridLayout_2.addWidget(self.Sone1, 1, 0, 1, 1)
        self.title = QtWidgets.QLabel(self.sone1_1)
        font = QtGui.QFont()
        font.setFamily("Dubai")
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.gridLayout_2.addWidget(self.title, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_8.addWidget(self.sone1_1, 0, 0, 1, 1)
        self.Sone2 = QtWidgets.QWidget(self.frame)
        self.Sone2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Sone2.setStyleSheet("#timeRead{\n"
"        background-color: rgb(70,70,70); \n"
"        border-radius: 4px;\n"
"        color: rgb(249,249,249);\n"
"}\n"
"QDoubleSpinBox{\n"
"        background-color: rgb(70,70,70); \n"
"        border-radius: 4px;\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#forceRead{\n"
"        background-color: rgb(70,70,70); \n"
"        border-radius: 4px;\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#lengthRead{\n"
"        background-color: rgb(70,70,70); \n"
"        border-radius: 4px;\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#stressRead{\n"
"        background-color: rgb(70,70,70); \n"
"        border-radius: 4px;\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#resetTimeButton{\n"
"        background-color: rgb(70,70,70); \n"
"        border-radius: 4px;\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#resetTimeButton:pressed{\n"
"        background-color:rgb(65,65,65);\n"
"}\n"
"#setZeroButton{\n"
"        background-color: rgb(70,70,70); \n"
"        border-radius: 4px;\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#setZeroButton:pressed{\n"
"        background-color:rgb(65,65,65);\n"
"}\n"
"\n"
"")
        self.Sone2.setObjectName("Sone2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.Sone2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_17 = QtWidgets.QLabel(self.Sone2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout_4.addWidget(self.label_17, 0, 2, 1, 2, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.widget = QtWidgets.QWidget(self.Sone2)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 150))
        self.widget.setObjectName("widget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 0, 3, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        spacerItem = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem, 1, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_5.addWidget(self.label_6, 3, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.setZeroButton = QtWidgets.QPushButton(self.widget)
        self.setZeroButton.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(11)
        self.setZeroButton.setFont(font)
        self.setZeroButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setZeroButton.setObjectName("setZeroButton")
        self.gridLayout_5.addWidget(self.setZeroButton, 5, 1, 1, 1)
        self.timeRead = QtWidgets.QSpinBox(self.widget)
        self.timeRead.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.timeRead.setFont(font)
        self.timeRead.setAlignment(QtCore.Qt.AlignCenter)
        self.timeRead.setReadOnly(True)
        self.timeRead.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.timeRead.setMinimum(0)
        self.timeRead.setMaximum(999999999)
        self.timeRead.setObjectName("timeRead")
        self.gridLayout_5.addWidget(self.timeRead, 1, 3, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_5.addWidget(self.label_9, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_5.addWidget(self.label_8, 0, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.forceRead = QtWidgets.QSpinBox(self.widget)
        self.forceRead.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.forceRead.setFont(font)
        self.forceRead.setAlignment(QtCore.Qt.AlignCenter)
        self.forceRead.setReadOnly(True)
        self.forceRead.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.forceRead.setPrefix("")
        self.forceRead.setMinimum(-999999999)
        self.forceRead.setMaximum(999999999)
        self.forceRead.setObjectName("forceRead")
        self.gridLayout_5.addWidget(self.forceRead, 4, 0, 1, 1)
        self.lengthRead = QtWidgets.QSpinBox(self.widget)
        self.lengthRead.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.lengthRead.setFont(font)
        self.lengthRead.setAlignment(QtCore.Qt.AlignCenter)
        self.lengthRead.setReadOnly(True)
        self.lengthRead.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.lengthRead.setMinimum(-999999999)
        self.lengthRead.setMaximum(999999999)
        self.lengthRead.setObjectName("lengthRead")
        self.gridLayout_5.addWidget(self.lengthRead, 4, 1, 1, 1)
        self.stressRead = QtWidgets.QSpinBox(self.widget)
        self.stressRead.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.stressRead.setFont(font)
        self.stressRead.setAlignment(QtCore.Qt.AlignCenter)
        self.stressRead.setReadOnly(True)
        self.stressRead.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.stressRead.setMinimum(-999999999)
        self.stressRead.setMaximum(999999999)
        self.stressRead.setObjectName("stressRead")
        self.gridLayout_5.addWidget(self.stressRead, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 3, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.espilonRead = QtWidgets.QDoubleSpinBox(self.widget)
        self.espilonRead.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.espilonRead.setFont(font)
        self.espilonRead.setAlignment(QtCore.Qt.AlignCenter)
        self.espilonRead.setReadOnly(True)
        self.espilonRead.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.espilonRead.setSuffix("")
        self.espilonRead.setDecimals(3)
        self.espilonRead.setObjectName("espilonRead")
        self.gridLayout_5.addWidget(self.espilonRead, 1, 1, 1, 1)
        self.gridLayout_4.addWidget(self.widget, 1, 2, 1, 2)
        self.gridLayout_8.addWidget(self.Sone2, 4, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame)
        self.widget_2 = QtWidgets.QWidget(self.Backround)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.forceGraph = QtWidgets.QWidget(self.widget_2)
        self.forceGraph.setStyleSheet("")
        self.forceGraph.setObjectName("forceGraph")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.forceGraph)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.forceWidget = QtWidgets.QWidget(self.forceGraph)
        self.forceWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.forceWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.forceWidget.setObjectName("forceWidget")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.forceWidget)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.gridLayout_7.addWidget(self.forceWidget, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.forceGraph)
        self.stressGraph = QtWidgets.QWidget(self.widget_2)
        self.stressGraph.setMinimumSize(QtCore.QSize(600, 0))
        self.stressGraph.setStyleSheet("")
        self.stressGraph.setObjectName("stressGraph")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.stressGraph)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.stressWidget = QtWidgets.QWidget(self.stressGraph)
        self.stressWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.stressWidget.setObjectName("stressWidget")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.stressWidget)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout_6.addWidget(self.stressWidget, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.stressGraph)
        self.horizontalLayout.addWidget(self.widget_2)
        self.gridLayout.addWidget(self.Backround, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1917, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuCOM_Port = QtWidgets.QMenu(self.menuTools)
        self.menuCOM_Port.setObjectName("menuCOM_Port")
        MainWindow.setMenuBar(self.menubar)
        self.actionGeometry = QtWidgets.QAction(MainWindow)
        self.actionGeometry.setObjectName("actionGeometry")
        self.actionCOM1 = QtWidgets.QAction(MainWindow)
        self.actionCOM1.setObjectName("actionCOM1")
        self.actionCOM9 = QtWidgets.QAction(MainWindow)
        self.actionCOM9.setObjectName("actionCOM9")
        self.actionReset_ADC = QtWidgets.QAction(MainWindow)
        self.actionReset_ADC.setObjectName("actionReset_ADC")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.menuFile.addAction(self.actionExport)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.menuCOM_Port.menuAction())
        self.menuTools.addAction(self.actionGeometry)
        self.menuTools.addAction(self.actionReset_ADC)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dataloggingButton.setText(_translate("MainWindow", "Data logging"))
        self.resetGraphButton.setText(_translate("MainWindow", "Reset datalog"))
        self.compressButton.setText(_translate("MainWindow", "Release"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.tensileButton.setText(_translate("MainWindow", "Tensile"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
        self.label_3.setText(_translate("MainWindow", "Length range:"))
        self.RWtensileSpeed.setSuffix(_translate("MainWindow", " μm/s"))
        self.label.setText(_translate("MainWindow", "Tensile-speed:"))
        self.RWlengthRange.setSuffix(_translate("MainWindow", " μm"))
        self.label_10.setText(_translate("MainWindow", "Strength range:"))
        self.label_2.setText(_translate("MainWindow", "Max force:"))
        self.RWmaxForce.setSuffix(_translate("MainWindow", " N"))
        self.strengthRangeCbox.setItemText(0, _translate("MainWindow", "S1 - 3KN"))
        self.strengthRangeCbox.setItemText(1, _translate("MainWindow", "S2 - 5KN"))
        self.strengthRangeCbox.setItemText(2, _translate("MainWindow", "S3 - 10KN"))
        self.title.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:26pt; font-weight:600;\">Tensile Testing</span></p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "Direct data"))
        self.label_7.setText(_translate("MainWindow", "Time"))
        self.label_6.setText(_translate("MainWindow", "Length"))
        self.setZeroButton.setText(_translate("MainWindow", "Set zero"))
        self.timeRead.setSuffix(_translate("MainWindow", " s"))
        self.label_9.setText(_translate("MainWindow", "Stress (σ)"))
        self.label_8.setText(_translate("MainWindow", "Strain (ɛ)"))
        self.forceRead.setSuffix(_translate("MainWindow", " N"))
        self.lengthRead.setSuffix(_translate("MainWindow", " μm"))
        self.stressRead.setSuffix(_translate("MainWindow", " Mpa"))
        self.label_5.setText(_translate("MainWindow", "Force"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuCOM_Port.setTitle(_translate("MainWindow", "Port"))
        self.actionGeometry.setText(_translate("MainWindow", "Geometry"))
        self.actionCOM1.setText(_translate("MainWindow", "COM1"))
        self.actionCOM9.setText(_translate("MainWindow", "COM9"))
        self.actionReset_ADC.setText(_translate("MainWindow", "Reset ADC"))
        self.actionExport.setText(_translate("MainWindow", "Export"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
