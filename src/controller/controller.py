from view.rootLayout import RootLayout
from PyQt6.QtCore import QTimer
import math
from .player import Player
from utils.index import trans_date_str_to_second


class RootController():
    def __init__(self, ui: RootLayout) -> None:
        self.timer = QTimer()
        self.ui = ui
        self.player = Player()
        self.setup_listener()

    def setup_listener(self):
        self.ui.spin_box.textChanged.connect(self.on_spin_box_changed)
        self.ui.start_btn.clicked.connect(self.on_start_btn_clicked)
        self.ui.stop_btn.clicked.connect(self.on_stop_btn_clicked)
        self.ui.reset_btn.clicked.connect(self.on_reset_btn_clicked)
        self.timer.timeout.connect(self.when_timer_timeout)

    def on_spin_box_changed(self, val: str):
        try:
            min = int(val)
            self.set_time_label_text(min*60)
        except ValueError:
            return

    def on_start_btn_clicked(self):
        self.ui.spin_box.setDisabled(True)
        self.ui.reset_btn.setDisabled(True)
        self.ui.stop_btn.setDisabled(False)
        self.ui.start_btn.setDisabled(True)
        self.timer.setInterval(1000)
        self.timer.start()

    def on_stop_btn_clicked(self):
        self.ui.spin_box.setDisabled(True)
        self.ui.reset_btn.setDisabled(False)
        self.ui.stop_btn.setDisabled(True)
        self.ui.start_btn.setDisabled(False)
        self.timer.stop()
        if self.ui.remind_dialog.isVisible():
            self.ui.remind_dialog.close()

    def on_reset_btn_clicked(self):
        self.ui.spin_box.setDisabled(False)
        self.ui.reset_btn.setDisabled(False)
        self.ui.stop_btn.setDisabled(True)
        self.ui.start_btn.setDisabled(False)
        self.timer.stop()
        minute = self.get_spin_box_value()
        self.set_time_label_text(minute*60)

    def get_spin_box_value(self):
        return self.ui.spin_box.value()

    def when_timer_timeout(self):
        prev_second = trans_date_str_to_second(self.ui.time_label.text())
        if prev_second == 'error':
            return
        elif prev_second == 1:
            self.total_time_out()
        else:
            self.set_time_label_text(prev_second-1)
        if prev_second == 60:
            self.play_music()
        if prev_second <= 60 and prev_second > 1:
            self.set_dialog_time_label(prev_second-1)

    def play_music(self):
        self.player.play()

    def remind_dialog_is_show(self):
        return self.ui.remind_dialog.isVisible()

    def show_remind_dialog(self):
        self.ui.remind_dialog.show_self()

    def set_time_label_text(self, total_second: int):
        min = math.floor(total_second/60)
        second = total_second % 60
        min_str = str(min)
        second_str = str(second)
        text = f'{min_str if len(min_str) ==2 else "0"+min_str}:{second_str if len(second_str) ==2 else "0"+second_str}'
        self.ui.time_label.setText(text)

    def set_dialog_time_label(self, second: int):
        dialog = self.ui.remind_dialog
        dialog.show_self()
        dialog.set_text(str(second))

    def total_time_out(self):
        self.ui.remind_dialog.close_self()
        self.on_reset_btn_clicked()
        self.set_time_out_dialog_full_screen()

    def set_time_out_dialog_full_screen(self):
        self.ui.time_out_dialog.showMaximized()
        self.ui.time_out_dialog.activateWindow()
