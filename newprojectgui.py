import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("New Project")
        self.setFixedSize(QSize(700, 600))
        app.setWindowIcon(QIcon("icon.jpeg"))


app = QApplication(sys.argv)

window = MainWindow()
window.show()


if __name__ == "__main__":
    app.setWindowIcon(QIcon("icon.png"))
    app.exec()


