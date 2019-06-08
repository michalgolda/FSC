class StyleLoader:


	def __init__(self, parent=None, file_name=None, print_styles=False, file_path="FSC/assets/styles/"):
		self.file_name = file_name
		self.file_path = file_path
		self.print_styles = print_styles
		self.parent = parent
		self.styles = self._readFileStyles()

	def load(self):

		if self.styles != False:
			try:
				print("StyleLoader: Styles have been successfully loaded. \n")
				if self.print_styles == True:
					print(self.styles)
				self.parent.setStyleSheet(self.styles)
			except Exception as e:
				print(str(e) + "\n")


	def _readFileStyles(self) -> str:
		
		styles = None

		try:
			with open(self.file_path + self.file_name + ".qss") as f:
				styles = f.read()
		except Exception as e:
			print("StyleLoader: There was a problem loading styles from the file.")
			print("StyleLoader: Error: {}".format(str(e)))
			return False

		return styles