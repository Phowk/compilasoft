import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from welcome import Ui_Welcome 
from ui_main_window import Ui_MainWindow  

class Inicio(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Welcome()  # Carga la UI de la ventana de inicio
        self.ui.setupUi(self)

        
        self.ui.continuar.clicked.connect(self.abrir_main_window)

    def abrir_main_window(self):
        self.main_window = MainWindow()  
        self.main_window.show()  
        self.close()  


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana_inicio = Inicio()  
    ventana_inicio.show()  

    sys.exit(app.exec())  # Inicia la aplicación
