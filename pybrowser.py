import sys
from PyQt4 import QtGui, QtCore, QtWebKit


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
        self.resize(800,600)
        self.centralwidget = QtGui.QWidget(self)

        self.frame = QtGui.QFrame(self.centralwidget)
        self.mainLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.mainLayout.setSpacing(0)
        self.mainLayout.setMargin(1)

        self.gridLayout = QtGui.QVBoxLayout(self.frame)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)

        self.horizontalLayout = QtGui.QHBoxLayout()
        self.tb_url = QtGui.QLineEdit(self.frame)
        self.btn_back = QtGui.QPushButton(self.frame)
        self.btn_forward = QtGui.QPushButton(self.frame)

        self.btn_back.setIcon(QtGui.QIcon().fromTheme("go-previous"))
        self.btn_forward.setIcon(QtGui.QIcon().fromTheme("go-next"))

        self.horizontalLayout.addWidget(self.btn_back)
        self.horizontalLayout.addWidget(self.btn_forward)
        self.horizontalLayout.addWidget(self.tb_url)
        self.gridLayout.addLayout(self.horizontalLayout)

        self.html = QtWebKit.QWebView()
        self.gridLayout.addWidget(self.html)
        self.mainLayout.addWidget(self.frame)
        self.setCentralWidget(self.centralwidget)

        self.connect(self.tb_url, QtCore.SIGNAL("returnPressed()"),self.browse)
        self.connect(self.btn_back, QtCore.SIGNAL("clicked()"),self.html.back)
        self.connect(self.btn_forward, QtCore.SIGNAL("clicked()"),self.html.forward)

        self.default_url = "http://www.google.com"
        self.tb_url.setText(self.default_url)
        self.browse()

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

    def browse(self):
        """ Request HTML code and show it on Webview widget """

        url = self.tb_url.text() if self.tb_url.text() else self.default_url
        self.html.load(QtCore.QUrl(url))
        self.html.show()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Browser()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()