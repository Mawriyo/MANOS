from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtCore import Qt,QPoint,QRect

class CalibrationLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFocusPolicy(Qt.StrongFocus)
        self.drawing = False
        self.rect_start = None
        self.rect_end = None
        self.final_rect = None  # Store the final rectangle here
        self.setMouseTracking(True)
        self.xmin = float(0)
        self.xmax = float(480)
        self.ymin = float(0)
        self.ymax = float(680)

    def mousePressEvent(self, event):
        if event.modifiers() == Qt.ShiftModifier:
            self.drawing = True
            self.rect_start = event.pos()
            self.rect_end = event.pos()

    def mouseMoveEvent(self, event):
        if self.drawing:
            self.rect_end = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if self.drawing:
            self.drawing = False
            self.rect_end = event.pos()
            self.final_rect = QRect(self.rect_start, self.rect_end)
            self.updateRectangleCoordinates()  # Update coordinates here
            self.update()

    def updateRectangleCoordinates(self):
        if self.final_rect:
            self.xmin = float(self.final_rect.left())
            self.xmax = float(self.final_rect.right())
            self.ymin = float(self.final_rect.top())
            self.ymax = float(self.final_rect.bottom())
            
    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setPen(QPen(Qt.green, 2, Qt.SolidLine))
        if self.drawing and self.rect_start and self.rect_end:
            temp_rect = QRect(self.rect_start, self.rect_end)
            painter.drawRect(temp_rect)
        elif self.final_rect:
            painter.drawRect(self.final_rect)
            
    def getRectangleCoordinates(self):
        if self.final_rect:
            xmin = self.final_rect.left()
            xmax = self.final_rect.right()
            ymin = self.final_rect.top()
            ymax = self.final_rect.bottom()

            return {'xmin': xmin, 'xmax': xmax, 'ymin': ymin, 'ymax': ymax}
        else:
            return None