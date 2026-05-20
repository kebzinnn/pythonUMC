# 7) Elaborar um programa que leia uma nova chave e um valor do usuário e os adicione ao dicionário. 
# Caso a chave já exista, atualize o valor existente para o novo valor fornecido. No final, exiba o dicionário resultante.

dados = {
    "nome": "Sandro",
    "idade": 30,
    "cidade":"Sao Paulo",
    "estado":"Sao Paulo"

}

print(dados)

newkey = input("Digite uma nova chave: ")
newvalue = input("Digite um valor para a nova chave: ")     

dados[newkey] = newvalue
print(dados)
