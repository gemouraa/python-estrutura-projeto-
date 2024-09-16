from models.enums.sexo import Sexo
from models.endereco import Endereco
from models.enums.unidade_federativa import Unidade_federativa
class Pessoa:
    def __init__(self,nome: str, idade: int, sexo: Sexo, endereco: Endereco, unidade: Unidade_federativa) -> None:
     self.nome = nome
     self.idade = idade
     self.sexo = sexo
     self.endereco = endereco
     self.unidade = unidade
    
    def __str__(self) -> str:
       return (
                f"\nNome: {self.nome}"
                f"\nIdade: {self.idade}"
                f"\nSexo: {self.sexo.texto}"
                f"\nSexo: {self.sexo.caracter}"
                f"\nendereco: {self.endereco}"
                f"\nUnidade Federativa: {self.unidade.texto}"
                f"\nUnidade Federativa: {self.unidade.caracter}"
                
                
                ) 