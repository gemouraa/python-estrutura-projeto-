from models.enums.unidade_federativa import Unidade_federativa

class Endereco:
    def __init__(self,logradouro: str, numero: int,unidade: Unidade_federativa) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.unidade = unidade
        
        
    def __str__(self) -> str:
        return (f"\nLogradouro: {self.logradouro}"
                f"\nNúmero: {self.numero}"
                f"\nUnidade Federativa: {self.unidade.texto}"
                f"\nUnidade Federativa: {self.unidade.caracter}")    
        
        
     