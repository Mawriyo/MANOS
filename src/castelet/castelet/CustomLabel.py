from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt, pyqtSignal, QRect
from PyQt5.QtGui import QPainter, QPen

class CalibrationLabel(QLabel):
    rightClicked = pyqtSignal()
    leftClicked = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFocusPolicy(Qt.StrongFocus)
        self.drawing = False 
        self.rect_start = None
        self.rect_end = None
        self.setMouseTracking(True)
        
    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            print("huh")
            self.rightClicked.emit()  # Emit right-click signal
        elif event.button() == Qt.LeftButton:
            if event.modifiers() == Qt.ShiftModifier:
                self.drawing = True
                self.rect_start = event.pos()
                self.rect_end = event.pos()
            else:
                self.leftClicked.emit()  # Emit left-click signal

    def mouseMoveEvent(self, event):
        if self.drawing:
            self.rect_end = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if self.drawing:
            self.drawing = False
            self.rect_end = event.pos()
            self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.drawing and self.rect_start and self.rect_end:
            painter = QPainter(self)
            painter.setPen(QPen(Qt.green, 2, Qt.SolidLine))
            rect = QRect(self.rect_start, self.rect_end)
            painter.drawRect(rect)