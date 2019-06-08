from unittest import TestCase

from FSC.utils.styleLoader import StyleLoader


class TestStyleLoader(TestCase):


	def setUp(self):
		self.loader = StyleLoader(file_name="main")

	def test_readFileStyle_func(self):
		f = open("FSC/assets/styles/main.qss")
		f = f.read()

		self.assertEqual(f, self.loader._readFileStyles())