from PyQt6.QtWidgets import QApplication
from view.mainWindow import MainWindow
app = QApplication([])
window = MainWindow()
window.show()
app.setApplicationName("Text Editor")
app.exec()
