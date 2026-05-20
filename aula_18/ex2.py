# 2) Elaborar um programa para exibir todos os pares chave-valor no seguinte formato “chave=valor”.

dados = {
    "nome": "Sandro",
    "idade": 30,
    "cidade":"Sao Paulo",
    "estado":"Sao Paulo"

}

for chave, valor in dados.items():

    print(chave, valor, sep = "=") 
       