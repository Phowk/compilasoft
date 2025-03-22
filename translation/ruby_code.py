class RubyGenerator:
    def __init__(self, tokens):
        self.tokens = tokens
        self.ruby_code = []

    def generate(self):
        i = 0
        while i < len(self.tokens):
            token_type, value = self.tokens[i]

            if token_type == "KEYWORD":
                if value == "INICIO":
                    self.ruby_code.append("# Inicio del programa en Ruby")
                elif value == "FIN":
                    self.ruby_code.append("# Fin del programa")
                elif value == "VARIABLE":
                    i += 1  # Ir al identificador de la variable
                    var_name = self.tokens[i][1]
                    i += 1  # Ir al operador "="
                    
                    if self.tokens[i][1] == "=":  # Confirmar que es un operador de asignación
                        i += 1  # Moverse al valor real de la variable
                
                    value = self.tokens[i][1]  # Ahora sí obtiene el valor correcto
                    self.ruby_code.append(f"{var_name} = {value}")

                elif value == "SI":
                    i += 1
                    condition = []
                    while self.tokens[i][1] != "ENTONCES":
                        condition.append(str(self.tokens[i][1]))  # Convertir a string
                        i += 1
                    ruby_condition = " ".join(condition)
                    self.ruby_code.append(f"if {ruby_condition}")
                elif value == "ENTONCES":
                    self.ruby_code.append("  # Código dentro del if")
                elif value == "IMPRIMIR":
                    i += 1
                    text = self.tokens[i][1]
                    self.ruby_code.append(f'puts {text}')
                elif value == "FIN_SI":
                    self.ruby_code.append("end")
            
            i += 1  # Avanzar al siguiente token
        
        return "\n".join(self.ruby_code)

