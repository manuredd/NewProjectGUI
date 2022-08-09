from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("New Project")
        self.setWindowIcon("icon.jpeg")


app = QApplication(sys.argv)

window = QMainWindow()
window.show()


if __name__ == "__main__":
    app.exec()


