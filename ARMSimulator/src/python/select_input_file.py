import sys
from PyQt4 import QtGui
from ARMSimulator.src.python import armSimulator


class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.setWindowTitle("ARM SimSim")
        self.setGeometry(100,100,500,500)
        self.show()
        self.code_text = QtGui.QTextEdit()
        self.code_text.setReadOnly(True)

        show_menu_option = QtGui.QAction("&Select Option", self)
        show_menu_option.triggered.connect(self.open_file)

        run_simulator = QtGui.QAction("&Run", self)
        run_simulator.triggered.connect(armSimulator.run_arm_simulator)

        main_menu = self.menuBar()
        file_menu = main_menu.addMenu("&Open File")
        file_menu.addAction(show_menu_option)

        run_menu = main_menu.addMenu("&Run Simulator")
        run_menu.addAction(run_simulator)

    def open_file(self):
        name = QtGui.QFileDialog.getOpenFileName(QtGui.QFileDialog(), "Open File")
        self.make_ui()
        if name:
            file = open(name, 'r')
            with file:
                text = file.read()
                self.code_text.setText(text)
        else:
            print("invalid file")

    def editor(self):
        code_view = QtGui.QTextEdit()
        # self.setCentralWidget(code_view)
        code_view.setReadOnly(True)
        return code_view

    def make_ui(self):

        layout = QtGui.QGridLayout(self)
        layout.addWidget(self.code_text, 0, 0)
        out_text = QtGui.QTextEdit()
        out_text.setReadOnly(True)
        layout.addWidget(out_text,1,0)

        widget = QtGui.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)



def start_gui():
    app = QtGui.QApplication(sys.argv)
    gui = Window()
    app.exec_()
