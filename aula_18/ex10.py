# 10) Elaborar um programa que obtenha todas as chaves do dicionário e as armazene em uma lista, e faça o 
# mesmo com todos os valores do dicionário, armazenando-os em outra lista. Ao final, exiba as duas listas (lista 
# de chaves e lista de valores).

dados = {
    "nome": "Sandro",
    "idade": 30,
    "cidade":"Sao Paulo",
    "estado":"Sao Paulo"

}

listak = dados.keys()
listav = dados.values()

listak = list(listak)
listav = list(listav)

print(f"Lista de chaves: {listak} \nLista de valores: {listav}")
#aa