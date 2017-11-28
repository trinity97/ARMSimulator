import sys
from PyQt4 import QtGui


def open_file():
    app = QtGui.QApplication(sys.argv)
    name = QtGui.QFileDialog.getOpenFileName(QtGui.QFileDialog(), "Open File")
    return name
