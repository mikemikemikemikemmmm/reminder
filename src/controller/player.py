from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtCore import QUrl
import os


class Player(QMediaPlayer):
    def __init__(self) -> None:
        super().__init__()
        self._audio = QAudioOutput()
        self.setAudioOutput(self._audio)
        current_path = os.path.abspath(__file__)
        dir_path = os.path.dirname(os.path.dirname(current_path))
        mp3_path = os.path.join(dir_path, "assets", "time.mp3")
        url = QUrl.fromLocalFile(mp3_path)
        self.setSource(url)
