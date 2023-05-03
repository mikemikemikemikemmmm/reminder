from PyQt6.QtWidgets import QMainWindow
from controller.controller import RootController
from .rootLayout import RootLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCloseEvent


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        self.initControl(self.ui)
        self.setWindowTitle('計時器')
        self.setWindowFlags(Qt.WindowType.MSWindowsFixedSizeDialogHint)

    def minimumSize(self):
        return super().minimumSize()
    def initUI(self):
        self.ui = RootLayout()
        self.setCentralWidget(self.ui)

    def initControl(self, ui: RootLayout):
        self.root_controller = RootController(ui)

    def closeEvent(self, a0:QCloseEvent):
        for dialog in self.ui.child_dialog:
            dialog.close()
        super().closeEvent(a0)