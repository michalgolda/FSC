import sys

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import  QApplication, QMainWindow

from FSC import __version__, __author__
from FSC.widgets.mainWidget import MainWidget
from FSC.utils.styleLoader import StyleLoader



class MainWindow(QMainWindow):


	def __init__(self,parent=None):
		super(MainWindow, self).__init__(parent)

		self.main_widget = MainWidget(self)
		self.setCentralWidget(self.main_widget)

		self.styleLoader = StyleLoader(self, file_name="main")

		self.setWindowTitle("FSC")
		self.setWindowIcon(QtGui.QIcon("D:/Projects/FSC/fsc/assets/images/icon.ico"))
		self.setFixedSize(640, 300)

		self.styleLoader.load()

		self.statusBar().showMessage("Version: {}  Author: {}".format(__version__, __author__))

		self.show()


if __name__ == "__main__":
	app = QApplication(sys.argv)

	window = MainWindow()

	app.exec_()