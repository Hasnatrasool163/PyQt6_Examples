import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout,
                             QPushButton, QWidget, QAction, QMessageBox, QDialog, QLineEdit, QLabel, QGridLayout)

class EmployeeManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Employee Manager")
        self.setGeometry(100, 100, 600, 400)

        self.employees = []

        self.initialize_ui()

    def initialize_ui(self):
        self.create_menu_bar()
        self.create_status_bar()
        self.create_main_layout()

    def create_menu_bar(self):
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        employee_menu = menu_bar.addMenu("Employee")
        add_action = QAction("Add", self)
        add_action.triggered.connect(self.add_employee_dialog)
        employee_menu.addAction(add_action)

    def create_status_bar(self):
        self.statusBar().showMessage("Ready")

    def create_main_layout(self):
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(["ID", "Name", "Position"])

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.table_widget)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def add_employee_dialog(self):
        dialog = QDialog()
        dialog.setWindowTitle("Add Employee")
        dialog_layout = QGridLayout()

        name_label = QLabel("Name:")
        self.name_input = QLineEdit()
        position_label = QLabel("Position:")
        self.position_input = QLineEdit()

        add_button = QPushButton("Add")
        add_button.clicked.connect(lambda: self.add_employee(dialog))

        dialog_layout.addWidget(name_label, 0, 0)
        dialog_layout.addWidget(self.name_input, 0, 1)
        dialog_layout.addWidget(position_label, 1, 0)
        dialog_layout.addWidget(self.position_input, 1, 1)
        dialog_layout.addWidget(add_button, 2, 0, 1, 2)

        dialog.setLayout(dialog_layout)
        dialog.exec_()

    def add_employee(self, dialog):
        name = self.name_input.text()
        position = self.position_input.text()
        if name and position:
            employee_id = len(self.employees) + 1
            self.employees.append((employee_id, name, position))
            self.update_employee_table()
            self.statusBar().showMessage("Employee added")
            dialog.accept()
        else:
            QMessageBox.warning(self, "Error", "Name and position cannot be empty.")

    def update_employee_table(self):
        self.table_widget.setRowCount(len(self.employees))
        for row_number, employee in enumerate(self.employees):
            for column_number, data in enumerate(employee):
                self.table_widget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

def main():
    app = QApplication(sys.argv)
    manager = EmployeeManager()
    manager.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()