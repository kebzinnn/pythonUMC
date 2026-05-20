#4) Elaborar um programa para renomear uma chave existente do dicionário, preservando seu valor associado e 
# mantendo o restante do dicionário inalterado. Exibir o novo dicionário. 
dados = {
    "nome": "Sandro",
    "idade": 30,
    "cidade":"Sao Paulo",
    "estado":"Sao Paulo"

}

oldkey = input("Digite uma chave para renomear: ")

if oldkey in dados:
    newkey = input("Digite a nova chave: ")
    dados[newkey] = dados.pop(oldkey)

print(dados)


