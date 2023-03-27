# MAIN WINDOW FOR FITNESS APPLICATION
# ===================================

# LIBRARIES AND MODULES
from PyQt6 import QtCore # Core functionality of Qt
from PyQt6 import QtWidgets # UI elements functionality
from PyQt6.uic.load_ui import loadUi
import sys

# Class for the main window
class MainWindow(QtWidgets.QMainWindow):
    """MainWindow for the fitness app"""
    
    # Constructor for the main window
    def __init__(self):
        super().__init__()

        # Load the UI file
        loadUi('main.ui')

        # Define UI Controls ie buttons and input fields
        self.calculateButton = self.calculatePushButton
        self.calculateButton.clicked.connect(self.calculateAll)
        
    # Define slots ie methonds
    def calculateAll(self):
        self.bmiBox.setValue('100')

if __name__ == '__main__':

    # Create the application
    app = QtWidgets.QApplication(sys.argv)

    # Create the Main Window object from MainWindow class and show it on the screen
    appWindow = MainWindow()
    appWindow.main.show()
    sys.exit(app.exec())

    # Create the mainwindow (and show it)


    # Start the application