from PyQt6.QtWidgets import QVBoxLayout,QSpinBox,QHBoxLayout,QLabel,QWidget,QPushButton,QDialog
from .remindDialog import RemindDialog
from .timeOutDialog import TimeOutDialog
class RootLayout(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.layout = QVBoxLayout() 
        self.setLayout(self.layout)
        self.layout.addWidget(self.create_spin_box_input())
        self.layout.addWidget(self.create_btns())
        self.initChild()
        
    def initChild(self):
        self.child_dialog:list[QDialog] = []
        self.remind_dialog = RemindDialog()
        self.time_out_dialog = TimeOutDialog()
        self.child_dialog.append(self.remind_dialog)
        self.child_dialog.append(self.time_out_dialog)

    def create_spin_box_input(self)->QWidget:
        self.spin_box = QSpinBox()
        self.spin_box.setValue(1)
        self.spin_box.setMinimum(1)
        self.spin_box.setMaximum(60)
        self.spin_box.setFixedWidth(40)
        self.min_label =QLabel('分鐘')
        self.time_pre_text = QLabel("剩餘時間")
        self.time_label = QLabel("01:00")
        layout = QHBoxLayout()
        layout.addWidget(self.spin_box)
        layout.addWidget(self.min_label)
        layout.addWidget(self.time_pre_text)
        layout.addWidget(self.time_label)
        container = QWidget()
        container.setLayout(layout)
        return container
    def create_btns(self)->QWidget:
        self.start_btn = QPushButton('開始')
        self.stop_btn = QPushButton('暫停')
        self.stop_btn.setDisabled(True)
        self.reset_btn =  QPushButton('重設')
        layout = QHBoxLayout()
        layout.addWidget(self.start_btn)
        layout.addWidget(self.stop_btn)
        layout.addWidget(self.reset_btn)
        container = QWidget()
        container.setLayout(layout)
        return container