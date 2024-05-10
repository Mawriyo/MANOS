#https://forum.qt.io/topic/57462/fading-out-a-qlabel
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtWidgets import QLabel, QApplication
from PyQt5.QtCore import QTimer, Qt, QPropertyAnimation, pyqtSignal, pyqtSlot, QPoint
class Toast(QLabel):
    animationFinished = pyqtSignal()

    def __init__(self, parent=None, message="", timeout=3000):
        super().__init__(parent)
        self.setText(message)
        self.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint)
        self.setStyleSheet("background-color: rgba(0,0,0,160); color: white; border-radius: 8px; padding: 10px;")
        self.setWindowOpacity(0.0)  # Start fully transparent
        self.adjustSize()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.fadeOut)
        self.fadeInAnimation = QPropertyAnimation(self, b"windowOpacity")
        self.fadeInAnimation.setDuration(500)  # Duration in milliseconds
        self.fadeInAnimation.setStartValue(0.0)
        self.fadeInAnimation.setEndValue(0.9)
        self.fadeOutAnimation = QPropertyAnimation(self, b"windowOpacity")
        self.fadeOutAnimation.setDuration(500)  # Duration in milliseconds
        self.fadeOutAnimation.setStartValue(0.9)
        self.fadeOutAnimation.setEndValue(0.0)
        self.fadeOutAnimation.finished.connect(self.animationFinished.emit)

    def show(self, parent=None):
        if parent:
            parent_rect = parent.geometry()
            parent_bottom_center = parent_rect.bottomLeft() + QPoint(parent_rect.width() / 2, 0)
            toast_position = QPoint(parent_bottom_center.x() - self.rect().width() / 2, parent_bottom_center.y() - self.rect().height())
            self.move(toast_position)
        super().show()
        self.fadeInAnimation.start()
        self.timer.start(3000)  # Time displayed before starting to fade out

    @pyqtSlot()
    def fadeOut(self):
        self.fadeOutAnimation.start()