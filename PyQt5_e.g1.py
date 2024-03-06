from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel

def on_button_clicked():
    label.setText("Hello, PyQt!")

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()

button = QPushButton('Click Me')
button.clicked.connect(on_button_clicked)  

label = QLabel('Press the button...')
layout.addWidget(button)
layout.addWidget(label)

window.setLayout(layout)
window.show()
app.exec_()