import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class SimpleForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Form")
        self.setGeometry(100, 100, 200, 150)

        # Central Widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Layout
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Widgets
        self.name_label = QLabel("Name:")
        self.name_input = QLineEdit()

        self.age_label = QLabel("Age:")
        self.age_input = QLineEdit()

        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.on_submit)

        # Adding Widgets to Layout
        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.name_input)
        self.layout.addWidget(self.age_label)
        self.layout.addWidget(self.age_input)
        self.layout.addWidget(self.submit_button)

    def on_submit(self):
        name = self.name_input.text()
        age = self.age_input.text()
        greeting = f"Hello, {name}! You are {age} years old."
        QMessageBox.information(self, "Greeting", greeting)

def main():
    app = QApplication(sys.argv)
    form = SimpleForm()
    form.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()