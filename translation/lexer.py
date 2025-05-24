import re

class Lexer:

    KEYWORDS = {
    "INICIO", "FIN", "SI", "SINO", "ENTONCES", "FIN_SI", "INGRESAR",
    "IMPRIMIR", "VARIABLE", "MIENTRAS", "HACER", "FIN_MIENTRAS",
    "PARA", "DESDE", "HASTA", "FIN_PARA", "NUMERO", "DECIMAL"
}
    TYPES = {"NUMERO", "DECIMAL", "FLOTANTE", "CADENA"}

    OPERATORS = {"=", ">", "<", "+", "-", "*", "/", "%", ">=", "<="}
    STRING_PATTERN = r'"[^"]*"'  # Detectar cadenas
    NUMBER_PATTERN = r"\b\d+\b"   # Detectar números
    IDENTIFIER_PATTERN = r"\b[a-zA-Z_][a-zA-Z0-9_]*\b"  # Variables y palabras clave

    def __init__(self, code):
        self.code = code
        self.tokens = []

    def convert_to_tokens(self):
        words = re.findall(r'"[^"]*"|\b\w+\b|>=|<=|[=><+\-*/%]', self.code)

        for word in words:
            if word in self.TYPES:
                self.tokens.append(("TYPE", word))
            elif word in self.KEYWORDS:
                self.tokens.append(("KEYWORD", word))
            elif word in self.OPERATORS:
                self.tokens.append(("OPERATOR", word))
            elif re.fullmatch(self.NUMBER_PATTERN, word):
                self.tokens.append(("NUMBER", int(word)))
            elif re.fullmatch(self.STRING_PATTERN, word):
                self.tokens.append(("STRING", word))
            elif re.fullmatch(self.IDENTIFIER_PATTERN, word):
                self.tokens.append(("IDENTIFIER", word))
            else:
                raise ValueError(f"Token desconocido: {word}")

        return self.tokens
    

if __name__ == "__main__":
    code = """
    INICIO
        VARIABLE i = 0
        MIENTRAS i < 5 HACER
            IMPRIMIR "Hola"
            i = i + 1
        FIN_MIENTRAS
    FIN
    """
    lexer = Lexer(code)
    tokens = lexer.convert_to_tokens()
    print("Tokens:")
    for token in tokens:
        print(token)