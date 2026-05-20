# 12) Elaborar um programa que tenha que ler do usuário 5 pares de informações (nome e idade). 
# Crie um dicionário esses dados fornecidos e, ao final, imprima o dicionário.

dados = {}

for k in range(5):
    nome = input("Digite um nome: ")
    idade = input("Digite uma idade: ")

    # dados[nome] = idade 
    dados[k] = (nome, idade) #nao substitui os valores pois define a posição [k]

print(dados)