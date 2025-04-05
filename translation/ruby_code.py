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

                    if i + 1 < len(self.tokens) and self.tokens[i + 1][1] == "=":
                        i += 2  # Saltar el "="
                        expr = []
                        while i < len(self.tokens) and self.tokens[i][0] not in ["KEYWORD"]:
                            expr.append(str(self.tokens[i][1]))
                            i += 1
                        i -= 1  # retroceder porque el while principal también incrementa
                        ruby_expr = " ".join(expr)
                        self.ruby_code.append(f"{var_name} = {ruby_expr}")
                    else:
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
                elif value == "PARA":
                    i += 1
                    var_name = self.tokens[i][1]  # nombre de la variable
                
                    # Validar "DESDE"
                    i += 1
                    if self.tokens[i][1] == "DESDE":
                        i += 1
                        start_value = self.tokens[i][1]
                    else:
                        raise SyntaxError("Se esperaba 'DESDE' después de PARA")
                
                    # Validar "HASTA"
                    i += 1
                    if self.tokens[i][1] == "HASTA":
                        i += 1
                        end_value = self.tokens[i][1]
                    else:
                        raise SyntaxError("Se esperaba 'HASTA' después de DESDE")
                
                    # Validar "HACER"
                    i += 1
                    if self.tokens[i][1] == "HACER":
                        pass
                    else:
                        raise SyntaxError("Se esperaba 'HACER' después de HASTA")
                
                    self.ruby_code.append(f"for {var_name} in {start_value}..{end_value}")


            elif token_type == "IDENTIFIER":
                var_name = value
                if (i + 1 < len(self.tokens) and self.tokens[i + 1][1] == "="):
                    i += 2  # saltar "="
                    expr = []
                    while i < len(self.tokens) and self.tokens[i][0] not in ["KEYWORD"]:
                        expr.append(str(self.tokens[i][1]))
                        i += 1
                    i -= 1
                    ruby_expr = " ".join(expr)
                    self.ruby_code.append(f"{var_name} = {ruby_expr}")
                    
            i += 1  # Avanzar al siguiente token
        
        return "\n".join(self.ruby_code)

