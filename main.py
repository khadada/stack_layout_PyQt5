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
        self.display_contents()
    
    def display_contents(self):
        """
        Display the widget for the main window
        Like tab widget.
        """
        # Create the main layout for the program
        main_layout = QVBoxLayout()
        # Create buttons layout
        btn_layout = QHBoxLayout()
        # Add the btn layout to the main layout:
        main_layout.addLayout(btn_layout)
        # Create stacked layout 
        # Means multiple widgets in the same space of the main window
        self.stack_layout = QStackedLayout()
        # Create btns && push it to btn_layout
        btn = QPushButton("red")
        btn_layout.addWidget(btn)
        btn.pressed.connect(self.active_lab_1)
        
        btn = QPushButton("blue")
        btn_layout.addWidget(btn)
        btn.pressed.connect(self.active_lab_2)
        
        btn = QPushButton("green")
        btn_layout.addWidget(btn)
        btn.pressed.connect(self.active_lab_3)
        
        # Create Stacked and push it to stacked layout
        self.stack_layout.addWidget(Color("red"))
        self.stack_layout.addWidget(Color("blue"))
        self.stack_layout.addWidget(Color("green"))
        
        # Add stacked layout to the main layout out:
        main_layout.addLayout(self.stack_layout)
        # Create the container that use the main_layout
        container = QWidget()
        # Set the main layout to the container:
        container.setLayout(main_layout)
        # Set the contrainer as central widget for the main window:
        self.setCentralWidget(container)
    
    def active_lab_1(self):
        """
        Change to index of stacked layout [Z-index] to: 0
        """
        self.stack_layout.setCurrentIndex(0)
    def active_lab_2(self):
        """
        Change to index of stacked layout [Z-index] to: 1
        """
        self.stack_layout.setCurrentIndex(1)
    def active_lab_3(self):
        """
        Change to index of stacked layout [Z-index] to: 2
        """
        self.stack_layout.setCurrentIndex(2)

    
    
        