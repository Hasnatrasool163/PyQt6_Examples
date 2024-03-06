import sys
from PyQt5.QtWidgets import QApplication,QAction,QTableWidget, QMainWindow, QDockWidget, QTextEdit, QListWidget, QMenuBar, QTabWidget, QAction, QFileDialog, QVBoxLayout, QWidget



class IDE(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt IDE')
        self.setGeometry(100, 100, 1200, 600)
        self.initUI()

    def initUI(self):
        self.createMenuBar()
        self.createEditor()
        self.createFileExplorer()
        self.createOutputConsole()

    def createMenuBar(self):
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('File')
        
        openAction = QAction('Open', self)
        fileMenu.addAction(openAction)

        saveAction = QAction('Save', self)
        fileMenu.addAction(saveAction)

    def createEditor(self):
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        self.tabs.addTab(QTextEdit(), "Untitled")

    def createFileExplorer(self):
        self.explorer = QDockWidget("File Explorer", self)
        # self.explorer.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        self.explorer.setWidget(QListWidget())
        # self.addDockWidget(Qt.LeftDockWidgetArea, self.explorer)

    def createOutputConsole(self):
        self.outputConsole = QDockWidget("Output", self)
        # self.outputConsole.setAllowedAreas(Qt.BottomDockWidgetArea)
        self.outputConsole.setWidget(QTabWidget())
        # self.addDockWidget(Qt.BottomDockWidgetArea, self.outputConsole)
        
       
        consoleTab = QTabWidget()
        consoleTab.addTab(QTextEdit(), "Output")
        self.outputConsole.setWidget(consoleTab)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = IDE()
    mainWin.show()
    sys.exit(app.exec_())