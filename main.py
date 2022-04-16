# Import necessary modules and classes:
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget,QStackedLayout,QPushButton,QVBoxLayout,QHBoxLayout,QLabel)
from custom_widget_placeholder import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initialize_ui()
        self.show()
    
    def initialize_ui(self):
        """
        Initalize the main window and display its content.
        """
        self.setWindowTitle("Stack Layout PyQt5")
        self.setGeometry(40, 40, 800, 700)