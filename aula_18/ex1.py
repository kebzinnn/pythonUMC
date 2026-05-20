# 1) Elaborar um programa para adicionar um novo par chave-valor ao dicionário, modificar um valor existente e 
# acessar uma chave específica. 

from dados import dados

print(dados)
chave, valor = input("Digite uma chave-valor para adicionar ou modificar (** valor ** chave) **: ").split()

dados[chave] = valor
print(dados)

n3 = input("Digite uma chave para acessar o valor: ")
print(dados[chave])


 