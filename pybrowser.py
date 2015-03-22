import sys
from PyQt4 import QtGui


class Browser(QtGui.QMainWindow):

    def __init__(self):
        super(Browser,self).__init__()

        self.initUI()

    def initUI(self):
        """ A function to handle all GUI stuff """
        # Setting windows title
        self.setWindowTitle("Untitled - PyBrowser")
        # Moving windows to desktop center when opened by default
        self.move(QtGui.QApplication.desktop().screen().rect().center()-self.rect().center())
        self.statusBar()
        self.menu()
        self.resize(500,500)
        self.show()

    def menu(self):
        """ To display menu bar """

        exit_option = QtGui.QAction('E&xit',self)
        exit_option.setStatusTip("Exit Program")
        exit_option.setShortcut("Ctrl+P")
        exit_option.triggered.connect(sys.exit)

        # initiate a menubar instance
        menubar = self.menuBar()
        # menu options
        fileMenu = menubar.addMenu('&File')

        fileMenu.addAction(exit_option)

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Browser()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()