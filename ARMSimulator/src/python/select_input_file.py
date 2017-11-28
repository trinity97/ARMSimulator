import sys
from PyQt4 import QtGui
from ARMSimulator.src.python import armSimulator

class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.setWindowTitle("ARM SimSim")
        self.setGeometry(100,100,500,500)
        self.show()

        show_menu_option = QtGui.QAction("&Select Option",self)
        show_menu_option.triggered.connect(self.open_file)

        run_simulator = QtGui.QAction("&Run",self)
        run_simulator.triggered.connect(armSimulator.run_arm_simulator)

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("&Open File")
        fileMenu.addAction(show_menu_option)

        runMenu = mainMenu.addMenu("&Run Simulator")
        runMenu.addAction(run_simulator)

    def open_file(self):
        name = QtGui.QFileDialog.getOpenFileName(QtGui.QFileDialog(), "Open File")
        self.editor()
        if name:
            file = open(name,'r')
            with file:
                text = file.read()
                self.textEdit.setText(text)
        else:
            print("invalid file")

    def editor(self):
        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.textEdit.setReadOnly(True)


def start_gui():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    app.exec_()