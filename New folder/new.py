import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QComboBox, QLabel

class UnitConverter(QWidget):
    def _init_(self):
        super()._init_()
        self.setWindowTitle('Enhanced Unit Converter')
        self.setGeometry(300, 300, 400, 200)
        self.unit_data = self.get_unit_data()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Category Selection
        self.categoryCombo = QComboBox()
        self.categoryCombo.addItems(sorted(self.unit_data.keys()))
        self.categoryCombo.currentIndexChanged.connect(self.update_units)
        
        # From Unit
        self.fromUnitCombo = QComboBox()
        
        # To Unit
        self.toUnitCombo = QComboBox()
        
        # Input Field
        self.inputValue = QLineEdit()
        self.inputValue.setPlaceholderText('Enter value...')
        self.inputValue.textChanged.connect(self.convert_units)

        # Output Display
        self.outputValue = QLabel('Result')
        
        # Assembling Layouts
        layout.addWidget(self.categoryCombo)
        
        unitSelectionLayout = QHBoxLayout()
        unitSelectionLayout.addWidget(self.fromUnitCombo)
        unitSelectionLayout.addWidget(self.toUnitCombo)
        
        layout.addLayout(unitSelectionLayout)
        layout.addWidget(self.inputValue)
        layout.addWidget(self.outputValue)
        
        self.setLayout(layout)
        self.update_units()  # Initialize unit dropdowns

    def get_unit_data(self):
        # Define conversion functions and units for each category
        return {
            'Length': {
                'units': ['Kilometers', 'Meters', 'Miles'],
                'conversions': {
                    ('Kilometers', 'Meters'): lambda x: x * 1000,
                    ('Kilometers', 'Miles'): lambda x: x * 0.621371,
                    ('Meters', 'Kilometers'): lambda x: x / 1000,
                    ('Meters', 'Miles'): lambda x: x * 0.000621371,
                    ('Miles', 'Kilometers'): lambda x: x / 0.621371,
                    ('Miles', 'Meters'): lambda x: x * 1609.34,
                }
            },
            'Weight': {
                'units': ['Kilograms', 'Grams', 'Pounds'],
                'conversions': {
                    ('Kilograms', 'Grams'): lambda x: x * 1000,
                    ('Kilograms', 'Pounds'): lambda x: x * 2.20462,
                    ('Grams', 'Kilograms'): lambda x: x / 1000,
                    ('Grams', 'Pounds'): lambda x: x * 0.00220462,
                    ('Pounds', 'Kilograms'): lambda x: x / 2.20462,
                    ('Pounds', 'Grams'): lambda x: x * 453.592,
                }
            },
            # Additional categories can be added here
        }

    def update_units(self):
        category = self.categoryCombo.currentText()
        units = self.unit_data[category]['units']
        self.fromUnitCombo.clear()
        self.fromUnitCombo.addItems(units)
        self.toUnitCombo.clear()
        self.toUnitCombo.addItems(units)
        self.convert_units()

    def convert_units(self):
        from_unit = self.fromUnitCombo.currentText()
        to_unit = self.toUnitCombo.currentText()
        category = self.categoryCombo.currentText()
        conversions = self.unit_data[category]['conversions']
        value = self.inputValue.text()
        
        try:
            value = float(value)
            if (from_unit, to_unit) in conversions:
                result = conversions[(from_unit, to_unit)](value)
                self.outputValue.setText(f"{result:.2f}")
            else:
                self.outputValue.setText("Conversion not available")
        except ValueError:
            self.outputValue.setText("Invalid input")

def main():
    app = QApplication(sys.argv)
    converter = UnitConverter()
    converter.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()