# MAIN WINDOW FOR FITNESS APPLICATION
# ===================================

# LIBRARIES AND MODULES
import sys
from PyQt5 import QtCore # Core functionality of Qt
from PyQt5 import QtWidgets # UI elements functionality
from PyQt5.uic import loadUi
import kuntoilija
import timetools
# TODO: Import some library able to plot trends and make it as widget in the UI

# Class for the main window
class MainWindow(QtWidgets.QMainWindow):

    """MainWindow for the fitness app"""

    # Constructor for the main window
    def __init__(self):
        super().__init__()

        # Load the UI file
        loadUi('main.ui', self)

        # Define UI Controls ie buttons and input fields
        self.nameLE = self.nameLineEdit
        self.birthDateE = self.birthDateEdit
        self.genderCB = self.genderComboBox
        self.weighingDateE = self.weighingDateEdit
        
        # Set the weighing date to the current date
        self.weighingDateE.setDate(QtCore.QDate.currentDate()) 
        self.heightSB = self.heightSpinBox
        self.weightSB = self.weightSpinBox
        self.neckSB =  self.neckSpinBox
        self.waistSB = self.waistSpinBox 
        self.hipSB = self.hipSpinBox
        
        self.calculatePB = self.calculatePushButton
        self.calculatePB.clicked.connect(self.calculateAll)

        self.savePB = self.savePushButton
        self.savePB.clicked.connect(self.saveData)

    # Define slots ie methods

    # Calculates BMI, Finnish and US fat percentages and updates corresponding labels
    def calculateAll(self):
        height = self.heightSB.value() # Spinbox value as an integer
        weight = self.weightSB.value()
        
        # Convert birthday to ISO string using QtCore's methods
        birthday = self.birthDateE.date().toSring(format=QtCore.Qt.ISODate)
        
        # Set Gender Value according to ComboBox value
        gendertext = self.genderCB.currentText()
        if gendertext == 'Mies':
            gender = 1
            
        else:
            gender = 0
            
        # Convert weighing day to ISO string
        dateOfWeighing = self.weighingDateE.date().toString(format=QtCore.Qt.ISODate)
        
        # Calculate time difference using our home made tools
        age = timetools.datediff2(birthday, dateOfWeighing, 'year') 
        
        # Create an athlete from Kuntoilija class
        # athlete = kuntoilija.Kuntoilija()
        # bmi = athlete.bmi

        self.bmiLabel.setText(dateOfWeighing)

    # Saves data to disk
    def saveData(self):
        pass

if __name__ == "__main__":
    # Create the application
    app = QtWidgets.QApplication(sys.argv)

    # Create the Main Window object from MainWindow class and show it on the screen
    appWindow = MainWindow()
    appWindow.show()
    sys.exit(app.exec())