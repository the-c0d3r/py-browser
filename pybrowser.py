import sys
from PyQt4 import QtGui


class Browser(QtGui.QMainWindow):

	def __init__(self):
		super(Browser,self).__init__()

		self.initUI()

	def initUI(self):
		# Setting windows title
		self.setWindowTitle("Untitled - PyBrowser")
		# Moving windows to desktop center when opened by default
		self.move(QtGui.QApplication.desktop().screen().rect().center()-self.rect().center())
		self.statusBar()
		self.resize(500,500)
		self.show()

def main():
	app = QtGui.QApplication(sys.argv)
	ex = Browser()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()