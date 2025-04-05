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
                    self.ruby_code.append("# Inicio del programa en Ruby\n")
                elif value == "FIN":
                    self.ruby_code.append("\n# Fin del programa")
                elif value == "VARIABLE":
                    i += 1  # Ir al nombre de la variable
                    var_name = self.tokens[i][1]
                    
                    # Verificar si viene una asignación con "="
                    if i + 1 < len(self.tokens) and self.tokens[i + 1][1] == "=":
                        i += 2  # Saltar el "="
                        value = self.tokens[i][1]
                        self.ruby_code.append(f"{var_name} = {value}")
                    else:
                        # Si no hay asignación, inicializar como nil
                        self.ruby_code.append(f"{var_name} = nil")

                elif value == "INGRESAR":
                    i += 1
                    var_name = self.tokens[i][1]
                    self.ruby_code.append(f"{var_name} = gets.chomp")
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
                elif value == "MIENTRAS":
                    i += 1
                    condition = []
                    while self.tokens[i][1] != "HACER":
                        condition.append(str(self.tokens[i][1]))
                        i += 1
                    ruby_condition = " ".join(condition)
                    self.ruby_code.append(f"while {ruby_condition}")
                elif value == "FIN_MIENTRAS":
                    self.ruby_code.append("end")

            elif token_type == "IDENTIFIER":
                # Detectar patrón: variable = valor o expresión
                var_name = value
                if (i + 1 < len(self.tokens) and self.tokens[i + 1][1] == "="):
                    i += 2  # Saltar el "="
                    expr = []
                    while i < len(self.tokens) and self.tokens[i][0] not in ["KEYWORD"]:
                        expr.append(str(self.tokens[i][1]))
                        i += 1
                    i -= 1  # Ajustar para no saltar el siguiente token en el while principal
                    ruby_expr = " ".join(expr)
                    self.ruby_code.append(f"{var_name} = {ruby_expr}")
            
            elif token_type == "OPERATOR":
                self.ruby_code.append(f"{value}")

            i += 1  # Avanzar al siguiente token
        
        return "\n".join(self.ruby_code)

