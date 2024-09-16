from enum import Enum

class Unidade_federativa(Enum):
    BAHIA = ("Bahia", "BA")
    RIO_DE_JANEIRO = ("Rio de janeiro", "RJ")
    SAO_PAULO = ("São Paulo","SP")
    def __init__(self, texto: str, caracter: str) -> None:
        self.texto = texto
        self.caracter = caracter
    
    