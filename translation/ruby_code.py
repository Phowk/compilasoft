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
                        while i < len(self.tokens):
                            # Si empieza una nueva asignación, detenemos
                            if (
                                self.tokens[i][0] == "IDENTIFIER" and 
                                i + 1 < len(self.tokens) and self.tokens[i + 1][1] == "="
                            ):
                                break
                            # Si viene una palabra clave que indica otra estructura
                            if self.tokens[i][0] == "KEYWORD":
                                break
                            expr.append(str(self.tokens[i][1]))
                            i += 1
                        i -= 1  # retroceder porque el while principal también incrementa
                        ruby_expr = " ".join(expr)
                        self.ruby_code.append(f"{var_name} = {ruby_expr}")
                    else:
                        self.ruby_code.append(f'{var_name} = ""')

                elif value == "INGRESAR":
                    i += 1
                    var_name = self.tokens[i][1]
                    input_conversion = ".chomp"

                    # Verifica si hay un tercer token (el tipo)
                    if i + 1 < len(self.tokens) and self.tokens[i + 1][0] == "TYPE":
                        i += 1
                        tipo = self.tokens[i][1]
                        if tipo == "NUMERO":
                            input_conversion += ".to_i"
                        elif tipo == "DECIMAL":
                            input_conversion += ".to_f"
                        # podrías agregar más casos como .to_s si lo deseas

                    self.ruby_code.append(f"{var_name} = gets{input_conversion}")

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
                    expr = []
                    while i < len(self.tokens):
                        token_type, token_val = self.tokens[i]

                        # Si empieza una nueva asignación, detenemos
                        if (
                            token_type == "IDENTIFIER" and 
                            i + 1 < len(self.tokens) and self.tokens[i + 1][1] == "="
                        ):
                            i -= 1  # Retroceder porque el while principal incrementa
                            break
                        
                        # Si viene una palabra clave, terminamos la expresión
                        if token_type == "KEYWORD":
                            i -= 1
                            break
                        
                        if token_type == "IDENTIFIER":
                            # Convertir identificador si hay cadena antes o concatenación
                            if len(expr) >= 1 and (expr[-1] == '+' or '"' in expr[-1]):
                                expr.append(f"{token_val}.to_s")
                            else:
                                expr.append(token_val)
                        else:
                            expr.append(str(token_val))

                        i += 1

                    ruby_expr = " ".join(expr)
                    self.ruby_code.append(f"puts {ruby_expr}")
                elif value == "SINO":
                    self.ruby_code.append("else")
                elif value == "FIN_SI" or value == "FIN_PARA":
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
                        if (
                            self.tokens[i][0] == "IDENTIFIER" and 
                            i + 1 < len(self.tokens) and self.tokens[i + 1][1] == "="
                        ):
                            break
                        # Si viene una palabra clave que indica otra estructura
                        if self.tokens[i][0] == "KEYWORD":
                            break
                        expr.append(str(self.tokens[i][1]))
                        i += 1
                    i -= 1
                    ruby_expr = " ".join(expr)
                    self.ruby_code.append(f"{var_name} = {ruby_expr}")
                            
            i += 1  # Avanzar al siguiente token
        self.ruby_code.append("""
                              require 'io/console'
puts
puts "----------------------------------"
puts "Presiona una tecla para cerrar..."
STDIN.getch  # Espera una tecla sin necesidad de presionar Enter
                              """)
        return "\n".join(self.ruby_code)

