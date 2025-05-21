import sys, os
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from welcome import Ui_Welcome
from ui_main_window import Ui_MainWindow
from traducir import Ui_Traducir  # Importar la UI de la ventana traducir
from translation.lexer import Lexer
from translation.ruby_code import RubyGenerator


class TraducirWindow(QMainWindow):
    def __init__(self, translated_code):
        super().__init__()
        self.ui = Ui_Traducir()  # Cargar la interfaz de traducir.ui
        self.ui.setupUi(self)
        self.ui.textEdit.setReadOnly(True)  # Deshabilitar la edición en el textEdit
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
        self.ui.nuevo_bt.clicked.connect(self.confirmar_nuevo_codigo)
        self.ui.guardar_bt.clicked.connect(self.guardar_codigo)

        # Conectar el botón "Ejecutar" con la función para mostrar la traducción
        self.ui.ejecutar_bt.clicked.connect(self.mostrar_traduccion)
        self.ui.input_bt.setDisabled(True)
        self.ui.output_bt.setDisabled(True)
        self.ui.assign_bt.setDisabled(True)
        self.ui.ifthen_bt.setDisabled(True)
        self.ui.while_bt.setDisabled(True)
        self.ui.for_bt.setDisabled(True)

    def mostrar_traduccion(self):
    # Limpiar mensajes anteriores
        self.ui.label.setText("")

        # Obtener el pseudocódigo del QTextEdit
        pseudocodigo = self.ui.Code_space.toPlainText().strip()

        if not pseudocodigo:
            self.ui.label.setText("Error: El campo de codigo esta vacio.")
            return

        try:
            lexer = Lexer(pseudocodigo)
            tokens = lexer.convert_to_tokens()

            # Validaciones adicionales
            self.validar_tokens(tokens)

            ruby_generator = RubyGenerator(tokens)
            ruby_code = ruby_generator.generate()

            self.traducir_window = TraducirWindow(ruby_code)
            self.traducir_window.show()

        except (ValueError, SyntaxError, IndexError) as e:
            self.ui.label.setText(f"Error: {str(e)}")
            
    def validar_tokens(self, tokens):
        pila = []
        variables_definidas = set()

        for i, (tipo, valor) in enumerate(tokens):
            # Verificar definición de variable
            if tipo == "KEYWORD" and valor == "VARIABLE":
                if i + 1 < len(tokens) and tokens[i + 1][0] == "IDENTIFIER":
                    variables_definidas.add(tokens[i + 1][1])

            # Verificar uso de variables no definidas
            if tipo == "IDENTIFIER":
                if i == 0 or tokens[i - 1][1] != "VARIABLE":
                    if valor not in variables_definidas:
                        raise SyntaxError(f"La variable '{valor}' no ha sido definida.")

            # Verificar estructuras anidadas
            if tipo == "KEYWORD":
                if valor in ["SI", "MIENTRAS", "PARA"]:
                    pila.append(valor)
                elif valor in ["FIN_SI", "FIN_MIENTRAS", "FIN_PARA"]:
                    if not pila:
                        raise SyntaxError(f"Estructura de cierre '{valor}' sin apertura.")
                    apertura = pila.pop()
                    esperado = {"FIN_SI": "SI", "FIN_MIENTRAS": "MIENTRAS", "FIN_PARA": "PARA"}[valor]
                    if apertura != esperado:
                        raise SyntaxError(f"Se esperaba cerrar '{apertura}', pero se encontró '{valor}'.")
        if pila:
            raise SyntaxError(f"Falta cerrar la estructura: '{pila[-1]}'")
    
    def confirmar_nuevo_codigo(self):
        contenido = self.ui.Code_space.toPlainText().strip()
        if contenido and contenido != "INICIO\nFIN":
            respuesta = QMessageBox.question(
                self,
                "Confirmar",
                "¿Deseas guardar el código antes de comenzar uno nuevo?",
                QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
                QMessageBox.Cancel
            )

            if respuesta == QMessageBox.Yes:
                guardado = self.guardar_codigo()
                if guardado:  # Solo limpia si se guardó con éxito
                    self.limpiar_editor()
            elif respuesta == QMessageBox.No:
                self.limpiar_editor()
            else:
                # Cancelado: no hacer nada
                return
        else:
            self.limpiar_editor()
            
    def limpiar_editor(self):
        self.ui.Code_space.setPlainText("INICIO\nFIN")

    def guardar_codigo(self):
        # Pedir nombre base del archivo (se usará para ambos archivos)
        nombre_archivo, _ = QFileDialog.getSaveFileName(
            self,
            "Guardar pseudocódigo",
            "",
            "Archivos de texto (*.txt)"
        )

        if nombre_archivo:
            try:
                # Obtener pseudocódigo del QTextEdit
                pseudocodigo = self.ui.Code_space.toPlainText()

                # Guardar pseudocódigo como .txt
                with open(nombre_archivo, "w", encoding="utf-8") as archivo_txt:
                    archivo_txt.write(pseudocodigo)

                # Generar código Ruby
                lexer = Lexer(pseudocodigo)
                tokens = lexer.convert_to_tokens()
                ruby_generator = RubyGenerator(tokens)
                codigo_ruby = ruby_generator.generate()

                # Obtener ruta para archivo .rb (mismo nombre base)
                nombre_base = os.path.splitext(nombre_archivo)[0]
                ruta_ruby = f"{nombre_base}.rb"

                # Guardar código Ruby como .rb
                with open(ruta_ruby, "w", encoding="utf-8") as archivo_rb:
                    archivo_rb.write(codigo_ruby)

                QMessageBox.information(self, "Éxito", "Archivos guardados correctamente.")
                return True

            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo guardar:\n{str(e)}")
                return False
        else:
            return False  # El usuario canceló







if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana_inicio = Inicio()  # Iniciar la ventana de bienvenida
    ventana_inicio.show()

    sys.exit(app.exec())  # Iniciar la aplicación
