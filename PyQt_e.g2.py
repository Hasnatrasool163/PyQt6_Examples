from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

def show_message():
    QMessageBox.information(window, "Message", f"You entered: {line_edit.text()}")

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()

line_edit = QLineEdit()
submit_button = QPushButton('Submit')
submit_button.clicked.connect(show_message)

layout.addWidget(line_edit)
layout.addWidget(submit_button)

window.setLayout(layout)
window.show()
app.exec_()