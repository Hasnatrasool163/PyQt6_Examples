from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# Main Window Class
class MockGameEngineUI(QMainWindow):
    def _init_(self):
        super()._init_()
        self.setWindowTitle("Mock Game Engine UI - Advanced Customization")
        self.setGeometry(100, 100, 1200, 800)
        self.initUI()

    def initUI(self):
        # Central Editor Area
        self.editorTabWidget = QTabWidget()
        self.editorTabWidget.addTab(QWidget(), "Scene Editor")
        self.editorTabWidget.addTab(QWidget(), "Game Preview")
        self.setCentralWidget(self.editorTabWidget)
        
        # Dockable Panels
        self.createDockablePanels()
        
        # Toolbar
        self.initToolbar()

        # Status Bar
        self.initStatusBar()

        # Styling
        self.applyStyling()

    def createDockablePanels(self):
        # Reusing previous code for dockable panels like Project Explorer, Properties, Asset Library, and Console
        # Adding Layer Panel and Animation Panel as examples
        self.layerDock = self.createDockWidget("Layers", QListView())
        self.animationDock = self.createDockWidget("Animations", QListWidget())
        self.addDockWidget(Qt.RightDockWidgetArea, self.layerDock)
        self.splitDockWidget(self.layerDock, self.animationDock, Qt.Vertical)

    def createDockWidget(self, title, widget):
        dock = QDockWidget(title, self)
        dock.setWidget(widget)
        return dock

    def initToolbar(self):
        self.toolbar = self.addToolBar('Main Toolbar')
        self.toolbar.addAction(QAction(QIcon('play_icon.png'), 'Play', self))
        self.toolbar.addAction(QAction(QIcon('pause_icon.png'), 'Pause', self))
        self.toolbar.addAction(QAction(QIcon('stop_icon.png'), 'Stop', self))
        # Example of adding more actions with icons
        self.toolbar.addSeparator()
        self.toolbar.addAction(QAction(QIcon('add_icon.png'), 'Add Object', self))
        self.toolbar.addAction(QAction(QIcon('delete_icon.png'), 'Delete Object', self))

    def initStatusBar(self):
        self.statusBar().showMessage("Ready")

    def applyStyling(self):
        # Applying QSS for a dark theme similar to Unity or GDevelop
        self.setStyleSheet("""
        QMainWindow, QDockWidget, QTabWidget, QStatusBar {
            background-color: #2a2a2a;
            color: #ffffff;
        }
        QDockWidget::title {
            text-align: center;
            background: #1e1e1e;
            padding: 6px;
        }
        QToolBar, QToolBar::action {
            background-color: #333333;
            border: none;
            color: white;
        }
        QListView, QTextEdit, QListWidget {
            background-color: #1e1e1e;
            color: white;
            border: 1px solid #444;
        }
        """)

def main():
    app = QApplication([])
    window = MockGameEngineUI()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()