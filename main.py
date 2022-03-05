from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import numpy as np
import math
from PyQt5.QtWidgets import QPushButton




pg.setConfigOption('background', (33, 33, 33))
pg.setConfigOption('foreground', (197, 198, 199))
# Interface variables
app = QtGui.QApplication([])
view = pg.GraphicsView()
Layout = pg.GraphicsLayout()
view.setCentralItem(Layout)
view.show()
view.setWindowTitle('Flight monitoring')
view.resize(1200, 700)




#
# Altitude graph
l1 = Layout.addLayout(colspan=20, rowspan=2)
l11 = l1.addLayout(rowspan=1, border=(83, 83, 83))
p1 = l11.addPlot(title="Altitude (m)")
altitude_plot = p1.plot(pen=(29, 185, 84))
altitude_data = np.linspace(0, 0, 30)
ptr1 = 0




# Start Qt event loop unless running in interactive mode.

if __name__ == '__main__':

    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
