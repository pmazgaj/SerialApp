"""
Module handling popups
"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

__author__ = "Przemek"


class Window(QtWidgets.QMainWindow, GUI.MainUI.Ui_MainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("PyQT tuts!")
        self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))

        extract_action = QtGui.QAction("&GET TO THE CHOPPAH!!!", self)
        extract_action.setShortcut("Ctrl+Q")
        extract_action.setStatusTip('Leave The App')
        extract_action.triggered.connect(self.close_application)

        self.statusBar()

        main_menu = self.menuBar()
        file_menu = main_menu.addMenu('&File')
        file_menu.addAction(extract_action)

        self.home()

    def home(self):
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(0, 100)

        extractAction = QtGui.QAction(QtGui.QIcon('todachoppa.png'), 'Flee the Scene', self)
        extractAction.triggered.connect(self.close_application)

        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractAction)

        check_box = QtGui.QCheckBox('Enlarge Window', self)
        check_box.move(100, 25)
        check_box.stateChanged.connect(self.enlarge_window)
        # depending on what you want the default to be.
        # checkBox.toggle()
        self.show()

    def enlarge_window(self, state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(50, 50, 1000, 600)
        else:
            self.setGeometry(50, 50, 500, 300)

    def close_application(self):
        choice = QtGui.QMessageBox.question(self, 'Extract!',
                                            "Get into the chopper?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            print("Extracting Naaaaaaoooww!!!!")
            sys.exit()
        else:
            pass


def run():
    app = QtGui.QApplication(sys.argv)
    gui = Window()
    sys.exit(app.exec_())


run()
