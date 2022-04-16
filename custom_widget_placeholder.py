# Importing necessary class:
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QColor, QPalette

class Color(QWidget):
    def __init__(self,color):
        super().__init__()
        # Turn on The auto fill background attribute:
        self.setAutoFillBackground(True)
        # Create the palette (wrap)
        palette = self.palette()
        # Set Color for the palette & the purpose of that palette:
        palette.setColor(QPalette.Window, QColor(color))
        # Set the palette to QWigdet:
        self.setPalette(palette)