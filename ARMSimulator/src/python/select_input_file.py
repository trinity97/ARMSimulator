import sys
from PyQt4 import QtGui
from ARMSimulator.src.python import armSimulator
import helper
import setup
import time

class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("ARM SimSim")
        self.setGeometry(100, 100, 500, 500)
        self.show()

        self.register_values = QtGui.QTextEdit()
        self.register_values.setReadOnly(True)

        self.code_text = QtGui.QTextEdit()
        self.code_text.setReadOnly(True)

        self.out_text = QtGui.QTextEdit()
        self.out_text.setReadOnly(True)

        show_menu_option = QtGui.QAction("&Select Option", self)
        show_menu_option.triggered.connect(self.open_file)

        run_simulator = QtGui.QAction("&Run", self)
        run_simulator.triggered.connect(armSimulator.run_arm_simulator)

        step_into = QtGui.QAction("&Step Into", self)
        step_into.triggered.connect(armSimulator.step_into)

        main_menu = self.menuBar()

        file_menu = main_menu.addMenu("&Open File")
        file_menu.addAction(show_menu_option)

        run_menu = main_menu.addMenu("&Run Simulator")
        run_menu.addAction(run_simulator)
        run_menu.addAction(step_into)


    def open_file(self):
        helper.reset_values()
        file = open("../../output/output.txt", "w").close()
        self.out_text.clear()
        name = QtGui.QFileDialog.getOpenFileName(QtGui.QFileDialog(), "Open File")
        self.make_ui()
        if name:
            file = open(name, 'r')
            helper.read_file(name)
            with file:
                text = file.read()
                self.code_text.setText(text)
        else:
            print("invalid file")

    def editor(self,string):
        self.out_text.append(string)
        QtGui.QApplication.processEvents()

    def registers_construct(self):
        s = ''
        for i in range(16):
            s += 'R' + str(i) + " : " +str(setup.registers[i]) + '\n'

        return s

    def registers(self):
        self.register_values.setText(self.registers_construct())
        QtGui.QApplication.processEvents()



    def make_ui(self):

        layout = QtGui.QGridLayout(self)
        layout.addWidget( self.register_values, 0, 0)
        layout.addWidget(self.code_text, 0, 1)
        layout.addWidget(self.out_text, 1, 0, 1, 2)
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 4)

        widget = QtGui.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


def start_gui():
    app = QtGui.QApplication(sys.argv)
    setup.gui = Window()
    app.exec_()
