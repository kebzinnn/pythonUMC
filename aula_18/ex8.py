# 8) Elaborar um programa que permite o usuário informar uma chave a ser removida. Remova do dicionário o par 
# referente a essa chave, caso ela exista. Se a chave informada não estiver no dicionário, exiba uma mensagem 
# de aviso. Mostre o dicionário atualizado após a operação

dados = {
    "nome": "Sandro",
    "idade": 30,
    "cidade":"Sao Paulo",
    "estado":"Sao Paulo"

}

print(dados)

chave_removida = input("Digite uma chave a ser removida: ")

if chave_removida not in dados.keys():
    print("Chave inexistente.")
elif chave_removida in dados.keys():
    dados.pop(chave_removida)
    print(dados) 


