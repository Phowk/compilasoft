import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from welcome import Ui_Welcome
from ui_main_window import Ui_MainWindow
from traducir_ui import Ui_Traducir  # Importar la UI de la ventana traducir
from translation.lexer import Lexer
from translation.ruby_code import RubyGenerator

class TraducirWindow(QMainWindow):
    def __init__(self, translated_code):
        super().__init__()
        self.ui = Ui_Traducir()  # Cargar la interfaz de traducir.ui
        self.ui.setupUi(self)
        self.ui.textEdit.setPlainText(translated_code)  # Mostrar la traducción en la ventana

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

        # Conectar el botón "Ejecutar" con la función para mostrar la traducción
        self.ui.ejecutar_bt.clicked.connect(self.mostrar_traduccion)

    def mostrar_traduccion(self):
        # Obtener el código del QTextEdit
        pseudocodigo = self.ui.Code_space.toPlainText()

        # Procesar el pseudocódigo con el lexer y generar código Ruby
        lexer = Lexer(pseudocodigo)
        tokens = lexer.convert_to_tokens()
        ruby_generator = RubyGenerator(tokens)
        ruby_code = ruby_generator.generate()

        # Mostrar la ventana de traducción con el código Ruby
        self.traducir_window = TraducirWindow(ruby_code)
        self.traducir_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana_inicio = Inicio()  # Iniciar la ventana de bienvenida
    ventana_inicio.show()

    sys.exit(app.exec())  # Iniciar la aplicación
