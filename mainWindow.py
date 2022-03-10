# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FirstWindowV2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1917, 973)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 600))
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
"#autoZeroButton:pressed{\n"
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
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setMaximumSize(QtCore.QSize(500, 16777215))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.Sone2 = QtWidgets.QWidget(self.frame)
        self.Sone2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Sone2.setStyleSheet("#timeRead{\n"
"        background-color: rgb(70,70,70); \n"
"        border-radius: 4px;\n"
"        color: rgb(249,249,249);\n"
"}\n"
"#epsilonRead{\n"
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
        self.label_9 = QtWidgets.QLabel(self.Sone2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 4, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.setZeroButton = QtWidgets.QPushButton(self.Sone2)
        self.setZeroButton.setMinimumSize(QtCore.QSize(0, 25))
        self.setZeroButton.setObjectName("setZeroButton")
        self.gridLayout_4.addWidget(self.setZeroButton, 12, 3, 1, 1)
        self.epsilonRead = QtWidgets.QSpinBox(self.Sone2)
        self.epsilonRead.setAlignment(QtCore.Qt.AlignCenter)
        self.epsilonRead.setReadOnly(True)
        self.epsilonRead.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.epsilonRead.setObjectName("epsilonRead")
        self.gridLayout_4.addWidget(self.epsilonRead, 5, 3, 1, 1)
        self.stressRead = QtWidgets.QSpinBox(self.Sone2)
        self.stressRead.setAlignment(QtCore.Qt.AlignCenter)
        self.stressRead.setReadOnly(True)
        self.stressRead.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.stressRead.setObjectName("stressRead")
        self.gridLayout_4.addWidget(self.stressRead, 5, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 200, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_4.addItem(spacerItem, 0, 3, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.Sone2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout_4.addWidget(self.label_17, 1, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.timeRead = QtWidgets.QSpinBox(self.Sone2)
        self.timeRead.setAlignment(QtCore.Qt.AlignCenter)
        self.timeRead.setReadOnly(True)
        self.timeRead.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.timeRead.setObjectName("timeRead")
        self.gridLayout_4.addWidget(self.timeRead, 5, 5, 1, 1)
        self.lengthRead = QtWidgets.QSpinBox(self.Sone2)
        self.lengthRead.setAlignment(QtCore.Qt.AlignCenter)
        self.lengthRead.setReadOnly(True)
        self.lengthRead.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.lengthRead.setObjectName("lengthRead")
        self.gridLayout_4.addWidget(self.lengthRead, 11, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_4.addItem(spacerItem1, 2, 3, 1, 1)
        self.resetTimeButton = QtWidgets.QPushButton(self.Sone2)
        self.resetTimeButton.setMinimumSize(QtCore.QSize(0, 25))
        self.resetTimeButton.setObjectName("resetTimeButton")
        self.gridLayout_4.addWidget(self.resetTimeButton, 6, 5, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.Sone2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 4, 3, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem2 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 5, 4, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.Sone2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 4, 5, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_5 = QtWidgets.QLabel(self.Sone2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 10, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.forceRead = QtWidgets.QSpinBox(self.Sone2)
        self.forceRead.setAlignment(QtCore.Qt.AlignCenter)
        self.forceRead.setReadOnly(True)
        self.forceRead.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.forceRead.setPrefix("")
        self.forceRead.setObjectName("forceRead")
        self.gridLayout_4.addWidget(self.forceRead, 11, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.Sone2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 10, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_8.addWidget(self.Sone2, 2, 0, 1, 1)
        self.Sone1 = QtWidgets.QWidget(self.frame)
        self.Sone1.setStyleSheet("")
        self.Sone1.setObjectName("Sone1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Sone1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget = QtWidgets.QWidget(self.Sone1)
        self.widget.setObjectName("widget")
        self.gridLayout_3.addWidget(self.widget, 8, 1, 1, 1)
        self.saveGraphButton = QtWidgets.QPushButton(self.Sone1)
        self.saveGraphButton.setMinimumSize(QtCore.QSize(0, 25))
        self.saveGraphButton.setObjectName("saveGraphButton")
        self.gridLayout_3.addWidget(self.saveGraphButton, 9, 0, 1, 1)
        self.compressButton = QtWidgets.QPushButton(self.Sone1)
        self.compressButton.setMinimumSize(QtCore.QSize(190, 25))
        self.compressButton.setObjectName("compressButton")
        self.gridLayout_3.addWidget(self.compressButton, 7, 1, 1, 1)
        self.sone1_1 = QtWidgets.QWidget(self.Sone1)
        self.sone1_1.setObjectName("sone1_1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.sone1_1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.sone1_1)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.releaseMatButton = QtWidgets.QPushButton(self.sone1_1)
        self.releaseMatButton.setMinimumSize(QtCore.QSize(80, 25))
        self.releaseMatButton.setObjectName("releaseMatButton")
        self.gridLayout_2.addWidget(self.releaseMatButton, 5, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_2.addItem(spacerItem3, 6, 1, 1, 1)
        self.RWmaxForce = QtWidgets.QDoubleSpinBox(self.sone1_1)
        self.RWmaxForce.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.RWmaxForce.setMaximum(2500.0)
        self.RWmaxForce.setObjectName("RWmaxForce")
        self.gridLayout_2.addWidget(self.RWmaxForce, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_2.addItem(spacerItem4, 3, 1, 1, 1)
        self.autoZeroButton = QtWidgets.QPushButton(self.sone1_1)
        self.autoZeroButton.setMinimumSize(QtCore.QSize(0, 25))
        self.autoZeroButton.setObjectName("autoZeroButton")
        self.gridLayout_2.addWidget(self.autoZeroButton, 5, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.sone1_1)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.sone1_1)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.sone1_1)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.RWinitialForce = QtWidgets.QDoubleSpinBox(self.sone1_1)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.RWinitialForce.setPalette(palette)
        self.RWinitialForce.setFrame(False)
        self.RWinitialForce.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.RWinitialForce.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.RWinitialForce.setKeyboardTracking(True)
        self.RWinitialForce.setObjectName("RWinitialForce")
        self.gridLayout_2.addWidget(self.RWinitialForce, 4, 1, 1, 1)
        self.RWtensileSpeed = QtWidgets.QDoubleSpinBox(self.sone1_1)
        self.RWtensileSpeed.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.RWtensileSpeed.setObjectName("RWtensileSpeed")
        self.gridLayout_2.addWidget(self.RWtensileSpeed, 1, 1, 1, 1)
        self.RWlengthRange = QtWidgets.QDoubleSpinBox(self.sone1_1)
        self.RWlengthRange.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.RWlengthRange.setObjectName("RWlengthRange")
        self.gridLayout_2.addWidget(self.RWlengthRange, 2, 1, 1, 1)
        self.gridLayout_3.addWidget(self.sone1_1, 8, 0, 1, 1)
        self.tensileButton = QtWidgets.QPushButton(self.Sone1)
        self.tensileButton.setMinimumSize(QtCore.QSize(190, 25))
        self.tensileButton.setObjectName("tensileButton")
        self.gridLayout_3.addWidget(self.tensileButton, 6, 1, 1, 1)
        self.stopButton = QtWidgets.QPushButton(self.Sone1)
        self.stopButton.setMinimumSize(QtCore.QSize(0, 25))
        self.stopButton.setObjectName("stopButton")
        self.gridLayout_3.addWidget(self.stopButton, 7, 0, 1, 1)
        self.startButton = QtWidgets.QPushButton(self.Sone1)
        self.startButton.setMinimumSize(QtCore.QSize(0, 25))
        self.startButton.setObjectName("startButton")
        self.gridLayout_3.addWidget(self.startButton, 6, 0, 1, 1)
        self.sone1_1.raise_()
        self.saveGraphButton.raise_()
        self.widget.raise_()
        self.tensileButton.raise_()
        self.compressButton.raise_()
        self.stopButton.raise_()
        self.startButton.raise_()
        self.gridLayout_8.addWidget(self.Sone1, 1, 0, 1, 1)
        self.TitleBox = QtWidgets.QWidget(self.frame)
        self.TitleBox.setMinimumSize(QtCore.QSize(0, 100))
        self.TitleBox.setMaximumSize(QtCore.QSize(16777215, 100))
        self.TitleBox.setStyleSheet("")
        self.TitleBox.setObjectName("TitleBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.TitleBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.title = QtWidgets.QLabel(self.TitleBox)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.title.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Yrsa Light")
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.gridLayout_5.addWidget(self.title, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_8.addWidget(self.TitleBox, 0, 0, 1, 1)
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
        self.forceWidget.setObjectName("forceWidget")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.forceWidget)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.forceWidget)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.gridLayout_10.addWidget(self.graphicsView_2, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.forceWidget, 1, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.forceGraph)
        self.label_15.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_15.setObjectName("label_15")
        self.gridLayout_7.addWidget(self.label_15, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_14 = QtWidgets.QLabel(self.forceGraph)
        self.label_14.setMaximumSize(QtCore.QSize(20, 16777215))
        self.label_14.setObjectName("label_14")
        self.gridLayout_7.addWidget(self.label_14, 1, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.forceGraph)
        self.label_16.setMaximumSize(QtCore.QSize(16777215, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.label_16.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Yrsa Light")
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gridLayout_7.addWidget(self.label_16, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.forceGraph)
        self.stressGraph = QtWidgets.QWidget(self.widget_2)
        self.stressGraph.setMinimumSize(QtCore.QSize(600, 0))
        self.stressGraph.setStyleSheet("")
        self.stressGraph.setObjectName("stressGraph")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.stressGraph)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_12 = QtWidgets.QLabel(self.stressGraph)
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_12.setObjectName("label_12")
        self.gridLayout_6.addWidget(self.label_12, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.stressWidget = QtWidgets.QWidget(self.stressGraph)
        self.stressWidget.setObjectName("stressWidget")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.stressWidget)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.graphicsView = QtWidgets.QGraphicsView(self.stressWidget)
        self.graphicsView.setMinimumSize(QtCore.QSize(0, 0))
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_9.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.stressWidget, 1, 1, 1, 1)
        self.label_1 = QtWidgets.QLabel(self.stressGraph)
        self.label_1.setMaximumSize(QtCore.QSize(35, 16777215))
        self.label_1.setObjectName("label_1")
        self.gridLayout_6.addWidget(self.label_1, 1, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.stressGraph)
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.label_13.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Yrsa Light")
        font.setUnderline(False)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout_6.addWidget(self.label_13, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.stressGraph)
        self.horizontalLayout.addWidget(self.widget_2)
        self.gridLayout.addWidget(self.Backround, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1917, 21))
        self.menubar.setObjectName("menubar")
        self.menusssss = QtWidgets.QMenu(self.menubar)
        self.menusssss.setObjectName("menusssss")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.actionCOM_Port = QtWidgets.QAction(MainWindow)
        self.actionCOM_Port.setObjectName("actionCOM_Port")
        self.actionGeometry = QtWidgets.QAction(MainWindow)
        self.actionGeometry.setObjectName("actionGeometry")
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.actionCOM_Port)
        self.menuTools.addAction(self.actionGeometry)
        self.menubar.addAction(self.menusssss.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_9.setText(_translate("MainWindow", "Stress"))
        self.setZeroButton.setText(_translate("MainWindow", "Set zero"))
        self.epsilonRead.setSuffix(_translate("MainWindow", " ɛ "))
        self.stressRead.setSuffix(_translate("MainWindow", " Mpa"))
        self.label_17.setText(_translate("MainWindow", "Direct data"))
        self.timeRead.setSuffix(_translate("MainWindow", " s"))
        self.lengthRead.setSuffix(_translate("MainWindow", " μm"))
        self.resetTimeButton.setText(_translate("MainWindow", "Reset"))
        self.label_8.setText(_translate("MainWindow", "Epsilon"))
        self.label_7.setText(_translate("MainWindow", "Time"))
        self.label_5.setText(_translate("MainWindow", "Force"))
        self.forceRead.setSuffix(_translate("MainWindow", " N"))
        self.label_6.setText(_translate("MainWindow", "Length"))
        self.saveGraphButton.setText(_translate("MainWindow", "Save graph"))
        self.compressButton.setText(_translate("MainWindow", "Compress"))
        self.label.setText(_translate("MainWindow", "Tensile-speed:"))
        self.releaseMatButton.setText(_translate("MainWindow", "Release"))
        self.RWmaxForce.setSuffix(_translate("MainWindow", " N"))
        self.autoZeroButton.setText(_translate("MainWindow", "Auto zero"))
        self.label_4.setText(_translate("MainWindow", "Initial force:"))
        self.label_2.setText(_translate("MainWindow", "Max force:"))
        self.label_3.setText(_translate("MainWindow", "Set length range:"))
        self.RWinitialForce.setSuffix(_translate("MainWindow", " N"))
        self.RWtensileSpeed.setSuffix(_translate("MainWindow", " μm/s"))
        self.RWlengthRange.setSuffix(_translate("MainWindow", " μm"))
        self.tensileButton.setText(_translate("MainWindow", "Tensile"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.title.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:26pt; font-weight:600; text-decoration: underline;\">Tensile Testing</span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "L [μm]"))
        self.label_14.setText(_translate("MainWindow", "F[N]"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">Tensile</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "ɛ "))
        self.label_1.setText(_translate("MainWindow", "δ[MPa]"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">Stress</span></p></body></html>"))
        self.menusssss.setTitle(_translate("MainWindow", "File"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.actionCOM_Port.setText(_translate("MainWindow", "COM Port"))
        self.actionGeometry.setText(_translate("MainWindow", "Geometry"))
import Her_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
