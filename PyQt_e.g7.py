import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class UnitConverter(QtWidgets.QWidget):
    def _init_(self):
        super()._init_()
        self.init_ui()

    def init_ui(self):
        # Unit dictionaries for better organization
        self.length_units = {"Kilometers": 1000, "Meters": 1, "Centimeters": 0.01, "Inches": 0.0254, "Feet": 0.3048}
        self.weight_units = {"Kilograms": 1000, "Grams": 1, "Pounds": 453.592, "Ounces": 28.3495}
        self.temperature_units = {"Celsius": 1, "Fahrenheit": 9/5 * (-273.15 + 32), "Kelvin": 1 + 273.15}

        # Main layout and widgets
        self.layout = QtWidgets.QVBoxLayout(self)

        # Category selection combobox
        self.category_label = QtWidgets.QLabel("Category:")
        self.category_combo = QtWidgets.QComboBox()
        self.category_combo.addItems(["Length", "Weight", "Temperature"])
        self.layout.addWidget(self.category_label)
        self.layout.addWidget(self.category_combo)

        # Input and output value displays with sliders
        self.input_label = QtWidgets.QLabel("Input Value:")
        self.input_display = QtWidgets.QLineEdit()
        self.input_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.input_slider.setMinimum(5)  # Set minimum slider value

        self.output_label = QtWidgets.QLabel("Output Value:")
        self.output_display = QtWidgets.QLineEdit()
        self.output_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.output_slider.setMinimum(5)  # Set minimum slider value

        self.layout.addWidget(self.input_label)
        self.layout.addWidget(self.input_display)
        self.layout.addWidget(self.input_slider)
        self.layout.addWidget(self.output_label)
        self.layout.addWidget(self.output_display)
        self.layout.addWidget(self.output_slider)

        # Unit selection comboboxes
        self.input_unit_label = QtWidgets.QLabel("From:")
        self.input_unit_combo = QtWidgets.QComboBox()
        self.output_unit_label = QtWidgets.QLabel("To:")
        self.output_unit_combo = QtWidgets.QComboBox()

        self.layout.addWidget(self.input_unit_label)
        self.layout.addWidget(self.input_unit_combo)
        self.layout.addWidget(self.output_unit_label)
        self.layout.addWidget(self.output_unit_combo)

        # Convert button
        self.convert_button = QtWidgets.QPushButton("Convert")
        self.layout.addWidget(self.convert_button)

        # Clear button
        self.clear_button = QtWidgets.QPushButton("Clear")
        self.layout.addWidget(self.clear_button)

        # Connections
        self.category_combo.currentTextChanged.connect(self.update_units)
        self.input_display.textChanged.connect(self.convert_on_input)
        self.input_slider.valueChanged.connect(self.update_output_from_input)
        self.output_display.textChanged.connect(self.convert_on_output)
        self.output_slider.valueChanged.connect(self.update_input_from_output)
        self.convert_button.clicked.connect(self.convert)
        self.clear_button.clicked.connect(self.clear)

        # Set initial states
        self.update_units()
        self.current_category = "Length"
        self.current_input_unit = "Meters"
        self.current_output_unit = "Kilometers"
        self.update_sliders()

        self.setWindowTitle("Unit Converter")
        self.show()

    def update_units(self):
        self.current_category = self.category_combo.update()