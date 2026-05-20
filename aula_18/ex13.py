# 13) Elaborar um programa para mesclar dois dicionários de forma que, quando ambos compartilharem a mesma chave, 
# seus valores sejam somados em vez de um sobrescrever o outro.

#
dicionario1 = {"v6": 1, "v1": 30, "v5": 2}
dicionario2 = {"v1": 1, "v2": 20, "v3": 40}
dicionario3 = dicionario1.copy

for chave, valor in dicionario2.items():
    if chave in dicionario3:
        dicionario3[chave] = valor + dicionario2.get(valor)
    else:
        dicionario3[chave] = valor

print(dicionario3)





# dicionario1.update(dicionario2)
# print(dicionario2)
# 

# def mesclar_dicionarios(dicionario1:dict, dicionario2:dict):
#     return dicionario1.update(dicionario2)