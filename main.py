import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel

from src.view.main_window import MainWindow

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())