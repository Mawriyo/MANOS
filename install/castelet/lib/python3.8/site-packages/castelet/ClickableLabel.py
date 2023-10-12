import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget


class ClickableLabel(QLabel):
    def __init__(self, text):
        super().__init__(text)
        self.setCursor(Qt.PointingHandCursor)  # Change the cursor to a pointing hand
        self.setStyleSheet("color: blue; text-decoration: underline;")  # Make the label look like a clickable link

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.emitClickedSignal()

    def emitClickedSignal(self):
        self.clicked.emit()
