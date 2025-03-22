from PySide6.QtWidgets import QApplication, QMainWindow
from ui_main_window import Ui_MainWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)

    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec())
