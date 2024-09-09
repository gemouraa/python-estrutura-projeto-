import os

from models.enums.sexo import Sexo
from models.pessoa import Pessoa
from models.endereco import Endereco

os.system("cls || clear")

#instanciando classe
pessoa_1 = Pessoa("Moura", 22,Sexo.MASCULINO, Endereco("Rua anisio Goncalves",115))
print(pessoa_1)