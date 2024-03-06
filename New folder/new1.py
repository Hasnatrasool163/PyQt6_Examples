import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QPushButton, QSlider, QComboBox)
from PyQt5.QtCore import Qt

class UnitConverter(QWidget):
    def _init_(self):
        super()._init_()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Unit Converter')
        self.setGeometry(300, 300, 400, 200)

        # Styling
        self.setStyleSheet("""
            QWidget {
                font-size: 16px;
            }
            QLineEdit, QLabel, QPushButton, QSlider, QComboBox {
                margin: 10px;
            }
        """)

        # Layout
        layout = QVBoxLayout()
        inputLayout = QHBoxLayout()
        outputLayout = QHBoxLayout()

        # Input Components
        self.inputValue = QLineEdit(self)
        self.inputValue.setPlaceholderText('Enter value...')
        self.inputValue.textChanged.connect(self.convert_units)

        self.unitComboFrom = QComboBox(self)
        self.unitComboFrom.addItems(["Kilometers", "Meters", "Miles"])
        self.unitComboFrom.currentIndexChanged.connect(self.convert_units)

        # Output Components
        self.outputValue = QLineEdit(self)
        self.outputValue.setReadOnly(True)

        self.unitComboTo = QComboBox(self)
        self.unitComboTo.addItems(["Kilometers", "Meters", "Miles"])
        self.unitComboTo.currentIndexChanged.connect(self.convert_units)

        # Add widgets to layouts
        inputLayout.addWidget(self.inputValue)
        inputLayout.addWidget(self.unitComboFrom)

        outputLayout.addWidget(self.outputValue)
        outputLayout.addWidget(self.unitComboTo)

        layout.addLayout(inputLayout)
        layout.addLayout(outputLayout)

        self.setLayout(layout)

    def convert_units(self):
        value = self.inputValue.text()
        from_unit = self.unitComboFrom.currentText()
        to_unit = self.unitComboTo.currentText()

        try:
            value = float(value)
        except ValueError:
            self.outputValue.setText('')
            return

        # Conversion Logic
        if from_unit == to_unit:
            result = value
        else:
            # Convert from_unit to meters
            if from_unit == "Kilometers":
                value = value * 1000
            elif from_unit == "Miles":
                value = value * 1609.34

            # Convert meters to to_unit
            if to_unit == "Kilometers":
                result = value / 1000
            elif to_unit == "Meters":
                result = value
            elif to_unit == "Miles":
                result = value / 1609.34

        self.outputValue.setText(f"{result:.2f}")

def main():
    app = QApplication(sys.argv)
    ex = UnitConverter()
    ex.show()
    sys.exit(app.exec_())

if __name__== '__main__':
    main()