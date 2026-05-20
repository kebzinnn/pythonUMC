# 6) Elaborar um programa que solicite ao usuário para digitar uma chave e verifique se essa chave existe no 
# dicionário. Se a chave existir, exiba o valor correspondente; caso contrário, mostre uma mensagem informando 
# que a chave não foi encontrada. 

dados = {
    "nome": "Sandro",
    "idade": 30,
    "cidade":"Sao Paulo",
    "estado":"Sao Paulo"

}

'''

a = input("Digite uma chave existente: ")

chaves = dados.keys()

if a in chaves:
    print(dados[a])
else:
    print("chave nao encontrado")
'''
print(dados)
chave = input("Digite uma chave existente para exibir o valor: ")
print(dados.get(chave, "Esta chave não existe."))