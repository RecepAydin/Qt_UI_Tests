import sys

from PySide6.QtCore import QLoggingCategory
from PySide6.QtWidgets import QApplication

from mainwindow import MainWindow


if __name__ == "__main__":
    QLoggingCategory.setFilterRules("qt.speech.tts=true\nqt.speech.tts.*=true")

    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
