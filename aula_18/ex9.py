# 9) Elaborar um programa que solicite ao usuário para informar um valor e verifique se esse valor existe em algum 
# dos pares do dicionário. Se existir, exiba todas as chaves que possuem esse valor; caso não exista, exiba uma 
# mensagem indicando que o valor não foi encontrado.

dados = {
    "nome": "Sandro",
    "idade": 30,
    "cidade":"Sao Paulo",
    "estado":"Sao Paulo"

}

valor = input("Digite um valor existente: ")

if valor in dados.values():
    print("Valor existente.")
    print("Chaves que possuem esse valor: " )
    for k, v in dados.items():
        if v == valor:
            print(k)
else:
    print("Valor inexistente.")