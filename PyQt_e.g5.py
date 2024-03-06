import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTextEdit, QListWidget, QAction, QFileDialog,
                             QVBoxLayout, QWidget, QMessageBox,QLineEdit, QComboBox,QHBoxLayout)
from PyQt5.QtCore import Qt 
from PyQt5.QtPrintSupport import QPrinter
class NoteTakingApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.notes = {}
        self.current_note_id = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Note Taking App')
        self.setGeometry(100, 100, 800, 600)

        self.textEdit = QTextEdit()
        self.listWidget = QListWidget()
        self.listWidget.currentItemChanged.connect(self.note_selected)

        layout = QHBoxLayout()
        layout.addWidget(self.listWidget, 1)
        layout.addWidget(self.textEdit, 3)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.searchBar = QLineEdit()
        self.searchBar.setPlaceholderText("Search notes...")
        self.searchBar.textChanged.connect(self.search_notes)
        layout.addWidget(self.searchBar, 0)

        self.create_menu_bar()
        self.create_tool_bar()
        self.formatToolBar = self.addToolBar('Format')
        self.add_formatting_actions()
        self.statusBar()

    def create_menu_bar(self):
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')

        new_action = QAction('New', self)
        new_action.triggered.connect(self.new_note)
        file_menu.addAction(new_action)

        save_action = QAction('Save', self)
        save_action.triggered.connect(self.save_note)
        file_menu.addAction(save_action)

        delete_action = QAction('Delete', self)
        delete_action.triggered.connect(self.delete_note)
        file_menu.addAction(delete_action)
        
        export_action = QAction('Export to PDF', self)
        export_action.triggered.connect(self.export_note_to_pdf)
        file_menu.addAction(export_action)

        file_menu.addSeparator()

        exit_action = QAction('Exit', self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

    def create_tool_bar(self):
        toolbar = self.addToolBar('Toolbar')

        new_action = QAction('New', self)
        new_action.triggered.connect(self.new_note)
        toolbar.addAction(new_action)

        save_action = QAction('Save', self)
        save_action.triggered.connect(self.save_note)
        toolbar.addAction(save_action)

        delete_action = QAction('Delete', self)
        delete_action.triggered.connect(self.delete_note)
        toolbar.addAction(delete_action)
        
    def search_notes(self):
        query = self.searchBar.text().lower()
        for i in range(self.listWidget.count()):
            item = self.listWidget.item(i)
            item.setHidden(query not in item.text().lower())

    def new_note(self):
        note_name, ok = QFileDialog.getSaveFileName(self, 'Save Note', '', 'Text Files (*.txt)')
        if ok:
            note_name = os.path.basename(note_name)
            self.notes[note_name] = ''
            self.listWidget.addItem(note_name)
            self.listWidget.setCurrentRow(self.listWidget.count() - 1)

    def save_note(self):
        if self.current_note_id is not None:
            note_name = self.listWidget.item(self.current_note_id).text()
            with open(note_name, 'w') as f:
                f.write(self.textEdit.toPlainText())
            self.notes[note_name] = self.textEdit.toPlainText()
            self.statusBar().showMessage(f"'{note_name}' saved", 2000)

    def delete_note(self):
        if self.current_note_id is not None:
            note_name = self.listWidget.item(self.current_note_id).text()
            del self.notes[note_name]
            self.listWidget.takeItem(self.current_note_id)
            self.textEdit.clear()
            self.current_note_id = None

    def note_selected(self, current, previous):
        if current:
            note_name = current.text()
            self.textEdit.setText(self.notes[note_name])
            self.current_note_id = self.listWidget.row(current)
        else:
            self.textEdit.clear()
            self.current_note_id = None
   


    def export_note_to_pdf(self):
        if self.current_note_id is not None:
            note_name = self.listWidget.item(self.current_note_id).text()
            file_path, _ = QFileDialog.getSaveFileName(self, "Export PDF", note_name, "PDF Files (*.pdf)")
            if file_path:
                printer = QPrinter(QPrinter.HighResolution)
                printer.setOutputFormat(QPrinter.PdfFormat)
                printer.setOutputFileName(file_path)
                self.textEdit.document().print_(printer)
                QMessageBox.information(self, "Export to PDF", "Note exported successfully.")
                
    def add_formatting_actions(self):
        bold_action = QAction('Bold', self)
        bold_action.triggered.connect(lambda: self.textEdit.setFontWeight(20))
        self.formatToolBar.addAction(bold_action)

        italic_action = QAction('Italic', self)
        italic_action.triggered.connect(lambda: self.textEdit.setFontItalic(not self.textEdit.fontItalic()))
        self.formatToolBar.addAction(italic_action)

        underline_action = QAction('Underline', self)
        underline_action.triggered.connect(lambda: self.textEdit.setFontUnderline(not self.textEdit.fontUnderline()))
        self.formatToolBar.addAction(underline_action)

        self.fontSizeComboBox = QComboBox()
        for i in range(8, 30, 2):  # Adding common font sizes
            self.fontSizeComboBox.addItem(str(i))
        self.fontSizeComboBox.setEditable(True)
        self.fontSizeComboBox.currentTextChanged.connect(lambda size: self.textEdit.setFontPointSize(int(size)))
        self.formatToolBar.addWidget(self.fontSizeComboBox)

def main():
    app = QApplication(sys.argv)
    ex = NoteTakingApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()