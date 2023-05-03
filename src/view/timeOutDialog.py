from PyQt6.QtWidgets import QDialog, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt

class TimeOutDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('時間到囉')
        self.label = QLabel('時間到囉')
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("color:black; font-size:100px")
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)