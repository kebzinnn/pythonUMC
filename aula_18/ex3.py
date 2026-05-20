# 3) Elaborar um programa para verificar se todos os valores em um dicionário são distintos (ou seja, se não há 
# duas chaves com o mesmo valor). Exibir mensagem caso exista algum valor repetido ou não.

dados = {
    "nome": "Sandro",
    "idade": 30,
    "cidade":"Sao Paulo",
    "estado":"Sao Paulo"

}

print(list(dados.values()))

valores = list(dados.values())

for k in valores:
    if valores.count(k) > 1:
        print(k)
        print("Valor existe!")
    else:
        print("Valor inexistente.")

        
