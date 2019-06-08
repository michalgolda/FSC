import hashlib

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import  (QWidget, QFileDialog, QLabel, QVBoxLayout, 
	QHBoxLayout, QGridLayout, QLineEdit, QPushButton, QProgressBar)

from FSC.utils.styleLoader import StyleLoader

class MainWidget(QWidget):


	def __init__(self, parent):
		super(MainWidget, self).__init__(parent)

		self.parent = parent
		self.file_path = None
		self.checking = False

		mainContainer = QVBoxLayout()

		self.fileLabelInfo = QLabel("File")
		self.fileLabel = QLabel("Not selected file.")
		self.fileSelectBtn = QPushButton("Select")
		self.fileSelectBtn.clicked.connect(self.browse_file)

		fileSelectorContainer = QHBoxLayout()
		fileSelectorContainer.setContentsMargins(0, 50, 0, 0)
		fileSelectorContainer.addWidget(self.fileLabel)
		fileSelectorContainer.addStretch()
		fileSelectorContainer.addWidget(self.fileSelectBtn)

		dialogContainer = QVBoxLayout()
		dialogContainer.setContentsMargins(0, 50, 0, 0)

		informationContainer = QGridLayout()
		informationContainer.setContentsMargins(0, 0, 0,0)

		self.providedHashInput = QLineEdit()
		self.providedHashInput.setPlaceholderText("Enter hash.")
		self.startCheckBtn = QPushButton("Check")
		self.startCheckBtn.clicked.connect(self.verify_hash)
		self.informationLabel = QLabel(" ")

		self.informationProgressBar = QProgressBar(self)
		self.informationProgressBar.setTextVisible(False)
		self.informationProgressBar.hide()
	
		informationContainer.addWidget(self.informationLabel, 0, 1, Qt.AlignCenter)

		dialogContainer.addWidget(self.providedHashInput)
		dialogContainer.addWidget(self.startCheckBtn)
		dialogContainer.addWidget(self.informationProgressBar)
		dialogContainer.addLayout(informationContainer)
		
		mainContainer.addLayout(fileSelectorContainer)
		mainContainer.addLayout(dialogContainer)
		
		self.setLayout(mainContainer)

		self.show()


	def browse_file(self):
		self.file = QFileDialog.getOpenFileName()
		self.file_path = self.file[0]
		if not self.file_path:
			self.fileLabel.setText("Not selected file.")
		elif self.file_path != 0:
			self.fileLabel.setText("{}".format(self.file_path))


	def verify_hash(self):


		if not self.file_path:
			return False
		else:
			self.stored_hash = self.generate_file_hash(self.file_path)


		if not self.providedHashInput.text():
			self.informationLabel.setText("Enter hash input!")
			self.informationLabel.setStyleSheet("color: #ff3535;")
			self.informationLabel.show()
			return False
		elif self.providedHashInput.text() != 0:
			self.provided_hash = self.providedHashInput.text()
			self.informationLabel.hide()

		self.runProgressBar()

		if self.stored_hash == self.provided_hash:
			self.informationLabel.setText("Hash is correct :)")
			self.informationLabel.setStyleSheet("color: #53f44;")
			self.informationLabel.show()
			self.informationProgressBar.hide()
		else:
			self.informationLabel.setText("Hash is bad :(")
			self.informationLabel.setStyleSheet("color: #ff3535;")
			self.informationLabel.show()
			self.informationProgressBar.hide()


	def runProgressBar(self):
		self.completed = 0
		self.startCheckBtn.hide()
		self.informationProgressBar.show()
		while self.completed < 100:
			self.completed += 0.0001
			self.informationLabel.hide()
			self.informationProgressBar.show()
			self.informationProgressBar.setValue(self.completed)
			if self.informationProgressBar.value() == 100:
				self.startCheckBtn.show()
				self.informationProgressBar.hide()
				break
				
	@staticmethod
	def generate_file_hash(file_path: str) -> str:

		hash = hashlib.md5()

		with open(file_path, "rb") as f:
			for chunk in iter(lambda: f.read(4096), b""):
				hash.update(chunk)

		return hash.hexdigest()