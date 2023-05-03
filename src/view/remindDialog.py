from PyQt6.QtWidgets import QDialog, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt
# from PyQt6.QtGui import QFont


class RemindDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('時間快到囉')
        self.label = QLabel('還剩下60秒')
        self.label.setStyleSheet("color:black; font-size:30px")
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)
        self.setFixedWidth(self.sizeHint().width())

    def show_self(self):
        if not self.isVisible():
            self.show()
        if not self.isActiveWindow():
            self.activateWindow()
            self.raise_()
    def set_text(self, second: str):
        self.label.setText(f'還剩下{second}秒')
    def close_self(self):
        self.close()
