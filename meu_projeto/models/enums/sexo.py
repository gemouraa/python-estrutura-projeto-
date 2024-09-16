from enum import Enum

class Sexo(Enum):
    MASCULINO = ("Masculino", "F")
    FEMININO = ("Feminino", "F")
    
    def __init__(self, texto: str, caracter: str) -> None:
        self.texto = texto
        self.caracter = caracter
    
    

